# Fleet Manager Backend API

Fleet Manager is a Django-based web application that allows users to manage their fleet of vehicles and drivers, along with their respective details. This is the backend codebase for the application, built with Django REST Framework.

## Installation

1. Clone the repository to your local machine.
2. Create a virtual environment and activate it, with pipenv pipenv --python 3.11 and `pipenv shell`.
3. Install all dependencies, with pipenv `pipenv install`.
4. Create a database (MySQL was used) and configure it in the settings.py file.
5. Make and run the database migrations using the commands `python manage.py makemigrations` and `python manage.py migrate`.
6. Start the development server using the command `python manage.py runserver`.

## Endpoints

The following API endpoints are available:

`/api/status/` - GET the API status <br>
<br>
`/api/vehicles/` - GET a list of all vehicles or CREATE a new vehicle <br>
`/api/vehicles/<int:pk>/` - GET, PUT, or DELETE a single vehicle <br>
<br>
`/api/drivers/` - GET a list of all drivers or CREATE a new driver <br>
`/api/drivers/<int:pk>/` - GET, PUT, or DELETE a single driver <br>
<br>
`/api/makes/` - GET a list of all makes or CREATE a new make <br>
`/api/makes/<int:pk>/` - GET, PUT, or DELETE a single make <br>
<br>
`/api/models/` - GET a list of all models or CREATE a new model <br>
`/api/models/<int:pk>/` - GET, PUT, or DELETE a single model <br>
<br>
`/api/locations/` - GET a list of all locations or CREATE a new location <br>
`/api/locations/<int:pk>/` - GET, PUT, or DELETE a single location <br>
<br>
`/api/statuses/` - GET a list of all statuses or CREATE a new status <br>
`/api/statuses/<int:pk>/` - GET, PUT, or DELETE a single status <br>
