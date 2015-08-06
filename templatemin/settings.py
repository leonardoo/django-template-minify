from django.conf import settings

MINIFIER = "html_minifier.minify.Minifier"

HTML_MINIFIER = getattr(settings, 'HTML_MINIFIER', MINIFIER)
HTML_EXCLUDE_MINIFIER = getattr(settings, 'HTML_EXCLUDE_MINIFIER', [])
