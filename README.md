# PythonDeveloperTasks

This repository contains solutions for various Python assessment projects and miscellaneous questions related to Python programming. The repository is organized into folders for each microservice and a separate folder for general answers.

## Python Misc Questions

1. **To indicate and propagate errors: use try/except or return an error value?**
2. **Explain the difference between mutable and immutable types**
3. **Define lambda, iterator, generator; and give examples how to use them**
4. **What do you use for testing? Linting? Debugging? Type enforcement?**

## Python Assessment Projects

### 1. FastAPI Microservice // Generic CRUD Service

#### Description:
Create a simple user registry microservice using FastAPI. The service should:
1. Provide endpoints to create, read, update, and delete user profiles.
2. Each user profile should contain fields like id, name, email, and age.
3. Store the user profiles in a SQLite or PostgreSQL database.

### 2. FastAPI Microservice // Caching Service

#### Description:
Create a simple caching microservice using FastAPI. The service should:
1. Provide endpoints to create and read generated payloads files. The create endpoint returns an identifier of the generated payload, and the read endpoint returns the actual payload.
2. Payloads files are generated as follows:
   - The input is two lists of strings (of same length)
   - The strings are transformed by a “transformer function” (simulate external service)
   - The output is the interleaving of the transformed strings from the two lists
3. The service should cache the outcome of the “transformer function” for use in future requests
   - Reuse cached outcomes instead of calling the “transformer function” if possible
   - Reuse payload identifier for generated payloads already generated before
4. Store the cached outcome results in a SQLite or PostgreSQL database.

#### Requirements:
- Use FastAPI to create the API endpoints.
- Use SQLModel or SQLAlchemy for database interactions.
- Dockerize the application for deployment.
