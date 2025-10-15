# file: README.md
# CRUD Todos

A minimal REST CRUD service for managing Todos.

## Setup and Running

This project uses `uv` for environment and package management.

1.  **Install `uv`**:
    If you don't have `uv` installed, follow the official installation instructions:
    ```bash
    pip install uv
    ```

2.  **Create a virtual environment and install dependencies**:
    ```bash
    uv venv
    uv pip install -r pyproject.toml
    ```

3.  **Run the server**:
    ```bash
    uv run uvicorn app.main:app --reload
    ```
    The application will be available at `http://127.0.0.1:8000`.

## Running Tests

To run the tests, use the following command:

```bash
uv run pytest
```

## API Endpoints & `curl` Examples

### Create a Todo

*   **Endpoint**: `POST /todos`
*   **Example**:
    ```bash
    curl -X POST "http://127.0.0.1:8000/todos/" -H "Content-Type: application/json" -d '{"title": "Buy groceries", "completed": false}'
    ```

### List Todos

*   **Endpoint**: `GET /todos`
*   **Example**:
    ```bash
    curl "http://127.0.0.1:8000/todos/?limit=2&offset=0"
    ```

### Read a Todo

*   **Endpoint**: `GET /todos/{id}`
*   **Example**:
    ```bash
    curl "http://127.0.0.1:8000/todos/1"
    ```

### Update a Todo

*   **Endpoint**: `PATCH /todos/{id}`
*   **Example**:
    ```bash
    curl -X PATCH "http://127.0.0.1:8000/todos/1" -H "Content-Type: application/json" -d '{"completed": true}'
    ```

### Delete a Todo

*   **Endpoint**: `DELETE /todos/{id}`
*   **Example**:
    ```bash
    curl -X DELETE "http://127.0.0.1:8000/todos/1"
    ```
