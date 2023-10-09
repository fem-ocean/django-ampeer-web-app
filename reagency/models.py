from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from PIL import Image
from django.core.exceptions import ValidationError


# Create your models here.

# class Role(models.Model):
#     role = models.CharField(max_length=64, default="client")

#     def __str__(self):
#         return f"{self.id} Role is: {self.role}"
    

class User(AbstractUser):
    gender = models.CharField(max_length=1)
    tel = models.CharField(max_length=12)
    alt_tel = models.CharField(max_length=12, blank=True, null=True)
    profile_pic = models.URLField(max_length=200, blank=True, null=True)
    
    # role
    # role = models.ManyToManyField(Role, default="client")
    
    def __str__(self):
        return f"{self.id} {self.username} {self.email} {self.gender}"


class ScoutUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField()
    maritalStatus = models.CharField(max_length=1)
    idtype = models.CharField(max_length=60, default="")
    govt_id = models.URLField(max_length=200)
    # BankDetails
    bank_name = models.CharField(max_length=60)
    bank_acct_num = models.CharField(max_length=10)

    state = models.CharField(max_length=50) 
    lga = models.CharField(max_length=50)
    area_name = models.CharField(max_length=160)
    estate_name = models.CharField(max_length=250, blank=True, null=True)
    street = models.CharField(max_length=50)
    house_number = models.CharField(max_length=15)

    # role = models.ManyToManyField(Role, default="scout")


class ListingSpecialistUser(models.Model):
    # Emergency Contact
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    dob = models.DateField()
    maritalStatus = models.CharField(max_length=1)
    govt_id = models.URLField(max_length=200)
    idtype = models.CharField(max_length=60, default="")

    # BankDetails
    bank_name = models.CharField(max_length=60)
    bank_acct_num = models.CharField(max_length=10)

    state = models.CharField(max_length=50) 
    lga = models.CharField(max_length=50)
    area_name = models.CharField(max_length=160)
    estate_name = models.CharField(max_length=250, blank=True, null=True)
    street = models.CharField(max_length=50)
    house_number = models.CharField(max_length=15)

    emergency_contact_name = models.CharField(max_length=200)
    emergency_contact_address = models.CharField(max_length=400)
    emergency_contact_phone = models.CharField(max_length=12)
    emergency_contact_email = models.EmailField(max_length=254,blank=True, null=True)


    def __str__(self):
        return f"{self.id} {self.maritalStatus} {self.idtype} {self.bank_name} {self.bank_acct_num}"

    

class PropManagerUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    dob = models.DateField()
    govt_id = models.URLField(max_length=200)
    idtype = models.CharField(max_length=60, default="")

    # BankDetails
    bank_name = models.CharField(max_length=60)
    bank_acct_num = models.CharField(max_length=10)
    # role = models.ManyToManyField(Role, default="property manager")

    company_name = models.CharField(max_length=200)
    company_address = models.CharField(max_length=200)
    position = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.id} {self.user} {self.dob} {self.idtype} {self.bank_name} {self.company_name} {self.position}"


class LandlordUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    maritalStatus = models.CharField(max_length=1)
    dob = models.DateField()
    govt_id = models.URLField(max_length=200)
    idtype = models.CharField(max_length=60, default="")

    bank_name = models.CharField(max_length=60)
    bank_acct_num = models.CharField(max_length=10)

    state = models.CharField(max_length=50) 
    lga = models.CharField(max_length=50)
    area_name = models.CharField(max_length=160)
    estate_name = models.CharField(max_length=250, blank=True, null=True)
    street = models.CharField(max_length=50)
    house_number = models.CharField(max_length=15)

    # emergency_contact_name = models.CharField(max_length=200)
    # emergency_contact_address = models.CharField(max_length=400)
    # emergency_contact_phone = models.CharField(max_length=12)
    # emergency_contact_email = models.EmailField(max_length=254, blank=True, null=True)
    
    def __str__(self):
        return f"{self.id} {self.user} {self.dob} {self.idtype} {self.bank_name} {self.state} {self.lga}"


class Location(models.Model):
    state = models.CharField(max_length=50)
    lga = models.CharField(max_length=50)
    area_name = models.CharField(max_length=160)
    estate_name = models.CharField(max_length=250, default="")
    estate_name2 = models.CharField(max_length=200, blank=True, null=True)
    street = models.CharField(max_length=50)
    street2 = models.CharField(max_length=200, blank=True, null=True)
    landmark = models.CharField(max_length=200, blank=True, null=True)
    closest_busstop = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.id} {self.lga} {self.area_name} {self.estate_name} {self.street} {self.landmark} {self.closest_busstop}"

class ScoutedProperty(models.Model):
    scout = models.ForeignKey(ScoutUser, on_delete=models.CASCADE, related_name="propertyfinder")
    # location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="address")
    
    state = models.CharField(max_length=50, default="")
    lga = models.CharField(max_length=100, default="")
    area_name = models.CharField(max_length=100, default="")
    in_estate = models.CharField(max_length=3, default="")
    estate_name = models.CharField(max_length=250, default="")
    street = models.CharField(max_length=50, default="")
    house_number = models.CharField(max_length=15)
    # relationship_with_property = models.CharField(max_length=200)
    
    banner_on_house = models.CharField(max_length=5)
    banner_pic = models.URLField(max_length=200, blank=True, null=True)
    house_pic = models.URLField(max_length=200)

    manager_name = models.CharField(max_length=100, default="")
    manager_tel = models.CharField(max_length=15, default="")
    owner_name = models.CharField(max_length=100, blank=True, null=True)
    owner_tel = models.CharField(max_length=15, blank=True, null=True)

    status = models.CharField(max_length=50, default="pending")
    reason_for_rejection = models.TextField(default="")

    def __str__(self):
        return f"{self.id} {self.scout} {self.street} {self.banner_on_house} {self.status}"

    # I own the property 
    # i have been mandated by the owner to manage the property
    # i dont own/manage the property


    # is there a banner in front of the house(yes/no)
    # upload the picture of the banner

    # UPload a picture of the front view of the house


class Property(models.Model):
    scouted_property = models.OneToOneField(ScoutedProperty, on_delete=models.CASCADE, default="")
    # scout = models.ForeignKey(ScoutUser, on_delete=models.CASCADE, related_name="finder", default="")
    listing_specialist = models.ForeignKey(ListingSpecialistUser, on_delete=models.CASCADE, related_name="poster", default="")
    property_manager = models.ForeignKey(PropManagerUser, on_delete=models.CASCADE, related_name="manager", default="")
    landlord = models.ForeignKey(LandlordUser, on_delete=models.CASCADE, related_name="propowner", default="")


    rent_sale = models.CharField(max_length=10)
    type = models.CharField(max_length=50)
    bed = models.CharField(max_length=50)
    price = models.PositiveBigIntegerField()

    in_estate = models.CharField(max_length=3, default="")
    
    
    compound_size = models.PositiveSmallIntegerField()
    interior_size = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    is_active = models.BooleanField(default=True)

    prop_location = models.ForeignKey(Location,on_delete=models.CASCADE, related_name="proplocation")
    house_number = models.CharField(max_length=15)

    # Media files
    int_vid = models.URLField(max_length=200)
    ext_vid = models.URLField(max_length=200)
    street_vid = models.URLField(max_length=200)

    # A property listed can only have a paid user at a time.
    user_locker = models.ForeignKey(User, on_delete=models.CASCADE, related_name="paiduser", blank=True, null=True, default="")

    def __str__(self):
        return f"{self.id} {self.rent_sale} {self.type} {self.bed} {self.price} {self.is_active} {self.house_number} {self.prop_location.street} {self.prop_location.area_name}"
    


# users get electricity supply info of a property
class ElectricitySupply(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="electricitylocation")
    house_number = models.CharField(max_length=15)
    avg_supply_per_day = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.house_number}, {self.location.street}, {self.location.area_name}, {self.location.state}  Avg Power Supply is {self.avg_supply_per_day} hrs/day"



# users can save properties and reference later. A user can only have a unique set of saved properties. We are creating a SavedPropertyManager class to help with that


class SavedPropertyManager(models.Manager):
    def add_property(self, user, property):
        if self.filter(user=user, saved_property=property).exists():
            raise ValidationError("User already has this property saved.")
        saved_property = self.create(user=user)
        saved_property.saved_property.add(property)

class SavedProperty(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usersavedprop")
    saved_property = models.ManyToManyField(Property, blank=True, related_name="savedproperties")

    objects = SavedPropertyManager()

    def __str__(self):
        return f"{self.id} {self.user} {self.saved_property}"

# class SavedProperty(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usersavedprop")
#     saved_property = models.ManyToManyField(Property, blank=True, related_name="savedproperties")

#     def __str__(self):
#         return f"{self.id} {self.user} {self.saved_property}"

#     class Meta:
#         unique_together = ['user', 'saved_property']


# base class for payment
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_inflow = models.BooleanField(default=True)  #true for inflow, false for outflow

    def __str__(self):
        return f"{self.id} {self.user.username} {self.amount} {self.timestamp} {self.is_inflow} "

# payments made into the company by clients
class Inflow(models.Model):
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE, primary_key=True)
    source = models.CharField(max_length=100)
    reference_number = models.CharField(max_length = 50)

    def __str__(self):
        return f"{self.payment.user.username} {self.source} {self.reference_number}"

# payments made by the company to users
class Outflow(models.Model):
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE, primary_key=True)
    recipient = models.CharField(max_length=100)
    transaction_id = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.payment.user.username} {self.recipient} {self.transaction_id}"
