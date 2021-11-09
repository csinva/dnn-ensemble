import numpy as np
import shutil
import os
from .edua_utils import imagenet_dict

"""
    Creates dataset targets a given path to a partial dataset.
"""

def create_partial_dataset_targets():
    path_to_imagenet_train = '/accounts/projects/vision/scratch/data/cv/imagenet_full/train'
    partial_path = '/accounts/projects/vision/scratch/data/cv/imagenet_partial/10percent/train'

    targets = []
    imagenet_classes = list(imagenet_dict.values())

    for img in os.listdir('/accounts/projects/vision/scratch/data/cv/imagenet_partial/10percent/train'):
        folder_name = img.split('_')[0]
        class_name = imagenet_folder_to_class_dict[folder_name]
        targets.append(imagenet_classes.index(class_name))
    print(targets)

if __name__ == "__main__":
    create_partial_dataset_targets()