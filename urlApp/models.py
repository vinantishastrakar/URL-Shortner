from django.db import models
import random
import string

# Create your models here.
class DataUrl(models.Model):
    longurl = models.URLField(max_length=2000)
    shorturl = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return "Short URL for: " + self.longurl + "is: " + self.shorturl
    
    @staticmethod
    def generate_shorturl():
        length = 10
        while True:
            shorturl = "".join(random.choices(string.ascii_letters + string.digits, k=length))
            if not DataUrl.objects.filter(shorturl=shorturl).exists():
                return shorturl
            super().save()