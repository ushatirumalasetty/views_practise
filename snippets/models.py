from django.db import models

class Snippet(models.Model):
    title = models.TextField()
    code = models.TextField()
    
