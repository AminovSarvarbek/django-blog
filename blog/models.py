from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=255)
	date = models.DateField(auto_now_add=True)
	body = RichTextUploadingField()

	is_video = models.BooleanField(default=False)

	def __str__(self):
		return self.title


