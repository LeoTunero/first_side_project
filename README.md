# sharky

## Requirements

Data Management System requires the following:

- Python 3.8+
- pipenv
- Django 3.0+

The following packages are required:

- django-environ

## Quick Start

```bash
# Clone this project to local
git clone https://github.com/LeoTunero/sharky.git

# cd to project folder and create a env.
cd sharky
pip3 install pipenv
pipenv install

# Run server
pipenv shell
python sharky/manage.py migrate
python sharky/manage.py runserver
```
