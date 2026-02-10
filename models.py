from django.db import models

from jobs.models import Job
from students.models import Student


class JobApplication(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        SELECTED = "SELECTED", "Selected"
        REJECTED = "REJECTED", "Rejected"

    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="applications"
    )
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applications")
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.PENDING
    )
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("student", "job")
        ordering = ["-applied_at"]

    def __str__(self) -> str:
        return f"{self.student} -> {self.job}"
