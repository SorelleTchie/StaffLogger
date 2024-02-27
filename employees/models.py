from django.db import models
from django.utils.crypto import get_random_string
from datetime import timedelta
from django.utils import timezone


# Create your models here.
class Employee(models.Model):
    id = models.CharField(primary_key=True, max_length=12)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = get_random_string(length=12, allowed_chars='0123456789')
            super(Employee, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class AttendanceRecord(models.Model):
    employee= models.ForeignKey(Employee, on_delete=models.CASCADE)
    check_in_time = models.DateTimeField(null=True, blank=True)
    check_out_time = models.DateTimeField(null=True, blank=True)
    message = models.TextField(blank=True)


    def check_in(self):
        self.check_in_time = timezone.now()
        self.save()

    def check_out(self):
        self.check_out_time = timezone.now()
        self.save()

    def total_time(self):
        if self.check_in_time and self.check_out_time:
            return self.check_out_time - self.check_in_time
        return None 


