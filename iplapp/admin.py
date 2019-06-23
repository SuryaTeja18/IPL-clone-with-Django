from django.contrib import admin

# Register your models here.
from .models import Matches,Deliveries
admin.site.register(Matches)
admin.site.register(Deliveries)
