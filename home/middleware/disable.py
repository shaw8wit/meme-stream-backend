from django.utils.deprecation import MiddlewareMixin

# middleware to disable csrf globally to make anonymous requests


class DisableCSRF(MiddlewareMixin):
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
