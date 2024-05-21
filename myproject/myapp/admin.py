from django.contrib import admin

# Register your models here.

from .models import ImagePrediction


# # Add the model to the admin interface to view and manage the records.
# @admin.register(ImagePrediction)
# class ImagePredictionAdmin(admin.ModelAdmin):
#     list_display = ('image_url', 'timestamp')
#     readonly_fields = ('timestamp',)
