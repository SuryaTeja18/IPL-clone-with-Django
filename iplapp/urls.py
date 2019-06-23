from django.contrib import admin
from django.urls import path,include
from iplapp.views import matches,auth
from django.urls import include, path

urlpatterns = [
    path('matches/', matches.DisplaySeasonMatches.as_view(),name='display_2019_matches'),
    path('matches/<int:season>',matches.DisplaySeasonMatches.as_view(),name='display_season_matches'),
    path('matchDetails/<int:id>',matches.DisplayMatchDetails.as_view(),name='display_match_details'),
    path('login/',auth.Login.as_view(),name='login'),
    path('logout/',auth.logout_user,name='logout'),
    path('register/',auth.SignUp.as_view(),name='register'),
    path('teamhome/<int:id>',matches.TeamHomePage.as_view(),name = 'displayTeamHome'),
]