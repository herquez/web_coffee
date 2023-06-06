# Empresarial Website | Django

## About

This is the second project from a course about django, the web framework from python.
In this project we develop a web site for a business, in this case a caffeteria. There is dynamic content in the page that is administrated by data bases, and static content that is just there.

## Installations

### In machine

- python 3 or later
- pip
- pipenv

### Packages

All packages must be installed into the virtual enviroment. You are able to use de the next bash command followed by the package name.

```bash
pipenv install <package_name>
```

| Package          |Description                                                                                       |
|------------------|---------------------------------------------------------------------------------------------------|
| django           | A high-level Python web framework that enables rapid development of secure and scalable websites.  |
| django-ckeditor  | A Django package that integrates the CKEditor rich text editor into Django admin and forms.         |
| Pillow           | A powerful Python library for image processing tasks, providing capabilities like image resizing, cropping, and more. |
| pylint           | A widely used Python static code analysis tool that checks for programming errors and enforces coding standards. |
| pylint-django    | A plugin for Pylint that adds specific checks for Django projects, ensuring adherence to best practices and Django conventions. |
| pylint-celery    | A plugin for Pylint that provides additional checks and warnings for Celery, a distributed task queue library for Python. |

### Initial migrations

To create and update the database connected through the settings.py is necessary follow the next commands in order to migrate changes from the models in our project to the respective database.

#### Make migrations

```bash
python manage.py makemigrations
```

#### Migrate

```bash
python manage.py migrate
```

### Media Files

#### Settings

Into settings.py lets configure the url and root to media files as the next way:

```python
# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```
