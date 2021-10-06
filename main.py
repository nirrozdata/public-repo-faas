import dtlpy as dl
import logging
import time

class ServiceRunner(dl.BaseServiceRunner):

    def update_item_metadata(self, item):
        # Get Item - update metadata

        item.metadata["user"] = {"user" : time.time()}
        item.update()
        

        print('Successfully move all items to new dir')


