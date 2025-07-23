from django.contrib import admin
from .models import Students, ExtraCurricular, Address

# Register your models here.

admin.site.register(Students)
admin.site.register(ExtraCurricular)
admin.site.register(Address)
