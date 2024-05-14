# Logging System

This Logging System is a Django-based web application that allows users to log messages and filter logs based on different criteria.

## How to Run the Project

1. Clone the repository to your local machine:

```
https://github.com/pavan-atchutha/pavan-atchutha-Quality-Log-Control.git
```

2. Navigate to the project directory:

```
cd logging-system
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Apply migrations to create the database schema:

```
python manage.py migrate
```

5. Run the Django development server:

```
python manage.py runserver
```

6. Access the application in your web browser at [http://localhost:8000/](http://localhost:8000/).

## System Design

The Logging System is built using the Django web framework. It consists of the following components:

- **Models**: The main model `LogEntry` stores log messages with attributes such as level, log string, metadata source, and timestamp.
- **Views**: Views handle user requests and interact with models and templates.
- **Templates**: HTML templates are used to render the user interface.
- **Forms**: Django forms handle user input for logging messages and filtering logs.

## Features Implemented

- **Log Sending**: Users can send log messages with different levels (DEBUG, INFO, WARNING, ERROR, CRITICAL) along with metadata source.
- **Log Filtering**: Users can filter logs based on level, source, and timestamp.
- **JSON Field Handling**: Form data is converted to JSON format and stored in the JSONField of the model.

## Identified Issues

- **Error Handling**: Error handling for JSON decoding errors and form validation errors needs to be improved.
- **Authentication and Authorization**: Currently, there is no authentication and authorization implemented. Adding user authentication and authorization would enhance security.
- **User Interface**: The user interface can be improved for better user experience.
