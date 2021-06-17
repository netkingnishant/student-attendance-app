from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class attendance(models.Model):
    status_choices = [
        ('P', 'PRESENT'),
        ('A', 'ABSENT'),
    ]
    student_class = [
        ('1', '1️⃣'),
        ('2', '2️⃣'),
        ('3', '3️⃣'),
        ('4', '4️⃣'),
        ('5', '5️⃣'),
        ('6', '6️⃣'),
        ('7', '7️⃣'),
        ('8', '8️⃣'),
        ('9', '9️⃣'),
        ('10', '🔟'),
    ]
    Name = models.CharField(max_length=50)
    Status = models.CharField(max_length=2, choices=status_choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    Class = models.CharField(max_length=2, choices=student_class)
