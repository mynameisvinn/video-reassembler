import cv2
import argparse
import pandas as pd

'''
function
--------
given sequence of images from csv, display images in sequential order.

for example, do $ python image_loader.py -s glider.csv
''' 

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--sequence", required = True)
args = vars(ap.parse_args())

print args

ls_sequences_x = pd.read_csv(args['sequence'])
print ls_sequences_x

sorted_list_image_paths = list(ls_sequences_x['0'])
print sorted_list_image_paths

for cycle, path in enumerate(sorted_list_image_paths):

	image = cv2.imread(path)
	cv2.putText(image, "Status: {}".format(str(cycle) + '_' + path), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
	cv2.imshow("image", image)
	cv2.waitKey(0)