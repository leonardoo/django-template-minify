import django
if django.get_version >= (1, 8, 0):
    from .mixin import LoaderMixin
else:
    from .mixin import LoaderMixinDjangoLess18 as LoaderMixin


__all__ = [
    LoaderMixin.__name__
]