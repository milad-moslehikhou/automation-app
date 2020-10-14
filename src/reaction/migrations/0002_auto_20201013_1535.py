# Generated by Django 2.2 on 2020-10-13 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reaction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reaction',
            name='script',
            field=models.TextField(verbose_name='script'),
        ),
        migrations.AlterField(
            model_name='reaction',
            name='subject',
            field=models.CharField(max_length=255, unique=True, verbose_name='subject'),
        ),
    ]
