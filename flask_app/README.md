## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/redianmarku/image-background-remover-website
   cd image-background-remover-website
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:

   ```bash
   python app.py
   ```

5. **Access the app**:
   - Open your web browser and go to `http://127.0.0.1:5000/`.



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
