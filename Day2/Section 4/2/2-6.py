def role_required(role):
    def decorator(func):
        def wrapper(user_role, *args, **kwargs):
            if user_role != role:
                raise PermissionError("Access Denied: Insufficient permissions.")
            return func(user_role, *args, **kwargs)
        return wrapper
    return decorator


@role_required("admin")
def view_dashboard(user_role):
    return "Dashboard content"


try:
    print(view_dashboard("admin"))
    print(view_dashboard("user"))
except PermissionError as e:
    print(e)