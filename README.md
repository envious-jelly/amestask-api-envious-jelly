# AmesTask API Backend
This project was made using Python 3.13.5 and MySQL MariaDB 11.4.5.
It includes a database and backend API for an Angular project (Angular repo: amestask-fe-envious-jelly).

## Local Database
Create a new schema:
```sql
CREATE SCHEMA name CHARACTER SET utf8mb4 COLLATE utf8mb4_slovenian_ci;
USE name;
```
Run the `database/baza.sql` file to create the necessary tables. It will also create some data for testing.

Once you have the schema ready, you'll have to change the value of `URL_DATABASE` in `database.py`:
```python
URL_DATABASE = 'mysql+pymysql://USER:PASSWORD@localhost:3306/name'
```
Replace the values `USER` and `PASSWORD` so that the application can access the schema `name`.

## Running the Application
Run the following command in a terminal:
```bash
uvicorn main:app --reload
```
and navigate to `http://127.0.0.1:8000/docs` in your browser.
