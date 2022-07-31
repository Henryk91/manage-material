# Manage Material 

This is a python django serverside app to manage and log waste material.
It uses a postgres database and has docker config to get up and running quickly.

NB: This project is not intended to be used in production 
<hr>
<br>

## Setup:

### Setting up the project

1. Make sure you have docker and docker-compose
2. Make sure you have make installed (https://stat545.com/make-windows.html)
3. CD into project directory
3. run: make run (or without make docker-compose up)

### Setting up
- After running the project you will need to create a super user to log in to the admin (make superuser)
- You can add data via the Django Admin, api or via the swagger page.
- Just remember to add `Bearer <token>` in the authentication headers
- To get a token you need to create a superuser and then create the token on Django Admin
- I have added a default .env file with test configs for docker and postgres


### Run the project
1. make run
2. stop the app
3. make superuser

- Default admin url is http://127.0.0.1:8000/admin/
- Default api url is http://127.0.0.1:8000/api/
- Default swagger url is http://127.0.0.1:8000/swagger/

<hr>
<br>
## Usefull Commands
<br>

### Run Server
- make run

### Run Detached Server
- make run-detach
### To add Admin creds to your project
- make superuser
