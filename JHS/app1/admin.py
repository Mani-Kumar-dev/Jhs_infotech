from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Placements
from app1.models import Contact,Blogs,Courses,Gallery,Registration
# Register your models here.
admin.site.register(Contact)
admin.site.register(Blogs)
admin.site.register(Courses)
admin.site.register(Gallery)
admin.site.register(Registration)

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Placements, MyModelAdmin)