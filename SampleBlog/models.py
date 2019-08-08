from django.db import models

# Create your models here.


class Level (models.Model):
    level = models.CharField(max_length=255)

    class Meta:
        db_table = 'Level'

    def __str__(self):
        return self.level


class Subject(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'Subject'

    def __str__(self):
        return self.name


class Note(models.Model):

    description = models.CharField(max_length= 255, blank=True)
    document = models.FileField(upload_to="documents/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        db_table = "note_table"

