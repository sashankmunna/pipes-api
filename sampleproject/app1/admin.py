from django.contrib import admin
from app1.models import pipes
# Register your models here.
class pipesadmin(admin.ModelAdmin):
	list_display=['Pipe_name','Stock','Grade','colour','size','quality']
admin.site.register(pipes,pipesadmin)