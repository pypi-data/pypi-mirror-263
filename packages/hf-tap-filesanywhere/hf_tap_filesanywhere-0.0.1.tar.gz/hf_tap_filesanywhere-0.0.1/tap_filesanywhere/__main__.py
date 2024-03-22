"""FilesAnywhere entry point."""

from __future__ import annotations

from tap_filesanywhere.tap import TapFilesAnywhere

TapFilesAnywhere.cli()
