from django.contrib import admin

# Register your models here.
from . models import UserMovie, UserProfile, NowPlayingMovie, Comments

admin.site.register(UserMovie)
admin.site.register(UserProfile)
admin.site.register(NowPlayingMovie)
admin.site.register(Comments)
