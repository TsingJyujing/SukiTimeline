# Run main in PyCharm django console
from PIL import Image
import os
from data_flow.models import EventModel
from util.files import filter_images
from util import *
import traceback
import imagehash

raw_image_dir = "raw_files"
target_dir = "data"


def hash_algorithm(file):
    return str(imagehash.average_hash(Image.open(file), hash_size=10))


def process_image(image_filename):
    image = Image.open(image_filename)
    _exif = image._getexif()
    try:
        tick_info = exif_to_tick(_exif[36867])
    except:
        tick_info = os.path.getmtime(image_filename)
        print("Warning: No exif time in %s" % image_filename)
    hash_value = str(imagehash.average_hash(image, hash_size=10))
    emodel = EventModel(
        tick=tick_info,
        title="Title",
        comment=image_filename,
        image_hash=hash_value
    )
    emodel.save()
    img_id = emodel.id
    image.save(os.path.join(target_dir, "%s.jpg" % hash_value))



def clean_table():
    EventModel.objects.all().delete()


def main():
    clean_table()
    image_files = filter(
        lambda filename: filter_images(filename),
        os.listdir(raw_image_dir)
    )
    for image_file in image_files:
        try:
            process_image(os.path.join(raw_image_dir, image_file))
            print("Process %s successfully" % image_file)
        except Exception as ex:
            print("Error while processing: %s" % image_file)
            print(traceback.format_exc())

# from util.import_tool import main; main()
