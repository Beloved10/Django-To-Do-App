# Generated by Django 4.1.7 on 2023-02-24 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_remove_todo_complete_remove_todo_details_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
