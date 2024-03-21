import os
import shutil

from mrcnn.my_inference import predict_images
from mrcnn.preprocess_images import preprocess_images
from mrcnn.convert_to_image import convert_to_image, convert_to_imagej

def perform_segmentation(input_dir, output_dir):
  """
  Performs image segmentation tasks with predefined options.

  Args:
      input_dir (str): Path to the directory containing images for segmentation.
      output_dir (str): Path to the directory for saving outputs.
  """

  # Define segmentation options
  rescale = False
  scale_factor = 2  # Factor to downsize images by if rescale is True
  save_preprocessed = True
  save_compressed = True
  save_masks = True
  verbose = True
  output_imagej = True

  # Create output directory if it doesn't exist
  if output_dir != '' and not os.path.isdir(output_dir):
    os.mkdir(output_dir)

  # Check if output directory is empty
  if os.path.isdir(output_dir) and len(os.listdir(output_dir)) > 0:
    print("ERROR: Make sure the output directory is empty.")
    return

  # Define subdirectory paths based on output_dir
  preprocessed_image_dir = os.path.join(output_dir, "preprocessed_images/")
  preprocessed_image_list = os.path.join(output_dir, "preprocessed_images_list.csv")
  rle_file = os.path.join(output_dir, "compressed_masks.csv")
  output_mask_dir = os.path.join(output_dir, "masks/")
  output_imagej_dir = os.path.join(output_dir, "imagej/")

  # Preprocess the images
  if verbose:
    print("\nPreprocessing your images...")
  preprocess_images(input_dir,
                    preprocessed_image_dir,
                    preprocessed_image_list,
                    verbose=verbose)

  # Run inference on the neural network
  if verbose:
    print("\nRunning your images through the neural network...")
  predict_images(preprocessed_image_dir,
                  preprocessed_image_list,
                  rle_file,
                  rescale=rescale,
                  scale_factor=scale_factor,
                  verbose=verbose)

  # Save masks based on options
  if save_masks:
    if verbose:
      print("\nSaving the masks...")

    if output_imagej:
      convert_to_image(rle_file,
                       output_mask_dir,
                       preprocessed_image_list,
                       rescale=rescale,
                       scale_factor=scale_factor,
                       verbose=verbose)

      convert_to_imagej(output_mask_dir,
                       output_imagej_dir)
    else:
      convert_to_image(rle_file,
                       output_mask_dir,
                       preprocessed_image_list,
                       rescale=rescale,
                       scale_factor=scale_factor,
                       verbose=verbose)

  # Cleanup temporary files
  os.remove(preprocessed_image_list)

  if not save_preprocessed:
    shutil.rmtree(preprocessed_image_dir)

  if not save_compressed:
    os.remove(rle_file)

  if not save_masks:
    shutil.rmtree(output_mask_dir)

# Example usage
perform_segmentation("/16Tbdrive1/vishakhag/CamAge_Package_ingredients/sample1/",
                     "/16Tbdrive1/vishakhag/CamAge_Package_ingredients/seg_outputs/out4/")
