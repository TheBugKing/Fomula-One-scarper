from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
import requests
import datetime
from bs4 import BeautifulSoup as bs
from .utilities import All_historical_driver_standings

# Create your views here.
#should go to team api  app folder
class Team_Standings_current(APIView):
    """pulls current season team standings as it stands"""
    permission_classes =[AllowAny]

    def scrapper_team_standings_current(self):
        "scrapper that pulls current season team standings"
        url = 'https://www.formula1.com/en/teams.html'
        page = requests.get(url)
        print("\n\n\n\n\n\n\n\n\n", page)
        if page:
            soup = bs(page.content, 'html.parser')
            team_div = soup.find_all('div', class_='listing-item')
            season = soup.find('h1', class_='f1-black--xxl no-margin').text


            formulaOne = []
            teams_list = []

            for _ in team_div:
                team_name = _.find('span', class_='f1-color--black').text
                team_rank = _.find('div', class_='rank').text
                team_points = _.find('div', class_='points').find('div', class_='f1-wide--s').text
                # listing-team-drivers
                drivers_fname = _.findAll('span', class_='first-name')
                drivers_lname = _.findAll('span', class_='last-name')
                drivers = []

                for i, j in zip(drivers_fname, drivers_lname):
                    temp_driver = i.text + " " + j.text
                    drivers.append(temp_driver)

                teams_list.append({'name': team_name,
                                   'drivers': drivers,
                                   'rank': team_rank,
                                   'point': team_points,
                                   })

            Season = {
                'season': season,
                'teams': teams_list
            }
            formulaOne.append(Season)

            return Response({'message': formulaOne})
        else:
            return Response({ 'message':"failed to connect to {}".format(url)})





    def get(self,request):
        """Get api for current season team standngs"""
        print("error in def get \n\n\n\n\n")
        return self.scrapper_team_standings_current()

class DriverAllStandings(APIView):
    permission_classes = [AllowAny]
    " this api will give driver standings for historical years"

    def get(self,requests):
        "provide all historical data from 1950-2020"
        year = datetime.date.today().year
        value =All_historical_driver_standings.all_historical_driver_standings(1950,year)
        return Response({'message':value})

    def post(self, requests):
        """provide standings for a given range"""
        start = requests.data.get('start')
        end = requests.data.get('end')
        value =All_historical_driver_standings.all_historical_driver_standings(start,end)
        return  Response({'message':value})

class DriverStandingsCurrent(APIView):
    permission_classes = [AllowAny]
    """provide current driver standings"""

    def get(self):
        year = datetime.date.today().year
        value = All_historical_driver_standings.all_historical_driver_standings(year,year+1)
        return Response({'message': value})