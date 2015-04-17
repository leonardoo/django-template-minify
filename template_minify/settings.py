from django.conf import settings

MINIFIER = "html_minifier.minify.Minifier"

HTML_MINIFIER = getattr(settings, 'HTML_MINIFIER', MINIFIER)