from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Commentary(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='posted_comments',
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    task = models.ForeignKey('Task', on_delete=models.CASCADE)


class Task(models.Model):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='authored_tasks',
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=1000)
    description = models.TextField(blank=True)
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="assigned_tasks",
        null=True
    )

    class Status(int, models.Choices):
        IN_PROGRESS = 0, _("In Progress")
        FINISHED = 1, _("Finished")

    status = models.IntegerField(
        choices=Status.choices,
        default=Status.IN_PROGRESS,
        verbose_name=_('task status')
    )
