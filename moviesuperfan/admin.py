from django.contrib import admin

# Register your models here.
from . models import UserMovie, UserProfile, NowPlayingMovie

admin.site.register(UserMovie)
admin.site.register(UserProfile)
admin.site.register(NowPlayingMovie)
# admin.site.register(Comments)
