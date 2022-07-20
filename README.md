
<h1>
  <p align="center">
   Django Rest Framework Basic Auth
  </p>
</h1>

# :book: Overview

This project was built in order to practice the Django Rest Framework JWT authentication, I'm using the [Django Rest Framework Simple Jwt](https://github.com/jazzband/djangorestframework-simplejwt) library. I followed this tutorial https://medium.com/django-rest/django-rest-framework-b3028b3f0b9 to learn how to build the basic auth and then improved the password change logic to get the user id from the JWT without the need to send it via URL params

# :pushpin: Table of Contents
     
* [Technologies](#computer-technologies)
* [Features](#rocket-features)
* [How to Run](#construction_worker-how-to-run)

# :computer: Technologies
This project was made using the following technologies:

* Django  
* Django Rest Framework    

# :rocket: Features

* JWT Authentication
* Image Upload
* A CRUD of products, comments and categories

# :construction_worker: How to run
```bash
# Clone Repository
$ git clone https://github.com/MatheusBLopes/drf-basic-auth.git
```

For this project you will need to install [Poetry](https://python-poetry.org/) for package management, after this, run the commands:

```bash
# Install Dependencies
$ poetry install

# Run Aplication
$ python manage.py runserver
```
Go to http://localhost:8000/ to see the result.


Give a ⭐️ if this project helped you!
