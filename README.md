<div align="center" style="padding-bottom: 20px">
    <h1>Django + React + Postgres + Docker + Heroku template</h1>
    <img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white" alt=""/>
    <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt=""/>
    <img src="https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white" alt=""/>
    <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" alt=""/>
    <img src="https://img.shields.io/badge/Vite-B73BFE?style=for-the-badge&logo=vite&logoColor=FFD62E" alt=""/>
    <img src="https://img.shields.io/badge/Sass-CC6699?style=for-the-badge&logo=sass&logoColor=white" alt=""/>
    <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt=""/>
    <img src="https://img.shields.io/badge/Docker-008FCC?style=for-the-badge&logo=docker&logoColor=white" alt=""/>
    <img src="https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white" alt=""/>
</div>

### Important:

Heroku is removing its free tier on 28th November 2022.

If you want to use this template, be aware that **Heroku is no longer free**. This template is still valid and can be
deployed anywhere else if you want to do some adjustments.

#### https://help.heroku.com/RSBRUH58/removal-of-heroku-free-product-plans-faq

In the nearest future I am going to create another template using other providers such as
Railway.app or Render.com, etc.

---

This repository serves as a starting point for developing a
production-ready application using Django Rest Framework,
React with Typescript and Postgres in a Dockerized environment
with an option to deploy to Heroku. Running development setup
without docker-compose is also possible.

### Tools, libraries, frameworks:

This setup has been tested with Python 3.10 and Node 16. (previously Python 3.8/3.9, Node 12/14)

### Backend

- Django + Django Rest Framework `django` `djangorestframework`
- `django-cors-headers` - handling cross origin requests
- `django-extensions` - utilities such as shell plus
- `coverage` - for code coverage reports and running unit tests
- `mypy` + `djangorestframework-stubs` - for better typing experience
- `psycopg2` - needed to use Postgres (in Docker container)
- `gunicorn` - production wsgi http server
- `whitenoise` - building static files
- `pipenv` - replacement for venv, works similarly to package.json

Suggested packages:

- `drf-yasg` - open api documentation (swagger and redoc)
- `django-rest-auth`, `django-allauth`, `djoser` - making auth easier
- `django-filter` - enables filtering querysets with url parameters and more
- `django-import-export` - import/export data from admin page
- `django-debug-toolbar` - useful debugging tool

### Frontend

- React `react`
- Typescript `typescript`
- `react-router-dom` - frontend routing
- `sass` - enables scss/sass support
- `axios` - for making HTTP requests
- `yarn` - package manager
- `vite` - bundler
- `jest` - unit testing

Suggested packages:

- UI libraries such as `Chakra-UI`, `Material-UI`, `Mantine`, `Reactstrap`, `TailwindCSS` etc. (personally I recommend
  Chakra-UI)
- `react-query` - highly encouraged, very useful package which handles data fetching logic for you
- `formik` + `yup` - handling form state and validation
- `@reduxjs/toolkit` + required packages
  (react-redux, redux etc.) - library which makes Redux much easier to understand and use
- `playwright` / `cypress` - for e2e testing

# Development setup

## Without Docker

### Backend

Create a virtual environment and install dependencies from Pipfile with `pipenv`

```shell
cd backend

pipenv shell

pipenv run pip install --upgrade pip

pipenv install
```

Or create a virtual environment traditionally and install dependencies from requirements.txt

```shell script
cd backend

python -m venv venv

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

Install node dependencies with `yarn`.

```shell script
cd frontend

yarn install
```

Run development server in second terminal

```shell script
yarn dev --port 3000
```

### Backend tests

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

### Frontend tests

Run unit tests

```shell
yarn test
```

Run coverage report

```shell
yarn test --coverage
```

## With Docker

**IMPORTANT:** You need to change CRLF to LF in entrypoint-dev.sh, entrypoint-prod.sh and entrypoint-build.sh,
otherwise build will fail because Linux uses different line endings than Windows.
You can do this e.g. using Pycharm, choosing LF in Line Separator at the bottom bar.
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
docker exec -it frontend bash
```

### 2) Build configuration

**In build configuration changes made locally are not reflected in running application. It is a simulation of the
production environment.**

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
7) Deploy your app by running: `git push heroku master` (make sure you added a remote heroku
   repository: ```heroku git:remote -a <your app name>```)
8) Go to `<your app name>.herokuapp.com` to see the published website.

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
