# LUDIDO

![Am I Responsive](documentation/readme/amiresponsive.png)

(Developer: Martyna Nowak)

[Live Webpage](https://mmnowak.github.io/tarot-quiz/index.html)

## Table of Contents

1. [Project Goals](#project-goals)
    1. [Overview](#overview)
    2. [Goals](#goals)
2. [User Experience Design](#user-experience-design)
    1. [Strategy Plane](#strategy-plane)
    1. [Scope Plane](#scope-plane)
    2. [Structure Plane](#structure-plane)
    3. [Surface Plane](#surface-plane)
        1. [Wireframes](#wireframes)
        2. [Typography](#typography)
        3. [Imagery](#imagery)
        4. [Colour scheme](#colour-scheme)
3. [Features](#features)
4. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks and Tools](#frameworks-and-tools)
5. [Testing and bugs](#testing-and-bugs)
6. [Credits](#credits)
    1. [Media](#media)
    2. [Code used](#code-used)
    3. [Content](#content)
7. [Deployment](#deployment)
8. [Acknowledgements](#acknowledgements)

## Project Goals

### Overview

The main purpose of this project is to create a user-friendly website designed to find and share games and activities filtered by occasion, age group, developmental area and activity type. The website allows all users to browse existing activities and registered users to add or edit their own activities and occasions, as well as add existing activities to favourites. 

### Goals

1. A website that can be navigated easily and intuitively.
2. A clean design that catches the eye.
3. A website that looks good and responds correctly on all device sizes.
4. A website that is accessible to all users.
5. A website that allows users to register.
6. A website that allows registered users to add new entries to the database.
7. A website that allows registered users to edit their own entries.
8. A website that allows users to add existing activities to favourites.

## User Experience Design

### Strategy Plane

#### Target Audience

Target audience of this website are people working with children, i.e. playworkers, nannies, childminders, au-pairs, nursery nurses, teachers etc, as well as parents.

#### User Requirements and Expectations

* Links and buttons that work as expected.
* A simple and intuitive navigation system.
* Interactive feedback and notifications.
* Information presented in a clear and concise manner.
* Visually appealing design.
* Easy way to create an account.
* Easy way to log in for existing users.
* Ability to add, edit or delete own data.
* Ability to add existing activities to favourites.
* Accessibility.

#### User Stories

**As a User:**
1.	I want to know the purpose of the site immediately.
2.  I want to be able to navigate the site easily and intuitively.
3.	I want to be able to view the website on any device.
4.  I want to be able to return to the page without using browser buttons if I encounter an error.
5.  I want to view activities and occasions.
6.  I want to filter activities by occasion or by age.

**As a logged out User:**

7.  I want to be able to easily register a new account.
8.  I want to be able to locate a log in page easily.
9.  I want to know the benefits of registering as a user.

**As a logged in User:**

10.  I want to be able to see my profile.
11.	 I want to be able to add, edit or delete my own occasions.
12.	 I want to be able to add, edit or delete my own activities.
13.	 I want to easily locate occasions and activities I have created.
14.	 I want to be able to add existing activities to favourites.
15.  I want to be able to easily view my favourite activities.
16.  I want to be able to remove one or all of my favourite activities.
17.  I want to receive feedback when completed an action.

### Scope Plane

**Features Planned**

* All Users
1.  Responsive design
2.  Postgres database to store activities, occasions, users and user favourites
3.  Activities Page
4.  Occasions Page
5.  Age groups Page
6.  Pages displaying activities filtered by either occasion or age group
* Logged out Users
7.  Register Form
8.  Login Form
* Logged in Users
8.  Activities Page with Add Activity link and edit/delete links for own Activities
9.  Add Activity form
10. Edit Activity form and Delete Activity functionallity for Activities created by User
11. Occasions Page with Add Occasion link and edit/delete links for own Occasions
12. Add Occasion form
13. Edit Occasion form and Delete Occasion functionallity for Occasions created by User
14. Profile displaying Activities and Occasions created by User
15. Favourites Page with functionallity to delete favourites

### Structure Plane

Based on the User stories and planned features, I created a website flowchart:

![Flowchart](documentation/readme/site-flowchart.png)

The website structure targets the user stories as follows:

User Story 2:  I want to be able to navigate the site easily and intuitively.

* Navigation bar to be displayed on all pages with relevant nav links, based on whether the user is logged in or not
* User is led through site in an intuitive way
    * Register page contains a link to Log in Page and vice versa
    * Logging in leads to user profile
    * Full Activity page contains links to return to Activities Page or Favourites if user is logged in
    * Occasion and Ages pages lead to filtered Activities page

User Story 3:	I want to be able to view the website on any device.

* The website is built with Bootstrap CSS and fully tested to ensure it is responsive on differend size devices

User Story 4:  I want to be able to return to the page without using browser buttons if I encounter an error.

* Custom Error 404 and Error 500 built
* A link to return to the index page

User Story 5:  I want to view activities and occasions.

* Activities page contains Activities cards with clickable links to see more information
* Occasions page contains Occasion cards

User Story 6:  I want to filter activities by occasion or by age.

* Occasion page contains clickable links leading users to a page which displays filtered Activities
* Ages page contains clickable links leading users to a page which displays filtered Activities

User Story 7:  I want to be able to easily register a new account.

* The navbar contains a link to Register Page
* Index Page and Log in Page contain links to Register Page
* Register form is easy to fill in

User Story 8:  I want to be able to locate a log in page easily.

* The navbar contains a link to Log In Page
* Index Page and Register Page contain links to Log in Page
* User is redirected to Log in Page if they try to access a page avaliable to logged in users only

User Story 9:  I want to know the benefits of registering as a user.

* Index Page contains information on features avaliable to logged in users

User Story 10:  I want to be able to see my profile.
* The nav bar contains a link to User profile for logged in users
* Logging in directs users to Profile page

User Story 11:	 I want to be able to add, edit or delete my own occasions.

* Occasions Page contains a link to Add Occasion Page
* Add Occasion page contains a form allowing the user to add their own occasions easily
* Upon submission the created Occasion will appear on Occasions Page and User Profile Page
* Occasion cards displayed on Occasion Page and in User Profile feature a link to Edit Occasion Page
* Edit Occasion page contains a form
* Upon submission the user is notified they have successfully edited the Occasion
* Occasion cards displayed on Occasion Page and in User Profile feature a button to Delete Occasion function
* When the delete button is clicked, a modal appears to ensure the user intends to delete the occasion
* The user is notified they have successfully deleted the Occasion

User Story 12:	 I want to be able to add, edit or delete my own activities.

* Activities Page contains a link to Add Activity Page
* Add Activity page contains a form allowing user to add their own activities easily
* Upon submission the created Activity will appear on Activity Page, User Profile Page and on the relevant Occasion and Age Group pages
* Activity cards displayed on Activity Page, Activity by Occasion Page, Activities by Age Page and in User Profile feature a button to Edit Activity Page
* Edit Activity page contains a form
* Upon submission the user is notified they have successfully edited the Activity
* Activity cards displayed on Activity Page, Activity by Occasion Page, Activities by Age Page and in User Profile feature a button to trigger the Delete Activity function
* When the delete button is clicked, a modal appears to ensure the user intends to delete the Activity
* The user is notified they have successfully deleted the Activity

User Story 13:	 I want to easily locate occasions and activities I have created.

* Profile page contains sections featuring occasions and activities created by user

User Story 14:	 I want to be able to add existing activities to favourites.

* Activity cards on Activities Page, Activities by Occasion Page and Activities by Age Page contain a button triggering the Add to Favourites Function 

User Story 15:  I want to be able to easily view my favourite activities.

* Index Page, Activities Page and Profile Page contain links to Favourites Page

16.  I want to be able to delete one or all of my favourite activities.

* Activity cards on Activities Page, Activities by Occasion Page and Activities by Age Page contain a button triggering the Remove from Favourites Function if the Activity is favourited
* Favourites Page features a button triggering the Unfavourite All function

17.  I want to receive feedback when completed an action.

* Flash messages appear to confirm an action initiated by user was executed.

#### Database Schema

![DBSchema](documentation/readme/dbschema.png)

### Surface Plane

#### Wireframes

<details><summary>Index Page</summary>
<img src="documentation/readme/wireframes/index.png">
<img src="documentation/readme/wireframes/login-mobile.png">
</details>

<details><summary>Login Page</summary>
<img src="documentation/readme/wireframes/login.png">
<img src="documentation/readme/wireframes/login-mobile.png">
</details>

<details><summary>Register Page</summary>
<img src="documentation/readme/wireframes/register.png">
<img src="documentation/readme/wireframes/register-mobile.png">
</details>

<details><summary>Profile Page</summary>
<img src="documentation/readme/wireframes/profile.png">
<img src="documentation/readme/wireframes/profile-mobile.png">
</details>

<details><summary>Activities Page</summary>
<img src="documentation/readme/wireframes/activities.png">
<img src="documentation/readme/wireframes/activities-mobile.png">
</details>

<details><summary>Full Activity Page</summary>
<img src="documentation/readme/wireframes/full-activity.png">
<img src="documentation/readme/wireframes/full-activity-mobile.png">
</details>

<details><summary>Add Activity Page</summary>
<img src="documentation/readme/wireframes/submit-activity.png">
<img src="documentation/readme/wireframes/submit-activity-mobile.png">
</details>

<details><summary>Occasions Page</summary>
<img src="documentation/readme/wireframes/occasions.png">
<img src="documentation/readme/wireframes/occasions-mobile.png">
</details>

<details><summary>Add/Edit Occasion Page</summary>
<img src="documentation/readme/wireframes/submit-occasion.png">
<img src="documentation/readme/wireframes/submit-occasion-mobile.png">
</details>

<details><summary>Ages Page</summary>
<img src="documentation/readme/wireframes/ages.png">
<img src="documentation/readme/wireframes/ages-mobile.png">
</details>

<details><summary>Activities by Age Page</summary>
<img src="documentation/readme/wireframes/activities-by-age.png">
<img src="documentation/readme/wireframes/activities-byage-mobile.png">
</details>

<details><summary>Custom Error 404 and 500 Pages</summary>
<img src="documentation/readme/wireframes/error.png">
</details>


## Features

### All Pages

**Navigation Bar**

* Fully responsive; collapapses into a toggler menu on small devices;
* Features a logo which leads to the Index page when clicked;
* Logo increases in size on hover;
* Features links to the Index, Activities, Occasion and Ages pages;
* For users that are not logged in, it features links to the Register and Log In pages;
* For logged in users, it features links to the Profile Page and Log Out functionallity;
* Links change colour on hover.

User Stories covered: 2, 3.

![Navigation bar for logged in users](documentation/readme/features/navbar.png)
![Navigation bar for logged out users](documentation/readme/features/navbar2.png)
![Navigation bar on mobile](documentation/readme/features/navbar-mobile.png)

**Footer**

* Contains credits and a link to the developer's Github and Linkedin accounts;
* The link icons change colour on hover;

![Footer](documentation/readme/features/footer.png)

**Flash messages**

* Flash messages give user feedback after they completed an action, e.g. delete an Occasion or add an Activity to favourites;
* They also appear to inform a user they do not have an access to certain pages; e.g. if a user who is not logged in tries to add an Activity;
* A flash message appears upon logging in to inform the user they need to reload their profile to see their Occasions and Activities;
* Flash messages div is incorporated into the header and matches the aesthetic of the website.

User Stories covered: 17.

![Flash messages](documentation/readme/features/flash-msg.png)

### Index Page

**Text paragraph**

* Informs the user about the purpose of the site;
* Lists benefits of creating an account

User Stories covered: 1, 9.

**Action Buttons**

* The Explore button leads to the Activities page;
* Logged in users see the My Profile button which leads to the Profile Page;
* Logged out users see a Log in button and a Register link;
* The buttons change size on hover.

User stories covered: 2, 8, 13. 

![Action buttons for logged in users](documentation/readme/features/indexbuttons.png)
---
![Action buttons for logged out users](documentation/readme/features/indexbuttons2.png)

**Features section**

* Three containers of images and text which describe some of the website's features;
* The containers are clickable links and increase in size on hover;
* The first container informs user they can add their own occasion or filter activities by existing occasions.
* It leads to the Occasions page when clicked.
* The second container informs user they can filter activities by age and learn more about play at each development stage.
* It leads to the Ages page when clicked.
* The third container informs user they can add activities to favourites if they have an account.
* It leads to the Favourites page if the user is logged in and the Register page if they are not logged in.
* The images used match the imagery used in the header as well as the colour scheme.

User stories covered: 1, 7, 15.

![Features section](documentation/readme/features/indexfeatures.png)

### Activities Page

**Add Activity button**

* Displayed if the user is logged in;
* Leads to the Add Activity page;
* Changes colour on hover.

User stories covered: 2, 12.

**My Favourites button**

* Displayed if the user is logged in;
* Leads to the Favourites page;
* Changes colour on hover.

User stories covered: 2, 12, 15.

![Acctivities page buttons](documentation/readme/features/activities-buttons.png)

**Activity cards**

* Display activities added by users;
* Contain activity name, age group, developmental area, activity type, occasion and the username of the user who created the activity.
* Contain See Instructions button;
* If the user is logged in and has created the activity, the cards contain Edit and Delete buttons;
* If the user is logged in and has not created the activity, the cards contain Add to Favoutites/Remove from favourites button.

User stories covered: 5.

![Activity cards](documentation/readme/features/activity-cards.png)
![Activity cards](documentation/readme/features/activity-cards2.png)

**See Instructions button**

* Leads to the Full Activity page where the users can obtain instructions for the selected activity;
* Changes colour on hover.

User stories covered: 5.

![See Instructions button](documentation/readme/features/instruction-button.png)

**Edit and Delete button**

* Displayed if the user is logged in and has created the activity;
* The Edit button leads to the Edit Activity page;
* The Delete button triggers a modal which ask the user if they are sure they want to delete the activity.
* The Delete button on the modal triggers the delete_activity functionallity.

User stories covered: 12.

![Edit and delete button](documentation/readme/features/activitycard-buttons.png)

ADD MODAL SCREENSHOT HERE

**Add to favourites button**

* Displayed if the user is logged in and is not the author of the activity.
* Adds the activity to user's favourites when clicked.

User stories covered: 14.

![Add to favourites button](documentation/readme/features/fav-button.png)

**Removed from favourites button**

* Displayed if the user is logged in, is not the author of the activity and has previously added the activity to their favourites.
* Removes the activity from user's favourites when clicked.

User stories covered: 16.

![Remove from favourites button](documentation/readme/features/unfav-button.png)