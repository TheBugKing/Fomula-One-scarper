from django.urls import path,include
from .views import RaceResultsAll , RaceResultsCurrent

app_name ='race-results-api'


urlpatterns = [
    path('current/', RaceResultsCurrent.as_view(), name='current-team-standing'),
    path('all/', RaceResultsAll.as_view(), name='driver-standings'),

]