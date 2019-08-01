from django.db import models

# Create your models here.
class Note(models.Model):
    description = models.CharField(max_length= 255, blank=True)
    document = models.FileField(upload_to="documents/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "note_table"
