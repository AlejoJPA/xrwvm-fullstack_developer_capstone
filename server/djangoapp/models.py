from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Car make model
class CarMake(models.Model):
    # Car maker name and description
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.name


# Car model
class CarModel(models.Model):
    # Car type choices
    SEDAN = 'SEDAN'
    SUV = 'SUV'
    WAGON = 'WAGON'
    HATCHBACK = 'HATCHBACK'
    COUPE = 'COUPE'
    TRUCK = 'TRUCK'

    CAR_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (HATCHBACK, 'Hatchback'),
        (COUPE, 'Coupe'),
        (TRUCK, 'Truck'),
    ]

    # Many-To-One relationship to CarMake model
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)

    # Car model name, type, and release year
    name = models.CharField(max_length=100)
    car_type = models.CharField(
        max_length=10,
        choices=CAR_TYPES,
        default=SUV,
    )
    year = models.IntegerField(
        default=2023,
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023),
        ],
    )

    # Report creation date
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.name
