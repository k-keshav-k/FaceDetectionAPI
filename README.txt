README

Course:  CS305

=================================


1. What does this program do

This program implements an application to do "facial search" on a database of images.
The application provides a secure API service that gets invoked by sending a HTTP POST request.
API endpoint is provided to search the database of images and find top-k match with a minimum confidense level.
Api endpoints are provided to add faces to the database one by one or from a zip file, where all images in the zip file get added to the database.
Api endpoints are also provided to get meta-data of a particular image as well as to add meta data to a particular image of the database.

2. A description of how this program works (i.e. its logic)

This pogram provides many api routes, each performing different functions:
Description of these routes are:

i. search_faces
This route takes image file, number of matches to be found: k, and the confidense level.
First, it is verified if the file provided is an image file or not. If not, the function returns with an error status.
Then connectionClass is envoked to establish a connection to the database.
Then face_recognition library is used to find all faces in the image.
If there are no faces, the program just return an error status.
Each row of the database is accessed and comparred with the given image to get matches for each face of the given image.
Then images are sorted on the basis of euclidean distance and returned.

ii. add_face
This route takes an image file and adds its encoding to the faces table of the database.
Here also, checks are performed on the image file, prior to being added.
It is checked whether the image file has an image extension or not.
It is then checked if the image file contains only a single face or not.
If all checks are passed, face_recognition is used to get encoding of the face and the encoding is added to the faces table.

iii. add_faces_in_bulk
This route takes a zip file and adds all images in it to the table.
First it is checked whether the file provided is a zip file or not.
Then all the image files are iterated over of yhe zip files and added in succession into the faces table.

iv. get_face_info
This api end point uses face_id to get all meta data and info regarding a face record from the table.
It first checks if the id provided exists in the table or not, and then references the table to get all information about the face from the table and return to the user.

v. add_meta_data
This api route uses face_id and accepts information: person_name, version and date and inserts it into the table for the particular face id.
It first checks if the face id exists or not and then uses sql UPDATE to set all relevant column names.

3. How to compile and run this program

Create the database and table
CREATE DATABASE facesdb
create table faces (
   id SERIAL,
   name character varying (200),
   vector double precision [],
   person_name character varying (200),
   version int,
   date character varying(200)
 )

Activate the virtual env

Navigate to src directory of the folder

Start the fast api server: uvicorn main:app --reload

Run the tests:
	To run specific tests: pytest test1.py
	To run all the tests: pytest test1.py test2.py test3.py test4.py test5.py
	To run the tests with coverage: coverage run -m pytest test1.py test2.py test3.py test4.py test5.py
	To get the coverage report: coverage report -m
	To get the coverage html page: coverage html


4. Provide a snapshot of a sample run

(myvenvpy) keshav@keshav-Lenovo-ideapad:~/Desktop/CS305/assignment2/src$ uvicorn main:app --reload
INFO:     Will watch for changes in these directories: ['/home/keshav/Desktop/CS305/assignment2/src']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [77315] using watchgod
INFO:     Started server process [77317]
INFO:     Waiting for application startup.
INFO:     Application startup complete.

(myvenvpy) keshav@keshav-Lenovo-ideapad:~/Desktop/CS305/assignment2/src$ coverage run -m pytest test1.py test2.py test3.py test4.py test5.py
================================== test session starts ==================================
platform linux -- Python 3.8.10, pytest-7.0.1, pluggy-1.0.0
rootdir: /home/keshav/Desktop/CS305/assignment2/src
plugins: anyio-3.5.0
collected 15 items                                                                      

test1.py .....                                                                    [ 33%]
test2.py ....                                                                     [ 60%]
test3.py ..                                                                       [ 73%]
test4.py ..                                                                       [ 86%]
test5.py ..                                                                       [100%]

================================== 15 passed in 8.34s ===================================

(myvenvpy) keshav@keshav-Lenovo-ideapad:~/Desktop/CS305/assignment2/src$ coverage report -m
Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
connection.py        12      0   100%
list_sublist.py      15      0   100%
main.py             117      0   100%
test1.py             31      0   100%
test2.py             26      0   100%
test3.py             16      0   100%
test4.py             14      0   100%
test5.py             14      0   100%
-----------------------------------------------
TOTAL               245      0   100%


