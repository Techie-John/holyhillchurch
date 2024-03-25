from django.contrib import admin
from .models import Male, Offering, Female, ChildrenFemale, ChildrenMale, Attendance

admin.site.register(Male)
admin.site.register(Female)
admin.site.register(ChildrenFemale)
admin.site.register(ChildrenMale)
admin.site.register(Attendance)
admin.site.register(Offering)
# Register your models here.
