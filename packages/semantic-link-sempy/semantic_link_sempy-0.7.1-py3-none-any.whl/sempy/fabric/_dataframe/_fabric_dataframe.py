import pandas as pd
from uuid import UUID
from numpy import ndarray
from typing import Any, Callable, List, Iterable, Dict, Union, Optional, Tuple, TYPE_CHECKING
from pyspark.sql.types import StructField, StructType, StringType, IntegerType, FloatType, BooleanType, BinaryType, TimestampType

from sempy.fabric._utils import SparkConfigTemporarily
from sempy.dependencies._find import _find_dependencies_with_stats
from sempy.dependencies._stats import DataFrameDependencyStats
from sempy.functions import _SDataFrame
from sempy.dependencies._validate import (
    _drop_dependency_violations,
    _list_dependency_violations,
    _plot_dependency_violations,
)
from sempy._utils._log import log

if TYPE_CHECKING:
    import graphviz


class FabricDataFrame(_SDataFrame):
    """
    A dataframe for storage and propogation of PowerBI metadata.

    The elements of :attr:`~sempy.fabric.FabricDataFrame.column_metadata` can contain the following keys:

        - ``table``: table name in originating dataset
        - ``column``: column name
        - ``dataset``: originating dataset name
        - ``workspace_id``: string form of workspace GUID
        - ``workspace_name``: friendly name of originating workspace
        - ``description``: description of column (if one is present)
        - ``data_type``: `PowerBI data type <https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-data-types>`_ for this column
        - ``data_category``: `PowerBI data category <https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-data-categorization>`_ for this column
        - ``alignment``: `PowerBI visual alignment <https://learn.microsoft.com/en-us/dotnet/api/microsoft.analysisservices.tabular.alignment?view=analysisservices-dotnet>`_ for this column

    Parameters
    ----------
    data : numpy.ndarray, typing.Iterable, dict or pandas.DataFrame, default=None
        Dict can contain Series, arrays, constants, dataclass or list-like objects. If
        data is a dict, column order follows insertion-order. If a dict contains Series
        which have an index defined, it is aligned by its index. This alignment also
        occurs if data is a Series or a DataFrame itself. Alignment is done on
        Series/DataFrame inputs.

        If data is a list of dicts, column order follows insertion-order.
    *args : list
        Remaining arguments to be passed to standard pandas constructor.
    column_metadata : dict, default=None
        Information about dataframe columns to be stored and propogated.
    dataset : str or uuid.UUID, default=None
        Name or UUID of the dataset to list the measures for.
    workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID. Defaults to None which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.
    verbose : int, default=0
        Verbosity. 0 means no verbosity.
    **kwargs : dict
        Remaining kwargs to be passed to standard pandas constructor.
    """
    def __init__(
        self,
        data: Optional[Union[ndarray, Iterable, dict, pd.DataFrame]] = None,
        *args: Any,
        column_metadata: Optional[Dict[str, Any]] = None,
        dataset: Optional[Union[str, UUID]] = None,
        workspace: Optional[Union[str, UUID]] = None,
        verbose: int = 0,
        **kwargs: Any
    ):
        super().__init__(data, *args, column_metadata=column_metadata, **kwargs)

        if self.column_metadata is None and dataset is not None:
            # auto-resolve column metadata
            from sempy.fabric._cache import _get_or_create_workspace_client
            from Microsoft.AnalysisServices import OperationException

            try:
                self.column_metadata = _get_or_create_workspace_client(workspace) \
                    .get_dataset_client(dataset) \
                    .resolve_metadata(self.columns, verbose)
            except OperationException as e:
                if verbose > 0:
                    print(f"Warning: failed to resolve column metadata: {e}")

                self.column_metadata = {}

    @property
    def _constructor_sliced(self) -> Callable:
        # Manipulation result should be a Series
        from sempy.fabric import FabricSeries

        return FabricSeries

    def _get_common_workspace_and_dataset(self) -> Tuple[Union[str, UUID], str]:
        from sempy.fabric import MetadataKeys

        # column names are rows
        df_column_metadata = pd.DataFrame(self.column_metadata).transpose()

        # check if all columns are from the same workspace & dataset
        num_workspace_names = df_column_metadata[MetadataKeys.WORKSPACE_NAME].nunique() if MetadataKeys.WORKSPACE_NAME in df_column_metadata else 0
        num_workspace_ids = df_column_metadata[MetadataKeys.WORKSPACE_ID].nunique() if MetadataKeys.WORKSPACE_ID in df_column_metadata else 0
        num_datasets = df_column_metadata[MetadataKeys.DATASET].nunique()

        if num_datasets != 1:
            raise ValueError("Cannot join measures from different datasets.")

        dataset = df_column_metadata[MetadataKeys.DATASET].iloc[0]

        if num_workspace_ids > 1 or num_workspace_names > 1:
            raise ValueError("Cannot join measures from different workspaces.")

        if num_workspace_names == 1:
            return (df_column_metadata[MetadataKeys.WORKSPACE_NAME].iloc[0], dataset)
        elif num_workspace_ids == 1:
            return (df_column_metadata[MetadataKeys.WORKSPACE_ID].iloc[0], dataset)
        else:
            raise ValueError("Cannot join measures without workspace information.")

    def _metadata_to_fully_qualified_columns(self, columns: Optional[List[str]] = None) -> List[Tuple[str, str]]:
        """
        Converts specified columns (or all columns with metadata if columns=None) to fully qualified column references.
        """
        from sempy.fabric import MetadataKeys

        columns = columns if columns else list((self.column_metadata or dict()).keys())
        return [
            "'" + metadata[MetadataKeys.TABLE] + "'[" + metadata[MetadataKeys.COLUMN] + "]"
            for col, metadata in (self.column_metadata or dict()).items()
            if col in columns
        ]

    def _pandas_to_spark_schema(self) -> StructType:
        """
        Converts the dtype of each column to a string.
        Default pandas-spark conversion relies on values in the column instead of dataframe metadata; when nulls are encountered, auto-inference of types fails.
        """
        conversion_map = {
            'object': StringType(),
            'string': StringType(),
            'int8': IntegerType(),
            'uint8': IntegerType(),
            'int64': IntegerType(),
            'UInt64': IntegerType(),
            'Int64': IntegerType(),
            'int32': IntegerType(),
            'UInt32': IntegerType(),
            'Int32': IntegerType(),
            'int16': IntegerType(),
            'UInt16': IntegerType(),
            'Int16': IntegerType(),
            'Float64': FloatType(),
            'float64': FloatType(),
            'float32': FloatType(),
            'float16': FloatType(),
            'boolean': BooleanType(),
            'bytes': BinaryType(),
            'datetime64[ns]': TimestampType(),
            'bool': BooleanType()
        }

        schema = StructType(
            [
                StructField(name, conversion_map.get(str(dtype), StringType()))
                for name, dtype in self.dtypes.items()
            ]
        )

        return schema

    @log
    def add_measure(
        self,
        *measures: List[str],
        dataset: Optional[Union[str, UUID]] = None,
        workspace: Optional[Union[str, UUID]] = None,
        use_xmla: bool = False,
        verbose: int = 0
    ) -> "FabricDataFrame":
        """
        Join measures from the same dataset to the dataframe.

        Parameters
        ----------
        *measures : list[str]
            List of measure names to join.
        dataset : str or uuid.UUID, default=None
            Name or UUID of the dataset to list the measures for. If not provided it will be auto-resolved from column metadata.
        workspace : str or uuid.UUID, default=None
            The Fabric workspace name or UUID object containing the workspace ID. Defaults to None which resolves to the workspace of the attached lakehouse
            or if no lakehouse attached, resolves to the workspace of the notebook.
        use_xmla : bool, default=False
            Whether or not to use `XMLA <https://learn.microsoft.com/en-us/analysis-services/xmla/xml-for-analysis-xmla-reference?view=asallproducts-allversions>`_ as the backend for the client.
            If there are any issues using the default Client, make this argument True.
        verbose : int, default=0
            Verbosity. 0 means no verbosity.

        Returns
        -------
        FabricDataFrame
            A new FabricDataFrame with the joined measures.
        """
        from sempy.fabric import MetadataKeys
        from sempy.fabric._client._connection_mode import ConnectionMode

        if dataset is None:
            if self.column_metadata is None:
                raise ValueError("Cannot join measures without column metadata or dataset. "
                                 "Provide a dataset name to enable auto-resolution of column names, "
                                 "set column metadata manually or retrieve a FabricDataFrame from a "
                                 "PowerBI dataset using read_table.")
        else:
            # auto-resolve column metadata, regardless if column metadata is already set
            return FabricDataFrame(self, dataset=dataset, workspace=workspace).add_measure(*measures)

        # get common workspace and dataset
        workspace, dataset = self._get_common_workspace_and_dataset()

        mode = ConnectionMode.XMLA if use_xmla else ConnectionMode.REST

        # get measures
        from sempy.fabric._cache import _get_or_create_workspace_client
        dataset_client = _get_or_create_workspace_client(workspace) \
            .get_dataset_client(dataset, mode)  # type: ignore

        valid_columns = []
        for col, metadata in (self.column_metadata or dict()).items():
            if metadata[MetadataKeys.DATA_TYPE] == "Binary":
                continue
            valid_columns.append(col)
        df_measure = dataset_client.evaluate_measure(measures[0], self._metadata_to_fully_qualified_columns(valid_columns), verbose=verbose)  # type: ignore

        left_on = list(valid_columns)
        right_on = list(df_measure.columns[:len(valid_columns)].values)

        # left-outer join measures
        df_output = self.merge(
            df_measure,
            how="left",
            left_on=left_on,
            right_on=right_on)

        # remove duplicate join columns
        duplicate_join_columns = [c for c in right_on if c not in left_on]
        df_output.drop(columns=duplicate_join_columns, inplace=True)

        return df_output

    @log
    def find_dependencies(
        self,
        dropna: bool = False,
        threshold: float = 0.01,
        verbose: int = 0
    ) -> "FabricDataFrame":
        """
        Detect functional dependencies between the columns of a dataframe.

        Columns that map 1:1 will be represented as a list.

        Uses a threshold on conditional entropy to discover approximate functional dependencies.
        Low conditional entropy means strong dependence (i.e. conditional entropy of 0 means complete dependence).
        Therefore a lower threshold is more selective.

        The function tries to prune the potential dependencies by removing transitive edges.

        When dropna=True is specified, rows that have a NaN in either columns are eliminated from evaluation.
        This may result in dependencies being non-transitive, as in the following example. Even though A maps 1:1
        with B and B maps 1:1 with C, A does not map 1:1 with C, because comparison of A and C includes
        additional NaN rows that are excluded when comparing A and C with B:

            ===  ===  ===
             A    B    C
            ===  ===  ===
             1    1    1
             1    1    1
             1   NaN   9
             2   NaN   2
             2    2    2
            ===  ===  ===

        In some dropna=True cases the dependency chain can form cycles. In the following example, NaN values mask
        the pairwise mappings in such a way that A->B, B->C, C->A:

            ===  ===  ===
             A    B    C
            ===  ===  ===
             1    1   NaN
             2    1   NaN
            NaN   1    1
            NaN   2    1
             1   NaN   1
             1   NaN   2
            ===  ===  ===

        Parameters
        ----------
        dropna : bool, default=False
            Ignore rows where either column is NaN in dependency calculations.
        threshold : float, default=0.01
            Threshold on conditional entropy to consider a pair of columns a dependency.
            Lower thresholds result in less dependencies (higher selectivity).
        verbose : int, default=0
            Verbosity. 0 means no verbosity.

        Returns
        -------
        pandas.DataFrame
            A dataframe with dependencies between columns and groups of columns.
            To better visualize the 1:1 groupgings, columns that belong to a single groups are
            put into a single cell. If no suitable candidates are found, returns an empty DataFrame.
        """
        return FabricDataFrame(_find_dependencies_with_stats(self, DataFrameDependencyStats(self), dropna, threshold, verbose))

    @log
    def list_dependency_violations(
            self,
            determinant_col: str,
            dependent_col: str,
            *,
            dropna: bool = False,
            show_feeding_determinants: bool = False,
            max_violations: int = 10000,
            order_by: str = "count"
    ) -> "FabricDataFrame":
        """
        Show violating values assuming a functional dependency.

        Assuming that there's a functional dependency between column A (determinant)
        and column B (dependent), show values that violate the functional dependency
        (along with the count of their respective occurences).

        Allows inspecting approximate dependencies and find data quality issues.

        For example, given a dataset with zipcodes and cities, we would expect the
        zipcode to determine the city. However, if the dataset looks like this
        (where ZIP is the determinant and CITY is the dependent):

            =====      ==============
            ZIP        CITY
            =====      ==============
            12345      Seattle
            12345      Boston
            12345      Boston
            98765      Baltimore
            00000      San Francisco
            =====      ==============

        Running this function would output the following violation:

            =====      ========    =====
            ZIP        CITY        count
            =====      ========    =====
            12345      Boston      2
            12345      Seattle     1
            =====      ========    =====

        The same zipcode is attached to multiple cities, which means there is some
        data quality issue within the dataset.

        Parameters
        ----------
        determinant_col : str
            Candidate determinant column.
        dependent_col : str
            Candidate dependent column.
        dropna : bool, default=False
            Whether to drop rows with NaN values in either column.
        show_feeding_determinants : bool, default=False
            Show values in a that are mapped to violating values in b,
            even if none of these values violate the functional constraint.
        max_violations : int, default=10,000
            The number of violations to return.
        order_by : str, default="count"
            Primary column to sort results by ("count" or "determinant").
            If "count", sorts in order of determinant with highest number of dependent occurences (grouped by determinant).
            If "determinant", sorts in alphabetical order based on determinant column.

        Returns
        -------
        FabricDataFrame
            FabricDataFrame containing all violating instances of functional dependency.
            If there are no violations, returns an empty DataFrame.
        """
        return FabricDataFrame(
            _list_dependency_violations(self,
                                        determinant_col,
                                        dependent_col,
                                        dropna=dropna,
                                        show_feeding_determinants=show_feeding_determinants,
                                        max_violations=max_violations,
                                        order_by=order_by))

    @log
    def plot_dependency_violations(
        self,
        determinant_col: str,
        dependent_col: str,
        *,
        dropna: bool = False,
        show_feeding_determinants: bool = False,
        max_violations: int = 10000,
        order_by: str = "count"
    ) -> 'graphviz.Graph':
        """
        Show functional dependency violations in graphical format.

        Parameters
        ----------
        determinant_col : str
            Candidate determinant column.
        dependent_col : str
            Candidate dependent column.
        dropna : bool, default=False
            Whether to drop rows with NaN values in either column.
        show_feeding_determinants : bool, default=False
            Show values in a that are mapped to violating values in b,
            even if none of these values violate the functional constraint.
        max_violations : int, default=10,000
            The number of violations to return.
        order_by : str, default="count"
            Primary column to sort results by ("count" or "determinant").
            If "count", sorts in order of determinant with highest number of dependent occurences (grouped by determinant).
            If "determinant", sorts in alphabetical order based on determinant column.

        Returns
        -------
        graphviz.Graph
            Graph of violating values.
        """
        return _plot_dependency_violations(self,
                                           determinant_col,
                                           dependent_col,
                                           dropna=dropna,
                                           show_feeding_determinants=show_feeding_determinants,
                                           max_violations=max_violations,
                                           order_by=order_by)

    @log
    def drop_dependency_violations(
        self,
        determinant_col: str,
        dependent_col: str,
        verbose: int = 0
    ) -> "FabricDataFrame":
        """
        Drop rows that violate a given functional constraint.

        Enforces a functional constraint between the determinant and dependent columns provided.
        For each value of the determinant, the most common value of the dependent is picked,
        and all rows with other values are dropped.
        For example given

            =====      =============
            ZIP        CITY
            =====      =============
            12345      Seattle
            12345      Boston
            12345      Boston
            98765      Baltimore
            00000      San Francisco
            =====      =============

        The row with CITY=Seattle would be dropped, and the functional dependency
        ZIP -> CITY holds in the output.

        Parameters
        ----------
        determinant_col : str
            Determining column name.
        dependent_col : str
            Dependent column name.
        verbose : int, default=0
            Verbosity; 0 means no messages, 1 means showing the number of dropped rows,
            greater than one shows entire row content of dropped rows.

        Returns
        -------
        FabricDataFrame
            New dataframe with constraint determinant -> dependent enforced.
        """

        return _drop_dependency_violations(self, determinant_col, dependent_col, verbose=verbose)

    @log
    def to_lakehouse_table(self, name: str, mode: Optional[str] = "error", spark_schema: Optional[StructType] = None):
        """
        Write the data to OneLake as a Delta table with VOrdering enabled.

        Parameters
        ----------
        name : str
            The name of the table to write to.
        mode : str, default="error"
            Specifies the behavior when table already exists, by default "error".
            Details of the modes are available in the `Spark docs <https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrameWriter.mode.html>`_.
        spark_schema : pyspark.sql.types.StructType, default=None
            Specifies the schema of spark table to which the dataframe will be written in the lakehouse. If not provided, will be auto-generated via _pandas_to_spark_schema function.
        """
        from pyspark.sql import SparkSession

        spark = SparkSession.builder.getOrCreate()

        df_converted = self

        converted_schema = spark_schema if spark_schema is not None else df_converted._pandas_to_spark_schema()

        conversion_map: dict = {}
        for i in range(len(df_converted.dtypes)):
            col_name = df_converted.columns[i]
            col_type = df_converted.dtypes[i]
            if col_type in ['Float64', 'Int64', 'boolean']:
                # Spark does not like pd.NA (pandas 2.0.0+), and prefers python None, which can
                # only be setup in an 'object' column:
                conversion_map[col_name] = 'object'
            elif col_type == 'datetime64[ns]':
                # Spark wants python datetime. To convert pandas doc advise to use to_pydatetime,
                # which seems to leave pd.NaT (Not-a-Time) alone. So far, no better conversion
                # method found, even by Mr. Bing/ChatGPT:
                df_converted[col_name] = df_converted[col_name].apply(lambda v: v.to_pydatetime())

        df_converted = df_converted.astype(conversion_map)
        df_converted = df_converted.replace(pd.NA, None)

        # Adomd uses "1899-12-30" as a "zero date" following Excel/Access/SQL-Server going
        # back to Lotus 1-2-3 compatibility. We have little choice but to follow:
        #
        # https://stackoverflow.com/questions/3963617/why-is-1899-12-30-the-zero-date-in-access-sql-server-instead-of-12-31
        #
        #  Trying to write such a date fails on a default Spark installation with an exception:
        #
        #    Caused by: org.apache.spark.SparkUpgradeException: [INCONSISTENT_BEHAVIOR_CROSS_VERSION.WRITE_ANCIENT_DATETIME]
        #    You may get a different result due to the upgrading to Spark >= 3.0:
        #    writing dates before 1582-10-15 or timestamps before 1900-01-01T00:00:00Z
        #    into Parquet INT96 files can be dangerous, as the files may be read by Spark 2.x
        #    or legacy versions of Hive later, which uses a legacy hybrid calendar that
        #    is different from Spark 3.0+'s Proleptic Gregorian calendar. See more
        #    details in SPARK-31404. You can set "spark.sql.parquet.int96RebaseModeInWrite" to "LEGACY" to rebase the
        #    datetime values w.r.t. the calendar difference during writing, to get maximum
        #    interoperability. Or set the config to "CORRECTED" to write the datetime
        #    values as it is, if you are sure that the written files will only be read by
        #    Spark 3.0+ or other systems that use Proleptic Gregorian calendar.
        #
        # "spark.sql.parquet.int96RebaseModeInWrite" is not a static configuration, so it can be modified
        # during the session. Static configurations (such as delta extensions) have to be modified before
        # session is created. Fabric does not set this option as of November 2023:

        with SparkConfigTemporarily(spark, "spark.sql.parquet.int96RebaseModeInWrite", "CORRECTED"):
            spark_df = spark.createDataFrame(df_converted, schema=converted_schema)

            (spark_df.write
                .option("parquet.vorder.enabled", True)
                .mode(mode)
                .format("delta")
                # enable column mapping to support special characters common w/ Power BI (e.g. [])
                .option("delta.columnMapping.mode", "name")
                .saveAsTable(name))

    # repeating functions to make sure they show up in the docs

    @log
    def to_parquet(self, path: str, *args, **kwargs) -> None:
        """
        Write DataFrame to a parquet file specified by path parameter using `Arrow <https://arrow.apache.org/docs/python/index.html>`_ including metadata.

        Parameters
        ----------
        path : str
            String containing the filepath to where the parquet should be saved.
        *args : list
            Other args to be passed to PyArrow ``write_table``.
        **kwargs : dict
            Other kwargs to be passed to PyArrow ``write_table``.
        """
        super(_SDataFrame, self).to_parquet(path, *args, **kwargs)

    @property
    def column_metadata(self) -> Optional[dict]:
        """
        Information for the columns in the table.
        """
        return super(_SDataFrame, self).column_metadata

    @column_metadata.setter
    def column_metadata(self, value: Optional[dict]) -> None:
        """
        Update column_metadata to new value.

        Parameters
        ----------
        value : dict
            New value for column_metadata.
        """

        self._column_metadata_setter(value)


# Note: read_parquet should return a FabricDataFrame so that all functions (e.g. add_measure and semantic functions) are available
@log
def read_parquet(path: str) -> FabricDataFrame:
    """
    Read FabricDataFrame from a parquet file specified by path parameter using `Arrow <https://arrow.apache.org/docs/python/index.html>`_ including column metadata.

    Parameters
    ----------
    path : str
        String containing the filepath to where the parquet is located.

    Returns
    -------
    FabricDataFrame
        FabricDataFrame containing table data from specified parquet.
    """
    import json
    import pyarrow.parquet as pq

    table = pq.read_table(path)
    df = FabricDataFrame(table.to_pandas())
    metadata = table.schema.metadata.get(b"column_metadata", None)

    if metadata:
        df.column_metadata = json.loads(metadata)

    return df
