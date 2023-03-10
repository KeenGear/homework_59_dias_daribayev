# Generated by Django 4.1.6 on 2023-02-16 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_alter_tasks_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='description',
            field=models.TextField(default='Description', max_length=100, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='status',
            field=models.CharField(choices=[('Ongoing', 'Ongoing'), ('Completed', 'Completed'), ('Held', 'Held')], default='Ongoing', max_length=20),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='text',
            field=models.TextField(max_length=100, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
    ]
