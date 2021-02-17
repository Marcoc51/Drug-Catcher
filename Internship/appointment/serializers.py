from rest_framework import serializers
from .models import Appointment, CompanyNames, CountryCodes, CountryNames, Objectives


class ScreenOneSerializer(serializers.Serializer):
    Home = serializers.ReadOnlyField()
    Video = serializers.URLField(read_only=True)
    appointment = serializers.URLField(read_only=True)


class HomeButton(serializers.Serializer):
    Home = serializers.URLField(read_only=True)


class AppointmentSerializer(serializers.ModelSerializer):
    # CountryCode = serializers.ChoiceField(choices=CountryCodes)
    # OperationCountries = serializers.ChoiceField(choices=CountryNames)
    # CompanyName = serializers.ChoiceField(choices=CompanyNames)
    # Objective = serializers.ChoiceField(choices=Objectives)

    class Meta:
        model = Appointment
        fields = ['first_name', 'last_name', 'email', 'country_code', 'phone_number', 'operation_countries',
                  'company_name', 'objective', 'description']


class ScreenThreeSerializer(serializers.Serializer):
    Finish = serializers.ReadOnlyField()
    Home = serializers.URLField(read_only=True)
