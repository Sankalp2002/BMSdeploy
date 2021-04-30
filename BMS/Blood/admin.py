from django.contrib import admin
from Blood.models import BloodInventory, BloodRequest,BRtype
# Register your models here.
admin.site.register(BloodInventory)
admin.site.register(BloodRequest)
admin.site.register(BRtype)
