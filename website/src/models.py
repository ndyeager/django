from django.db import models

class Person(models.Model): 
	first_name = models.CharField()
	last_name = models.CharField()

	about_me = models.TextArea()

	def __str__(self): 
		return self.first_name






