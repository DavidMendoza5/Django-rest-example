# Django restframework
## Virtual environment
### Virtualenv
- Create:
```
virtualenv venv
```
- Activate:
```
source venv/bin/activate
```
- Install dependencies:
```
pip install -r requirements.txt
```
### Pipenv
- Create:
```
pipenv shell
```
- Install dependencies from requirements.txt:
```
pipenv install -r requirements.txt
```
- Install dependencies from Pipfile:
```
pipenv install
```
## Run migrations
```
python manage.py makemigrations
```
```
python manage.py migrate
```
## Run server
```
python manage.py runserver
```