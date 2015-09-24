import datetime

from django.db import models
from django.utils import timezone

class Post(models.Model):
	title = models.CharField(max_length=255)
	blog_text = models.TextField()
	pub_date = models.DateTimeField('date published')
	author = models.CharField(max_length=255)


	def __str__(self):
		return self.title

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'