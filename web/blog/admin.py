from django.contrib import admin

from .models import Post

class BlogAdmin(admin.ModelAdmin):
	list_display = ('title', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_field = ['question_text']
	
admin.site.register(Post)


