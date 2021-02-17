from .models import Appointment
from .serializers import AppointmentSerializer, ScreenOneSerializer, ScreenThreeSerializer, HomeButton
from rest_framework import generics, viewsets, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponseRedirect


class ScreenOne(APIView):
    def get(self, request):
        your_data = [{"Home": "You could request an Appointment with our team",
                      "Video": "https://www.youtube.com/watch?v=XxaE6UZt4J4",
                      "appointment": "http://127.0.0.1:8000/Appointment/"}]
        results = ScreenOneSerializer(your_data, many=True).data
        return Response(results)


class AppointmentView(viewsets.ModelViewSet, APIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def create(self, request, *args, **kwargs):
        response = super(AppointmentView, self).create(request, *args, **kwargs)
        return HttpResponseRedirect(redirect_to="http://127.0.0.1:8000/Finish/")


class ScreenThree(APIView):
    def get(self, request):
        your_data = [{"Finish": "Your request is received and someone will be in touch with you soon",
                      "Home": "http://127.0.0.1:8000/"}]
        results = ScreenThreeSerializer(your_data, many=True).data
        return Response(results)
