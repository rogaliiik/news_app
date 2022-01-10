from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    title = models.CharField(max_length=100, )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']
        permissions = (
            ['can_publish', "может публиковать"],
        )


class Commentary(models.Model):
    STATUS_CHOICE = [
        ('d', 'delete_by_admin'),
    ]
    user_name = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, default=None, null=True)

    news = models.ForeignKey(News, default=None, on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.id}, {self.news}'
