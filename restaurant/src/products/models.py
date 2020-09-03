import random
import os
from django.db import models


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    # print(instance)
    # print(filename)
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
            new_filename=new_filename,
            final_filename=final_filename
            )


class Product(models.Model):
    id              = models.IntegerField(primary_key=True)
    title           = models.CharField(max_length=120)
    description     = models.TextField()
    price           = models.DecimalField(decimal_places=3, max_digits=20, null=True)
    image           = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    def __str__(self):
        return self.title