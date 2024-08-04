WHAT IS THIS PROJECT

Sayem's mini project WHAT THE PROJECT DOES! This is a application inteded to be used by a cafe. This product is inteded to be used in-house and is not meant to be for general use by the public, hence the functioality and what it displays is tailored to fit this criteria. In the app you have the ability to create/ammend/delete products, orders, and couriers. All the information is stored onto a MYSQL database.

HOW TO RUN THE PROJECT:

It is neccessary that you use a MYSQL database, when making the project i used 'Adminer'. when running the application in this project
There are 4 files listed in the folder:
database_link.py (contains all functions for the python code to connect to the database and send/retrive requests
MINI PROJECT.py (contains the main code for this project and also contains the UI to receieve user input, it also output requests)
form_db.sql (contains SQL code that you can execute directly into your MYSQL application to create a new database, necessary tables, columns, and keys. It also contains some preset records so you can use the application straight away
.ENV (contains host/user/password setup for the database
please setup your data base first using the form_db.sql file and execute this in your MYSQL. Then ensure the .env file has the relevant connection information. Finally ensure that both database_link.py and MINI PROJECT.py are loaded up, and run the MINI PROJECT.py file.


WHAT REQUIREMENTS DOES THE PROJECT MEET:
create a product, courier, or order and add it to a table
view all products, couriers, or orders
update the status of an order
persist my data in a database
delete or update a product, order, or courier
display orders by status or courier


UNIT TESTING:

TBC
