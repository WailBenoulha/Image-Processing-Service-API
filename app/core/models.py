from django.db import models

class ImageUpload(models.Model):
    title = models.CharField(max_length = 255,editable=False)
    image = models.ImageField(upload_to='images',blank=True,null=True)

    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        self.title = self.image.name
        return super(ImageUpload,self).save(*args,**kwargs)