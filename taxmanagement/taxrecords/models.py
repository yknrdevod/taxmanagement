from django.db import models

class TaxRecord(models.Model):
    assessment_year = models.IntegerField()
    assessment_number = models.IntegerField()
    door_number = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255)
    relative_name = models.CharField(max_length=255)
    house_tax = models.FloatField()
    library_cess = models.FloatField()
    water_tax = models.FloatField()
    lightning_tax = models.FloatField()
    fire_tax = models.FloatField()
    sports_cess = models.FloatField()
    drainage_tax = models.FloatField()
    total_current_year_tax = models.FloatField()
    arrear_tax = models.FloatField()
    total_tax = models.FloatField()
    cluster_number = models.IntegerField()
    payment = models.BooleanField()

    def __str__(self):
        return f"{self.assessment_year} - {self.assessment_number}"