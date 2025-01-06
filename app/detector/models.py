from django.db import models
import random
import string
from django.utils.timezone import now

def generate_random_filename(instance, filename):
    timestamp = now().strftime('%Y%m%d_%H%M%S')  # Current time in 'YYYYMMDD_HHMMSS' format
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))  # Random 8-character string
    extension = filename.split('.')[-1]
    return f'photos/{timestamp}_{random_string}.{extension}'  # Unique filename using timestamp and random string


class Photo(models.Model):
    image = models.ImageField(upload_to=generate_random_filename)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.description or "Untitled"