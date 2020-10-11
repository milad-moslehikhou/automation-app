from django.db import models


class Execution(models.Model):
    task = models.ForeignKey(
        "task.Task",
        verbose_name="task",
        on_delete=models.PROTECT
    )
    start_at = models.DateTimeField(
        verbose_name='start'
    )
    end_at = models.DateTimeField(
        verbose_name='end'
    )
    stdout = models.TextField(
        verbose_name='reaction script stdout',
        null=True
    )
    stderr = models.TextField(
        verbose_name='reaction script stderr',
        null=True
    )
