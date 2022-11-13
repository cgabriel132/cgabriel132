#importing the library
import cv2
import dlib
from imutils import face_utils

cap = cv2.VideoCapture(0) #Creating the object

detect = dlib.get_frontal_face_detector() # Object Created
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
while True:
	ret, img = cap.read()  # Reading images

	if not ret:           #Checking that image is recieved
		break

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	
	boxes = detect(gray)  # Detection the location of faces
	#print(boxes)
	for i,d in enumerate(boxes):
		shape = predictor(gray, d) #Applying predictor on each face we detect
		shape = face_utils.shape_to_np(shape) # Converting the object to numpy array
		for i in shape[48:68]:
			cv2.line(img,tuple(i),tuple(i),(255,0,0),5) # Drawing points on the coordinates

		#left, top, right, bottom = d.left(), d.top(), d.right(), d.bottom()
		#cv2.rectangle(img, (left, top), (right, bottom),(0, 255, 0), 2)

	cv2.imshow("Image", img)    # Showing the video feed
	key = cv2.waitKey(1) & 0xFF  
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

cv2.destroyAllWindows()