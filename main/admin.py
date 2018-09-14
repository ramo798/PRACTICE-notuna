from django.contrib import admin
from .models import Userinfor
from .models import Post


class UserinforAdmin(admin.ModelAdmin):
    list_display = ('userid', 'profname', 'profpic', 'proftext', 'usiusi')

class PostAdmin(admin.ModelAdmin):
    list_display = ('userids', 'posttext')


admin.site.register(Userinfor, UserinforAdmin)
admin.site.register(Post, PostAdmin)
