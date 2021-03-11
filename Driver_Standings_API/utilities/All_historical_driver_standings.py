from bs4 import BeautifulSoup as bs
import requests
import json


#overall driver standings in a season
#1950-2020 total season
def all_historical_driver_standings(start,end):
    standings = []
    #change to current year datetime later
    site ="https://www.formula1.com/en/results.html"
    for _ in range(start, end+1):

        temp_url = 'https://www.formula1.com/en/results.html/{}/drivers.html'.format(_)
        response = requests.get(temp_url)

        if response:
            # if connection successfull
            soup = bs(response.content, 'html.parser')

            # get the table wraping where the required data is
            div_wrapper = soup.find('div', class_='resultsarchive-wrapper')

            # get season title
            season_title = div_wrapper.find('h1', class_='ResultsArchiveTitle').text.strip()[:4]
            print(season_title + " scrapping... pleast wait")
            # get all table rows for all data
            rows = div_wrapper.findAll('tr')

            temp_std = []
            # from each row get the details for each season
            for _ in rows[1:]:
                pos = _.find('td', class_='dark').text.strip()
                fname = _.find('span', class_='hide-for-tablet').text.strip()
                lname = _.find('span', class_='hide-for-mobile').text.strip()
                nationality = _.find('td', class_='dark semi-bold uppercase').text.strip()
                car = _.find('a', class_='grey semi-bold uppercase ArchiveLink').text.strip()
                pts = _.find('td', class_='dark bold').text.strip()
                driver_url = site+_.find('a', class_ = 'dark bold ArchiveLink')['href']
                temp_std.append({'postion': pos, 'name': fname + " " + lname, 'driver_stats' :driver_url, 'nationality': nationality, 'car': car,
                                 'points': pts})
            standings.append({season_title: temp_std})



        else:
            print("failed to connect to {}".format(temp_url))

    return standings