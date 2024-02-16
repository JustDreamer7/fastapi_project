from email.message import EmailMessage
from app.config import settings
from pydantic import EmailStr
def create_booking_confirmation_template(booking: dict, email_to: EmailStr) -> EmailMessage:
    email = EmailMessage()
    email['Subject'] = 'Подтверждение бронирования'
    email['From'] = settings.SMTP_USER
    email['To'] = email_to

    email.set_content(
        f"""
        <h1>Подтверждение бронирования</h1>
        <p>Здравствуйте!</p>
        <p>Вы успешно забронировали номер в отеле с {booking['date_from']} по {booking['date_to']}.</p>
        """
    )
    return email

def create_booking_reminder_template(
    booking: dict,
    email_to: EmailStr,
    days: int,
):
    email = EmailMessage()

    email["Subject"] = f"Осталось {days} дней до заселения"
    email["From"] = settings.SMTP_USER
    email["To"] = email_to

    email.set_content(
        f"""
            <h1>Напоминание о бронировании</h1>
            Вы забронировали отель с {booking["date_from"]} по {booking["date_to"]}
        """,
        subtype="html"
    )
    return email