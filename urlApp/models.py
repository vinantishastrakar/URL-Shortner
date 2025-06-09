from django.db import models
import random
import string

# Create your models here.
class DataUrl(models.Model):
    longurl = models.URLField(max_length=2000)
    shorturl = models.CharField(max_length=20, blank = True)

    def generate_shorturl(self):
        length = 10
        while True:
            shorturl = "".join(random.choices(string.ascii_letters + string.digits, k=length))
            if not DataUrl.objects.filter(shorturl=shorturl).exists():
                return shorturl

    def save(self, *args, **kwargs):
        if not self.shorturl:
            self.shorturl = self.generate_shorturl()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.longurl
    
   