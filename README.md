# Resume Builder Using Django

#### Main Features:
* Create a Resume by just filling a Django form.
* Check Resume's of All the candidates from your local visit.
* An awesome template of your Resume will be built accordingly.


## To run this project follow the instructions given below:

#### First Clone the project
```
git clone https://github.com/altamash23820/resume-builder.git
cd resumebuilder
```

#### After cloning, run following commands:-
```
pip install django[argon2]
```
#### After running commands use following commands:
```
python manage.py migrate
python manage.py makemigrations
python manage.py migrate
```

#### Once done with that create a superuser account:
```
python manage.py createsuperuser
```

#### Once superuser account is created we can run the website
```
python manage.py runserver
```

#### If there are no errors website will be running on [http://127.0.0.1:8000/](http://127.0.0.1:8000/) (default)