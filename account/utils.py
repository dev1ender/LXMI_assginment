
ROLES = (
    ('manager', 'MANAGER'),
    ('task_manager', 'TASK MANAGER'),
)


from rolepermissions.checkers import has_permission
from django.core.exceptions import PermissionDenied
# Decorator for permission checking
def access_permission(per):
    
    def _method_wrapper(view_method):

        def _arguments_wrapper(request, *args, **kwargs) :
            user  = args[0].user
            if has_permission(user,per):
                return view_method(request, *args, **kwargs)
            raise PermissionDenied
        return _arguments_wrapper

    return _method_wrapper