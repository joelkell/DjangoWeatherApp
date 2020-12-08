# AWM2021 Assignment 2

[www.joelkell.xyz](https://www.joelkell.xyz)

For your assignment, you are required to create a location-based services (LBS) application which exercised the technologies listed below. This builds on the work done in Assignment Part 1.

## To build your application you are required to use:
* Database: PostgreSQL with PostGIS
* Middle tier(s): Django with Django REST Framework
* Front-end: Progressive Web Application (PWA) and Android or iOS app developed in Cordova. You can use any framework you like for layout such as jQueryMobile, Ionic, Bootstrap etc.
* Mapping: Leaflet JS with OpenStreetMap
* Deployment (middle tier(s)): Any cloud provider. I suggest using Docker to create an image and deploy an instance of this. The back-end components of your app must be web-accessible or the front-end component will not work.
* Technologies (optional)
* Companion Django Admin website to your mobile application
* Django REST Framework
* Android or iOS app developed in Cordova
* Client-side frameworks such as Angular, React etc.
* Link to external API for additional data such as points of interest etc. OpenStreetMap's Overpass API is useful in this regard.
* Cloud providers: Suggestions include but are not limited to Amazon AWS, Microsoft Azure, Digital Ocean, Okeanos.

## Content
The idea is to build a full-stack application that has a location-based or mapping component. To this end, it is required to:

1. Create/store/manipulate spatial data, hence PostgreSQL/PostGIS
2. Create a middle layer based on the Model-View-Controller (MVC) pattern, hence Django.
3. Create a mobile application, deployable on any platform, hence PWA.
4. Be deployed to the Cloud, hence, Docker and external provider for hosting.