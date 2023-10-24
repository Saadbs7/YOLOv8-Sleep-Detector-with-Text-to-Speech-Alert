import os
import pandas as pd
import cv2
# import re

# Function to convert (xmin, ymin, width, height) to YOLOv8 format
def convert_to_yolov8(xmin, ymin, width, height, image_width, image_height):
    # Calculate bounding box center coordinates (x_center, y_center)
    x_center = (xmin + width / 2) / image_width
    y_center = (ymin + height / 2) / image_height

    # Normalize width and height (w_normalized, h_normalized)
    w_normalized = width / image_width
    h_normalized = height / image_height

    return x_center, y_center, w_normalized, h_normalized

# Write the Path Addresses
Path = r'C:\Users\pc\Desktop\Python Snippets\Yolov8\MATLAB to Yolov8\Sleep\images\train'
filelist = os.listdir(Path)        # Makes a list of names of the images in the Path Folder
savePath = r'C:\Users\pc\Desktop\Python Snippets\Yolov8\MATLAB to Yolov8\Sleep\labels\train'
csvfile = r'C:\Users\pc\Desktop\Python Snippets\Yolov8\MATLAB to Yolov8\SleepMATLAB.csv'

# Create labels folder if it does not exist
if not os.path.exists(savePath):
    os.makedirs(savePath)

# Give an image sample for extracting the images shapes. If images have different sizes, then implement different strategy
img = cv2.imread(Path + '//' + filelist[0])

df = pd.read_csv(csvfile)
df.columns = list(range(df.columns.size))
df = df.dropna()

df1 = df.copy()

df1.iloc[:,0], df1.iloc[:,1], df1.iloc[:,2], df1.iloc[:,3] = convert_to_yolov8(df.iloc[:,0], df.iloc[:,1], df.iloc[:,2], df.iloc[:,3], img.shape[0], img.shape[0])

# Iterate over each image and rename the corresponding new annotation text file 
count = 0
for i in filelist:
    i = i.replace('jpg', 'txt')
    with open(savePath + '\\' + i, 'w') as f:
        # line = str(df1.iloc[count].values)
        # line = line.replace('[','')
        # line = line.replace(']','')
        # line = re.sub(r'\s+', ' ', line)  #In case there are some extra spaces coming in the label files
        # f.write('0' + line)
        
        # Change number with classes, e.g., 0, 1, 2, etc.
        f.write('1 {} {} {} {}'.format(df1.iloc[count,0], df1.iloc[count,1], df1.iloc[count,2], df1.iloc[count,3]))

    count += 1

print('Done')

