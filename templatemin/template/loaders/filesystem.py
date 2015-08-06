"""
Wrapper for loading templates from the filesystem.
"""

from .base import LoaderMixin
from django.template.loaders.filesystem import Loader as BaseLoader


class Loader(LoaderMixin, BaseLoader):
    pass
