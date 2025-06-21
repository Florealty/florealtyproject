from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from functools import wraps

def custom_login_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('unauthorized')
        return view_func(request, *args, **kwargs)
    return _wrapped_view
