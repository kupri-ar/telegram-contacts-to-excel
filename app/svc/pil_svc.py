from io import BytesIO
from PIL import Image as PILImage
from openpyxl.drawing.image import Image


def download_and_resize_image(client, ph):
    try:
        downloaded_ph = client.download_file(ph)
        file_in_memory = BytesIO(downloaded_ph)

        pil_img = PILImage.open(file_in_memory)
        new_width = int(92)
        new_height = int(92)
        resized_img = pil_img.resize((new_width, new_height))

        resized_img_io = BytesIO()
        resized_img.save(resized_img_io, format='JPEG')
        resized_img_io.seek(0)

        return Image(resized_img_io)
    except Exception as e:
        # print(e)
        pass
