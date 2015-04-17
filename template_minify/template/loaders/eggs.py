# Wrapper for loading templates from eggs via pkg_resources.resource_string.
from .base import LoaderMixin
from django.template.loaders.eggs import Loader as BaseLoader

class Loader(LoaderMixin, BaseLoader):
    pass