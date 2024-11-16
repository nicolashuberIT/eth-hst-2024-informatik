-- 1. Erstelle eine neue Tabelle
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    position VARCHAR(50),
    salary DECIMAL(10, 2)
);

-- 2. Füge Datensätze in die Tabelle ein
INSERT INTO employees (id, name, position, salary) 
VALUES 
    (1, 'Alice', 'Manager', 75000.00),
    (2, 'Bob', 'Entwickler', 60000.00),
    (3, 'Charlie', 'Analyst', 55000.00);

-- 3. Wähle Daten aus der Tabelle aus
SELECT * FROM employees;

-- 4. Aktualisiere einen Datensatz
UPDATE employees 
SET salary = 65000.00 
WHERE name = 'Bob';

-- 5. Lösche einen Datensatz
DELETE FROM employees 
WHERE id = 3;

-- 6. Erstelle eine weitere Tabelle
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

-- 7. Füge Daten in die Tabelle "departments" ein
INSERT INTO departments (dept_id, dept_name) 
VALUES 
    (1, 'HR'),
    (2, 'IT');

-- 8. Ändere die Tabelle, um eine neue Spalte hinzuzufügen
ALTER TABLE employees 
ADD COLUMN dept_id INT;

-- 9. Aktualisiere die Tabelle "employees", um Mitarbeiter einer Abteilung zuzuweisen
UPDATE employees 
SET dept_id = 2 
WHERE id IN (1, 2);

-- 10. Verbinde die Tabellen "employees" und "departments"
SELECT e.name, e.position, d.dept_name 
FROM employees e 
JOIN departments d 
ON e.dept_id = d.dept_id;

-- 11. Sortiere das Ergebnis nach Gehalt in absteigender Reihenfolge
SELECT * FROM employees 
ORDER BY salary DESC;

-- 12. Lösche die Tabellen (Bereinigung)
DROP TABLE employees;
DROP TABLE departments;