# Dogwood Big Money APP_DIRS

If you would like to become involved, please contact an existing collaborator.

[![License: CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/80x15.png)](http://creativecommons.org/licenses/by-nc-sa/4.0/)

### Setup instructions
Setup up your virtual environment.  You may use virtualenv (or any equivalent, like conda).  Use python 3.4+

Once you've setup your virtual environment, initialize it using source activate <name-of-your-virtualenvironment>, and then run

`pip install -r requirements.txt`

to install the package dependencies.

### Database setup

Setup your postgres db as following (assuming you have postgres 9.4+ installed)
- Login as the postgres user `sudo su - postgres`
- `createdb -U postgres bigmoney`
- `createuser -U postgres -P bigmoney`
- `psql -U postgre`s
  - `grant all privileges on database bigmoney to bigmoney`

Now you want to make sure that the following variables are set as environment variables:

```
export DATABASE_NAME='bigmoney'
export DATABASE_USER='bigmoney'
export DATABASE_PASSWORD='*****'
export DATABASE_HOST='127.0.0.1'
export DATABASE_PORT='5432' # Default Postgres port
export SECRET_KEY='****' # Make up a secret key here, used to generate csrf tokens among other things
```

or, depending on your hosting configuration it might be preferable to amend `settings.py` to contain those values. (Remember: never commit passwords into the Git repository!)

To initialize the application-specific database content
- Run database migrations: `python manage.py migrate`
- Create an administrative user: `python manage.py createsuperuser`
- Load the donation data into the database: `python manage.py loaddata data/fixtures/data.json`

### Major dependencies
This project uses:
- [Django Rest Framework](http://www.django-rest-framework.org/)
- [Postgresql](postgresql.org)

### TODO:
- Tests!
- See issues in github
