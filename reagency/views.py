from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.db import IntegrityError
from django.contrib.auth import get_user_model
from .models import User, ScoutUser, ListingSpecialistUser, PropManagerUser, LandlordUser, Property, ScoutedProperty, Location, ElectricitySupply, SavedProperty, Payment
from django.contrib.auth.models import User
from django.contrib import messages
from cloudinary.uploader import upload 
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q, F
from django.core import serializers
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from rave_python import Rave, RaveExceptions
from django.conf import settings
import requests
import json



# FLUTTERWAVE PAYMENT PROCESSING

@csrf_exempt
def initiate_payment(request):
    # amount = 5000  # The amount to be paid
    # user_email = request.user.email  # User's email address

    # data = {
    #     'amount':amount,
    #     'currency':'NGN',
    #     'redirect_url':'https://yourapp.com/payment/callback/',
    #     'payment_type':'card',
    #     'country':'Nigeria',
    #     'email': user_email,
    #     'phonenumber': '12345678901',
    #     'firstname': 'examplefname',
    #     'lastname': 'examplelname',
            
    # }

    # Define headers (e.g., authorization headers) if needed
    # hed = {
        # 'Authorization': 'Bearer '+ settings.RAVE_SECRET_KEY,
        # Add other headers if required
    # }

    # Define the URL for making the POST request to Flutterwave's API
    # url = 'https://api.flutterwave.com/v3/payments'

    # response = requests.post(url, json=data, headers=hed)

    # Parse the response as JSON
    # response_data = response.json()

    # Extract the payment link from the response
    # link = response_data['data']['link']

    # Return the payment link to the caller
    # print(link)

 
    # try:
    #     rave = Rave(settings.RAVE_PUBLIC_KEY, settings.RAVE_SECRET_KEY, usingEnv=False)

    #     # CHARGE
    #     response = rave.Card.charge({
    #         'cardno':'4242424242424242',
    #         'cvv':'123',
    #         'currency':'NGN',
    #         'country':'Nigeria',
    #         'expirymonth':'12',
    #         'expiryyear':'23',
    #         'amount':amount,
    #         'email': user_email,
    #         'phonenumber': '12345678901',
    #         'firstname': 'examplefname',
    #         'lastname': 'examplelname',
    #         'IP': '1111111',


    #         # 'order_id':'your_unique_order_id',
    #         # 'tx_ref':'your_transaction_reference',
    #         # 'redirect_to_payment':True,
    #         # 'meta':None,
    #         # 'payment_plan':None,
    #         # 'subaccounts':None,
    #         # 'split_type':None
    #     })
    #     print(f"first response: {response}")    

    #     # For OTP validation. Most txns requires OTP
    #     if response['validationRequired'] == True:
    #         otp = "12345"
            
    #         try:
    #             # validating with otp
    #             response2 = rave.Card.validate(response["flwRef"], otp)
    #             print(f"Second response: {response2}")

    #             if response2['status'] == "success":
    #                 # verify if the payment is successful. returns an object.
    #                 payment = rave.Card.verify(response2['txRef'])
    #                 print(f"This is payment verification: {payment}")

    #                 # if payment is successful, assign the property to the user who made the payment and lock the property
    #                 User=get_user_model()
    #                 current_user_id = request.user.id
    #                 user_who_locked = User.objects.get(id=current_user_id)
    #                 property_to_lock = Property.objects.get(id=propertyid)
    #                 property_to_lock.is_active = False
    #                 property_to_lock.user_locker = user_who_locked
    #                 property_to_lock.save()

    #                 # send all properties locked by a user to the frontend
    #                 all_properties_locked_byuser = Property.objects.filter(user_locker=user_who_locked, is_active=False)
                   
    #                 # redirect to d properties_paid page with the property details(need to send propid
                    
    #                 # return redirect("properties_paid", {
    #                 #     "all_properties_locked_byuser": all_properties_locked_byuser
    #                 # })

    #                 return JsonResponse({"success":True,
    #                                     "message": "payment successful",
    #                                     "redirect_url": "/propertiespaid",
    #                                     "all_properties": list(all_properties_locked_byuser.values())}, status=201) 

    #                 # set property is_active to false so that others cannot see it and pay for it.
                


    #         except RaveExceptions.TransactionValidationError as e:
    #             # validating with OTP except error
    #             print(e.err['errMsg'])
    #             error = e.err['errMsg']
    #             print(e.err['flwRef'])
    #             # let the user know txn wasnt successful. there's a problem with the txn
    #             return JsonResponse({"success":False, "message":error}, status=403)


    #     # WITHOUT OTP VALIDATION
    #     else:
    #         if not response['error']:
    #             # payment = rave.Card.verify(response2['txRef'])
    #             # return redirect("properties_paid", {
    #             #         "all_properties_locked_byuser": all_properties_locked_byuser
    #             #     })

    #             # payment was successful. return a json response
    #            return JsonResponse({"success":True,
    #                                     "message": "payment successful",
    #                                     "redirect_url": "/propertiespaid",
    #                                     "all_properties": list(all_properties_locked_byuser.values())}, status=201) 



        
    
    # except RaveExceptions.CardChargeError as e:
    #     print(e.err['errMsg'])
    #     error = e.err['errMsg']
    #     print(e.err['flwRef'])
    #     # let the user know txn wasnt successful. & there's a problem with the txn ON D FRONTEND
    #     return JsonResponse({"success":False, "message":error}, status=403)
        
        
        
    

    # if payment is successful, assign the property to the user who made the payment and lock the property
    if request.method == "POST":
        # I am sending data as a JSON object in the request body, not as form data. Therefore, i should use request.body in Django to parse the JSON data, not request.POST. I can do this using json.loads(request.body) to deserialize the JSON data.
        
        data = json.loads(request.body.decode('utf-8'))

        print(data.get('propertyid'))
        print(data.get('amount'))

        
        propertyid = int(data.get('propertyid'))
        amount = int(data.get('amount'))
        
        User=get_user_model()
        current_user_id = request.user.id
        user_who_locked = User.objects.get(id=current_user_id)
        property_to_lock = Property.objects.get(id=propertyid)
        property_to_lock.is_active = False
        property_to_lock.user_locker = user_who_locked
        property_to_lock.save()

        # send all properties locked by a user to the frontend
        all_properties_locked_byuser = Property.objects.filter(user_locker=user_who_locked, is_active=False)

        # After a successful payment, it records the payment/inflow in the payment/inflow table.
        new_payment = Payment(user=user_who_locked, amount=amount)
        new_payment.save()

        if new_payment:
            # Payment successful
            response_data = {
                "success":True,
                "message": "payment successful",
                "redirect_url": "propertiespaid",
                "all_properties": list(all_properties_locked_byuser.values())}
            
            return JsonResponse(response_data, status=201)
        else:
            # Payment failed 
            response_data = {
                "success":False,
                "message": "payment failed",
            }
            return JsonResponse(response_data, status=400)


    
                   
    # redirect to d properties_paid page with the property details with javascript on the frontend
                    
   
                

    
    
    

# # Create your views here.

def index(request):

    # get the roles users register for:
    currentUser = request.user
    userRoles = []
    try:
        if ScoutUser.objects.get(user=currentUser) is not None:
            userRoles.append("Scout")
        if ListingSpecialistUser.objects.get(user=currentUser) is not None:
            userRoles.append("Lisiting Specialist")
        if PropManagerUser.objects.get(user=currentUser) is not None:
            userRoles.append("Property Manager")
        if PropManagerUser.objects.get(user=currentUser) is not None:
            userRoles.append("Property Owner")
    except:
        print("something went wrong")



    # display all active properties 
    all_active_properties = Property.objects.filter(is_active=True)





    #Get the number of watchlist items for a user
    if request.user.is_authenticated:
        user_saved_property = SavedProperty.objects.filter(user=request.user)
        savedPropertyNum = sum(properties.saved_property.count() for properties in user_saved_property)
    
        # display all active properties     
        all_active_properties = Property.objects.filter(is_active=True)
        
        # number of paid/locked properties for the user signed in
        paidPropertyNum = Property.objects.filter(user_locker=currentUser, is_active=False).count()


        if all_active_properties:
            return render(request, "reagency/index.html", {
                "all_active_properties": all_active_properties,
                "savedPropertyNum": savedPropertyNum,
                "userRoles": userRoles,
                "paidPropertyNum": paidPropertyNum
            })
    else:
       
        return render(request, "reagency/index.html", {
            "userRoles": userRoles,
            "all_active_properties": all_active_properties,
            
        })


     
    


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "reagency/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "reagency/login.html")


def logout_view(request):
    
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "reagency/register.html", {
                "message": "Passwords must match."
            })
        
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        tel = request.POST['tel']
        alt_tel = request.POST['alt_tel']

        gender = request.POST['gender']
        profile_pic = request.FILES['profile_pic']

        # Cloudinary url
        profile_pic_result = upload(profile_pic, folder='profilepic')
        profile_pic_url = profile_pic_result['secure_url']
        

        # Attempt to create new user
        try:
            User = get_user_model()
            user = User.objects.create_user(
                username=username,email=email,password=password, first_name=first_name, last_name=last_name, tel=tel, alt_tel=alt_tel, gender=gender, profile_pic=profile_pic_url
            )
            
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "reagency/register.html")
    


def registerscout(request):

    dob = request.POST['dob']
    maritalStatus = request.POST['maritalStatus']
    idtype = request.POST['idtype']
    govt_id = request.FILES['govt_id']
    # These section commented out are on the frontend but not transmitted to backend
    # state = request.POST['state']
    # lga = request.POST['lga']
    # area = request.POST['area']
    estate_name = request.POST['estate_name']
    street = request.POST['street']
    house_number = request.POST['house_number']
    bankname = request.POST['bankname']
    accountno = request.POST['accountno']

    # Cloudinary upload
    govt_id_result = upload(govt_id, folder="validid")
    govt_id_url = govt_id_result['secure_url']

    User = get_user_model()

    scoutUser = ScoutUser(
        user = User.objects.get(id=request.user.id),
        dob = dob,
        maritalStatus = maritalStatus,
        idtype = idtype,
        govt_id = govt_id_url,
        state = "lagos",
        lga = "ibeju-lekki local government",
        area_name = "awoyaya",
        estate_name = estate_name,
        street = street,
        house_number = house_number,
        bank_name = bankname,
        bank_acct_num = accountno 
    )

    scoutUser.save()

    json_response = JsonResponse({"successful":"You have been registered as a scout"}, status=201)

    # return json_response
    message = "You have been successfully registered as a scout. Now you can start making money by letting us know about the properties available for rent or sale in your neighborhood"

    messages.success(request,message)

    return redirect("index")
    

def registerlistingspecialist(request):

    dob = request.POST['dob']
    maritalStatus = request.POST['maritalStatus']
    idtype = request.POST['idtype']
    govt_id = request.FILES['govt_id']
    # These section commented out are on the frontend but not transmitted to backend
    # state = request.POST['state']
    # lga = request.POST['lga']
    # area = request.POST['area']
    estate_name = request.POST['estate_name']
    street = request.POST['street']
    house_number = request.POST['house_number']
    bankname = request.POST['bankname']
    accountno = request.POST['accountno']

    emergency_contact_name = request.POST['emergency_contact_name']
    emergency_contact_address = request.POST['emergency_contact_address']
    emergency_contact_phone = request.POST['emergency_contact_phone']
    emergency_contact_email = request.POST['emergency_contact_email']

    # Cloudinary upload
    try:
        govt_id_result = upload(govt_id, folder="validid")
        govt_id_url = govt_id_result['secure_url']
    except:
        print("Something went wrong with cloudinary. Check your interner connection")
        

    User = get_user_model()

    new_listingSpecialist = ListingSpecialistUser(
        user = User.objects.get(id=request.user.id),
        dob = dob,
        maritalStatus = maritalStatus,
        idtype = idtype,
        govt_id = govt_id_url,

        state = "lagos",
        lga = "ibeju-lekki local government",
        area_name = "awoyaya",
        estate_name = estate_name,
        street = street,
        house_number = house_number,

        bank_name = bankname,
        bank_acct_num = accountno, 

        emergency_contact_name = emergency_contact_name,
        emergency_contact_address = emergency_contact_address,
        emergency_contact_phone = emergency_contact_phone,
        emergency_contact_email = emergency_contact_email
    )

    new_listingSpecialist.save()

    json_response = JsonResponse({"successful":"You have been registered as a scout"}, status=201)

    # return json_response
    message = "You have been successfully registered as a listing Specialist. An Ampeer representative will contact you shortly"

    messages.success(request,message)

    return redirect("index")
    


def registerpropertymanager(request):

    dob = request.POST['dob']
    idtype = request.POST['idtype']
    govt_id = request.FILES['govt_id']
    
    company_name = request.POST['company_name']
    company_address = request.POST['company_address']
    position = request.POST['position']
    bankname = request.POST['bankname']
    accountno = request.POST['accountno']

    # Cloudinary upload
    govt_id_result = upload(govt_id, folder="validid")
    govt_id_url = govt_id_result['secure_url']

    User = get_user_model()

    new_propertyManager = PropManagerUser(
        user = User.objects.get(id=request.user.id),
        dob = dob,
        idtype = idtype,
        govt_id = govt_id_url,

        company_name = company_name,
        company_address = company_address,
        position = position,

        bank_name = bankname,
        bank_acct_num = accountno, 
    )

    new_propertyManager.save()

    json_response = JsonResponse({"successful":"You have been registered as a scout"}, status=201)

    # return json_response
    message = "You have been successfully registered as a Property Manager. An Ampeer representative will contact you shortly"

    messages.success(request,message)

    return redirect("index")



def registerpropertyowner(request):

    dob = request.POST['dob']
    maritalStatus = request.POST['maritalStatus']
    idtype = request.POST['idtype']
    govt_id = request.FILES['govt_id']
    state = request.POST['state']
    lga = request.POST['lga']
    area = request.POST['area']
    estate_name = request.POST['estate_name']
    street = request.POST['street']
    house_number = request.POST['house_number']
    bankname = request.POST['bankname']
    accountno = request.POST['accountno']

    emergency_contact_name = request.POST['emergency_contact_name']
    emergency_contact_address = request.POST['emergency_contact_address']
    emergency_contact_phone = request.POST['emergency_contact_phone']
    emergency_contact_email = request.POST['emergency_contact_email']

    # Cloudinary upload
    govt_id_result = upload(govt_id, folder="validid")
    govt_id_url = govt_id_result['secure_url']

    User = get_user_model()

    new_propertyOwner = LandlordUser(
        user = User.objects.get(id=request.user.id),
        dob = dob,
        maritalStatus = maritalStatus,
        idtype = idtype,
        govt_id = govt_id_url,

        state = state,
        lga = lga,
        area_name = area,
        estate_name = estate_name,
        street = street,
        house_number = house_number,

        bank_name = bankname,
        bank_acct_num = accountno, 

        emergency_contact_name = emergency_contact_name,
        emergency_contact_address = emergency_contact_address,
        emergency_contact_phone = emergency_contact_phone,
        emergency_contact_email = emergency_contact_email
    )

    new_propertyOwner.save()

    json_response = JsonResponse({"successful":"You have been registered as a scout"}, status=201)

    # return json_response
    message = "You have been successfully registered as a Property Owner"

    messages.success(request,message)

    return redirect("index")


@login_required
def scout_view(request):

    # grab data from the form on the frontend
    if request.method == "POST":
        in_estate = request.POST['in_estate'].lower()
        estate_name = request.POST.get('estate_name').lower()
        # estate_name2 = request.POST['estate_name2'].lower()
        street = request.POST['street'].lower()
        # street2 = request.POST['street2'].lower()
        house_number = request.POST['house_number']
        banner_on_house = request.POST['banner_on_house']
        manager_name = request.POST['manager_name']
        manager_tel = request.POST['manager_tel']
        owner_name = request.POST.get('owner_name')
        owner_tel = request.POST.get('owner_tel')

        house_pic = request.FILES['house_pic']


        # Cloudinary upload
        banner_pic_url = None

        banner_pic = request.FILES.get('banner_pic')
        if banner_pic:

            banner_pic_result = upload(banner_pic, folder="bannerpics")
            banner_pic_url = banner_pic_result['secure_url']

        house_pic_result = upload(house_pic, folder="housepics")
        house_pic_url = house_pic_result['secure_url']
        

        # handle new estates and new streets
        # get all the estate in db in a list, convert the location from form to lower case and check if it already exist in db. if it does exist, ignore else save in database.
        # locations = Location.objects.all()
        # location_in_database = [[location.estate_name, location.estate_name2, location.street, location.street2] for location in locations]

        scout = ScoutUser.objects.get(user=request.user)

        # new_location = None
    
        # if [estate_name, estate_name2, street, street2] not in location_in_database:
        #     new_location = Location(
        #         state = "lagos",
        #         lga = "ibeju-lekki",
        #         area_name = "awoyaya",
        #         estate_name = estate_name,
        #         estate_name2 = estate_name2,
        #         street = street,
        #         street2 = street2
        #     )

        #     new_location.save()

        # if new_location:

        #     new_scouted_property = ScoutedProperty(
        #         scout = scout,
        #         location = new_location,
        #         house_number = house_number,
        #         banner_on_house = banner_on_house,
        #         banner_pic = banner_pic_url,
        #         house_pic = house_pic_url,
        #     )
        #     new_scouted_property.save()
        
        # else:
            # if new_location is none, it means the location alrady exist, so i save the scouted prop directly

        new_scouted_property = ScoutedProperty(
            state="lagos",
            lga="ibeju-lekki",
            area_name="awoyaya",
            in_estate = in_estate,
            estate_name = estate_name,
            street = street,
            scout = scout,
            # location = Location.objects.get(state = "lagos", lga = "ibeju-lekki",area_name = "awoyaya",estate_name=estate_name, estate_name2=estate_name2, street=street, street2=street2),
            house_number = house_number,
            banner_on_house = banner_on_house,
            banner_pic = banner_pic_url,
            house_pic = house_pic_url,

            manager_name=manager_name,
            manager_tel = manager_tel,
            owner_name = owner_name,
            owner_tel = owner_tel,
        )

        new_scouted_property.save()
        
        # I still need to include a successful message here
       
        message = "You have successfully posted a new scouted property"
        messages.success(request,message)
        return HttpResponseRedirect(reverse("scout_role"))
    

    User=get_user_model()
    current_user_id = request.user.id
    current_user = User.objects.get(id=current_user_id)

    # for the number of liked properties count
    user_saved_property = SavedProperty.objects.filter(user=current_user )
    savedPropertyNum = sum(properties.saved_property.count() for properties in user_saved_property)

    # for number of locked properties count
    paidPropertyNum = Property.objects.filter(user_locker=current_user, is_active=False).count()
    
    
    current_scout = ScoutUser.objects.get(user=request.user)
    pending_properties = ScoutedProperty.objects.filter(status="pending", scout=current_scout)
    active_properties = ScoutedProperty.objects.filter(status="active", scout=current_scout)
    sold_properties = ScoutedProperty.objects.filter(status="sold", scout=current_scout)
    rejected_properties = ScoutedProperty.objects.filter(status="rejected", scout=current_scout)

    # location_estate = Location.objects.all()

    # convert to a set then to a list to remove repetition
    # estates = list(set([estate.estate_name for estate in location_estate]))
    # streets = list(set([estate.street for estate in location_estate]))
    

    return render(request, "reagency/scout.html", {
        "pending_properties": pending_properties,
        "active_properties": active_properties,
        "sold_properties": sold_properties,
        "rejected_properties": rejected_properties,
        "savedPropertyNum": savedPropertyNum,
        "paidPropertyNum": paidPropertyNum
        # "location_estate": estates,
        # "location_street": streets,
    })




@login_required
@csrf_exempt
def listingspecialist_view(request):


    # Post method for form to create a new property listing
        # Save new Property Owners
        # Save new Property Managers
        # Save new location

    listingSpUser = request.user

    if request.method == "POST":
        # property owner information from frontend
            # id from dropdown
        landlord_id = request.POST.get('landlord')
            # creating a new property owner
        landlord_marital_status = request.POST.get('maritalStatus')
        landlord_dob = request.POST.get('dob')
        landlord_idtype = request.POST.get('idtype')
        landlord_bank_name = request.POST.get('bank_name')
        landlord_bank_acct_num = request.POST.get('bank_acct_num')
        landlord_state = request.POST.get('state')
        landlord_lga = request.POST.get('lga')
        landlord_area_name = request.POST.get('area_name')
        landlord_estate_name = request.POST.get('estate_name')
        landlord_street = request.POST.get('street')
        landlord_house_number = request.POST.get('house_number')
            # Cloudinary upload 
        landlord_id_url = None
        landlord_govt_id = request.FILES.get('govt_id')
        print("I am here before the if statement")
        print(landlord_govt_id)
        if landlord_govt_id:
            landlord_govt_id_result = upload(landlord_govt_id, folder="govtid")
            landlord_id_url = landlord_govt_id_result['secure_url']
            print("I am here in if statement")
            print(landlord_id_url)

        if landlord_id is None:
            # Anonymous user i created in db for landlords that are not registered
            User = get_user_model()

            user = User.objects.get(id=4)
            # save new property owner(assuming property owner is not a registered user. I created an anonymous user in the database for unrgistered user with userid)
            new_landlord = LandlordUser(user=user, maritalStatus=landlord_marital_status, dob=landlord_dob, govt_id=landlord_id_url, idtype=landlord_idtype, bank_name=landlord_bank_name, bank_acct_num=landlord_bank_acct_num, state=landlord_state, lga=landlord_lga, area_name=landlord_area_name, estate_name=landlord_estate_name, street=landlord_street, house_number=landlord_house_number)

            new_landlord.save()
            landlord_id = new_landlord.id




        # property manager information
            # id from dropdown
        manager_id = request.POST.get('manager')
            # creating a new property manager if not in list
        manager_dob = request.POST.get('dobman')
        manager_idtype = request.POST.get('idtypeman')
        manager_bank_name = request.POST.get('bank_nameman')
        manager_bank_acct_num = request.POST.get('bank_acct_numman')
        manager_company_name = request.POST.get('company_name')
        manager_company_address = request.POST.get('company_address')
        manager_position = request.POST.get('position')

            # cloudinary
        manager_govt_id_url = None
        manager_govt_id = request.FILES.get('govt_idman')
        if manager_govt_id:
            manager_govt_id_result = upload(manager_govt_id, folder='govtid')
            manager_govt_id_url = manager_govt_id_result['secure_url']

        if manager_id is None:
            # Anonymous user i created in db for managers that are not registered
            User = get_user_model()

            user = User.objects.get(id=4)
            new_prop_manager = PropManagerUser(user=user, dob=manager_dob,idtype=manager_idtype, govt_id=manager_govt_id_url, bank_name=manager_bank_name, bank_acct_num=manager_bank_acct_num, company_name=manager_company_name,company_address=manager_company_address, position=manager_position)

            new_prop_manager.save()
            manager_id = new_prop_manager.id

        


        # Property Information

        scouted_prop_id = request.POST['scouted_prop_id']
        rent_sale = request.POST['rent_sale']
        type = request.POST['type_of_house']
        bed = request.POST['bed']
        price = request.POST['price']
        print("price is:" + price)
        compound_size = request.POST['compound_size']
        interior_size = request.POST['interior_size']
            # for location in list
        location_id = request.POST.get('location')
        
            # for manually created location if not in list
        in_estate = request.POST.get('in_estate')
        estate_name = request.POST.get('estate_name')
        house_number_prop = request.POST.get('house_number_prop')
        street_prop = request.POST.get('street_prop')

            # cloudinary int_vid
        int_vid_url = None
        int_vid = request.FILES.get('int_vid')
        if int_vid:
            int_vid_result = upload(int_vid, folder="interiorVideo", resource_type="video")
            int_vid_url = int_vid_result['secure_url']

            # cloudinary street_vid
        street_vid_url = None
        street_vid = request.FILES.get('street_vid')
        if street_vid:
            street_vid_result = upload(street_vid, folder="streetVideo", resource_type="video")
            street_vid_url = street_vid_result['secure_url']

             # cloudinary ext_vid
        ext_vid_url = None
        ext_vid = request.FILES.get('ext_vid')
        if ext_vid:
            ext_vid_result = upload(ext_vid, folder="compoundVideo", resource_type="video")
            ext_vid_url = ext_vid_result['secure_url']

            # new location
        if location_id is None:
            new_location = Location(state="lagos",lga="ibeju-lekki",area_name="awoyaya",estate_name=estate_name, street=street_prop)
            new_location.save()
            location_id = new_location.id

            # get location  of the property from db with location id
        new_property_location = Location.objects.get(id=location_id)


        # get the id of d accepted scouted prop from frontend that will be linked with d property and set it to active and get the Scout Details
        scouted_prop = ScoutedProperty.objects.get(id=scouted_prop_id)
        scoutDetails = {"username":scouted_prop.scout.user.username,
                        "firstname": scouted_prop.scout.user.first_name,
                        "lastname":scouted_prop.scout.user.last_name,
                        "profilepic":scouted_prop.scout.user.profile_pic,
                        "tel":scouted_prop.scout.user.tel,
                        "alternativetel":scouted_prop.scout.user.alt_tel,
                        "message":"New Property Upload Successful"
                        }
        

        
        # get the current signed in listing specilaist
        current_listing_specialist = ListingSpecialistUser.objects.get(user=request.user)
        new_listing_property_manager = PropManagerUser.objects.get(id=manager_id)
        new_listing_landlord = LandlordUser.objects.get(id=landlord_id)

        new_property_listing = Property(scouted_property=scouted_prop, 
                 listing_specialist=current_listing_specialist,
                 property_manager=new_listing_property_manager,
                 landlord=new_listing_landlord,

                 rent_sale=rent_sale,
                 type=type,
                 bed=bed,
                 price=price,

                 in_estate=in_estate,

                 compound_size=compound_size,
                 interior_size=interior_size,

                 prop_location=new_property_location,
                 house_number = house_number_prop,

                 int_vid=int_vid_url,
                 ext_vid=ext_vid_url,
                 street_vid=street_vid_url,
        )
        new_property_listing.save()

        accepted_property = ScoutedProperty.objects.get(id=scouted_prop_id)
        accepted_property.status = "active"
        accepted_property.save()



        # Electricity Information
        avg_supply_per_day = request.POST.get('avg_supply_per_day')
        ElectricitySupply(location=new_property_location, house_number="house_number_prop", avg_supply_per_day=avg_supply_per_day)


        

        return JsonResponse(scoutDetails, status=201)


    User = get_user_model()
    current_listing_specialist = ListingSpecialistUser.objects.get(user=request.user)
    current_listing_sp_properties = Property.objects.filter(listing_specialist=current_listing_specialist)

    

    # location 
    locations = Location.objects.all()
    location_obj = [{"location_id":location.id, "location_area":location.area_name, "estate_name":location.estate_name,"street":location.street} for location in locations]

    # show scout listings that are still pending
    scout_listings = ScoutedProperty.objects.filter(status="pending")

    # Property Owners
    prop_owners = LandlordUser.objects.all()
    prop_owners_list = [{"id":owners.id,"username": owners.user.username} for owners in prop_owners]

    # Property Managers
    prop_managers = PropManagerUser.objects.all()
    prop_managers_list = [{"id":managers.id,"username": managers.user.username} for managers in prop_managers]
    


    current_user = ListingSpecialistUser.objects.get(user=request.user.id)
    if current_user:
        listing_specialist = True
    else:
        listing_specialist = False

    return render(request, 'reagency/listingspecialist.html',{
        "scout_listings":scout_listings,
        "listing_specialist": listing_specialist,
        "prop_owners_list": prop_owners_list,
        "prop_managers_list": prop_managers_list,
        "location_obj": location_obj,
        "current_listing_sp_properties": current_listing_sp_properties,
    })


def rejectproperty(request, propertyid):
    if request.method == "POST":

        reason_for_rejection = request.POST.get("reason_for_rejection")
        print(f"property id is {propertyid}")
        scout_property_to_reject = ScoutedProperty.objects.get(id=propertyid)
        scout_property_to_reject.status = "rejected"
        scout_property_to_reject.reason_for_rejection = reason_for_rejection

        scout_property_to_reject.save()

        return redirect("listing_specialist")

def propertymanager_view(request):

    User=get_user_model()
    current_user_id = request.user.id
    current_user = User.objects.get(id=current_user_id)

    # for the number of liked properties count
    user_saved_property = SavedProperty.objects.filter(user=current_user )
    savedPropertyNum = sum(properties.saved_property.count() for properties in user_saved_property)

    # for number of locked properties count
    paidPropertyNum = Property.objects.filter(user_locker=current_user, is_active=False).count()

    try:
        User = get_user_model()
        signed_in_user = User.objects.get(id=request.user.id)
        prop_manager_user = PropManagerUser.objects.get(user=signed_in_user)
        property_manager_properties = Property.objects.filter(property_manager=prop_manager_user, is_active=True)
        property_manager_properties_num = property_manager_properties.count()
        # print(f"property manager properties number {property_manager_properties_num}")


        if property_manager_properties_num > 0:
            return render(request, "reagency/propertymanager.html", {
                "property_manager_properties": property_manager_properties

            })
        
        
        if property_manager_properties_num == 0:
            return render(request, "reagency/propertymanager.html", {
                "property_manager_properties": property_manager_properties,
                "property_num": 0,
                "savedPropertyNum": savedPropertyNum,
                "paidPropertyNum": paidPropertyNum

            })  
        

    except ValueError:
        print("There was an error")
        return render(request, "reagency/propertymanager.html", {
            "savedPropertyNum": savedPropertyNum,
            "paidPropertyNum": paidPropertyNum
        })




def propertyowner_view(request):

    User=get_user_model()
    current_user_id = request.user.id
    current_user = User.objects.get(id=current_user_id)

    # for the number of liked properties count
    user_saved_property = SavedProperty.objects.filter(user=current_user )
    savedPropertyNum = sum(properties.saved_property.count() for properties in user_saved_property)

    # for number of locked properties count
    paidPropertyNum = Property.objects.filter(user_locker=current_user, is_active=False).count()

    try:

        User = get_user_model()
        signed_in_user = User.objects.get(id=request.user.id)
        prop_owner_user = LandlordUser.objects.get(user=signed_in_user)
        property_owner_properties = Property.objects.filter(landlord=prop_owner_user, is_active=True)
        property_owner_properties_num = property_owner_properties.count()
        # print(f"property manager properties number {property_manager_properties_num}")


        if property_owner_properties_num > 0:
            return render(request, "reagency/propertyowner.html", {
                "property_owner_properties": property_owner_properties,
                "savedPropertyNum": savedPropertyNum,
                "paidPropertyNum": paidPropertyNum
            })
        
        
        if property_owner_properties_num == 0:
            return render(request, "reagency/propertyowner.html", {
                "property_owner_properties": property_owner_properties,
                "property_num": 0,
                "savedPropertyNum": savedPropertyNum,
                "paidPropertyNum": paidPropertyNum

            })  
        

    except (ObjectDoesNotExist, ValueError):
        print("There was an error")
        return render(request, "reagency/propertyowner.html", {
            "savedPropertyNum": savedPropertyNum,
            "paidPropertyNum": paidPropertyNum
        })





def scoutedproperty(request):

    pass

@csrf_exempt
def propertysearch(request):
    # Get the query parameters:
    rent_sale = request.GET.get("rent")
    location = request.GET.get("loc")
    type = request.GET.get("type_of_house")
    bed = request.GET.get("bed")
    min_price = request.GET.get("min")
    max_price = request.GET.get("max")

    # location area
    queried_prop_location = Location.objects.get(id=location)
    location_area = queried_prop_location.area_name
    location_estate = queried_prop_location.estate_name
    print(f"location_area:{location_area}")
    print(f"location_estate:{location_estate}")


    # Base queryset
    queriedProperty = Property.objects.filter(rent_sale=rent_sale)
    print(f"queried property: ${queriedProperty}")



    # filter by location area
    if location is not None:
        queriedProperty.filter(prop_location__area_name__icontains=location_area)

    # filter by property type
    if type is not None:
        queriedProperty.filter(type=type)

    #filter by number of bedrooms
    if bed is not None:
        queriedProperty.filter(bed=bed)
        # print (queriedProperty)


    # filter based on price range if min_price and max_price is not provided and if either is provided 
    if min_price is not None and max_price is not None:
        price_filter = Q(price__range=(min_price, max_price))
        queriedProperty.filter(price_filter)
    elif min_price is not None and max_price is None:
        price_filter = Q(price__range=(min_price, 999999999999999))
        queriedProperty.filter(price_filter)
    else:
        price_filter = Q(price__range=(0, max_price))
        queriedProperty.filter(price_filter)

    queriedProperty = queriedProperty.annotate(estate=F('prop_location__estate_name'),area=F('prop_location__area_name'))

    print(queriedProperty)


    # Check if current property listing exist in saved properties
    # if request.user is None:
    #     listingInSavedProperty = False
    # else:
    #     listingInSavedProperty = request.user.usersavedprop.filter(saved_property=singleListing.pk).exists()

    # Current user details
    User = get_user_model()
    current_user = User.objects.get(id=request.user.id)
    user_details = {"name":current_user.first_name, "email":current_user.email, "tel":current_user.tel}

    
    


    
    # All liked properties
    allLikedPropertiesIdList = []


    if request.user.is_authenticated:
        try:
            allLikesInstances = SavedProperty.objects.filter(user=request.user)

            # get the properties and its id in the SavedProperty Table
            for items in allLikesInstances:
                allLikedProperties = items.saved_property.all()
                print(f"All Liked Properties: {allLikedProperties}")
                allLikedPropertiesIdList = [everyProperties.id for everyProperties in allLikedProperties]
                # allLikedPropertiesIdList.append(allLikedProperties.Property.id)
        except:
            allLikedPropertiesIdList = []
    else:
        allLikedPropertiesIdList = []


    print(allLikedPropertiesIdList)
    
    # try:
    #     for like in allLikes:
    #         if like.user.id == request.user.id:
    #             allPropertiesLiked = [like.saved_property for like in allLikes]
    # except:
    #     allPropertiesLiked = []
    # print(f"Arrays of ids of all properties liked is: {allPropertiesLiked}")

    # retrieve all filtered properties with specific fields from location table

    all_filtered_properties = queriedProperty.values(
        'id',
        'rent_sale',
        'type',
        'bed',
        'price',
        'is_active',
        'house_number',
        'prop_location__street',
        'prop_location__area_name',
        'prop_location__estate_name',
        'int_vid',
        'ext_vid',
        'street_vid'
    )


   


    # retrieve all filtered properties
    # all_filtered_properties = queriedProperty.all()

    non_serialized_filtered_properties = [properties for properties in all_filtered_properties]
    print(non_serialized_filtered_properties)

    # return render(request, "reagency/index.html", {1
    #     "all_properties": queriedProperty,
    # })


    # construct the json response manually without using serializer because we are specifying the fields manually with values() and converting them to a list of dictionaries.
    filtered_properties = list(all_filtered_properties)
    return JsonResponse({'results': len(filtered_properties), 'all_properties': filtered_properties, 'allLikedPropertiesIdList': allLikedPropertiesIdList, 'user_details': user_details })


    # serialize the filtered queryset to Json
    # filtered_properties = serializers.serialize('json', all_filtered_properties)
    # return JsonResponse({'results': len(queriedProperty), 'all_properties': filtered_properties })






    


def searchaddress(request):
    # provide an empty sting to avoid None error
    input_string = request.GET.get('q', "") 
    # print(input_string)

    # use Q to perform complex computation on multiple fields
    all_locations = Location.objects.filter(
        Q(area_name__icontains=input_string)|
        Q(estate_name__icontains=input_string)|
        Q(street__icontains=input_string)
    )

    # create a list object of the street, area and estate of the queryset
    filtered_locations = [{"id":location.id,"street":location.street, "area":location.area_name, "estate":location.estate_name} for location in all_locations]

    return JsonResponse(filtered_locations, safe=False)
    




def like(request, propertyid):
    propertyToLike = Property.objects.get(id=propertyid)
    if request.user.is_authenticated:
        # create a new object for the user
        # all_user_saved_properties = SavedProperty(user=request.user)
        # all_user_saved_properties.save()

        # Add the propertyToLike to the user's saved properties
        # all_user_saved_properties.saved_property.add(propertyToLike)

        User = get_user_model()
        # signed_in_user = User.objects.get(id=request.user.id)

        # method suggested by chatgpt
        user = User.objects.get(id = request.user.id)
        property_to_save = Property.objects.get(id=propertyid)

        try:
            # check if the user already has a SavedProperty object, if not create one
            saved_property, created = SavedProperty.objects.get_or_create(user=user)
            saved_property.saved_property.add(property_to_save)
            SavedProperty.objects.add_property(user, property_to_save)
        except ValidationError as e:
            print(e)



        # properties_like_num = SavedProperty.objects.filter(user=request.user).count()

    
        return JsonResponse({'message': 'liked successfully'})

        # allUserSavedProperties = SavedProperty.objects.filter(user=request.user)

        # for property in allUserSavedProperties:



def unlike(request,propertyid):
    property_to_unlike = Property.objects.get(id=propertyid)


    if request.user.is_authenticated:
        try:

            unliked_property = SavedProperty.objects.get(user=request.user, saved_property=property_to_unlike)

            unliked_property.saved_property.remove(property_to_unlike)


            return JsonResponse({'message': 'property unliked successfully'})
        except SavedProperty.DoesNotExist:
             # Handle the case where the property is not found in the user's saved properties
            return JsonResponse({'message': 'property not found in saved properties'})



def likeunlike(request, propertyid):
    
    # All liked properties
    allLikedPropertiesIdList = []


    if request.user.is_authenticated:
        try:
            allLikesInstances = SavedProperty.objects.filter(user=request.user)

            # get the properties and its id in the SavedProperty Table
            for items in allLikesInstances:
                allLikedProperties = items.saved_property.all()
                print(f"All Liked Properties: {allLikedProperties}")
                allLikedPropertiesIdList = [everyProperties.id for everyProperties in allLikedProperties]
                # allLikedPropertiesIdList.append(allLikedProperties.Property.id)
        except:
            allLikedPropertiesIdList = []
    else:
        allLikedPropertiesIdList = ['You may need to sign in to like this']


    print(allLikedPropertiesIdList)

    return JsonResponse( {'allLikedPropertiesIdList': allLikedPropertiesIdList} )



def properties_paid(request):

    User = get_user_model()

    userid = request.user.id
    current_user = User.objects.get(id=userid)

    
   
    # For liked Properties count
    user_saved_property = SavedProperty.objects.filter(user=current_user )
    savedPropertyNum = sum(properties.saved_property.count() for properties in user_saved_property)
    
    # get the properties that has the signed in user as user_locker and is_active as false
    # all_properties_paid = Property.objects.filter(user_locker=current_user, is_active=False).values()
    
    # convert the queryset to a list of dictionaries and serialize it to json in the template
    # all_properties_paid_list = list(all_properties_paid)

    all_properties_paid = Property.objects.filter(user_locker=current_user, is_active=False)
    paidPropertyNum = Property.objects.filter(user_locker=current_user, is_active=False).count()
    
    # serialize the data to JSON
    # all_properties_paid_json = json.dumps(all_properties_paid_list)
    
    print(all_properties_paid)

    return render(request, "reagency/propertiespaid.html", {
        # "all_properties_paid_json": all_properties_paid_json
        "all_properties_paid": all_properties_paid,
        "savedPropertyNum": savedPropertyNum,
        "paidPropertyNum": paidPropertyNum
    })


def liked_properties(request):
    User=get_user_model()
    current_user_id = request.user.id
    current_user = User.objects.get(id=current_user_id)

    # for the number of liked properties count
    user_saved_property = SavedProperty.objects.filter(user=current_user )
    savedPropertyNum = sum(properties.saved_property.count() for properties in user_saved_property)

    # for number of locked properties count
    paidPropertyNum = Property.objects.filter(user_locker=current_user, is_active=False).count()



    # all_saved_properties = [properties.saved_property for properties in user_saved_property]
    # print(all_saved_properties)

    for properties in user_saved_property:
        print(properties)
        all_saved_properties = properties.saved_property.all()
        print(all_saved_properties)

    return render(request, "reagency/likedproperties.html", {
        "all_saved_properties": all_saved_properties,
        "savedPropertyNum": savedPropertyNum,
        "paidPropertyNum": paidPropertyNum
    })