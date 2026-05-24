# Full Stack SQL Cheat Sheet (Django + React + PostgreSQL)

A complete beginner → advanced SQL reference for full-stack developers working with Django, React, and PostgreSQL (including AWS EC2 deployments).

---

# 🟢 LEVEL 1 — BEGINNER SQL

## 1. Create Database

```sql
CREATE DATABASE hms_db;
```

## 2. List Databases

```sql
\l
```

## 3. Connect to Database

```sql
\c hms_db
```

## 4. Delete Database

```sql
DROP DATABASE hms_db;
```

## 5. Create Table

```sql
CREATE TABLE patients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 6. Show Tables

```sql
\dt
```

## 7. Describe Table

```sql
\d patients
```

## 8. Insert Data

```sql
INSERT INTO patients (name, age)
VALUES ('John Doe', 30);
```

## 9. Read Data

```sql
SELECT * FROM patients;
```

## 10. Filter Data

```sql
SELECT * FROM patients WHERE age > 25;
```

---

# 🟡 LEVEL 2 — INTERMEDIATE SQL

## 11. Update Data

```sql
UPDATE patients
SET age = 35
WHERE id = 1;
```

## 12. Delete Data

```sql
DELETE FROM patients WHERE id = 1;
```

## 13. Sort Data

```sql
SELECT * FROM patients ORDER BY age DESC;
```

## 14. Limit Results

```sql
SELECT * FROM patients LIMIT 5;
```

## 15. Count Records

```sql
SELECT COUNT(*) FROM patients;
```

## 16. Group Data

```sql
SELECT age, COUNT(*)
FROM patients
GROUP BY age;
```

## 17. Rename Column Output

```sql
SELECT name AS patient_name FROM patients;
```

---

# 🟠 LEVEL 3 — RELATIONAL DATABASES (Django Core)

## 18. Foreign Key Relationship

```sql
CREATE TABLE appointments (
    id SERIAL PRIMARY KEY,
    patient_id INT REFERENCES patients(id),
    appointment_date DATE
);
```

## 19. INNER JOIN

```sql
SELECT patients.name, appointments.appointment_date
FROM patients
INNER JOIN appointments
ON patients.id = appointments.patient_id;
```

## 20. LEFT JOIN

```sql
SELECT patients.name, appointments.appointment_date
FROM patients
LEFT JOIN appointments
ON patients.id = appointments.patient_id;
```

---

# 🔵 LEVEL 4 — ADVANCED SQL (PRODUCTION LEVEL)

## 21. Create Index

```sql
CREATE INDEX idx_patients_name ON patients(name);
```

## 22. Transactions

```sql
BEGIN;

UPDATE patients SET age = 40 WHERE id = 1;

COMMIT;
```

## 23. Rollback Transaction

```sql
ROLLBACK;
```

## 24. Constraints

```sql
CREATE TABLE doctors (
    id SERIAL PRIMARY KEY,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) UNIQUE
);
```

## 25. Check Constraint

```sql
CREATE TABLE staff (
    id SERIAL PRIMARY KEY,
    salary INT CHECK (salary > 0)
);
```

## 26. Upsert (Insert or Update)

```sql
INSERT INTO patients (id, name)
VALUES (1, 'John')
ON CONFLICT (id)
DO UPDATE SET name = EXCLUDED.name;
```

## 27. Truncate Table

```sql
TRUNCATE TABLE patients;
```

---

# 🔴 LEVEL 5 — DJANGO + BACKEND SQL PATTERNS

## 28. Case-insensitive Search

```sql
SELECT * FROM patients WHERE name ILIKE '%john%';
```

## 29. Pagination

```sql
SELECT * FROM patients
ORDER BY id
LIMIT 10 OFFSET 20;
```

## 30. Dashboard Aggregation

```sql
SELECT COUNT(*) AS total_patients FROM patients;
```

## 31. Date Filtering

```sql
SELECT * FROM appointments
WHERE appointment_date >= CURRENT_DATE;
```

---

# 🧠 LEVEL 6 — DATABASE ADMIN (PRODUCTION)

## 32. Backup Database

```bash
pg_dump hms_db > backup.sql
```

## 33. Restore Database

```bash
psql hms_db < backup.sql
```

## 34. List Users

```sql
\du
```

## 35. Create User

```sql
CREATE USER damisa WITH PASSWORD 'password';
```

## 36. Grant Privileges

```sql
GRANT ALL PRIVILEGES ON DATABASE hms_db TO damisa;
```

---

# 🚀 CORE SQL SKILLS SUMMARY

Master these and you're strong in backend development:

* SELECT
* INSERT
* UPDATE
* DELETE
* JOIN
* INDEX
* TRANSACTIONS

Everything else builds on them.
