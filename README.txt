###################################### README DOCUMENT FOR "PRUEBA TÉCNICA WELIGHT" ######################################

Index

	A. Steps
	B. Requirements
	C. How to use 
	D. Future steps

A. Steps

	1- First of all, I decided to use Django as framework because I have read about it before and it is one of the most
	used python frameworks so it have enought documentation online for consulting. As database, I choose SQLite. I know
	that SQLite DB is not the best option for a huge amount of database interactions but as it is the default option for
	Django Framework and I have never worked before with it, I choose it this time.
	
	2- I have created a model for the object we are saving which is called "Measure" and it contains all the attributes
	given by the CSV columns in models.py.

	3- I have used csv library to read data from CSV file attached by mail which is located in reports folder. I have used
	just one main view that when you load it it reads the CSV files, an loops each row and saves it into the DB if the 
	format of the row is correct. We also calculate the amount of entries for our Measure table in order to know how many
	we have in the DB. For the view we have used a bootstrap in order to have a response and good looking table, but as 
	the main point of the test is not this I created a simple view with not many details, just the neccesary.

	4- Once we have the database populated and the view showing all the data, is time for the API. We have implemented
	all CRUD methods (Create, Read, Update and Delete) which use will be describe in step C.


B. Requirements

	- Python 3.8.2

	- Django 3.0.5


C. How to use

	1- If we haven't got a Pyhton Virtual Environment, we need to create one, in my case as I develop in Windows I used 
	this command in cmd to install all we need for the environment:

						"pip3 install virtualenvwrapper-win" 

	and then we create our environment:

						"mkvirtualenv my_django_environment"

	and then we install Django: 

						"pip3 install django".



	2- Once we have the enviroment ready we unzip the file mytestsite.7z in the place where we want to save all Django sites,
	and with cmd we move to that folder and we use this commands to apply our model to database and deal with the migrations:

						"python manage.py makemigrations"

						"python manage.py migrate"

	After this we are ready to run our site with the following command:

						"python manage.py runserver"

	If we have done everything right, if we go to: http://127.0.0.1:8000/measuresGrid/index we will see our site 
	(as it loads in DB the whole CSV file when we load this page, I recommend you to reduce the number of measures in the CSV)


	3- Once our site is ready, we just need to see if the API is working properly. For this, without closing the other cmd and having the
	site running, we open a new one and we can:

	- Create: http -j POST http://127.0.0.1:8000/measuresGrid/ energy=70 id=9999999 intensity=70 maximeter=70 power=70 powerFactor=70 reactiveEnergy=70 reactivePower=70 voltage=70 timestamp=2020-02-02T05:05
	- Read one: http -j GET http://127.0.0.1:8000/measuresGrid/1/	
	- Read all: http -j GET http://127.0.0.1:8000/measuresGrid/
	- Update: http -j PUT http://127.0.0.1:8000/measuresGrid/99/ energy=70 intensity=70 maximeter=70 power=70 powerFactor=70 reactiveEnergy=70 reactivePower=70 voltage=70 timestamp=2020-02-02T05:05 id=99
	- Delete: http -j DELETE http://127.0.0.1:8000/measuresGrid/2/


	######### Important!! #########

	- The CSV file attached in the mail has more than 11.000 rows. I have executed the site in my local
	and it took more than 10 minutes to import all the rows into the database, if you want to check if
	it works I recommend you to choose just first 1000 rows from CSV file in order to be faster. I know
	that SQLite DB is not the best option for a huge amount of database interactions but as it is the 
	default option for Django Framework and this is a technical test I selected it as my DB.

	- In the CSV file attached in the mail, data given in the row 4529, has different format 
	(17 Sep 2019 03:45:00,"20,255.801",0.200,24.709,24.876,-15.230,225.367,135.190,0.852) to the others in the document 
	(17 Sep 2019 06:30:00,6.200,0.299,24.758,25.079,-15.213,225.697,135.659,0.855) so, when the sistem try to converts 
	"20,255.801" to decimal number it can't, so I recommend you to choose just 1000 rows from CSV file once more
	because data from those rows have correct format.


D. Futures steps ( what can we do after this, to improve the site)

	- Modify de database, in order to save big data like measures from windfarms, for example a MongoDB is a good option
	 because we do not need it to be relational and gives you better performance for big amount of data.

	- If the goal of this app where saving in db data from CSV files, I would do a form to upload the csv file we want to 
	extact data from and a button to save it in database.


