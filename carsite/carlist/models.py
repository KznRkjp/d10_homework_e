from django.db import models

# Create your models here.

class Modeltype(models.Model):
    # это поле необходимо для связи с таблицей пользователя
    # текст сообщения пользователя.
    model_type = models.CharField(max_length = 255)

    def __str__(self):
        return self.model_type

class Manufacturer(models.Model):
    manufacturer = models.CharField(max_length = 255)

    def __str__(self):
        return self.manufacturer

class Productionyear(models.Model):
    year = models.IntegerField()

    def __str__(self):
        return str(self.year)


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    production_year = models.ForeignKey(Productionyear, on_delete=models.CASCADE)
    models_type = models.ForeignKey(Modeltype, on_delete=models.CASCADE)
    MANUAL = 'M'
    AUTOMATIC = 'A'
    ROBOT = 'R'
    GEARBOX_CHOICES =[
        (MANUAL, 'Manual'),
        (AUTOMATIC, 'Automatic'),
        (ROBOT, 'Robot'),
    ]
    gearbox_type = models.CharField(max_length=2, choices = GEARBOX_CHOICES, default = AUTOMATIC)
    color = models.CharField(max_length = 255)

    def __str__(self):
        return str(self.manufacturer)
        # return f'{self.manufacturer} ({self.models_type}, {self.production_year}, {self.color})'
