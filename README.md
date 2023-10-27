# django-ampeer-web-app
This is a proptech project built with django. Helps to display real estate properties in video format. The aim is to democratize real estate


## Ampeer Proptech Web Application

### Understanding
Ampeer is web application that focuses on using technology to provide efficient real estate agency services to property finders, owners and managers. The goal of the web application is to help people easily find a property to rent or buy in Awoyaya, Lagos State, Nigeria. The objectives of the application includes:
1. Using videos to display properties to improve transparency.
2. Reduce or emiminate real estate transaction frauds.
3. Improving the speed of real estate transactions by facilitating online payments for properties. 


### Specification
1. Mobile Responsive: The web application is mobile responsive.
   
2. Users: There are 5 roles a signed-in user can become for this web application. They are:
   - Scouts: These are users who provide the platform with the information of available properties in their neighborhood. They are financially rewarded when the property they have provided closes.
   - Listing Specialists: These are users who we have trained to professionally take property videos and details and upload them on the web platform. This is the only user allowed to post a property that would be visible to the general public on the web application. They also get financially rewarded when the property closes.
   - Property Managers: Property Managers are users who have been assigned to manage/rent/sell a property on behalf of the Property Owner.
   - Property Owners: Property Owners are users who own a property listed on the platform.
   - Clients: These are the consumers. They are users who need to rent or buy a property.
   - Role Registration: Every registered users is considered a client until they further register as a Scout, Listing Specialist, Property Manager, or Property Owner. During registration, a modal provides more information about each role and links to another modal for registration. Pictures or video resources uploaded by the user during registration are sent to cloudinary.Thereafter, cloudinary provides us with a url for the resource stored in cloudinary's database.
   - Users who are not signed-in or registered can make queries for properties and get results. However, they will not be able to pay for a property or like a property because they are not signed-in.
  
3. Forms/Page Dynamic rendering: Many forms in the web application uses javascript for dynamic rendering of inputs. Also, many pages are dynamically rendered using javascript.
   - For example, Javascript is used to dynamically render the scout user page into: New Scout Listing, Pending, Active, Sold/Rented, Rejected.
   
4. Navigation: There are 4 main navigations
   - Home - To direct users to the homepage
   - Partner - Depending on the roles (Scouts, Listing Specialists, Property Managers, Property Owners) users have registered for, they can access their dashboard/properties.
   - My Locked Properties - Users who have made a payment deposit of 10% for a property can access the properties they have locked. When a property is locked by a user, other users will not be able to see the full details of the property.
   - Liked Properties - Users can visit this page to view the properties they have liked.
   
5. Posting of Properties:
   a. Role of the Scout:
     - A scout should be able to upload pictures of properties only visible to the listing specialists. There will be a link on the homepage that encourages people to sign up as a scout.
     - All uploaded properties from the Scouts will appear on the Listing Specialist route. Listing specialist can see all the details of the property posted by the Scout and can either "Accept" or "Reject" the property. If accepted, the listing specialist will contact the property owner or manager and take the videos of the property, upload it on the web app, and it becomes visible to Clients who make queries. If rejected, the property appears under the tab "Rejected" when the scout signs in. The listing specialist gives a reason for rejecting the property for the Scout to make ammends. 
     - A property listing reflects the current status of the property to other users associated with that property.eg if scouted property is accepted by the listing specialist then the scout should see it under the "accepted" tab. Also if property is active, scout should see it under the "active" tab.
     - Throughout the lifetime of a property posted by a scout, the property can any of the following statuses: Pending, Accepted, Active, Rented/Sold, Rejected. By default, the status of a new property posted by a scout is "Pending".
     - When a Scout user is posting a new property, and they put in a new location, the new location automatically registers in d Location table of the database.
  
   b. Role of the Listing Specialist:
     - Only a listing specialist will be able to upload properties visible to the client when a query is made.
     - A listing specialist can reject a property by a scout in certain situations. For example, if the address is incorrect or property manager or owner information is incorrect. The listing specialist should give a reason for the rejection. The reason for rejection will be stored in the db. The reason will be shown to the scout for each of the properties rejected.
     - After the listing specialist has physically taken the property listing and uploaded the property videos, it can be queried and visible to Clients. It disappears from the list of scouted properties on the dashboard of the Listing Specialist. All accepted and active properties taken by the listing specialist appears below pending scouted properties.
  
   c. Role of the Property Manager:
     - Property managers can also see the property and its status. They only get to see the property when the listing specialist has physically taken the property listing and uploaded it on the site.
     - If a current user tries to access the property manager page and is not a registered property manager. He will get an error message that he is not registered. He would be encouraged to sign/up or login.


6. Video Upload:
   - Video uploads will be processed by Cloudinary.
   - Each listing should have 3 set of videos. One for the interior, one for the compound, and one for the street. Each not exceeding 2:30 secs.  - When the mouse hovers on the property card, the interior video should autoplay.

7. Searching for Properties:
   a. Client users can make queries for properties based on if to Buy, Rent or Shortlet.
   b. Client users can make queries on the type of properties (All Types, Apartment, House).
   c. Client users can make queries on the location of property.
   d. Client users can make queries on the number of bedrooms (1 bed, 2bed, 3bed, 4bed, 5bed, 6+bed).
   e. Client users can make queries based on price range (Minimum price and Maximum price) In addition, javascript is used to dynamically render different list options of minimum price and maximum price based on if the nature of query is for Buy, Rent or Shortlet.
   f. Javascript is used to dynamically generate a list of locations from the location table in the database when the client user begins typing an address in the address input bar.
-The address is based on the locations in the database
-autocomplete for address is removed and address inputted dynamically search the database for related addresses.

8. Saved Property:
   - User who are logged in should be able to save a property to refer to later. Users who aren't logged in should not 
   - Saved Properties can be accessed via the "Liked Properties" navigation item.
  
9. Payments:
   - Flutterwave is integrated with the web application to process payments.
   - A client can pay 10% of the property price to lock the property. i.e property will not be fully available to other users.
   - After making a successful payment, the client is redirected to the "My locked Properties page"


### What is contained in each File

- .vscode: This is a file automatically generated by my vscode to maintain my vscode settings across multiple devices. You do not need to touch this.

- Ampeer: The main Django project. 
   - In settings.py: I have added configurations for Cloudinary (to help with video processing). I have also added my Flutterwave public and secret test keys(to help with accepting payments). I also added AUTH_USER_MODEL = "reagency.User" to create a custom User model different from the one Django offers.
   - In urls.py: I have added a path to add all the urls in the "reagency" app into the main app.

- reagency: contains the static directory that holds the images and javascript files, templates/reagency directory, admin.py file, models.py file, urls.py file, and views.py file. 
   
   - In static directory: You would find images directory which contains the 3 images used in the project. They include a love.svg image, loved.svg image, and a backgroundImage.svg. You would also find the reagency directory that contains the following files:
        - Index.js file: includes javascript code functionalities that handles javascript events on the home page(index.html).
        - likedproperties.js file: contains javascript code functionalities that handles javascript events on the page that shows properties a user has saved(likedproperties.html).
        - listingspecialist.js file: contains javascript code functionalities that handles javascript events on the listingspecialist.html page.
        - propertiespaid.js file: contains javascript code functionalities that handles javascript events on the propertiespaid.html page.
        - scout.js file: contains javascript code functionalities that handles javascript events on the scout.html page.
        - style.css file: contains css code for the reagency app.
   
   - In templates/reagency directory: You would find all the html files for the reagency app. They include:
        - index.html: This html file helps to display the content of the home page.
        - layout.html: This html file helps to display the page content that is common across all the other pages. For example, the navigation bar.
        - likedproperties.html: This html file helps to display the page content of all the properties liked by a user.
        - listingspecialist.html: This html file helps to display a page that can only be accessed by users registered as a Listing Specialist.
        - login.html: This html file renders the page for users to sign-in.
        - propertiespaid.html: This html file is used to display the property listings a user has paid for. In the navigation bar, this can be assessed via "My Locked Properties".
        - propertymanager.html: This html file is used to display the property listings that is assigned to a particular property manager. The property manager must be registered as a property manager to be able to access this page.
        - propertyowner.html: This html file is used to display the property listings that is assigned to a particular property owner. The property owner must be registered as a property manager to be able to access this page.
        - register.html: This html file displays a form to help new users register to use the web application.
        - scout.html: Only users registered as a scout can access this page. It helps users registered as scout to post few informations about a property that can only be accessed by a Listing Specialist.


   -  admin.py file:  This file is used to change how the different models are displayed when a django administrator logs in
 
   -  models.py file: This file contains all the various models used in the project
 
   -  urls.py file: This file contains all the routes used in the app
 
   -  views.py file: This file contains all the functions used to manipulate the database.
   
   
- db.sqlite3: This file helps to maintain the models required for the database.
- manage.py: This file is for Django's command-line utility for administrative tasks. You do not need to touch this.
- README.md: This contains all you need to know about the web application.
- requirements.txt: This file outlines the basic requirements to run this web app.


### How to run the application
- In your terminal, cd into the Ampeer directory.
- Run python manage.py makemigrations reagency to make migrations for the reagency app.
- Run python manage.py migrate to apply migrations to your database. 
- Log-in or register if you do not have an account. 
- Begin searching for properties. You can use search words like: "awoyaya", "mayfair", "koledoye", "lanipekun".

### Distinctiveness and Complexity
This project satisfies the distinctiveness and complexity requirements in the following ways:

1. Video-based property Listings: Compared to the "Project 2: Commerce" where property listings are image based, this project meets the distinctiveness requirement because it presents property listings as videos rather than pictures. The implementation of this feature also raised the complexity of this project which requires integrating a 3rd party application (Cloudinary) for video processing and storage.

2. Category of Users: The distinctiveness and complexity of this project can also be highlighted by the number of roles a signed-in user can assume. Distinctiveness in the sense that all other projects in this course does not have a situation where a signed-in user can have various degrees of roles in the web app(not the database level) which therefore raises the complexity of this project. A signed-in user can be registered as a Scout, a Listing Specialist, a Property Manager and a Property Owner.  These various segmented roles of a user gives a user different level of priviledges depending on the role s/he is registered as. For example, if a user is registered as a Listing Specialist, he is only allowed to post property listings that can be seen by customers/consumers of the web application. Also, a user registered as a Scout can only post properties that is only seen/approved/rejected by the Listing Specialist. 

3. Video Selection: In this project, vanilla javascript is used to implement what to display on the main video card. Selecting/Clicking the interior video, compound video or street video card changes what is displayed on the main video card. Here, i used the knowledge of Javascript gained from this course to implement something completely different from other projects of this course.

4. Making Payments: Furthermore, the distinctiveness and complexity of this project is highlighted by integrating a payment processing SDK by Flutterwave (test mode). Accepting payments from consumers has not been implemented in any of the projects in this course.

5. Use of Javascript to dynamically generate a list of locations from the database that matches user input: When a user types in a location in the address input with placeholder "where will you like to live", a dropdown of matching locations displays. This functionality is achieved by using Javascript to add an event listener that listens to every user input and makes a GET request for possible locations in the database that matches the user input. All possible locations that matches the user input then displays for the user to select any of them. This functionality is complex and has not been implemented in any of the projects in this course.

