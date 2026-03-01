class TruckStop(models.Model):
    opis_truckstop_id = models.PositiveIntegerField(
        unique=True,
        db_index=True
    )

    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    city = models.CharField(max_length=100, db_index=True)
    state = models.CharField(max_length=2, db_index=True)

    latitude = models.FloatField()
    longitude = models.FloatField()

    retail_price = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        db_index=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=["latitude", "longitude"]),
            models.Index(fields=["retail_price"]),
        ]
        ordering = ["retail_price"]

    def __str__(self):
        return f"{self.name} - {self.city}, {self.state}"


# second recommended .......................................................................

from django.db import models
from django.db.models import Avg

class TruckStop(models.Model):
    opis_truckstop_id = models.PositiveIntegerField(
        db_index=True
    )

    name = models.CharField(max_length=255)

    address = models.CharField(max_length=255)

    city = models.CharField(max_length=100, db_index=True)

    state = models.CharField(max_length=2, db_index=True)

    latitude = models.FloatField(db_index=True)
    longitude = models.FloatField(db_index=True)

    retail_price = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        db_index=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=["state", "city"]),
            models.Index(fields=["latitude", "longitude"]),
            models.Index(fields=["retail_price"]),
        ]

    def __str__(self):
        return f"{self.name} - {self.city}, {self.state}"