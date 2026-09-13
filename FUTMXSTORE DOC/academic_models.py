from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


class Faculty(models.Model):
    name = models.CharField(max_length=150, unique=True)
    short_name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Faculties"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Department(models.Model):
    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.PROTECT,
        related_name="departments",
    )
    name = models.CharField(max_length=150)
    short_name = models.CharField(max_length=20, blank=True)
    slug = models.SlugField()
    is_active = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["faculty", "name"],
                name="unique_department_per_faculty",
            ),
            models.UniqueConstraint(
                fields=["faculty", "slug"],
                name="unique_slug_per_faculty",
            ),
        ]
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.faculty.short_name})"


class Program(models.Model):
    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name="programs",
    )
    name = models.CharField(max_length=150)
    slug = models.SlugField()
    degree = models.CharField(max_length=50, default="B.Tech")
    duration_years = models.PositiveSmallIntegerField(default=5)
    is_active = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["department", "name"],
                name="unique_program_per_department",
            ),
            models.UniqueConstraint(
                fields=["department", "slug"],
                name="unique_program_slug_per_department",
            ),
        ]
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} - {self.department}"


class ProgramOption(models.Model):
    """
    For programs that have specializations/options.
    Example: Science Education → Biology Education, Chemistry Education, etc.
    """
    program = models.ForeignKey(
        Program,
        on_delete=models.PROTECT,
        related_name="options",
    )
    name = models.CharField(max_length=150)
    slug = models.SlugField()
    is_active = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["program", "name"],
                name="unique_option_per_program",
            ),
            models.UniqueConstraint(
                fields=["program", "slug"],
                name="unique_option_slug_per_program",
            ),
        ]
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.program.name})"


class AcademicSession(models.Model):
    name = models.CharField(max_length=20, unique=True)  # e.g. 2025/2026
    is_current = models.BooleanField(default=False)

    class Meta:
        ordering = ["-name"]

    def save(self, *args, **kwargs):
        # Ensure only one session is marked as current
        if self.is_current:
            AcademicSession.objects.filter(is_current=True).update(is_current=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.CharField(max_length=20, unique=True)  # 100, 200, 300...
    order = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name


class Semester(models.Model):
    name = models.CharField(max_length=30, unique=True)  # First Semester, Second Semester
    order = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name


class Course(models.Model):
    code = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=200)
    units = models.PositiveSmallIntegerField(default=2)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["code"]

    def __str__(self):
        return f"{self.code} - {self.title}"


class CourseOffering(models.Model):
    """
    Links a Course to a specific Program + Level + Semester + Session.
    Option is optional (only used when the program has specializations).
    """
    course = models.ForeignKey(
        Course,
        on_delete=models.PROTECT,
        related_name="offerings",
    )
    program = models.ForeignKey(
        Program,
        on_delete=models.PROTECT,
        related_name="course_offerings",
    )
    option = models.ForeignKey(
        ProgramOption,
        on_delete=models.PROTECT,
        related_name="course_offerings",
        null=True,
        blank=True,
    )
    level = models.ForeignKey(
        Level,
        on_delete=models.PROTECT,
        related_name="course_offerings",
    )
    semester = models.ForeignKey(
        Semester,
        on_delete=models.PROTECT,
        related_name="course_offerings",
    )
    session = models.ForeignKey(
        AcademicSession,
        on_delete=models.PROTECT,
        related_name="course_offerings",
    )
    is_compulsory = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["course", "program", "level", "semester", "session", "option"],
                name="unique_course_offering",
            ),
        ]

    def clean(self):
        if self.option and self.option.program_id != self.program_id:
            raise ValidationError({
                "option": "This option does not belong to the selected program."
            })

    def __str__(self):
        return f"{self.course.code} → {self.program.name} ({self.level.name})"


class Material(models.Model):
    course_offering = models.ForeignKey(
        CourseOffering,
        on_delete=models.CASCADE,
        related_name="materials",
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to="materials/%Y/%m/")
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="uploaded_materials",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title