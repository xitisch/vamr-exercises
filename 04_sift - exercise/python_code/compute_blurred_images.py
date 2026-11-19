import cv2
import numpy as np

def computeBlurredImages(image_pyramid, num_scales, sift_sigma):
    """
    Compute the blurred images for the given image pyramid.
    Args:
        image_pyramid: The image pyramid.
        num_scales: The number of scales.
        sift_sigma: The sigma for the Gaussian blur.
    Returns:
        List[np.ndarray[width, height, num_scales + 3]]: The blurred images (gaussians) for each octave.
    """
    # The number of octaves can be inferred from the length of the image pyramid
    pass
    # TODO: Your code here
        
