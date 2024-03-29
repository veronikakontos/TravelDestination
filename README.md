# Travel Destination - a simple social media website for those who love to share travel destinations and ideas which city to visit and do fun activities!

The web app has an API with current weather 
<!-- > Live demo [_here_](https://www.example.com). -->
### Table of Contents

  - [Table of Contents](#table-of-contents)
  - [General Information](#general-information)
  - [Technologies Used](#technologies-used)
  - [Features](#features)
  - [Screenshots](#screenshots)
  - [Setup and Usage](#setup-and-usage)
  - [Project Status](#project-status)
  - [Room for Improvement](#room-for-improvement)
  - [Contact](#contact)

## General Information
This project is a full-stack web application built using Python, CSS, Html, Flask, MySQL, and API. 

After registering an account users can create new travel destinations, view and comment on posts from other users, as well, as current weather in real-time using Weather API features.

Destinations allow users to create, edit, update, or delete and share it with other registered users. Users can choose countries and cities in their preferred destination, travel date, and cost.

<br>


## Technologies Used

- Python
- Flask
- MySQL 
- Flask-bcrypt 
- Bcrypt
- Pymysql 
- API
- HTML5
- CSS

<br>


## Features
- Login and registration with validation and Bcrypt for password security
- Posts and comments
- Profile page
- Api weather (current weather)
- Responsive for small screen sizes

<br>


## Screenshots
Login and Registration page with designated validations 
![Login and Registration](/screenshots/logreg.png)

Main Homepage where each registered and logged-in user can see all destinations created by other users. Delete destination can only the creator of the destination 
![All Destinations](/screenshots/alldest.png)
![All Destinations](/screenshots/deletedest.png)

The welcome page where a user who is log in, will see his/her/their name and can see the destination and all info about the trip
![All Destinations](/screenshots/welcomedest.png)

Real-time weather from chosen city destination
![API](/screenshots/apiweather.png)

Edit or Update the destination with validation. Users must provide correct information to be able to continue with the website
![Edit/Update Profile](/screenshots/createdest.png)

A popular destination is previewed as a video MP4(repeating every 5sec)
![Video of popular destination](/screenshots/video.png)

<br>



## Setup and Usage
Project requirements/dependencies are located within Pipfile.lock file. 

        pipenv install 
        pipenv shell
        python3 server.py (for Mac users)
        python server.py (for Windows users)

<br>

## Project Status
Project MVP: _Complete_. However, additional features are planned!

<br>

## Room for Improvement

Room for improvement:
- CSS Responsiveness
> Aesthetic design and ease of use across a variety of device screen sizes


<br>

<br>

## Contact
Created by [@veronikakontos](https://www.linkedin.com/in/veronika-kontogiannopoulos/) - feel free to contact me!
