"""Stream type classes for tap-filesanywhere."""

from __future__ import annotations

import sys
import typing as t
from singer_sdk.streams import Stream # Stream base class

import tap_filesanywhere.format_handler as format_handler
import tap_filesanywhere.file_utils as file_utils


if sys.version_info >= (3, 9):
    import importlib.resources as importlib_resources
else:
    import importlib_resources

class FilesAnywhereStream(Stream):
    """Stream class for FilesAnywhere streams."""

    replication_key = "last_modified"
    is_sorted = True # Must sort list of files for each table by "last_modified"
    selected = True

    def get_records(
        self,
        context: dict | None,  # noqa: ARG002
    ) -> t.Iterable[dict]:
        """Return a generator of record-type dictionary objects.

        The optional `context` argument is used to identify a specific slice of the
        stream if partitioning is required for the stream. Most implementations do not
        require partitioning and should ignore the `context` argument.

        Args:
            context: Stream partition or context dictionary.

        Yields:
            record from stream
        """
        # Find corresponding table_spec for stream from tap config
        for i in range(len(self.config.get('tables'))):
            if self.config.get('tables')[i]['name'] == self.name:
                cfg_table_index = i
                
        table_spec = self.config.get('tables')[cfg_table_index]
        modified_since = self.get_starting_timestamp(context)

        target_files = file_utils.get_matching_objects(table_spec, modified_since)

        for file in target_files:
            target_uri = table_spec['path'] + "/" + file['key']
            records_synced = 0

            try:
                iterator = format_handler.get_row_iterator(table_spec, target_uri)
                
                for row in iterator:
                    custom_columns = {
                        # index zero, +1 for header row
                        file_utils.SDC_SOURCE_LINENO_COLUMN: records_synced + 2,
                        file_utils.SDC_SOURCE_BUCKET_COLUMN: file_utils.hide_credentials(table_spec['path']),
                        file_utils.SDC_SOURCE_FILE_COLUMN: file['key'],
                        file_utils.SDC_SOURCE_LAST_MODIFIED_COLUMN: file['last_modified']
                    }
                    
                    rec = {**row, **custom_columns}

                    records_synced +=1

                    yield rec
            
            except format_handler.InvalidFormatError as ife:
                    raise ife
