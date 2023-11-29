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

## Manual Testing

### Testing User Stories

1.	I want to know the purpose of the site immediately.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|:-----------:|:----------:|:-------------------:|:-----------------:|
| Index Page | Navigate to the index page | The index text paragraph displays | Works as expected |

2.  I want to be able to navigate the site easily and intuitively.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|:-----------:|:----------:|:-------------------:|:-----------------:|
| Navigation bar | Click on the nav links | Correct pages load | Works as expected |
| Log in page | Log in | Logging in leads to user profile | Works as expected |
| Register page | Navigate to the Register page and click the log in link | Log in page opens | Works as expected |
| Log in page | Navigate to the Log in page and click the Register link | Register page opens | Works as expected |
| Full Activity page | Click on either the'Return to Activities' button or the 'Favourites' button | Correct page opens | Works as expected |
| Occasions page | Click on a occasion name | A new page opens with activities filtered by the occasion | Works as expected |
| Ages page | Click on an age group | A new page opens with activities filtered by the age group
 | Works as expected |

3.	I want to be able to view the website on any device.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|:-----------:|:----------:|:-------------------:|:-----------------:|
| The webpage | Open the website on your device | The website displays correctly | Works as expected |


4.  I want to be able to return to the page without using browser buttons if I encounter an error.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|:-----------:|:----------:|:-------------------:|:-----------------:|
| Error 404 Page | Click on the 'Go Back' button | The Index page opens | Works as expected |
| Error 500 Page | Click on the 'Go Back' button | The Index page opens | Works as expected |


5.  I want to view activities and occasions.
6.  I want to filter activities by occasion or by age.
7.  I want to be able to easily register a new account.
8.  I want to be able to locate a log in page easily.
9.  I want to know the benefits of registering as a user.
10.  I want to be able to see my profile.
11.	 I want to be able to add, edit or delete my own occasions.
12.	 I want to be able to add, edit or delete my own activities.
13.	 I want to easily locate occasions and activities I have created.
14.	 I want to be able to add existing activities to favourites.
15.  I want to be able to easily view my favourite activities.
16.  I want to be able to remove one or all of my favourite activities.
17.  I want to receive feedback when completed an action.