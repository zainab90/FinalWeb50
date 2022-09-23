# CS50 WEB PROGRAMMING FINAL PROJECT: SEVEN SERVICES WEBSITE
## Main idea
I developed a cooperative web application for a seven services company, that focus attention on its  smartphone application, which is called a seven services app, that helps people while they at their home acquisition of craftsmen and technicians in Iraq without getting tired, and in the fastest time and the most appropriate price. The admin of website can edit the content through admin dashboard since the admin dashboard is developed using Django jazzmin library.
The main pages of website are listed as follows:
- Home page that consists of the following sections:
     - Header Section
     - section for categories of services that are offered by seven services app
     - Slideshow Section displays images about the offers presented by the Seven Service app.
     - Download Section presents a download link for seven services application on Android and iOS.
     - Blogs Section that display a slideshow for a list of blogs.
     - About us Section.
     - Footer Section.
- Service Page that views a list of services belonging to each category.
- Blog Page that displays details for each blog.
- Admin page that allows the admin of the application to enter the information about the followingt allows the admin of the application to enter the information about the following:
     - Categories of Professions.
     - services types belong to each category.
     - Blogs details.
     - Slideshow content.
## Distinctiveness and Complexity

The seven service website it's not a social media app nor an e-commerce, and it's not similar to other year’s final projects, so the distinctiveness of this website resides in the main idea and objective itself, since as mentioned above the main idea behind this website is to focus on the categories of services offered to Iraqi users, and offers presented by seven service company about each service in addition to writing blogs that contains  a detailed information, image and video about for example how to maintain and ensure the safety  the services installed in each house by seven service company. 
Thus, In terms of complexity at the backend, Django is used to build models and views, and in terms of complexity in frontend a several JavaScript files are used for adding fantastic interactivity to web pages besides utilizing CSS files for making templets responsive to different screen sizes. Moreover, the admin dashboard is implemented and customized using  a built-in UI customizer in Django jazzmin library.
The templates and views were written gradually. Each website pages were completed connected together, and then tested to create a project that was well-written and simple to administer.

## Files information

- In the views.py file,  the functions that illustrate all of the backend code are listed as follows:
     - Index function: to retrieve information about categories of Professions ,blogs, slideshow of offers and display download link for android and iOS version of seven services application
     - Show service: to display type of services belong to each category.
     - View blog: to view all details of blog such as image, video, and content of blog. 

- In Models.py file, the following models were created
   - A Category model: hold details- related information about category of Professions . 
   - A Service model : hold details- related information about a service belong to specific category.
   - A Blog model: contain a related information about blog such as Blog title, blog content and an image path and youtube video link related to each blog.
   - A Slideshow model: contains the path of images related to offers presented by seven service application.
   - A user model to create a superuser for the website.
   
- Templates:  contains the following HTML templates:
   - custom_admin.html : building customizable HTML page for admin dashboard via utilizing jazzmin library.
   - Blogview.html : HTML template for displaying Blog.
   - MyServices.html: HTML Template for displaying list of categories of professions that are offered by seven service company.
   - ServiceView.html: HTML template for displaying the list of services related to each category.
   - base.html: HTML template to home page.
   - footer.html: HTML template for footer section in each page.
   - 8)	header.html: HTML template that contains all links like that must be called in header section such as  bootstrap font-awesome, etc. 
   - navabr.html: HTML template for navbar section in each page.
   - downnloads.html: HTML template to display download link for seven service app.
   - aboutus.html: HTML template for about us section in each page.
   - scripts.html: HTML template that contains all referencing to JavaScript files.
- Media : contains all the images for this website.
- static : contains front end (CSS/JS) files as listed below:
   - BlogScript.js: to develop a slideshow for displaying the Blogs in Home page.
   - Script.js: For controlling the behavior of header section in all template pages and make it as stick header.
   - A CSS files that illustrate the techniques that are used in designing the above templates such flexbox and grid, besides using bootstrap for responsive design.
- migrations: for saving all sql data.
- forms : contains all the form files such as:
   - CategoryForm.
   - ServiceForm

## How to run the application

To run this project locally a on your computer, please run the following commands:

1. Install project dependencies by running 
```
python -m pip install -r requirements.txt
```
2. Make and apply migrations by running
```
 python manage.py makemigrations 
 python manage.py migrate.
 ```
4. For Creating a superuser to login to the admin page and insert all required tables, run the following commend:
```
python manage.py createsuperuser.
```
6. Run server by running the following command : 
```
python manage.py runserver
```



 
 




  






