from django.db import models

STATUS_CHOICES = (
    (0, "New"),
    (0, "Done"),
    (0, "Doing"),
)


# Create your models here.
class NewTask(models.Model):
    name=models.CharField(max_length=40)
    description = models.TextField()
    data_create = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES)
    def __str__(self):
        return self.name