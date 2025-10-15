**S—Specific Goal**
Build a minimal REST **CRUD “Todos”** service. Entity: `Todo { id:int, title:str, completed:bool, created_at:datetime }`. Expose endpoints:

* `POST /todos` → create
* `GET /todos` → list (`?limit=&offset=`)
* `GET /todos/{id}` → read
* `PATCH /todos/{id}` → partial update (`title`, `completed`)
* `DELETE /todos/{id}` → delete


**C—Context**

* Language: Python 3.11+
* Stack: FastAPI, SQLAlchemy, Pydantic v2, SQLite
* Tooling: we will **run via `uv run python -m ...`** (no global installs).
* Project layout:

  ```
  crud_todos/
    app/
      __init__.py
      main.py
      database.py
      models.py
      schemas.py
      crud.py
    tests/
      test_api.py
    pyproject.toml
    README.md
  ```


**O—Output Format**

* Generate **all files** above. For each file, output in its own code block with the exact path as the first comment line (e.g., `# file: app/main.py`).
* API must return JSON and consistent errors `{ "detail": "message" }`.
* OpenAPI docs available at `/docs`.
* Include a concise **README.md** with:

  1. how to run the server/tests using **uv** (see commands below),
  2. example `curl` calls.
* Keep code clear and small; add short docstrings where useful.


**R—Rules & Constraints**

* SQLite file `app.db`; SQLAlchemy sessions via dependency injection; no global session.
* Input validation: `title` length 1–120 chars; `completed` boolean.
* Don’t change response schemas between endpoints; use Pydantic `from_attributes=True`.
* Keep functions focused; no unrelated formatting changes in diffs (if you show diffs).
* No auth/secrets; security out of scope for this demo.
* Pagination defaults: `limit=50` (1–200), `offset=0`.



**E—Evaluation (Acceptance Criteria)**

* Provide **pytest** tests covering create → read → list → update → delete → 404-after-delete.
* All tests **pass** when run with uv.
* Manual smoke test works with the provided `curl` examples.