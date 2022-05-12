# help-ukrainians

## Setup

The first thing to do is clone this repository:

```bash
git clone https://github.com/dark-dave007/help-ukrainians
cd help-ukrainians
```

Install dependencies:

```bash
python3 -m pip install Django
```

Migrate:

```bash
python3 manage.py makemigrations network
python3 manage.py migrate
```

Go into ukrainehelp/settings.py and configure the smtp settings:
```python3
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "youremail@gmail.com"
EMAIL_HOST_PASSWORD = str(os.environ["EMAIL_HOST_PASSWORD"]) # Your password as an enviroment variable, or not, you choose :)
```

To run the development server:

```bash
python3 manage.py runserver
```

If you would like to create an admin user, run the following:

```bash
python3 manage.py createsuperuser
```
And follow the instructions given by Django.

## Contributing
Just make a pull request
