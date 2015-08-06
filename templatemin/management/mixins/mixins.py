class TemplateCachedClear(object):

    def _get_loaders(self):
        from django.template.loader import _engine_list
        # _engine_list delivery really the backends templates
        # when we can find the engines in django 1.8
        templates = _engine_list()
        loaders = []
        for template in templates:
            loaders += template.engine.template_loaders

        return loaders

    def reset_loaders(self):
        loaders = self._get_loaders()
        if loaders:
            [loadertemplate.reset() for loadertemplate in loaders]


class TemplateCachedClearless18(TemplateCachedClear):

    def _get_loaders(self):
        from django.template.loader import template_source_loaders
        return template_source_loaders
