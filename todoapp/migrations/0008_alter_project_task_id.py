# Generated by Django 4.1.6 on 2023-03-10 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0007_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='task_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todoapp.task'),
        ),
    ]
