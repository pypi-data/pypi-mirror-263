"""FilesAnywhere tap class."""

from __future__ import annotations


from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_filesanywhere.streams import FilesAnywhereStream
import tap_filesanywhere.file_utils as file_utils


class TapFilesAnywhere(Tap):
    """FilesAnywhere tap class."""

    name = "tap-filesanywhere"

    # Schema for nested 'tables' property
    table_schema = th.PropertiesList(
        th.Property(
            "path",
            th.StringType,
            required=True,
            description="The transport and bucket/root directory holding the targeted source files."
        ),
        th.Property(
            "name",
            th.StringType,
            required=True,
            description="The 'table' (aka Singer stream) into which the source data should be loaded."
        ),
        th.Property(
            "search_prefix",
            th.StringType,
            description="(optional) Prefix to apply after the bucket to filter files in the listing request."
        ),
        th.Property(
            "pattern",
            th.StringType,
            required=True,
            description="Escaped regular expression to filter the listing result set."
        ),
        th.Property(
            "key_properties",
            th.ArrayType(th.StringType),
            required=True,
            description="The 'primary keys' of the CSV files for deduplication and primary key definitions."
        ),
        th.Property(
            "format",
            th.StringType,
            required=True,
            description="Must be either 'csv', 'json', 'excel', or 'detect'."
        ),
        th.Property(
            "invalid_format_action",
            th.StringType,
            description="(optional) Set to 'ignore' to skip unreadable source files."
        ),
        th.Property(
            "field_names",
            th.ArrayType(th.StringType),
            description="(optional) The names of the columns in the targeted files."
        ),
        th.Property(
            "universal_newlines",
            th.BooleanType,
            description="(optional) Should the source file parsers honor universal newlines."
        ),
        th.Property(
            "sample_rate",
            th.IntegerType,
            default=10,
            description="(optional) The sampling rate when reading a source file for sampling in discovery mode."
        ),
        th.Property(
            "max_sampling_read",
            th.IntegerType,
            default=1000,
            description="(optional) How many lines of the source file should be sampled in discovery mode."
        ),
        th.Property(
            "max_sampled_files",
            th.IntegerType,
            default=5,
            description="(optional) The maximum number of files that will be sampled."
        ),
        th.Property(
            "max_records_per_run",
            th.IntegerType,
            description="(optional) The maximum number of records that should be written to this stream in a single sync run."
        ),
        th.Property(
            "prefer_number_vs_integer",
            th.BooleanType,
            description="(optional) Should number be used instead of integer for fields with only integer values."
        ),
        th.Property(
            "selected",
            th.BooleanType,
            default=True,
            description="(optional) Should this table be synced. Defaults to true."
        ),
        th.Property(
            "worksheet_name",
            th.StringType,
            description="(optional) The worksheet name to pull from in the targeted xls file(s)."
        ),
        th.Property(
            "worksheet_index",
            th.IntegerType,
            description="(optional) The worksheet index to pull from in the targeted xls file(s)."
        ),
        th.Property(
            "delimiter",
            th.StringType,
            description="(optional) The delimiter to use when format is 'csv'."
        ),
        th.Property(
            "quotechar",
            th.StringType,
            description="(optional) The character used to surround values that may contain delimiters."
        ),
        th.Property(
            "json_path",
            th.StringType,
            description="(optional) The JSON key under which the list of objects to use is located."
        ),
        th.Property(
            "extra_columns",
            th.ArrayType(th.StringType),
            description="(optional) Additional columns to be required in stream JSON schema. Useful to ensure rare columns are always included in stream output."
        ),
    )

    # Schema for YAML config
    config_jsonschema = th.PropertiesList(
        th.Property(
            "start_date",
            th.DateTimeType,
            default="1970-01-01T00:00:00Z",
            description="The datetime to filter files based on the modified timestamp."
        ),
        th.Property(
            "tables",
            th.ArrayType(table_schema),
            required=True,
            description="List of tables to sync."
        )
    ).to_dict()

    def discover_streams(self) -> list[FilesAnywhereStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        streams = []
        for table_spec in self.config.get('tables'):
            table_spec['start_date'] = self.config.get('start_date')
            schema = file_utils.discover_schema(table_spec)
            self.logger.debug(f"Discovered schema for '{table_spec.get('name')}': {schema}")
            streams.append(
                FilesAnywhereStream(
                    tap=self,
                    name=table_spec.get('name'),
                    schema=schema,
                )
            )

        return streams


if __name__ == "__main__":
    TapFilesAnywhere.cli()
