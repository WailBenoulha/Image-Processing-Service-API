from rest_framework.serializers import ModelSerializer,ImageField
from .models import ImageUpload

class ImageUploadSerializer(ModelSerializer):
    image = ImageField()
    class Meta:
        model = ImageUpload
        fields = ['id','image']