import django
if django.get_version >= (1, 8, 0):
    from .mixins import TemplateCachedClear
else:
    from .mixins import TemplateCachedClearLess18 as TemplateCachedClear


__all__ = [
    TemplateCachedClear.__name__
]
