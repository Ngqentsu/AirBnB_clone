#!/usr/bin/python3
"""To create unique FileStorage instance for this application."""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
