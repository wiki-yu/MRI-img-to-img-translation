# load, split and scale the maps dataset ready for training
from os import listdir
import numpy as np
from numpy import asarray
from numpy import vstack
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img

# load all images in a directory into memory
def load_images(path, size=(256,512)):
	src_list, tar_list = list(), list()
	# enumerate filenames in directory, assume all are images
	for filename in listdir(path):
		# load and resize the image
		pixels = load_img(path + filename, target_size=size)
		# convert to numpy array
		pixels = img_to_array(pixels)
		# split into satellite and map
		sat_img, map_img = pixels[:, :256], pixels[:, 256:]
		src_list.append(sat_img)
		tar_list.append(map_img)
	return [asarray(src_list), asarray(tar_list)]



def load_npy_images(input_path, target_path, num_imgs=20):
    input_list, target_list = list(), list()

    # Load input images
    for filename in listdir(input_path):
        if filename.endswith(".npy"):
            print(filename)
            img_npy = np.load(input_path + filename)
            print(np.shape(img_npy))
            # append the first num_imgs images
            input_list.extend(img_npy[:num_imgs])

   # Load target images
    for filename in listdir(target_path):
        if filename.endswith(".npy"):
            print(filename)
            img_npy = np.load(target_path + filename)
            print(np.shape(img_npy))
            target_list.extend(img_npy[0][:num_imgs])  # Take only the first set of 20 images

    return [np.array(input_list), np.array(target_list)]
