from django.contrib import admin

# Register your models here.
from examapp.models import EBooksModel
from examapp.models import students, skills, projects
from examapp.models import adminmodel


admin.site.register(EBooksModel)
admin.site.register(students)
admin.site.register(adminmodel)
admin.site.register(skills)
admin.site.register(projects)