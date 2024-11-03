import pathlib
import uuid
from django.utils.text import slugify


def image_path(instance, filename, folder_name) -> pathlib.Path:
    name = instance.first_name if hasattr(instance, "first_name") else instance.name
    filename = f"{slugify(name)}-{uuid.uuid4()}{pathlib.Path(filename).suffix}"
    return pathlib.Path(f"upload/images/{folder_name}") / pathlib.Path(filename)


def actor_image_path(instance, filename):
    return image_path(instance, filename, "actors")


def theatre_hall_image_path(instance, filename):
    return image_path(instance, filename, "theatre_halls")