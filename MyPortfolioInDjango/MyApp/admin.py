from django.contrib import admin
from .models import MySkill,Service

class MySkillAdmin(admin.ModelAdmin):
    list_display = ('id','skill','percent')
    
admin.site.register(MySkill,MySkillAdmin)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id','title','description')

