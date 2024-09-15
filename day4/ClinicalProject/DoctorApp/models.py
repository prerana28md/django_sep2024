from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=200)
    specialization = models.CharField(max_length=200)
    years_of_experience = models.IntegerField()

    def __str__(self):
        return f'[id={self.id}, name={self.name}, specialization={self.specialization}, years_of_experience={self.years_of_experience}]'
    
