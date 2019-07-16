from rolepermissions.roles import AbstractUserRole

class TaskManager(AbstractUserRole):
    available_permissions = {
        'add_user': False,
        'change_user': False,
        'delete_user': False,
        'view_user': False,
        'case_create': False,
        'case_delete': False,
        'case_edit': False,
        'case_view': True,
        'task_create': False,
        'task_delete': False,
        'task_edit': True,
        'task_view': True,
    }

class Manager(AbstractUserRole):
    available_permissions = {
        'add_user': True,
        'change_user': True,
        'delete_user': True,
        'view_user': True,
        'case_create': True,
        'case_delete': True,
        'case_edit': True,
        'case_view': True,
        'task_create': True,
        'task_delete': True,
        'task_edit': True,
        'task_view': True,
    }