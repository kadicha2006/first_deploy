from django.db import models

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=32)
    description = models.TextField()
    address = models.CharField(max_length=32)
    city = models.CharField(max_length=16)
    country = models.CharField(max_length=16)

    def __str__(self):
        return self.hotel_name


class Image(models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='hotel_images/')

class Room(models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    room_number=models.PositiveSmallIntegerField(default=0)
    capacity=models.PositiveSmallIntegerField(default=0)
    price_per_night=models.PositiveIntegerField(default=0)

class ImageRoom(models.Model):
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='room_images/')


class Booking(models.Model):
    user=models.CharField(max_length=16)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    check_in_date=models.DateTimeField()
    check_out_date=models.DateTimeField()
    total_price=models.PositiveIntegerField(default=0)


