from django.db import models


class Execution(models.Model):
    task = models.ForeignKey(
        "task.Task",
        verbose_name="task",
        on_delete=models.PROTECT
    )
    start_at = models.DateTimeField(
        verbose_name='execution start timestamp'
    )
    end_at = models.DateTimeField(
        verbose_name='execution end timestamp'
    )
    stdout = models.TextField(
        verbose_name='reaction script stdout',
        null=True
    )
    stderr = models.TextField(
        verbose_name='reaction script stderr',
        null=True
    )
