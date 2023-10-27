from django.apps import apps


def add_log_to_db(viewed, http_user_agent, request_method) -> bool:
    model = apps.get_model('aboutCompany', 'Logger')
    log = model(viewed=viewed, http_user_agent=http_user_agent,
                request_method=request_method)
    log.save()
    return True
