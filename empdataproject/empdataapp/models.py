from django.db import models

class empdata(models.Model):
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Email_id = models.EmailField(max_length=100)
    Mobile_number = models.BigIntegerField()
    Qualification = models.CharField(max_length=100)
    Stream = models.CharField(max_length=100)
    Percentage = models.IntegerField()
    Passed_out_year = models.IntegerField()
    Skill_set = models.CharField(max_length=100)
    