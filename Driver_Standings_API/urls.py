
from django.urls import path,include
from .views import Team_Standings_current , DriverAllStandings,DriverStandingsCurrent

app_name ='driver-standing-api'

urlpatterns = [
    path('current-team/', Team_Standings_current.as_view(), name='current-team-standing'),
    path('all/', DriverAllStandings.as_view(), name='driver-standings'),
    path('current/', DriverStandingsCurrent.as_view(), name='driver-standings'),

]