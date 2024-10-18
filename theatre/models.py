import pathlib
import uuid

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify


User = get_user_model()


def image_path(instance, filename, folder_name) -> pathlib.Path:
    name = instance.first_name if hasattr(instance, "first_name") else instance.name
    filename = f"{slugify(name)}-{uuid.uuid4()}{pathlib.Path(filename).suffix}"
    return pathlib.Path(f"upload/images/{folder_name}") / pathlib.Path(filename)


def actor_image_path(instance, filename):
    return image_path(instance, filename, "actors")


def theatre_hall_image_path(instance, filename):
    return image_path(instance, filename, "theatre_halls")


class Actor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(null=True, upload_to=actor_image_path)


class Genre(models.Model):
    name = models.CharField(max_length=50)


class Play(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()


class TheatreHall(models.Model):
    name = models.CharField(max_length=50)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()
    image = models.ImageField(null=True, upload_to=theatre_hall_image_path)


class Performance(models.Model):
    play = models.ForeignKey(Play, on_delete=models.CASCADE)
    theatre_hall = models.ForeignKey(TheatreHall, on_delete=models.CASCADE)
    show_time = models.DateTimeField()


class Reservation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Ticket(models.Model):
    row = models.IntegerField()
    seat = models.IntegerField()
    performance = models.ForeignKey(Performance, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
