# LXMI_assginment
## Documentation
This is case management system which incude account(user) , case , task 
Each user can have a role either manager,task_manager

### User API

```
create user
/account/create/ POST  <username, password,email,role> 
role have two choices manager or task_manager

update user
/account/<id>/update/ POST  <username, password,email,role>
role have two choices manager or task_manager

delete user
/account/<id>/delete/ DELETE   

list user
/account/list/ GET

view user
/account/<id>/view/ GET
````

### Case API
```
create case
/case/create/ POST  <name, task,assigned_to> 
In task pass task ids and in assigned_to pass user id 

update case
/case/<id>/update/ POST  <name, task,assigned_to>
In task pass task ids and in assigned_to pass user id 

delete case
/case/<id>/delete/ DELETE   

list case
/case/list/ GET

view case
/case/<id>/view/ GET

```  
### Task API

```
create task
/task/create/ POST  <name, content> 

update task
/task/<id>/update/ POST  <name, content>

delete task
/task/<id>/delete/ DELETE   

list task
/task/list/ GET

view task
/task/<id>/view/ GET
```
