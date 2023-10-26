from django.contrib import admin

from home.models import *
from home.models import Signup
from home.models import Content
# Register your models here.
 
admin.site.register(Product)
admin.site.register(Signup)
admin.site.register(Content)