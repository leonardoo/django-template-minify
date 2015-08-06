from django.utils.encoding import smart_text

from .template.base import get_minifier, minify


class HtmlMinifyMiddleware(object):
    def process_response(self, request, response):
        if self._is_html(response) and response.status_code == 200:
            try:
                response.content = minify(smart_text(response.content))
            except Exception as e:
                pass
        return response

    def _is_html(self, response):
        if response.has_header('Content-Type'):
            return 'text/html' in response['Content-Type']
        return False
