from django.db import models

class Todo(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50, unique=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title