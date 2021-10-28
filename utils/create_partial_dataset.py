import numpy as np
import shutil

"""
    Creates partial dataset of imagenet containing 10% of images from each class.
"""

def create_partial_dataset():
    rng = np.random.default_rng(42)

    path_to_imagenet_train = '/accounts/projects/vision/scratch/data/cv/imagenet_full/train'
    partial_path = '/accounts/projects/vision/scratch/data/cv/imagenet_partial/10percent/train'

    for folder in os.listdir(path_to_imagenet_train):
        folder_dir = join(path_to_imagenet_train, folder)
        if os.path.isdir(folder_dir):
            imgs = os.listdir(folder_dir)
            ten_percent_of_imgs = int(len(os.listdir(folder_dir)) * 0.1)
            rand_class_imgs = rng.permutation(imgs)[:ten_percent_of_imgs]
            for img in rand_class_imgs:
                img_path = join(folder_dir, img)
                shutil.copy(img_path, join(partial_path, img))
                
if __name__ == "__main__":
    create_partial_dataset()