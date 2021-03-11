from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
import datetime
from .Utilities import All_Season_Race_Results

# Create your views here.

class RaceResultsAll(APIView):
    permission_classes = [AllowAny]
    " this api will give driver standings for historical years"

    def get(self,request):
        "provide all historical data from 1950-2020"
        year = datetime.date.today().year
        value =All_Season_Race_Results.SeasonResults(1950,year)
        print("/n/n/n/n/n/n/n", year)
        return Response({'message':value})

    def post(self, requests):
        """provide race for a given range"""
        start = requests.data.get('start')
        end = requests.data.get('end')
        value = All_Season_Race_Results.SeasonResults(start,end)
        return  Response({'message':value})


class RaceResultsCurrent(APIView):
    permission_classes = [AllowAny]
    """provide current race standings"""
    def get(self):
        year = datetime.date.today().year
        value = All_Season_Race_Results.SeasonResults(year,year+1)
        return Response({'message': value})


