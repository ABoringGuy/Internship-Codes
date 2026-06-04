import uuid
from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.responses import FileResponse
from pathlib import Path
from PIL import Image
from camera_capture import capture_image#External  Python Program
import shutil#Used to copy file from one location to another
from pydantic import BaseModel


class Image_Parameters(BaseModel):
    width: int
    height: int

class Image_Format(BaseModel):
    format: str = "png"

valid_format_list=["png", "jpg", "webp", "PNG", "JPG", "JPEG", "WEBP"]
app=FastAPI()
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)
file_name=f"{uuid.uuid4()}"#Gives unique ID. Inbuilt function

def get_image():
    image_path= UPLOAD_DIR / f"{file_name}.jpg"
    if not image_path.is_file():
        raise HTTPException( status_code=404,detail="Image not found")
    image= Image.open(image_path)
    return image_path,image

@app.post("/camera_capture_image")
def camera_capture_image():
    image_path=Path(capture_image(UPLOAD_DIR / f"{file_name}.jpg"))
    if not image_path.is_file():
        raise HTTPException( status_code=404,detail="Image not found")
    return FileResponse(image_path)

@app.post("/upload_image")
def upload_image(file:UploadFile= File()):
    image_path=UPLOAD_DIR / f"{file_name}.jpg"
    with open(image_path, "wb") as original_file:
        shutil.copyfileobj(file.file, original_file)
    return FileResponse(image_path)

@app.get("/get_metadata")
def get_metadata():
    image_path,image= get_image()
    return [image.width, image.height, image.mode, image.format]

@app.put("/resize_image")
def resize_image(img_parameters:Image_Parameters):
    image_path,image= get_image()
    resized_image=image.resize((img_parameters.width,img_parameters.height))
    new_image_path= Path(UPLOAD_DIR/ f"resized_{file_name}.jpg")
    resized_image.save(new_image_path)
    return FileResponse(new_image_path)

@app.put("/change_format")
def change_format(img_format:Image_Format):
    image_path,image= get_image()
    if img_format.format not in valid_format_list:
        raise HTTPException( status_code=401,detail="Invalid Image Format")
    new_image_path= Path(f"changed_{file_name}.{img_format.format}")
    image.save(UPLOAD_DIR / new_image_path, format=f"{img_format.format}")
    return {"format":image.format,
            "filepath":new_image_path}
