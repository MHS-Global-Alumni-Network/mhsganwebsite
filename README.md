To start project:
1) Change directory to mhsganwebsite directory
2) Activate virtual environment by doing `source venv/bin/activate`
3) Install requirements by doing: `pip install -r requirements.txt`
4) Start Postgres database by doing `brew services start postgresql`
5) Start server by doing: `python manage.py runserver`


To Create a New Model
1) Run the command `python manage.py startapp <new_app_name>`
2) Add the new model in the models.py file:
```
from django.db import models
class NewModel(models.Model):
    # Add your fields here
    title = models.CharField(max_length=200)
```

3) Run `python manage.py makemigrations` to create a migration file.

4) Run `python manage.py migrate` to apply the changes and create the new table in the database.

5) To manage the new model in the Django admin panel, add it to the app's admin.py file.

```
from django.contrib import admin
from .models import NewModel

admin.site.register(NewModel)
```
