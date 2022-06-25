# import statements
# import temp file to avoid error in zip file opening
import tempfile

# import zipfile to open zip file
import zipfile

# import numpy to convert list to numpy
import numpy

# import FastApi for the API interface
from fastapi import FastAPI, File, UploadFile, Form

# import connectionClass to establish the connection
from connection import connectionClass

# import list_sublist to get list utilities like sort list
from list_sublist import listUtils

# import face recognition for face recognition part of the assignment
import face_recognition

app = FastAPI()

# api end point to serach top k matches in the table
@app.post("/search_faces/")
async def search_faces(file: UploadFile =
                      File(..., description="An image file, possible containing multiple human faces."), k: int = Form(...), confidence: float = Form(...)):

   # Implemented the logic for performing the facial search

   # check if the given image is an image file
   if (('.jpg' not in file.filename) and ('.jpeg' not in file.filename) and ('.png' not in file.filename)):
      return {"status": "ERROR", "body": "Not an image file"}

   # call connection class to establish the connection
   connObj = connectionClass()

   # get encoding of the given file, that is, the file that is taken as input
   image_given = face_recognition.load_image_file(file.file)
   image_encoding = face_recognition.face_encodings(image_given)

   # check if image has no face
   if (len(image_encoding) == 0):
      return {"status": "ERROR", "body": "No face in the given image"}

   # Run the query to get all rows of the database
   query = "select faces.id, faces.name, faces.vector from faces;"
   connObj.cursor.execute(query)
   data = connObj.cursor.fetchall()

   # myList would store all images from database that matched the faces of the input image 
   myList = []

   # access each row of the table
   for row in data:
      
      # tlist is a list of true or false value depending on the matching of the faces
      tlist = face_recognition.compare_faces(image_encoding, numpy.array(row[2]), 1-confidence)

      # access all the elements of tlist
      for i in range(0, len(tlist)):

          # if i-th face of the input image is a match to face of that row of table of database
          if tlist[i] == True:

              # get euclidean distance between the encodings
              fd = face_recognition.face_distance([numpy.array(row[2])], image_encoding[i])[0]

              # add all relevant fields from the row to the list
              myList.append([i, row[0], row[1], fd])

   # using listUtils sort the list by first face_number of face of the input image and then by euclidean distance
   myList = listUtils.Sort(myList)

   # iterate over the sorted list
   l = len(myList)

   # body is the final request body
   body = {}

   # initialize body dictionary
   for j in range(0, l):
       body["faces"+str(myList[j][0])] = []

   # count stores whether k matches have been found for a particular image or not
   count = 0

   # prev stores the previous image id being processed
   prev = 0

   # iterate over the sublists of the sorted list
   for i in myList:

       # if same face as the last is being processed
       if (i[0] == prev):

           # if less than k matches till now
           if (count < k):

               # add information about that face to body
               body["faces" + str(i[0])].append([i[1], i[2], i[3]])
               count = count+1

       # if new face number
       else:
           prev = i[0]
           count = 0
           body["faces" + str(i[0])].append([i[1], i[2], i[3]])
           count = count+1

   # commit to table          
   connObj.commitToDb()

   # close conection object
   connObj.closeConn()

   # return the status
   return {"status": "OK", "body": body}

# api end point to add a single face
@app.post("/add_face/")
async def add_face(file: UploadFile =
                  File(..., description="An image file having a single human face.")):

   # Implemented the logic for saving the face details in DB

   # establish connection to the database
   connObj = connectionClass()

   # check if file name is an image or not
   if (('.jpg' not in file.filename) and ('.jpeg' not in file.filename) and ('.png' not in file.filename)):
      return {"status": "ERROR", "body": "Not an image file"}

   # get the encoding of the given face image
   image_given = face_recognition.load_image_file(file.file)
   image_encoding_list = face_recognition.face_encodings(image_given)

   # check if image has no face
   if (len(image_encoding_list) == 0):
      return {"status": "ERROR", "body": "No face in the given image"}

   # check if image has multiple faces
   if (len(image_encoding_list) > 1):
      return {"status": "ERROR", "body": "Multiple faces found"}

   # get the first face in the 
   image_encoding = image_encoding_list[0]

   # run INSERT query to add the face details in the faces table
   a = str(image_encoding.tolist())
   query = "INSERT INTO faces(name, vector) values('"+ file.filename +"', ARRAY "+ a +");"
   connObj.cursor.execute(query)

   # commit the details to table
   connObj.commitToDb()

   # Closing the connection
   connObj.closeConn()

   # return the final status
   return {"status": "OK", "body": "successfully added " + file.filename}

# api endpoint to add all the faces from a zip file
@app.post("/add_faces_in_bulk/")
async def add_faces_in_bulk(file: UploadFile =
                           File(..., description="A ZIP file containing multiple face images.")):
   # Implemented the logic for saving the face details in DB

   if ('.zip' not in file.filename):
      return {"status": "ERROR", "body": "Not a zip file"}
   
   # establish connection to the database
   connObj = connectionClass()

   # copy contents to a temporary file to prevent "Spooled Temporary File object has no attribute seekable"
   temp = tempfile.TemporaryFile()
   temp.write(file.file.read())
   zfile = zipfile.ZipFile(temp, 'r')

   count = 0

   # access names in the zip file
   for f in zfile.namelist():
      
      # if the name contains a .jpg extension, that is, it is an image file
      if ('.jpg' in f or '.jpeg' in f or '.png' in f):

         # open that file
         t = zfile.open(f)

         # get encoding of that file
         image_given = face_recognition.load_image_file(t)
         image_encoding = face_recognition.face_encodings(image_given)

         # check if that file has a face image or not
         if len(image_encoding) != 0:

            # display name of file added
            print(f)

            # increase image count by 1
            count = count+1
            
            # insert the relevant information into the faces table
            a = str(image_encoding[0].tolist())
            query = "INSERT INTO faces(name, vector) values('"+ f +"', ARRAY "+ a +");"
            connObj.cursor.execute(query)

            # commit the insertion
            connObj.commitToDb()

   #Closing the connection
   connObj.closeConn()

   # if no image files in the zip file
   if count == 0:
      return {"status": "ERROR", "body": "No image file in given zip file"}

   # return the final response
   return {"status": "OK", "body": " Successfully added "+ str(count) + " images"}


# api end point to get information for a particular image
@app.post("/get_face_info/")
async def get_face_info(api_key: str = Form(...), face_id: str = Form(...)):
   
   # Implemented the logic for retrieving the details of a face record from DB.

   # establish the connection
   connObj = connectionClass()

   # execute the query to get information regarding a particular face
   query = "SELECT * from faces where id = "+face_id + ";"
   connObj.cursor.execute(query)
   data = connObj.cursor.fetchone()

   if not data:
      return {"status": "ERROR", "body": "No face with the given id"}

   # commit not nneded here, but then also done for better generality
   connObj.commitToDb()

   # define the response body
   body = dict()
   body["face ID"] = data[0]
   body["photo_name"] = data[1]
   body["person_name"] = data[3]
   body["version"] = data[4]
   body["date_of_photo"] = data[5]

   # close connection to database
   connObj.closeConn()

   # return the response
   return {"status": "OK", "body": body}

# api end point to add meta data for a particular image
@app.post("/add_meta_data/")
async def add_meta_data(person_name: str = Form(...), face_id: str = Form(...), version_face: int = Form(...), date: str = Form(...)):
   
   # Implemented the logic for adding meta data for a specific face in DB

   # get the connection
   connObj = connectionClass()

   # check if face id exists or not
   query = "SELECT * from faces where id = "+face_id + ";"
   connObj.cursor.execute(query)
   data = connObj.cursor.fetchone()

   # if no face id, then return with error
   if not data:
      return {"status": "ERROR", "body": "No face with the given id"}

   # execute the query to add details for the face_id
   query = "UPDATE faces set person_name = '" + person_name + "', version = " + str(version_face) +", date = '" + date +"' where id = "+face_id + ";"
   connObj.cursor.execute(query)

   # commit the changes to the database
   connObj.commitToDb()

   # close the connection
   connObj.closeConn()

   # return the response
   return {"status":"OK", "body" : "Meta Data added for "+ face_id}