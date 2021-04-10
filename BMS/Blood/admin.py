from django.contrib import admin
from Blood.models import BloodInventory, BloodRequest
# Register your models here.
admin.site.register(BloodInventory)
admin.site.register(BloodRequest)
