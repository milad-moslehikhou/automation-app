from django.db import models


class Execution(models.Model):

    STATUS_OK = 'OK'
    STATUS_ERROR = 'ERROR'
    STATUS_EXCEPTION = 'EXCEPTION'
    STATUS_CHOICES = [
        (STATUS_OK, 'ok'),
        (STATUS_ERROR, 'error'),
        (STATUS_EXCEPTION, 'exception')
    ]

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
    status = models.CharField(
        verbose_name='status',
        choices=STATUS_CHOICES,
        max_length=9,
    )

    def __str__(self):
        return "{}_{}".format(self.id, self.task.subject)

