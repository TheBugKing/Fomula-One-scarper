# Fomula-One-scarper
This repository contains and Django REST Framework project that use API endpoints to trigger various scraping functions

"All rights belong to their respective owners. I do not own any of this content."

-----------------------------------------------------------------------------------------------

urls : 
1 - localhost://driver-standings-api/all --- get request returns driver standings from 1950 - present

2 - localhost://driver-standings-api/all/ --- post request with year range as paramenter (returns records you want to scrape from the site )
						e.g : 2018,2020
3-  localhost://driver-standings-api/current/ --- get request returns current Driver standings 
	-					>NOTE : current standing is retrieveable only after the first race of the season is finished and scores, standings are updated
						else, it will throw you an error as scraped with return a NONE object

4-  localhost://driver-standings-api/current-team/ --- get request returns current constructor standings of the season
							->NOTE : current standing is retrieveable only after the first race of the season is finished and scores, standings are updated
							else, it will throw you an error as scraped with return a NONE object

5 - localhost://race-results-api/all/   --- get request returns race results from 1950 - present

6 - localhost://race-results-api/all/   --- post request with year range as paramenter (returns records you want to scrape from the site )
						e.g : 2018,2020

7 - localhost://race-results-api/current/   --- get request returns current race standings 
	-					>NOTE : current standing is retrieveable only after the first race of the season is finished and scores, standings are updated
						else, it will throw you an error as scraped with return a NONE object
