from django.contrib import admin
from busapp.models import Driver,User,Customer,Account
class DriverAdmin(admin.ModelAdmin):
    driverdetails=["drivername","age","contact_no","bus_no"]

class UserAdmin(admin.ModelAdmin):
    userdetails=["user_id","email","name","password"]


class CustomerAdmin(admin.ModelAdmin):
    consumerdetail=["name","age","address","phone","start","end","date","time"]

admin.site.register(Driver,DriverAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Account)

# Register your models here.
