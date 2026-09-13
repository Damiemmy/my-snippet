from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


# ======================================================
# Keep all previous models (Faculty, Department, Program,
# ProgramOption, AcademicSession, Level, Semester,
# Course, CourseOffering) exactly as we finalized them
# ======================================================


class Material(models.Model):
    """
    Main material model – linked to a specific CourseOffering
    """
    MATERIAL_TYPES = [
        ("note", "Lecture Note"),
        ("slide", "Slide / Presentation"),
        ("past_question", "Past Question"),
        ("assignment", "Assignment"),
        ("textbook", "Textbook / Reading Material"),
        ("video", "Video"),
        ("other", "Other"),
    ]

    course_offering = models.ForeignKey(
        CourseOffering,
        on_delete=models.CASCADE,
        related_name="materials",
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    material_type = models.CharField(
        max_length=20,
        choices=MATERIAL_TYPES,
        default="note",
    )

    file = models.FileField(
        upload_to="materials/%Y/%m/",
        blank=True,
        null=True,
    )
    external_link = models.URLField(
        blank=True,
        null=True,
        help_text="Use this if the material is hosted on Google Drive, YouTube, etc.",
    )

    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="uploaded_materials",
    )

    is_approved = models.BooleanField(
        default=False,
        help_text="Admin/moderator must approve before it becomes public",
    )
    is_active = models.BooleanField(default=True)

    download_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def clean(self):
        if not self.file and not self.external_link:
            raise ValidationError("You must either upload a file or provide an external link.")

    def __str__(self):
        return f"{self.title} ({self.course_offering})"


class MaterialReport(models.Model):
    """
    Allows students to report bad/wrong/outdated materials
    """
    material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        related_name="reports",
    )
    reported_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Report on {self.material.title}"


class MaterialRating(models.Model):
    """
    Simple rating system so good materials rise to the top
    """
    material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        related_name="ratings",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    rating = models.PositiveSmallIntegerField()  # 1 to 5
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("material", "user")

    def __str__(self):
        return f"{self.rating} stars - {self.material.title}"


'''

Key Design Decisions



Feature:                              Why it is useful:

is_approvedPrevents           spam / wrong materials from going public immediately
material_type           Makes filtering easy (Past Questions, Notes, Videos, etc.)
file + external_link           Supports both uploaded files and Google Drive / YouTube links download_count                      Helps show popular materials
MaterialReport                        Community moderation
MaterialRating                          Quality ranking


How the flow will work

Student selects:
Faculty → Department → Program → Level → Semester → Course
Student uploads material (file or link)
Material stays pending (is_approved=False)
Admin / Moderator reviews and approves
Once approved, it becomes visible to everyone

'''