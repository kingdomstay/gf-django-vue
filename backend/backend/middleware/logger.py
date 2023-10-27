from django.utils import timezone
from backend.services import add_log_to_db


class LoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        print(request.META.get("HTTP_USER_AGENT"))
        print(request.META.get("REQUEST_METHOD"))
        print(timezone.now())

        add_log_to_db(viewed=timezone.now(), http_user_agent=request.META.get("HTTP_USER_AGENT"),
                      request_method=request.META.get("REQUEST_METHOD"))
        return response
