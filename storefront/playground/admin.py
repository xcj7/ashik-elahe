# Register your models here.
from django.contrib import admin
from .models import MyModel
from .models import User

admin.site.register(MyModel)
admin.site.register(User)