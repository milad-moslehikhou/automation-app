# Generated by Django 3.1.2 on 2020-10-11 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Execution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_at', models.DateTimeField(verbose_name='start')),
                ('end_at', models.DateTimeField(verbose_name='end')),
                ('stdout', models.TextField(null=True, verbose_name='reaction script stdout')),
                ('stderr', models.TextField(null=True, verbose_name='reaction script stderr')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='task.task', verbose_name='task')),
            ],
        ),
    ]