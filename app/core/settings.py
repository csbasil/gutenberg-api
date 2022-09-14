"""
Import all environment variables here and setup all project configurations
"""

from os import environ

# database settings
DATABASE_URL = environ.get("DATABASE_URL", None)

# development settings
DEBUG = bool(environ.get("DEBUG", 0))
