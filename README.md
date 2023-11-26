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

**As a logged out User**
7.  I want to be able to easily register a new account.
8.  I want to be able to locate a log in page easily.
9.  I want to know the benefits of registering as a user.

**As a logged in User**
10.  I want to be able to see my profile.
11.	 I want to be able to add, edit or delete my own occasions.
12.	 I want to be able to add, edit or delete my own activities.
13.	 I want to easily locate occasions and activities I have created.
14.	 I want to be able to add existing activities to favourites.
15.  I want to be able to easily view my favourite activities.
16.  I want to be able to delete one or all of my favourite activities.

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
