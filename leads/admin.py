from django.contrib import admin

from leads.models import  Lead, User, Agent


admin.site.register(User)
admin.site.register(Lead)
admin.site.register(Agent)
