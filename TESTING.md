# LUDIDO Activity database

![Am I Responsive](documentation/readme/amiresponsive.png)

(Developer: Martyna Nowak)

[Live Webpage](https://ludido-ba4a496efb9b.herokuapp.com/)

This is the testing documentation for the LUDIDO website. For the README file, [click here](https://github.com/mmnowak/mp3_ludido/blob/main/README.md)

## Table of Contents

1. [Introduction](#introduction)
2. [Automated Testing](#automatic-testing)
    1. [HTML Validation](#html-validation)

## Introduction

## Automated Testing

### HTML Validation

The W3C Markup Validation Service was used to validate the HTML of the website. All errors found were corrected, currently there is no errors.

See results:

* [Index page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fludido-ba4a496efb9b.herokuapp.com%2Findex)
* [Activities page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fludido-ba4a496efb9b.herokuapp.com%2Factivities)
* [Add Activity page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fludido-ba4a496efb9b.herokuapp.com%2Fadd_activity)
* [Edit Activity page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fludido-ba4a496efb9b.herokuapp.com%2Fedit_activity%2F5)
* [Occasions page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fludido-ba4a496efb9b.herokuapp.com%2Foccasions)
* [Add Occasion page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fludido-ba4a496efb9b.herokuapp.com%2Fadd_occassion)
* [Edit Occasion page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fludido-ba4a496efb9b.herokuapp.com%2Fadd_occassion)
* [Ages page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fludido-ba4a496efb9b.herokuapp.com%2Fage-groups)
* [Activities by Age page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fludido-ba4a496efb9b.herokuapp.com%2Factivities_by_age%2F5)
* [Register page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fludido-ba4a496efb9b.herokuapp.com%2Fregister)
* [Log in page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fludido-ba4a496efb9b.herokuapp.com%2Flogin)
* [Profile page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fludido-ba4a496efb9b.herokuapp.com%2Fprofile%2Fadmin)
* [Favourites page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fludido-ba4a496efb9b.herokuapp.com%2Ffavourite-activities%2Fadmin)

### CSS validation

The W3C Jigsaw CSS Validation Service was used to validate the css file for the website via file upload. No errors were found.

![CSS Jigsaw score](documentation/testing/css-validation.png)

## Manual Testing

### Testing User Stories

1.	I want to know the purpose of the site immediately.

| **Feature** | **Action** | **Expected Result** | **Actual Result** | **Works as expected** |
|:-----------:|:----------:|:-------------------:|:-----------------:|:---------------------:|
| Index Page | Navigate to the index page | The index text paragraph displays | ![User story 1](documentation/testing/user-stories/us1.png) | Yes |

2.  I want to be able to navigate the site easily and intuitively.

| **Feature** | **Action** | **Expected Result** | **Actual Result** | **Works as expected** |
|:-----------:|:----------:|:-------------------:|:-----------------:|:---------------------:|
| Navigation bar | Click on the nav links | Correct pages load | ![User story 2](documentation/testing/user-stories/us2a.gif) | Yes |
| Log in page | Log in | Logging in leads to user profile | ![User story 2](documentation/testing/user-stories/us2b.gif) | Yes |
| Register page | Navigate to the Register page and click the log in link | Log in page opens | ![User story 2](documentation/testing/user-stories/us2c.gif) | Yes |
| Log in page | Navigate to the Log in page and click the Register link | Register page opens | ![User story 2](documentation/testing/user-stories/us2d.gif) | Yes |
| Full Activity page | Click on either the'Return to Activities' button or the 'Favourites' button | Correct page opens | ![User story 2](documentation/testing/user-stories/us2e.gif) | Yes |
| Occasions page | Click on a occasion name | A new page opens with activities filtered by the occasion | ![User story 2](documentation/testing/user-stories/us2f.gif) | Yes |
| Ages page | Click on an age group | A new page opens with activities filtered by the age group | ![User story 2](documentation/testing/user-stories/us2g.gif) | Yes |

3.	I want to be able to view the website on any device.

| **Feature** | **Action** | **Expected Result** | **Actual Result** | **Works as expected** |
|:-----------:|:----------:|:-------------------:|:-----------------:|:---------------------:|
| The webpage | Open the website on your device | The website displays correctly | [See here](#device-testing) | Yes |


4.  I want to be able to return to the page without using browser buttons if I encounter an error.

| **Feature** | **Action** | **Expected Result** | **Actual Result** | **Works as expected** |
|:-----------:|:----------:|:-------------------:|:-----------------:|:---------------------:|
| Error 404 Page | Click on the 'Go Back' button | The Index page opens | ![User story 4](documentation/testing/user-stories/us4.gif) | Yes |
| Error 500 Page | Click on the 'Go Back' button | The Index page opens | Works as expected | Yes |


5.  I want to view activities and occasions.

| **Feature** | **Action** | **Expected Result** | **Actual Result** | **Works as expected** |
|:-----------:|:----------:|:-------------------:|:-----------------:|:---------------------:|
| Activities Page | Navigate to the Activites Page | Activity cards are displayed | ![User story 5](documentation/testing/user-stories/us5a.gif) | Yes |
| Activity cards | Click on the 'See Instructions' button | Full Activity page opens | ![User story 5](documentation/testing/user-stories/us5b.gif) | Yes |
| Occasions Page | Navigate to the Occasions Page | Occasion cards are displayed | ![User story 5](documentation/testing/user-stories/us5c.gif) | Yes |

6.  I want to filter activities by occasion or by age.

| **Feature** | **Action** | **Expected Result** | **Actual Result** | **Works as expected** |
|:-----------:|:----------:|:-------------------:|:-----------------:|:---------------------:|
| Occasion cards | Click on a occasion name | Activities by Occasion page opens, displays activities for the correct occasion | ![User story 6](documentation/testing/user-stories/us16a.gif) | Yes |
| Age Group cards | Click on an age group card | Activities by Age page opens, displays activities for the correct age | ![User story 6](documentation/testing/user-stories/us5b.gif) | Yes |

7.  I want to be able to easily register a new account.

| **Feature** | **Action** | **Expected Result** | **Actual Result** | **Works as expected** |
|:-----------:|:----------:|:-------------------:|:-----------------:|:---------------------:|
| Register form | Fill out the register form | A new account is created | ![User story 7](documentation/testing/user-stories/us7.gif) | Yes |

8.  I want to be able to locate a log in page easily.

| **Feature** | **Action** | **Expected Result** | **Actual Result** | **Works as expected** |
|:-----------:|:----------:|:-------------------:|:-----------------:|:---------------------:|
| Navigation bar | Click on the 'Log in' link | The Log in page opens | ![User story 8](documentation/testing/user-stories/us8a.gif) | Yes |
| Index page | Click on the 'Log in' link | The Log in page opens | ![User story 8](documentation/testing/user-stories/us8b.gif) | Yes |
| Register page | Click on the 'Log in' link | The Log in page opens | ![User story 8](documentation/testing/user-stories/us2c.gif) | Yes |
| A page accesible to logged in users only | Try to access the page without logging in | Redirected to the Log in page | ![User story 8](documentation/testing/user-stories/us8d.gif) | Yes |

9.  I want to know the benefits of registering as a user.

| **Feature** | **Action** | **Expected Result** | **Actual Result** | **Works as expected** |
|:-----------:|:----------:|:-------------------:|:-----------------:|:---------------------:|
| Index Page | Navigate to the Index Page | A paragraph with information on features avaliable to logged in users appears | ![User story 9](documentation/testing/user-stories/us9.png) | Yes |

10.  I want to be able to see my profile.


| **Feature** | **Action** | **Expected Result** | **Actual Result** | **Works as expected** |
|:-----------:|:----------:|:-------------------:|:-----------------:|:---------------------:|
| Navigation bar | Click on the 'Profile' link | The Profile page loads | ![User story 10](documentation/testing/user-stories/us10a.gif) | Yes |
| Log in page | Log in to your accout | The Profile page loads | ![User story 10](documentation/testing/user-stories/us10b.gif) | Yes |

11.	 I want to be able to add, edit or delete my own occasions.

| **Feature** | **Action** | **Expected Result** | **Actual Result** | **Works as expected** |
|:-----------:|:----------:|:-------------------:|:-----------------:|:---------------------:|
| Occasions page | Click on the 'Add Occasion' button | The Add Occasion page opens | ![User story 11](documentation/testing/user-stories/us11a.gif) | Yes |
| Add Occasions form | Fill out the form | A new occasion is added | ![User story 11](documentation/testing/user-stories/us11b.gif) | Yes |
| Occasion cards | Click on the 'Edit' button | The Edit Occasion page opens | ![User story 11](documentation/testing/user-stories/us11c.gif) | Yes |
| Edit Occasion form | Fill out the form | The occasion is edited | ![User story 11](documentation/testing/user-stories/us11d.gif) | Yes |
| Occasion cards | Click on the 'Delete' button | The occasion is removed from the DB | ![User story 11](documentation/testing/user-stories/us11e.gif) | Yes |


12.	 I want to be able to add, edit or delete my own activities.

| **Feature** | **Action** | **Expected Result** | **Actual Result** | **Works as expected** |
|:-----------:|:----------:|:-------------------:|:-----------------:|:---------------------:|
| Activities page | Click on the 'Add Activity' button | The Add Activity page opens | ![User story 12](documentation/testing/user-stories/us12a.gif) | Yes |
| Add Activity form | Fill out the form | A new activity is added | ![User story 12](documentation/testing/user-stories/us12b.gif) | Yes |
| Activity cards | Click on the 'Edit' button | The Edit Activity page opens | ![User story 12](documentation/testing/user-stories/us12c.gif) | Yes |
| Edit Activity form | Fill out the form | The activity is edited | ![User story 12](documentation/testing/user-stories/us12d.gif) | Yes |
| Activity cards | Click on the 'Delete' button | The activity is removed from the DB | ![User story 12](documentation/testing/user-stories/us12e.gif) | Yes |

13.	 I want to easily locate occasions and activities I have created.

| **Feature** | **Action** | **Expected Result** | **Actual Result** | **Works as expected** |
|:-----------:|:----------:|:-------------------:|:-----------------:|:---------------------:|
| Profile page | Click on the 'My Occasions' dropdown | Occasions created by the user appear | ![User story 13](documentation/testing/user-stories/us13a.gif) | Yes |
| Profile page | Click on the 'My Activities' dropdown | Activities created by the user appear | ![User story 13](documentation/testing/user-stories/us13b.gif) | Yes |

14.	 I want to be able to add existing activities to favourites.

| **Feature** | **Action** | **Expected Result** | **Actual Result** | **Works as expected** |
|:-----------:|:----------:|:-------------------:|:-----------------:|:---------------------:|
| Activity cards | Click on the 'Add to favourites' button | The activity is added to favourites | ![User story 14](documentation/testing/user-stories/us14.gif) | Yes |

15.  I want to be able to easily view my favourite activities.

| **Feature** | **Action** | **Expected Result** | **Actual Result** | **Works as expected** |
|:-----------:|:----------:|:-------------------:|:-----------------:|:---------------------:|
| Index page | Click on the third feature section | My Favourites page opens | ![User story 15](documentation/testing/user-stories/us15a.gif) | Yes |
| Activities page | Click on the 'My favourites' button | My Favourites page opens | ![User story 15](documentation/testing/user-stories/us15b.gif) | Yes |
| Profile page | Click on the 'My favourites' button | My Favourites page opens | ![User story 15](documentation/testing/user-stories/us15c.gif) | Yes |
| Full Activity page | Click on the 'My favourites' button | My Favourites page opens | ![User story 15](documentation/testing/user-stories/us15d.gif) | Yes |


16.  I want to be able to remove one or all of my favourite activities.

| **Feature** | **Action** | **Expected Result** | **Actual Result** | **Works as expected** |
|:-----------:|:----------:|:-------------------:|:-----------------:|:---------------------:|
| Activity cards | Click on the 'Remove from Favourites' button | The activity is removed from favourites | ![User story 16](documentation/testing/user-stories/us16a.gif) | Yes |
| Favourites page | Click on the 'Unfavourite All' button | All favourite activities are removed from favourites | ![User story 16](documentation/testing/user-stories/us16b.gif) | Yes |

17.  I want to receive feedback when completed an action.

| **Feature** | **Action** | **Expected Result** | **Actual Result** | **Works as expected** |
|:-----------:|:----------:|:-------------------:|:-----------------:|:---------------------:|
| Add Activity page | Add a new activity | A flash message appears | ![User story 17](documentation/testing/user-stories/us17a.gif) | Yes |
| Edit Activity page | Edit the activity | A flash message appears | ![User story 17](documentation/testing/user-stories/us17b.gif) | Yes |
| Activities cards | Click on the 'delete' button | A flash message appears | ![User story 17](documentation/testing/user-stories/us17c.gif) | Yes |
| Add Occasion page | Add a new occasion | A flash message appears | ![User story 17](documentation/testing/user-stories/us17d.gif) | Yes |
| Edit Occasion page | Edit the occasion | A flash message appears | ![User story 17](documentation/testing/user-stories/us17e.gif) | Yes |
| Occasion cards | Click on the 'delete' button | A flash message appears | ![User story 17](documentation/testing/user-stories/us17f.gif) | Yes |
| Activities cards | Click on the 'Add to Favourites' button | A flash message appears | ![User story 17](documentation/testing/user-stories/us17g.gif) | Yes |
| Activities cards | Click on the 'Remove from Favourites' button | A flash message appears | ![User story 17](documentation/testing/user-stories/us17h.gif) | Yes |
| Favourites page | Click on the 'Unfavourite all' button | A flash message appears | ![User story 17](documentation/testing/user-stories/us17i.gif) | Yes |
| Navigation bar | Click on the 'Log out' link | A flash message appears | ![User story 17](documentation/testing/user-stories/us17j.gif) | Yes |
| Log in page | Log in | A flash message appears | ![User story 17](documentation/testing/user-stories/us17k.gif) | Yes |
| A page accesible to logged in users only | Try to access the page without logging in | A flash message appears | ![User story 17](documentation/testing/user-stories/us17l.gif) | Yes |