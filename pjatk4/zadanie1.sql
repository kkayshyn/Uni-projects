SELECT
    professor_id,
    first_name,
    last_name,
    birth_date,
    gender,
    email,
    phone_number,
    salary,
    department_id
FROM Professors;

SELECT
    course_name,
    credit_hours
FROM Courses;

SELECT
    first_name AS imie,
    last_name  AS nazwisko,
    tuition * 6 AS koszt_3_lata
FROM Students
LIMIT 80;

SELECT
    first_name AS imie,
    last_name  AS nazwisko,
    salary     AS pensja_miesieczna,
    (salary * 12) * 1.085 AS zarobki_roczne_z_premia
FROM Professors;

SELECT DISTINCT
    first_name
FROM Students
ORDER BY first_name ASC
LIMIT 80;

SELECT
    professor_id AS id_nauczyciela,
    first_name   AS imie,
    last_name    AS nazwisko,
    EXTRACT(YEAR FROM AGE(birth_date)) AS wiek
FROM Professors
ORDER BY wiek ASC;

SELECT
    first_name,
    last_name,
    tuition,
    email
FROM Students
ORDER BY last_name ASC, tuition DESC
LIMIT 80;
