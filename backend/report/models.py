from django.db import models
#from django.contrib.auth.models import User
from django.conf import settings
from django.db import models



class Report(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    department = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=50, null=True)
    report_type = models.CharField( max_length=50, null=True)
    contact = models.CharField(max_length=9)
    user_comment = models.TextField(max_length=150, blank=True, null=True)
    admin = models.CharField(max_length=50, blank=True, null=True)
    admin_comment = models.TextField(max_length=250, blank=True, null=True)

    status_options = (
        ('received', 'received'),
        ('approved', 'approved'),
        ('completed', 'completed'),
        ('refused', 'refused')
    )

    status = models.CharField(max_length=20, choices=status_options, default='received')
    received_date = models.DateTimeField(auto_now_add=True)
    approved_date = models.DateTimeField(blank=True, null=True)
    completed_date = models.DateTimeField(blank=True, null=True)
    refused_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'Report {self.id} by {self.user.username}'
        