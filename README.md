
<div align="center" style="padding-bottom: 20px">
    <h1>Django + React + Postgres + Heroku template</h1>
    <img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white" alt=""/>
    <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt=""/>
    <img src="https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white" alt=""/>
    <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" alt=""/>
    <img src="https://img.shields.io/badge/Sass-CC6699?style=for-the-badge&logo=sass&logoColor=white" alt=""/>
    <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt=""/>
    <img src="https://img.shields.io/badge/Docker-008FCC?style=for-the-badge&logo=docker&logoColor=white" alt=""/>
    <img src="https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white" alt=""/>
</div>

This repository serves as a starting point for developing a 
production-ready application using Django Rest Framework, 
React with Typescript and Postgres in a Dockerized environment 
with an option to deploy to Heroku. Running development setup
without docker-compose is also possible.

### Tools, libraries, frameworks:
This setup has been tested with Python 3.8/3.9 and Node 12.

### Backend
- Django + Django Rest Framework
- `django-cors-headers` - handling cross origin requests
- `coverage` - for code coverage reports and running unit tests
- `mypy` + `djangorestframework-stubs` - for better typing experience
- `psycopg2` - needed to use Postgres (in Docker container)
- `gunicorn` - production wsgi http server
- `whitenoise` - building static files

Suggested packages: 
- `drf-yasg` - open api documentation (swagger and redoc) 
- `django-rest-auth`, `django-allauth` - making auth easier

### Frontend
- React
- Typescript
- `node-sass` - enables scss/sass support
- `axios` - for making requests

Suggested packages: 
- `@material-ui/core`, `@material-ui/lab`, `@material-ui/icons` - UI library

# Development setup

## Without Docker
### Backend
Create a virtual environment from cmd (or do it in Pycharm manually)
```shell script
cd backend

py -3 -m venv venv

venv/Scripts/Activate

python -m pip install --upgrade pip

pip install -r requirements.txt
```

Run django application from cmd (or add new Django configuration if using Pycharm)
```shell script
python manage.py runserver
```

Preparing (if there are any changes to db schema) and running migrations
```shell script
python manage.py makemigrations

python manage.py migrate
```

Create superuser
```shell script
python manage.py createsuper user
```

### Frontend
Install node dependencies.
```shell script
cd frontend

npm i
```
Run development server in second terminal
```shell script
npm start
```

### Backend tests coverage
```shell script
cd backend
```
Run tests using Coverage instead of `python manage.py test`
```shell script
coverage run manage.py test
```
Get report from coverage:
```shell script
coverage report -m
```

## With Docker
Make sure Docker Engine is running.  

While in **root directory**, build docker images and run them with docker-compose. This might take up to few minutes.

```shell script
docker-compose up --build
```

Application should be up and running at `127.0.0.1` (by default)  

If images had been installed and **no changes have been made**, just run to start containers:
```shell script
docker-compose up
```

Bringing down containers with **optional** -v flag removes **all** attached volumes and invalidates caches.
```shell script
docker-compose down
```

To run commands in active container:
```shell script
docker exec -it CONTAINER_ID bash
```


# Production Deployment  
   1) [Create Heroku Account](https://signup.heroku.com/dc)  
   2) [Download/Install/Setup Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)  
    - After install, log into Heroku CLI: `heroku login`  
   3) Run: `heroku create <your app name>` to create the Heroku application    
   4) Set your environment variables for your production environment by running:  
    ```
    heroku config:set PRODUCTION_HOST=<your app name>.herokuapp.com SECRET_KEY=<your secret key> DJANGO_SETTINGS_MODULE=core.settings.prod
    ```  
   5) Run: `heroku stack:set container` so Heroku knows this is a containerized application  
   6) Run: `heroku addons:create heroku-postgresql:hobby-dev` which creates the postgres add-on for Heroku 
   7) Deploy your app by running: `git push heroku master`,  
   *or* by pushing to your github repository,  
   *or* manually in Heroku dashboard  
   8) Go to `<your app name>.herokuapp.com` to see the published website.  

If you are having issues with heroku repository, try ```heroku git:remote -a <your app name>```.

## CI
This repository uses Github Actions to run test pipeline.  
`tests.yml` - runs backend and frontend tests separately

I was no able to configure automatic deploys with Github Actions.
This was the [error](https://github.com/AkhileshNS/heroku-deploy/issues/84).

If you want to enable Automatic Deploys, use Heroku dashboard and enable waiting
for CI there.
