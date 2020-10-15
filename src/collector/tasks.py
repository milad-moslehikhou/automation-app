import os
import subprocess
import tempfile
from datetime import datetime
from django.utils import timezone

from .celery import app
from action.models.action import Action
from task.models.task import Task
from reaction.models.reaction import Reaction
from execution.models.execution import Execution


@app.task
def process_data(data):
    actions = Action.objects.all()
    for action in actions:
        if data['data'] == action.match_case:
            task = Task.objects.get(action_id__exact=action.id)
            if task is not None:
                execute(task=task)


def execute(task):
    reaction = Reaction.objects.get(id__exact=task.reaction.id)
    start_at = datetime.now(tz=timezone.utc)
    try:
        script = tempfile.NamedTemporaryFile(mode='w', delete=False)
        script.write(reaction.script)
        script.close()
        cmd = "python " + script.name
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, stderr = process.communicate(timeout=10)
        os.unlink(script.name)
        end_at = datetime.now(tz=timezone.utc)
        if stderr:
            execution = Execution(task=task, start_at=start_at, end_at=end_at, stdout=stdout,
                                  stderr=stderr,
                                  status=Execution.STATUS_ERROR)
            execution.save()
        elif stdout:
            execution = Execution(task=task, start_at=start_at, end_at=end_at, stdout=stdout,
                                  stderr=stderr,
                                  status=Execution.STATUS_OK)
            execution.save()
    except Exception as e:
        execution = Execution(task=task, start_at=start_at, end_at=None, stdout=None, stderr=str(e),
                              status=Execution.STATUS_EXCEPTION)
        execution.save()
