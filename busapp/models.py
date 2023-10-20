from django.db import models

class BusRoute(models.Model):
    route_name = models.CharField(max_length=255)
    route_length = models.DecimalField(max_digits=10, decimal_places=2)
    time_to_complete = models.PositiveIntegerField()  # Time in minutes
    stop_interval = models.PositiveIntegerField()  # Stop interval in minutes

class Driver(models.Model):
    driver_name = models.CharField(max_length=255)
    health_condition = models.CharField(max_length=255)
    assigned_routes = models.ManyToManyField(BusRoute)
    days_off = models.DateField()

class Bus(models.Model):
    bus_number = models.CharField(max_length=255)
    route = models.ForeignKey(BusRoute, on_delete=models.CASCADE)
    primary_driver_1 = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='primary_driver_1_for_buses')
    primary_driver_2 = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='primary_driver_2_for_buses')
    backup_driver_1 = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='backup_driver_1_for_buses')
    backup_driver_2 = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='backup_driver_2_for_buses')

class Stop(models.Model):
    stop_name = models.CharField(max_length=255)
    route = models.ForeignKey(BusRoute, on_delete=models.CASCADE)
    stop_interval = models.PositiveIntegerField()  # If different from the route's standard interval
