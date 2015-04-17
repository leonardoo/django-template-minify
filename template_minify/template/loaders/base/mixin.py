
import django
from django.template.base import TemplateDoesNotExist

from engine_minify.template.base import Template


class LoaderMixin(object):

    """
        Mixin for alter the load of templates, change the normal template for
        the custom template with minify method
    """

    def load_template(self, template_name, template_dirs=None):
        source, display_name = self.load_template_source(
            template_name, template_dirs)
        origin = self.engine.make_origin(
            display_name, self.load_template_source,
            template_name, template_dirs)

        try:
            template = Template(source, origin, template_name, self.engine)
        except TemplateDoesNotExist:
            # If compiling the template we found raises TemplateDoesNotExist,
            # back off to returning the source and display name for the
            # template we were asked to load. This allows for correct
            # identification of the actual template that does not exist.
            return source, display_name
        else:
            return template, None


if django.get_version < (1, 8, 0):
    from django.template.loader import make_origin


class LoaderMixinDjangoLess18(object):

    """
        Mixin for alter the load of templates in version less than django 1.8, 
        change the normal template for the custom template with minify method
    """

    def load_template(self, template_name, template_dirs=None):
        source, display_name = self.load_template_source(template_name, template_dirs)
        origin = make_origin(display_name, self.load_template_source, template_name, template_dirs)
        try:
            template = Template(source, origin, template_name)
            return template, None
        except TemplateDoesNotExist:
            # If compiling the template we found raises TemplateDoesNotExist, back off to
            # returning the source and display name for the template we were asked to load.
            # This allows for correct identification (later) of the actual template that does
            # not exist.
            return source, display_name