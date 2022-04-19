from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django_resized import ResizedImageField


# Create your models here.
CATEGORY_CHOICES = (
    ('English', 'English'),
    ('Hindi', 'Hindi'),
    ('Marathi', 'Marathi'),  
)
class Post(models.Model):
	category = models.CharField(choices=CATEGORY_CHOICES, max_length=10, null=True, blank=True)
	title = models.CharField(max_length = 100)
	overview = models.TextField()
	slug = models.SlugField(null=True, blank=True)
	body_text = RichTextField(null=True)
	time_upload = models.DateTimeField(auto_now_add = True)
	thumbnail = ResizedImageField(size=[1200, 1200], quality=75, upload_to='thumbnails', null=True, blank=True)
	publish = models.BooleanField()
	read = models.IntegerField(default = 0)

	class Meta:
		ordering = ['-pk']

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Post, self).save(*args, **kwargs)
