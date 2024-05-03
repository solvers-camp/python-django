# Description

## Django Employee Management System

The Django Employee Management System is a powerful web application designed to streamline the process of managing employee records within an organization. Built with Python Django, this system offers a comprehensive solution to efficiently handle various aspects of employee data.

## Prerequisites
Before you begin, ensure you have met the following requirements:

- Python installed on your local machine.
- pip package manager installed.
  
# Cloning the Repository

You can clone this repository to your local machine using the following command:

```bash
git clone <repository_url>
cd <repository_name>
```

# Installation

Install Django and other dependencies from the requirements.txt file

```bash
pip install -r requirements.txt
```
   
# Configuration and Migration

In this Django application, we use environment variables for configuration and migration for managing and applying changes to the database schema.

## Configuration

For Accessing the Database

1. Prerequisites
MySQL Server installed on your system.
MySQL client to interact with the database (e.g., MySQL Workbench, phpMyAdmin, or MySQL command-line client).

Here's a link to the MySQL download page where you can find the appropriate installer for your operating system:

[MySQL Downloads](https://dev.mysql.com/downloads/)

2. Create Database: Once MySQL is installed, create a new database for the Django project. 

3. Update .env File: We utilize the `dotenv/load_dotenv` module to manage environment variables. In the root directory of the project, create a .env file and fill in the following fields with your MySQL database details:

```bash
DB_HOST = <<Your Host Name>>
DB_PORT = <<Your Port Number>>
DB_USER = <<Your Username>>
DB_PASSWORD = <<Your Password>>
DB_NAME = <<Your Database Name>>

DJANGO_SECRET_KEY=<<Django secret key>>
```
DJANGO_SECRET_KEY is in setting.py file

## Migration

Apply Migrations: Once the migrations are created, apply them to the database to update the schema:

```bash
python manage.py migrate
```
This command will create the necessary tables in the MySQL database based on the models defined in your models.py file.

## Running Tests

```bash
pytest
```

## Create admin user

```bash
$ python manage.py createsuperuser
```

# For Running the Application

```bash
python manage.py runserver
```
Once the application is running, open your web browser.

Navigate to the following URL:

http://127.0.0.1:8000/
