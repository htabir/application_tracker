from django.db import models

from core.models import AbstractTimeStampModel


class Group(AbstractTimeStampModel):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class ApplicationStatus(AbstractTimeStampModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(
        verbose_name='Created By',
        to='accounts.User',
        on_delete=models.CASCADE,
        related_name='application_statuses'
    )

    def __str__(self):
        return self.name


class Application(AbstractTimeStampModel):
    application_id = models.CharField(max_length=255, unique=True)
    subject = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    note = models.TextField(null=True, blank=True)
    applicant_email = models.EmailField(null=True, blank=True)
    applicant_name = models.CharField(max_length=255, null=True, blank=True)
    applicant_phone = models.CharField(max_length=255, null=True, blank=True)
