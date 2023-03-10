from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Task(models.Model):
    STATUS_CHOICES = (
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('done', 'Done')
    )
    summary = models.CharField(max_length=255)
    description = models.TextField(max_length=255, null=True,)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.summary}, {self.description} {self.status}'


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.task_id.summary}'
