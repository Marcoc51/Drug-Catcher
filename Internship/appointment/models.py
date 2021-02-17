from django.db import models
from iso3166 import countries
from django.core.validators import RegexValidator, EmailValidator

CountryCodes = sorted([(country.numeric, country.numeric) for country in countries])
CountryNames = [('Country 1', 'Country 1'), ('Country 2', "Country 2"), ('Country 3', "Country 3")]
CompanyNames = [('Company 1', 'Company 1'), ('Company 2', 'Company 2'), ('Company 3', 'Company 3')]
Objectives = [('complaint', 'complaint'), ('suggestion', 'suggestion')]


# class OperationCountries(models.Model):
#     name = models.CharField(max_length=20, choices=CountryNames)
#
#      def __str__(self):
#         return self.name


# class Companies(models.Model):
#     country = models.ForeignKey(OperationCountries, on_delete=models.CASCADE)
#     name = models.CharField(max_length=20, choices=CompanyNames)
#
#     def __str__(self):
#         return self.name


class Appointment(models.Model):
    first_name = models.CharField(max_length=15, validators=[RegexValidator(r'^[a-zA-Z]*$',
                                                                            'Only Alpha Characters are Allowed')])
    last_name = models.CharField(max_length=15, validators=[RegexValidator(r'^[a-zA-Z]*$',
                                                                           'Only Alpha Characters are Allowed')])
    email = models.EmailField(blank=False, validators=[EmailValidator])
    country_code = models.CharField(max_length=3, choices=CountryCodes, default="")
    phone_number = models.CharField(max_length=11, validators=[RegexValidator(r'^[0-9]*$',
                                                                              'Only Numeric Characters are Allowed')])
    operation_countries = models.CharField(max_length=15, choices=CountryNames)
    company_name = models.CharField(max_length=15, choices=CompanyNames)
    objective = models.CharField(max_length=20, choices=Objectives)
    description = models.TextField()
