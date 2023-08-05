import numpy as np
from matplotlib import pyplot

def plot_sample(file_name):
    data = np.load(file_name)
    src_images, tar_images = data['arr_0'], data['arr_1']
    print('Loaded: ', src_images.shape, tar_images.shape)

    n_samples = 3
    for i in range(n_samples):
        pyplot.subplot(2, n_samples, 1 + i)
        pyplot.axis('off')
        pyplot.imshow(src_images[i].astype('uint8'))
    # plot target image
    for i in range(n_samples):
        pyplot.subplot(2, n_samples, 1 + n_samples + i)
        pyplot.axis('off')
        pyplot.imshow(tar_images[i].astype('uint8'))
    pyplot.show()


