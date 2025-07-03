import os
import django
from datetime import timedelta
from django.utils import timezone
from pytz import timezone as tz

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fitness_booking.settings")
django.setup()

from booking.models import FitnessClass

IST = tz("Asia/Kolkata")
now_ist = timezone.now().astimezone(IST)

FitnessClass.objects.all().delete()

FitnessClass.objects.create(
    name="Yoga", datetime=now_ist, instructor="Anjali", available_slots=10
)
FitnessClass.objects.create(
    name="Zumba",
    datetime=now_ist + timedelta(days=2, hours=2),
    instructor="Shivam",
    available_slots=10,
)
FitnessClass.objects.create(
    name="HIIT",
    datetime=now_ist + timedelta(days=1, hours=9),
    instructor="Ganesh",
    available_slots=5,
)

print("Seeded fitness classes successfully.")
