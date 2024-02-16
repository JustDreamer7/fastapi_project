import smtplib

from pydantic import EmailStr

from app.config import settings
from app.tasks.celery_app import celery
from PIL import Image
from pathlib import Path

from app.tasks.email_templates import create_booking_confirmation_template


@celery.task
def process_picture(path: str):
    pic_path = Path(path)
    pic = Image.open(pic_path)
    pic_resized_100 = pic.resize((100, 100))
    pic_resized_500 = pic.resize((500, 500))
    pic_resized_500.save(f"app/static/images/resized_500_{pic_path.name}")
    pic_resized_100.save(f"app/static/images/resized_100_{pic_path.name}")

@celery.task
def send_booking_confirmation_email(booking: dict, email_to: EmailStr):
    # email_to = settings.SMTP_USER # Временно для тестирования, отправка писем на свой почтовый ящик
    msg_content = create_booking_confirmation_template(booking, email_to)

    with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(msg_content)
