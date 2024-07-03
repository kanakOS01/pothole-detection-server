import os
import requests
from ultralytics import YOLO
import cloudinary
import cloudinary.uploader

cloudinary.config( 
    cloud_name = "dhbkszqxb", 
    api_key = "133271172794764", 
    api_secret = "UWX_WTSvW5zJM_nk2UFANh-wXMU",
    secure=True
)

def predict(image_url, conf):
    try:
        os.remove("input_img.jpg")
        os.remove("runs/detect/predict/input_img.jpg")
        os.rmdir("runs/detect/predict")
        print("Old image removed")
    except Exception:
        print("No old image found")

    print("Finding potholes...")
    model = YOLO("best.pt")

    img_reponse = requests.get(image_url)
    with open("input_img.jpg", 'wb') as f:
        f.write(img_reponse.content)

    _ = model.predict(source='input_img.jpg', conf=conf, save=True)

    print("Uploading image to cloudinary...")
    response = cloudinary.uploader.upload("runs/detect/predict/input_img.jpg")
    print(response['url'])
    return response['url']

if __name__ == '__main__':
    predict("https://res.cloudinary.com/dzr9gskix/image/upload/v1719934817/gvotlgdjjemjpf0rdxyj.jpg", 0.9)
