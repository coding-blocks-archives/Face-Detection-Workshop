import cv2


# Capture the Video from webcam..
cap = cv2.VideoCapture(0)

# load haarcascade file
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")


# Infinte Loop
while True:

	# Read the Webcam Image
	ret, frame  = cap.read()


	# If not able to read image
	if ret == False:
		continue


	# Detect faces on the current frame
	faces = face_cascade.detectMultiScale(frame)


	# Plot rectangle around all the faces
	for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)


	# Display the frame
	cv2.imshow("Video Frame", frame)
	

	# Find the key pressed
	key_pressed = cv2.waitKey(1) & 0xFF

	# If keypressed is q then quit the screen
	if key_pressed == ord('q'):
		break


# release the camera resource and destroy the window opened.
cap.release()
cv2.destroyAllWindows()