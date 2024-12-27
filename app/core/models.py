from django.db import models

class ImageUpload(models.Model):
    title = models.CharField(max_length = 255)
    image = models.ImageField(upload_to='images',blank=True,null=True)

    def __str__(self):
        return self.title