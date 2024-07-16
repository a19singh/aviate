from django.db import models

class Applicant(models.Model):
    """
    Django model to save details of the applicant 
    and application timestamp
    """
    class Gender(models.TextChoices):
        Male="Male"
        Female="Female"
        Other="Other"

    class Status(models.TextChoices):
        Applied = "Applied"
        Shortlisted = "Shortlisted"
        Rejected = "Rejected"

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    experience = models.IntegerField()
    gender = models.CharField(
        max_length=6,
        choices=Gender.choices
    ) # create enum
    contact = models.IntegerField()
    current_salary = models.IntegerField()
    expected_salary = models.IntegerField()
    status = models.CharField(
        max_length=11,
        choices=Status.choices,
        default=Status.Applied
    ) # create enum
    cdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


