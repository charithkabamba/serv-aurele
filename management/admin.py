from django.contrib import admin

from .models import *

# Register your models here()

admin.site.register(Messages)
admin.site.register(Subscribers)
admin.site.register(Portfolio)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Service)
admin.site.register(Newsletter)
admin.site.register(Teams)
# projects
admin.site.register(ProjectCategory)
admin.site.site_header = "Management Aurele Admin Portal"
admin.site.site_title = "Management Admin Portal"



