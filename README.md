
<div align="center" style="padding-bottom: 20px">
    <h1>Django + React + Postgres + Docker + Heroku template</h1>
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
This setup has been tested with Python 3.9 and Node 14. (previously Python 3.8, Node 12)

### Backend
- Django + Django Rest Framework `django` `djangorestframework`
- `django-cors-headers` - handling cross origin requests
- `coverage` - for code coverage reports and running unit tests
- `mypy` + `djangorestframework-stubs` - for better typing experience
- `psycopg2` - needed to use Postgres (in Docker container)
- `gunicorn` - production wsgi http server
- `whitenoise` - building static files

Suggested packages: 
- `drf-yasg` - open api documentation (swagger and redoc) 
- `django-rest-auth`, `django-allauth`, `djoser` - making auth easier
- `django-filter` - enables filtering querysets with url parameters and more
- `pip-chill` - works like pip freeze but does not output dependencies
- `pipenv` - replacement for venv, works similarly to package.json

### Frontend
- React `react`
- Typescript `typescript`
- `react-router-dom` - frontend routing
- `sass` - enables scss/sass support
- `axios` - for making requests

Suggested packages: 
- UI libraries such as `Chakra-UI`, `Material-UI`, `Reactstrap`, `TailwindCSS` etc. (personally I recommend Chakra-UI)
- `formik` + `yup` - handling form state and validation
- `@reduxjs/toolkit` + required packages 
(react-redux, redux etc.) - library which makes Redux much easier to understand and use
- `cypress` - for e2e testing

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
**IMPORTANT:** You need to change CRLF to LF in entrypoint-dev.sh, entrypoint-prod.sh and entrypoint-build.sh,
otherwise build will fail because Linux uses different line endings than Windows.
You can do this e.g using Pycharm, choosing LF in Line Separator at the bottom bar.
Other files are not affected by this issue.

Create `.env` file in projects root directory with variables (use your own values):
```
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=postgres
```

**Make sure Docker Engine is running.**  

### 1) Development configuration
While in **root directory**, build docker images and run them with docker-compose. 
This might take up to few minutes. 
Rebuilding image is crucial after installing new packages via pip or npm.

```shell script
docker-compose up --build
```

Application should be up and running: backend `127.0.0.1:8000`, frontend `127.0.0.1:3000`. 

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
docker exec -it <CONTAINER_ID/CONTAINER_NAME> <command>
```
e.g
```shell script
docker exec -it backend python manage.py createsuperuser
docker exec -it backend coverage run manage.py test
docker exec -it frontend /bin/sh
```

### 2) Build configuration
**In build configuration changes made locally are not reflected in running application. It is a simulation of the production environment.**  

The only difference when running containers is that you have to use **docker-compose-build.yml** file.
To achieve that use -f flag with filename: `-f docker-compose-build.yml`.

For example:
```shell script
docker-compose -f docker-compose-build.yml up --build

docker-compose -f docker-compose-build.yml down
```

Application should be up and running at `127.0.0.1:8000`. 
Now there is nothing at `127.0.0.1:3000` because static files have already been built. 

By default postgres service is shared between dev and build setups.
If you want to have a separate db, edit docker-compose-build.yml and set up new volume by yourself.

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

### Run commands in Heroku:
```shell
heroku run bash --app <your_app_name>
```
e.g
```shell
heroku run bash --app django-react-heroku-test
~ $ python backend/manage.py createsuperuser 
```

## CI
This repository uses Github Actions to run test pipeline.  
`tests.yml` - runs backend and frontend tests separately

I was not able to configure automatic deploys with Github Actions.
This was the [error](https://github.com/AkhileshNS/heroku-deploy/issues/84).

If you want to enable Automatic Deploys, use Heroku dashboard and enable waiting
for CI there.
