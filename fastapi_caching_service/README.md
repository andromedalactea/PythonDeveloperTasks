# FastAPI Caching Service

This is a simple FastAPI application that provides a RESTful API to perform caching of generated payloads. The application uses SQLAlchemy for database interactions and SQLite as the database.

## Features

- Create a new payload
- Retrieve a payload by ID
- Cache the results of the transformation function
- Reuse cached results for identical inputs

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

### Create a New Payload

- **URL:** `/payload/`
- **Method:** `POST`
- **Payload:**
    ```json
    {
        "list_1": ["first string", "second string", "third string"],
        "list_2": ["other string", "another string", "last string"]
    }
    ```
- **Response:**
    ```json
    {
        "id": 1,
        "input_data": {
            "list_1": ["first string", "second string", "third string"],
            "list_2": ["other string", "another string", "last string"]
        },
        "output_data": "FIRST STRING, OTHER STRING, SECOND STRING, ANOTHER STRING, THIRD STRING, LAST STRING"
    }
    ```

### Retrieve a Payload by ID

- **URL:** `/payload/{id}`
- **Method:** `GET`
- **Response:**
    ```json
    {
        "id": 1,
        "input_data": {
            "list_1": ["first string", "second string", "third string"],
            "list_2": ["other string", "another string", "last string"]
        },
        "output_data": "FIRST STRING, OTHER STRING, SECOND STRING, ANOTHER STRING, THIRD STRING, LAST STRING"
    }
    ```

## Running with Docker

### Build the Docker image:

```sh
docker build -t fastapi-caching-service .
```

### Run the Docker container:

```sh
docker run -d --name fastapi-caching-service -p 80:80 fastapi-caching-service
```

### Running Tests

1. **Install the test dependencies:**

    ```sh
    pip install pytest httpx
    ```

2. **Set the PYTHONPATH environment variable:**

    ```sh
    export PYTHONPATH=$(pwd)
    ```

3. **Run the tests:**

    ```sh
    pytest
    ```

### Test Coverage

- **Unit Tests:**
    - Test to create payload
    - Test to read payload

## AI Assistance
This project was developed with the assistance of AI tools to enhance the quality of the code and structure. AI was utilized to provide suggestions, improve code readability, and ensure adherence to best practices in software development.

## License
This project is licensed under the MIT License.