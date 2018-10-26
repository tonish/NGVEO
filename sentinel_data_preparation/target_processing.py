import os
from sentinel_data_preparation import utils
import numpy as np
import rasterio

class TargetProcessing():
    def __init__(self, params):
        self.params = params
        self.ignore_value = -1

    def process_target_data(self, sentinel_file, tile_id, cloud_mask=None):

        #Get the tile id
        # tile_id = utils.get_tile_id(sentinel2_file, self.params['tile_ids'])

        # Read target data
        target_filename = os.path.join(self.params['target_dir'], tile_id.lower() + "_"
                                       + self.params['target_basename'] + ".tif")
        with rasterio.open(target_filename) as target_file:
            target_data = target_file.read()

            # Set ignore value
            target_data[target_data <= 0] = self.ignore_value
            if cloud_mask is not None:
                for b in range(0, target_data.shape[0]):
                    target_b = target_data[b]
                    target_b[cloud_mask[0] > 0] = self.ignore_value
                    target_data[b] = target_b

            # Create a boolean mask
            mask = np.zeros(target_data[0].shape).astype(np.bool)
            mask[target_data[0] > 0] = True

            # Saving the cloud mask as memory map
            basename = os.path.splitext(os.path.basename(sentinel_file))[0]
            tiles_dir = os.path.join(self.params['outdir'], tile_id, basename)

            for band_ind, target_name in enumerate(self.params['target_names']):
                utils.save_np_memmap(os.path.join(tiles_dir, target_name), target_data[band_ind], 'float32')

            # Save list of coordinates of labelled pixels
            utils.save_list_of_labelled_pixels(mask, tiles_dir)

            return 0