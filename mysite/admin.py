from django.contrib import admin
from mysite.models import Post
# Register your models here.

#放入細項
class PostAdmin(admin.ModelAdmin):
    list_display  = ('title','slug','pub_date')

#將上面新增的細項class加入
admin.site.register(Post,PostAdmin)