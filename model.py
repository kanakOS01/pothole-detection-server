import shutil
import os
from ultralytics import YOLO
import requests
import cloudinary
import cloudinary.uploader

cloudinary.config( 
    cloud_name = os.getenv("CLOUD_NAME"), 
    api_key = os.getenv("API_KEY"), 
    api_secret = os.getenv("API_SECRET"),
    secure=True
)

def predict(image_url, conf):
    try:
        os.remove("input_img.jpg")
        print("Old input image removed")
    except Exception:
        print("No old input image found")

    try:
        # os.remove("runs/detect/predict/input_img.jpg")
        # os.rmdir("runs/detect/predict")
        shutil.rmtree("runs/detect/predict/")
        print("Old output image removed")
    except Exception:
        print("No old output image found")

    print("Finding potholes...")
    model = YOLO("best.pt")

    img_reponse = requests.get(image_url)
    with open("input_img.jpg", 'wb') as f:
        f.write(img_reponse.content)

    model.predict(source='input_img.jpg', conf=conf, save=True)

    print("Uploading image to cloudinary...")
    response = cloudinary.uploader.upload("runs/detect/predict/input_img.jpg")
    print(response['url'])
    return response['url']

if __name__ == '__main__':
    predict("https://res.cloudinary.com/dzr9gskix/image/upload/v1719934817/gvotlgdjjemjpf0rdxyj.jpg", 0.9)
