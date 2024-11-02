# Flask User Registration and Login API

This is a simple Flask application for user registration and login functionalities.

## Features

- User Registration
- User Login

## Installation

1. Clone the repository
2. Navigate to the project directory
3. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```
4. Create the database:
   ```bash
   flask create_db
   ```
5. Run the application:
   ```bash
   python app.py
   ```

## Usage

Use tools like Postman or cURL to interact with the API.

### Register a user

**POST** `/register` with JSON body:
```json
{
    "username": "testuser",
    "password": "testpass"
}
```

### Login a user

**POST** `/login` with JSON body:
```json
{
    "username": "testuser",
    "password": "testpass"
}
```

## License

This project is licensed under the MIT License.
