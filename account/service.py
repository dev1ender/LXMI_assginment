from rolepermissions.roles import assign_role
from rolepermissions.roles import get_user_roles
from rolepermissions.roles import remove_role



def assign_user_role(instance):
    role = get_user_roles(intance)
    if role:
        if role!=instance.role:
            remove_role(intance,role)
        
    assign_role(instance, instance.role)
