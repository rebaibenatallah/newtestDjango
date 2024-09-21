from django.contrib import admin
from .models import User_portfolio
from .models import Skills
from .models import Project
from .models import Skill
# Register your models here.
admin.site.register(User_portfolio)
admin.site.register(Skills)
admin.site.register(Project)
admin.site.register(Skill)