#!/usr/bin/python3

from models.engine.file_storage import FileStorage

storage = FileStorage()

storage = __import__('FileStorage').FileStorage


storage.reload()
