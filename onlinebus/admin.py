from django.contrib import admin
from onlinebus.models import bus,consumer,Mymodel,driver


class busadmin(admin.ModelAdmin):
    busdetails=["bus_name","bus_no","route","start", "end","seats","balanseat","date","time"]

admin.site.register(bus,busadmin)

class consumeradmin(admin.ModelAdmin):
    consumerdetail=["name","age","address","phone","start","end","date","time"]

class driveradmin(admin.ModelAdmin):
    driverdetail=["drivername","age","contact_no","bus_no"]


admin.site.register(consumer,consumeradmin)
admin.site.register(Mymodel)
admin.site.register(driver,driveradmin)


