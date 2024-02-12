#!/usr/bin/python3
"""
create a unique FileStorage instance for my program
"""
from .engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
