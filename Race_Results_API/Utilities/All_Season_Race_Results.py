from bs4 import BeautifulSoup as bs
import requests


def SeasonResults(start,end):
    """ get all race results"""
    site ="https://www.formula1.com"
    seasonResults =[]
    for year in range(start, end+1):
        url ="https://www.formula1.com/en/results.html/{}/races.html".format(year)
        page = requests.get(url)

        if page:
             soup = bs(page.content ,'html.parser')

             #find the warpper of table
             div_wrapper = soup.find('div', class_ = 'resultsarchive-content')

            #race result title
             race_season = div_wrapper.find('h1', class_ ='ResultsArchiveTitle').text.strip()
             rows = div_wrapper.findAll('tr')
             print(len(rows))
             temp_results = []
             for _ in rows[1:]:
                 grand_prix = _.find('a').text.strip()
                 grand_prix_url = site + _.find('a', class_='dark bold ArchiveLink')['href']
                 grand_prix_date = _.find('td', class_='dark hide-for-mobile').text.strip()
                 winner = _.find('span', class_='hide-for-tablet').text.strip() + " " + _.find('span',class_='hide-for-mobile').text.strip()
                 season = race_season[:4]
                 team = _.find('td', class_='semi-bold uppercase').text.strip()
                 laps = _.find('td', class_='bold hide-for-mobile').text.strip()
                 time = _.find('td', class_='dark bold hide-for-tablet').text.strip()

                 temp_results.append({'season': season, 'grand_prix': grand_prix, 'grand_prix_url': grand_prix_url,
                                      'date': grand_prix_date, 'winner': winner, 'team': team, 'laps': laps,
                                      'time': time})


             seasonResults.append({race_season:temp_results})

        else:
            return "something went wrong"
    return(seasonResults)

