"""
Wrapper for loading templates from "templates" directories in INSTALLED_APPS
packages.
"""

from .base import LoaderMixin
from django.template.loaders.app_directories import Loader as BaseLoader

class Loader(LoaderMixin, BaseLoader):
    pass
