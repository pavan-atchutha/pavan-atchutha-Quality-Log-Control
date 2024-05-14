# Quality Log Control

This Logging System is a Django-based web application that allows users to log messages and filter logs based on different criteria.

## Deployment

The Logging System is currently deployed and accessible online. You can access the deployed version of the application at https://pavan-atchutha-quality-log-control.onrender.com/.

## How to Run the Project Locally

1. Clone the repository to your local machine:

```
git clone https://github.com/pavan-atchutha/pavan-atchutha-Quality-Log-Control.git
```

2. Navigate to the project directory:

```
cd QL_Control
```

3. Create and activate a virtual environment (optional but recommended):

```
# On macOS/Linux
python3 -m venv env
source env/bin/activate

# On Windows
python -m venv env
.\env\Scripts\activate
```

4. Install the required dependencies:

```
pip install -r requirements.txt
```

5. Apply migrations to create the database schema:

```
python manage.py migrate
```

6. Run the Django development server:

```
python manage.py runserver
```

7. Access the application in your web browser at [http://localhost:8000/](http://localhost:8000/).

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

