# -*-coding:utf-8 -*-

from config import app_secret,app_key,app_id,imagePath

from piaoOCR import get_text_from_image as POCR
from piaoOCR import get_file_content

def main():
    image_data = get_file_content(imagePath)
    print('q')
    result = POCR(image_data,app_id, app_key, app_secret)

    print(result)


if __name__ == "__main__":
    main()