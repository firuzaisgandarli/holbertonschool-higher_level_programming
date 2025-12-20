# SQL - More Queries

## Project Description
This project continues the introduction to SQL with more advanced queries and user management tasks.  
All scripts are executed on **Ubuntu 20.04 LTS** using **MySQL 8.0 (version 8.0.25)**.

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be executed on Ubuntu 20.04 LTS using MySQL 8.0
- All files should end with a new line
- All SQL queries should have a comment just before (explaining the query)
- All files should start by a comment describing the task
- All SQL keywords must be in **UPPERCASE** (e.g., `SELECT`, `WHERE`)
- A `README.md` file at the root of the project folder is mandatory
- The length of files will be tested using `wc`

## Example
```sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
