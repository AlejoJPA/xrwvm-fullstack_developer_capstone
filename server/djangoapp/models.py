from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

#Car make model
class CarMake(models.Model):

    #car maker name an description
    name = models.CharField(max_length=30)
    description = models.TextField() #description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

#Car Model model
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

    #Many-To-One relationship to CarMake model
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)

    #car model name, type(car_type), release year(year)
    name = models.CharField(max_length=100)    
    car_type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(default=2023,
        validators=[MinValueValidator(2015),
                     MaxValueValidator(2023)
        ])

    #Report creation date (created_at)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f'Car name: {self.name} - Car type: {self.car_type} – Release Date: {self.year}'
