import os

from PIL import Image
from imagehash import average_hash

from data_flow.models import EventModel
if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "suki_timeline.settings")
    for obj in EventModel.objects.all():
        obj.image_hash = average_hash(
            Image.open(
                "static/image/%d.jpg" % obj.id
            ),
            10
        )
        obj.save()