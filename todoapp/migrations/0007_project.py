# Generated by Django 4.1.6 on 2023-03-10 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0006_tag_task_delete_tasks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('task_id', models.PositiveIntegerField()),
            ],
        ),
    ]
