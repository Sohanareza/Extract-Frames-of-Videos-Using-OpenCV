# Program To Read video and Extract Frame

import cv2 

# Function to extract frames 
def frame_capture(path): 

	# Path to video file 
	vid_obj = cv2.VideoCapture(path) 

	# Used as counter variable 
	count = 0

	# checks whether frames were extracted 
	success = 1

	while success: 

		# vid_obj object calls read 
		# function extract frames 
		success, image = vid_obj.read() 

		# Saves the frames with frame-count 
		cv2.imwrite("frame%d.jpg" % count, image) 

		count += 1


# Driver Code 
if __name__ == '__main__': 

	# Calling the function 
	frame_capture("C:\\Users\\rubai\\Desktop\\OpenCV Learning\\Projects\\Extract Frames From Video\\Extract-Frames-of-Videos-Using-OpenCV\\Video.mp4") 
