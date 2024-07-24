# FastAPI CRUD Application

This is a simple FastAPI application that provides a RESTful API to perform CRUD (Create, Read, Update, Delete) operations on user data. The application uses SQLAlchemy for database interactions and SQLite as the database.

## Features

- Create a new user
- Retrieve a user by ID
- Retrieve multiple users with pagination
- Update an existing user
- Delete a user by ID

## Requirements

- Python 3.8+
- pip (Python package installer)
- SQLite (comes with Python)

## Setup

1. **Create a virtual environment and activate it:**

    ```sh
    python -m venv .venv
    source .venv/bin/activate 
    ```

2. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

```sh
uvicorn app.main:app --reload
```



## API Endpoints

### Create a New User

- **URL:** `/users/`
- **Method:** `POST`
- **Payload:**
    ```json
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "age": 30
    }
    ```
- **Response:**
    ```json
    {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "age": 30
    }
    ```

### Retrieve a User by ID

- **URL:** `/users/{user_id}`
- **Method:** `GET`
- **Response:**
    ```json
    {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "age": 30
    }
    ```

### Retrieve Multiple Users with Pagination

- **URL:** `/users/`
- **Method:** `GET`
- **Parameters:**
    - `skip` (optional, default=0): Number of records to skip.
    - `limit` (optional, default=10): Maximum number of records to return.
- **Response:**
    ```json
    [
        {
            "id": 1,
            "name": "John Doe",
            "email": "john.doe@example.com",
            "age": 30
        },
        ...
    ]
    ```

### Update an Existing User

- **URL:** `/users/{user_id}`
- **Method:** `PUT`
- **Payload:**
    ```json
    {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "age": 31
    }
    ```
- **Response:**
    ```json
    {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "age": 31
    }
    ```

### Delete a User by ID

- **URL:** `/users/{user_id}`
- **Method:** `DELETE`
- **Response:**
    ```json
    {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "age": 30
    }
    ```

## Running with Docker

1. **Build the Docker image:**

    ```sh
    docker build -t fastapi-crud-service .
    ```

2. **Run the Docker container:**

    ```sh
    docker run -d --name fastapi-crud-service -p 80:80 fastapi-crud-service
    ```

## AI Assistance
This project was developed with the assistance of AI tools to enhance the quality of the code and structure. AI was utilized to provide suggestions, improve code readability, and ensure adherence to best practices in software development.

## License

This project is licensed under the MIT License.