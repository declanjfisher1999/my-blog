from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class CVPost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    profile = models.TextField()
    employment = models.TextField()
    education = models.TextField()
    skills = models.TextField()
    ecActivities = models.TextField()
    hobbies = models.TextField()
    references = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name