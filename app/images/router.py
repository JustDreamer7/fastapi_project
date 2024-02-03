from fastapi import APIRouter, UploadFile
import shutil

router = APIRouter(prefix="/images", tags=["Изображения"])

@router.post("/images")
async def add_hotel_image(image_id: int, file: UploadFile):
    with open(f"app/static/images/{image_id}.webp", "wb+") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}