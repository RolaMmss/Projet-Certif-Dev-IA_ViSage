from django.db import models

# In case we don't want to save the images and their predictions
# class ApiModel(models.Model):
#     url = models.URLField(
#         max_length=100,
#         blank=False,
#         null=True,
#     )
    
# Add a model to store the image information and predictions
class ImagePrediction(models.Model):
    image_url = models.URLField()
    prediction_data = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image URL: {self.image_url} - Predictions: {self.prediction_data}"

# After adding the model, run the migrations to create the table in your database.
# python manage.py makemigrations
# python manage.py migrate