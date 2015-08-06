import importlib

from django.template.base import Template as TemplateBase, TemplateEncodingError
from django.utils.encoding import smart_text
from templatemin import settings


_MINIFIER = None


def get_minifier():
    """ 
        get the object for minify from settings HTML_MINIFIER
    """
    global _MINIFIER

    if not _MINIFIER:
        html_minifier = getattr(settings, 'HTML_MINIFIER', None)
        if not html_minifier:
            raise ConfigsDoesNotExist("Must config the app minify class in setting")
        mod_path, _, cls_name = html_minifier.rpartition('.')
        module = importlib.import_module(mod_path)
        Minifier = getattr(module, cls_name)
        _MINIFIER = Minifier()

    return _MINIFIER


def minify(content):
    minify = get_minifier()
    minify.html = content
    return minify.minify()


class ConfigsDoesNotExist(Exception):
    pass


class Template(TemplateBase):

    """
        New template for apply a minify to the templates
    """

    def __init__(self, template_string, origin=None, name=None, *args, **kwargs):
        try:
            template = smart_text(template_string)
            if not self._exclude(name):
                template = self._minify(template)
                self._template_minify = template
        except UnicodeDecodeError:
            raise TemplateEncodingError("Templates can only be constructed "
                                        "from unicode or UTF-8 strings.")
        super(Template, self).__init__(template, origin, name, *args, **kwargs)

    def _minify(self, template_string):

        """
            get the minifier and return string with template minify
        """
        return minify(template_string)

    def _exclude(self, template_name):
        return template_name in getattr(settings, 'HTML_EXCLUDE_MINIFIER')
