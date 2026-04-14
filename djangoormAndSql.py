class Faculty(models.Model):
    faculty_name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Department(models.Model):
    department_name = models.CharField(max_length=100, unique=True)
    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.SET_NULL,
        null=True,
        related_name="departments"
    )
    created_at = models.DateTimeField(auto_now_add=True)


    CREATE TABLE faculty (
    id INT AUTO_INCREMENT PRIMARY KEY,
    faculty_name VARCHAR(100) UNIQUE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE department (
    id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(100) UNIQUE,
    faculty_id INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT fk_faculty
    FOREIGN KEY (faculty_id)
    REFERENCES faculty(id)
    ON DELETE SET NULL
);