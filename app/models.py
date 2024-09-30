from django.db import models

class File(models.Model):
    file = models.FileField(upload_to="files")

class Person(models.Model):
    enrollee_id = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    city_development_index = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    enrolled_university = models.CharField(max_length=100, blank=True, null=True)
    education_level = models.CharField(max_length=100, blank=True, null=True)
    major_discipline = models.CharField(max_length=100, blank=True, null=True)
    experience = models.FloatField(blank=True, null=True)
    company_size = models.CharField(max_length=100, blank=True, null=True)
    company_type = models.CharField(max_length=100, blank=True, null=True)
    last_new_job = models.IntegerField(blank=True, null=True)
    training_hours = models.IntegerField(blank=True, null=True)
    target = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"Person {self.enrollee_id}"
