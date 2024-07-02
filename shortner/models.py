from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone

# Create your models here.


class Url(models.Model):
    link = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=10, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    visit_count = models.IntegerField(default=0)
    expire_date = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        if not self.expire_date:
            self.expire_date = self.created_at + timedelta(days=30)
        super(Url, self).save(*args, **kwargs)

    def __str__(self):
        return self.uuid
