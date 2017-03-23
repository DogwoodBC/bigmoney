# Dogwood Big Money APP_DIRS

If you would like to become involved, please contact an existing collaborator.

### Setup instructions
Setup up your virtual environment.  You may use virtualenv (or any equivablent, like conda).  Use python 3.4+

Once you've setup your virtual environment, initialize it using source activate <name-of-your-virtualenvironment>, and the run

`pip install -r requirements.txt`

to install the package dependencies.

### Development

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


Get django going:
- Run database migrations `python manage.py migrate`
- `python manage.py createsuperuser`
- `python manage.py startapp api`

To populate the database, run the file `/bigmoney/scripts/import_donations.py` after modifying sys.path to include the absolute path to this repository's location on your computer.
`sys.path.append('~/youruser/some/place/bigmoney/')
`
### dependencies
This project uses:
- [Django Rest Framework](http://www.django-rest-framework.org/)
- [Postgresql](postgresql.org)

### TODO:
- Tests!
- See issues in github
