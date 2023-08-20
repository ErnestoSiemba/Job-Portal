from django.db import models
from account.models import User

class Job(models.Model):
    JOB_TYPE_FULL_TIME = 'FT'
    JOB_TYPE_PART_TIME = 'PT'
    JOB_TYPE_INTERNSHIP = 'IN'
    
    JOB_TYPE_CHOICES = [
        (JOB_TYPE_FULL_TIME, 'Full Time'),
        (JOB_TYPE_PART_TIME, 'Part Time'),
        (JOB_TYPE_INTERNSHIP, 'Internship'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    type = models.CharField(max_length=1, choices=JOB_TYPE_CHOICES, default=JOB_TYPE_FULL_TIME), 
    company_name = models.CharField(max_length=100)
    company_description = models.TextField()
    website = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['id']
        
class Applicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user
    
    class Meta:
        ordering = ['id']
        unique_together = ['user', 'job']
        