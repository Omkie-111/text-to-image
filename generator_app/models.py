from django.db import models


class GeneratedImage(models.Model):
    prompt = models.TextField()
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.prompt
