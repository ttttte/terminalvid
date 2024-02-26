import cv2
from time import sleep


name = "aki.mp4"
vidcap = cv2.VideoCapture(f'./{name}')

#calculate aspect ratio
original_width = int(vidcap.get(cv2.CAP_PROP_FRAME_WIDTH))
original_height = int(vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT))
aspect_ratio = original_width / original_height

#whatever fits your sreen
w = 106
#calculate the height to maintain aspect ratio
h = int(w / aspect_ratio)

total_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
iter = 0

filename = name.split(".")[0]
print (filename)
f = open(f"{filename}.txt", "a")

#save the video into txt file
while(True):       
    ret,frame = vidcap.read() 
    if ret:
        resized_frame = cv2.resize(frame, (w, h)) 
        for y in range(h):
            for x in range(w):
                (b, g, r) = resized_frame[y, x]
                f.write(f"{x},{y},{r},{g},{b}#")
        f.write("\n")
        print (f"{iter}/{total_frames}")
        iter += 1
  
    else: 
        break

vidcap.release() 
cv2.destroyAllWindows() 

