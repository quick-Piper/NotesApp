from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    content = models.TextField(blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('note-detail', kwargs={'pk': self.pk})
 
    class Meta:
        ordering = ('-modified_at',)