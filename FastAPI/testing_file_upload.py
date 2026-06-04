from fastapi import FastAPI, File, UploadFile
from pathlib import Path
import shutil

app = FastAPI()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@app.post("/upload_file")
def upload_file(file: UploadFile = File(...)):

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "saved_to": str(file_path)
    }