from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.timezone import localtime
from rest_framework import status
from pytz import timezone
from .models import FitnessClass, Booking


class ClassListView(APIView):
    def get(self, request):
        user_tz = request.query_params.get("tz", "Asia/Kolkata")
        try:
            tz = timezone(user_tz)
        except:
            return Response({"error": "Invalid timezone"}, status=400)

        classes = FitnessClass.objects.all()
        data = []
        for c in classes:
            dt = localtime(c.datetime, tz).strftime("%d-%m-%Y %H:%M:%S")
            data.append(
                {
                    "id": c.id,
                    "name": c.name,
                    "datetime": dt,
                    "instructor": c.instructor,
                    "available_slot": c.available_slots,
                }
            )
        return Response(data)


class BookClassView(APIView):
    def post(self, request):
        d = request.data
        class_id = d.get("class_id")
        name = d.get("client_name")
        email = d.get("client_email")

        if not all([class_id, name, email]):
            return Response({"error": "Missing fields"}, status=400)

        try:
            fc = FitnessClass.objects.get(id=class_id)
        except FitnessClass.DoesNotExist:
            return Response({"error": "Invalid class ID"}, status=404)

        if fc.available_slots <= 0:
            return Response({"error": "no slots available"}, status=400)

        Booking.objects.create(fitness_class=fc, client_name=name, client_email=email)
        fc.available_slots -= 1
        fc.save()
        return Response({"message": "Booking successful"}, status=201)


class BookingListView(APIView):
    def get(self, request):
        email = request.query_params.get("email")
        if not email:
            return Response({"error": "Email is required"}, status=400)

        bookings = Booking.objects.filter(client_email=email)
        data = []
        for b in bookings:
            dt = localtime(b.fitness_class.datetime).strftime("%d-%m-%Y %H:%M:%S")
            data.append(
                {
                    "id": b.id,
                    "client_name": b.client_name,
                    "client_email": b.client_email,
                    "class_name": b.fitness_class.name,
                    "class_datetime": dt,
                }
            )
        return Response(data)
