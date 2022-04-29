# help-ukrainians

## Setup

The first thing to do is clone this repository:

```bash
git clone https://github.com/dark-dave007/cs50w-network
cd cs50w-network
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
