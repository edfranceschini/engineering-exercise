# Engineering Exercise

## Description

Edson Franceschini attempt to impress the Avaaz team

## Prerequisites

- Docker
- Docker Compose

## Building and running the project

The project contains a file called ''entrypoint.sh'' that will handle the DB creation and initial migrations [1](#use-of-alembic-as-migration-handler) and populate the initial data.

```console
docker compose up -d --build
```

The database will expose port 3306 and the backend the port 8000

## Testing the project api

### Basic cUrl

```console
curl --location 'localhost:8000/search'
```

### Basic title search

```console
curl --location 'localhost:8000/search?title=Enterprise'
```

### Basic url search

```console
curl --location 'localhost:8000/search?url=matthews-espinoza.com'
```

### Basic dates combination

```console
curl --location 'localhost:8000/search?date_after=1999-01-01&date_before=2007-01-01'
```

### Basic title and dates

```console
curl --location 'localhost:8000/search?date_after=1999-01-01&date_before=2007-01-01&title=Operative'
```

## Unit Test

I added just one unittest for the view because of the time. The view was choosen because its is a more complex testing since it envolves mocking DB calls and other techniques.

# Final considerations

## Use of Flask SQLAlchemy as ORM

Using Flask-SQLAlchemy in a small Flask project offers several benefits:

1. Speeds Up Development: High-level ORM facilitates rapid application development.
1. Future Scalability: Lays a robust foundation for potential project growth.
1. Migration Support: Integrates with Alembic for smooth database schema changes.
1. Abstraction of Complexity: Abstracts SQL intricacies, focusing on Pythonic development.
1. Maintainable Code: Leads to more readable and maintainable codebase.

## Use of Alembic as migration handler

Taking care of migrations for the Database is beneficial for a lot or reasons bur manly for:

1. Future-Proofing: It prepares the project for future growth by establishing a structured approach to database migrations from the start.
1. Version Control for Database Schema: Alembic tracks changes to the database schema, similar to how Git tracks changes in source code, making it easier to manage and understand the evolution of your database.
1. Flexibility: Allows for easy testing of new features and changes in your database schema, ensuring your application remains robust and adaptable.

# Avaaz Engineering Exercise

Thanks for your interest in joining Avaaz! We are thrilled that you considered working with us.

Your task is to build a small application that allows a user to search data using several filters:

- Date range (after, before, and between)
- Title (text search, case-insensitive, full or partial matches)
- URL (full or partial matches)

The following things are provided in this repository:

- The destination database table (see `database/initdb.d/setup.sql`)
- A bare bones Flask app (see `app/server.py`)

**We recommend you spend a maximum of two hours on it, and don't worry if you didn’t cover all of the requirements.**

## Instructions

- Use Python and Flask for your application
- The application ingests JSON source data (see the input folder)
- The application stores valid data and normalized datetimes in the provided database
- The application allows searching the data through an API endpoint (using the filters described above)

Submit your solution by sending a zipped file via email to your Avaaz recruiting contact (you can reply to your existing email thread).
