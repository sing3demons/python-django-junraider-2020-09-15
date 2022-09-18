from django.db import models

# Create your models here.


class Subscription(models.Model):
    CONST_STATUS = [
        ('unapproved', 'Unapproved'),
        ('approved', 'Approved'),
        ('banned', 'Banned'),
    ]
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=60, unique=True)
    status = models.CharField(
        max_length=15, choices=CONST_STATUS, default='unapproved')
    register_at = models.DateTimeField(auto_now_add=True)
