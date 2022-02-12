from django.contrib import admin

from news.models import News
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ('origin', 'topic', 'pub_date', 'exp_date', 'status')
    list_filter = ('origin', 'status')
    search_fields = ('topic', 'origin', 'status')
    ordering = ('pub_date',)

admin.site.register(News, NewsAdmin)