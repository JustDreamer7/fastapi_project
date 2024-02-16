from fastapi import APIRouter, UploadFile
import shutil
from app.tasks.tasks import process_picture
router = APIRouter(prefix="/images", tags=["Изображения"])

@router.post("/images")
async def add_hotel_image(image_id: int, file: UploadFile):
    with open(f"app/static/images/{image_id}.webp", "wb+") as buffer:
        shutil.copyfileobj(file.file, buffer)
    process_picture.delay(f"app/static/images/{image_id}.webp")
    return {"filename": file.filename}