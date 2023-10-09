from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    

    # Registration Routes
    path("registerscout", views.registerscout, name="registerscout"),
    path("registerlistingspecialist", views.registerlistingspecialist, name="registerlistingspecialist"),
    path("registerpropertymanager", views.registerpropertymanager, name="registerpropertymanager"),
    path("registerpropertyowner", views.registerpropertyowner, name="registerpropertyowner"),

    # Role Route routes
    path("role/scout", views.scout_view, name="scout_role" ),
    path("role/listingspecialist", views.listingspecialist_view, name="listing_specialist" ),
    path("role/propertymanager", views.propertymanager_view, name="property_manager" ),
    path("role/propertyowner", views.propertyowner_view, name="property_owner" ),
    path("propertiespaid", views.properties_paid, name="properties_paid" ),
    path("likedproperties", views.liked_properties, name="liked_properties" ),
    path("role/rejectproperty/<int:propertyid>", views.rejectproperty, name="rejectproperty"),



    # Scouted Property Form Submission
    path("scoutedproperty", views.scoutedproperty, name="scoutedproperty"),

    # API's
    path("propertysearch", views.propertysearch, name="propertysearch"),
    path("searchaddress", views.searchaddress, name="searchaddress"),
    path("like/<int:propertyid>", views.like, name="like"),
    path("unlike/<int:propertyid>", views.unlike, name="unlike"),
    path("likeunlike/<int:propertyid>", views.likeunlike, name="likeunlike"),
    path("initiatepayment", views.initiate_payment, name="initiatepayment"),









    


]