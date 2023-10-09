from django.contrib import admin
from .models import User, Location, ScoutUser, ListingSpecialistUser, PropManagerUser, LandlordUser,Property, ScoutedProperty, ElectricitySupply, SavedProperty, Payment, Inflow, Outflow

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "gender")


class ListingSpecialistUserAdmin(admin.ModelAdmin):
    list_display = ("id", "maritalStatus", "idtype", "bank_name", "bank_acct_num")


class ScoutUserAdmin(admin.ModelAdmin):
    list_display = ("user","maritalStatus", "idtype", "bank_name", "area_name")

class PropManagerUserAdmin(admin.ModelAdmin):
    list_display = ("id", "user","dob", "idtype", "bank_name", "company_name", "position")

class LandlordUserAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "dob", "idtype", "bank_name", "state", "lga")

class LocationAdmin(admin.ModelAdmin):
    list_display = ("id", "lga", "area_name", "estate_name", "street", "landmark", "closest_busstop")

class PropertyAdmin(admin.ModelAdmin):
    list_display = ("id", "rent_sale", "type", "bed", "price", "is_active", "house_number", "get_street", "get_area_name")

    def get_street(self, obj):
        return obj.prop_location.street
    
    get_street.short_description = 'Street'

    def get_area_name(self, obj):
        return obj.prop_location.area_name
    
    get_area_name.short_desciption = 'Area Name'


class ScoutedPropertyAdmin(admin.ModelAdmin):
    list_display = ("id", "scout", "street", "banner_on_house", "status")

    # def get_street(self, obj):
    #     return obj.location.street

class ElectricitySupplyAdmin(admin.ModelAdmin):
    list_display = ("house_number", "get_street", "get_area_name", "get_state", "avg_supply_per_day")

    def get_street(self, obj):
        return obj.location.street
    
    get_street.short_description = 'Street'

    def get_area_name(self, obj):
        return obj.location.area_name
    
    get_area_name.short_desciption = 'Area'

    def get_state(self, obj):
        return obj.location.state
    
    get_state.short_desciption = 'State'


class SavedPropertyAdmin(admin.ModelAdmin):
    filter_horizontal = ( "saved_property",)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "get_username", "amount", "timestamp", "is_inflow")

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'UserName'



class InflowAdmin(admin.ModelAdmin):
    list_display = ( "get_username", "source", "reference_number")

    def get_username(self,obj):
        return obj.payment.user.username
    get_username.short_description = "Username"


class OutflowAdmin(admin.ModelAdmin):
    list_display = ("get_username", "recipient", "transaction_id")

    def get_username(self,obj):
        return obj.payment.user.username
    get_username.short_description = "Username"




# admin.site.register(Role, RoleAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(ScoutUser, ScoutUserAdmin)
admin.site.register(ListingSpecialistUser, ListingSpecialistUserAdmin)
admin.site.register(PropManagerUser, PropManagerUserAdmin )
admin.site.register(LandlordUser, LandlordUserAdmin )

admin.site.register(Location, LocationAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(ScoutedProperty, ScoutedPropertyAdmin)

admin.site.register(ElectricitySupply, ElectricitySupplyAdmin)
admin.site.register(SavedProperty, SavedPropertyAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Inflow, InflowAdmin)
admin.site.register(Outflow, OutflowAdmin)





