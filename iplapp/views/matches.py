from django.shortcuts import render
from iplapp.views import *
from django.http import HttpResponse
from django.views import View
from django.urls import resolve
from iplapp.models import *
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import *
from django.db.models import Count,Sum

def pointsTable(year):
    table = []
    total_teams = Matches.objects.filter(season=year).values('team1').distinct().count()
    total_matches = (total_teams-1) * 2
    total_matches_upto_playoffs = (total_matches*total_teams)//2
    temp = Matches.objects.filter(season = year).values_list('winner').annotate(won = Count('winner')).order_by('-won')
    for i in temp:
        a,b = i
        if(a is not None):
            table.append([a,b])
    for i in range(total_teams):
        table[i].insert(1,total_matches)
        table[i].append(total_matches - table[i][2])
        table[i].insert(0,i+1)
    return table

def getTeamStats(team):
    seasonStats = []
    for year in range(2008,2020):
        temp = pointsTable(year)
        for row in temp:
            if(row[1]==team):
                row.pop(1)
                row.insert(0,year)
                seasonStats.append(row)
    return seasonStats

class DisplaySeasonMatches(View):
    def get(self,request,*args,**kwargs):
        if(kwargs):
            mats = Matches.objects.filter(**kwargs).values_list("team1","team2","venue","toss","toss_decision","winner","mom","matchid")
            paginator = Paginator(mats, 10)
            page = request.GET.get('page')
            mats = paginator.get_page(page)
            pointstable = pointsTable(kwargs['season'])
            return render(request,"showAllMatches.html",{'matches':mats,'s':str(kwargs['season']),'user':request.user,'pt':pointstable})
        else:
            mats = Matches.objects.filter(season='2019').values_list("team1", "team2", "venue", "toss", "toss_decision","winner", "mom","matchid")
            paginator = Paginator(mats, 10)
            page = request.GET.get('page')
            mats = paginator.get_page(page)
            pointstable = pointsTable(2019)
            return render(request, "showAllMatches.html", {'matches': mats, 's':'2019','user':request.user,'pt':pointstable})

class DisplayMatchDetails(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self,request,*args,**kwargs):
        if(kwargs):
            match = Matches.objects.filter(matchid = kwargs['id']).values_list("team1", "team2", "venue", "toss", "toss_decision","winner", "mom","matchid")
            match_obj = Matches.objects.get(matchid = kwargs['id'])
            top3bats1 = Deliveries.objects.values('striker').filter(match_id_id=match_obj,inning=1). \
                               annotate(sum=Sum('total_runs')).order_by('-sum')[0:3]
            top3bats2 = Deliveries.objects.values('striker').filter(match_id_id=match_obj, inning=2). \
                            annotate(sum=Sum('total_runs')).order_by('-sum')[0:3]
            top3_wicket_takers1 = Deliveries.objects.values('bowler').filter(match_id_id=match_obj, inning=1).exclude(
                fielder=''). \
                                      annotate(count=Sum('total_runs')).order_by('-count')[0:3]
            top3_wicket_takers2 = Deliveries.objects.values('bowler').filter(match_id_id=match_obj, inning=2).exclude(
                fielder=''). \
                                      annotate(count=Count('total_runs')).order_by('-count')[0:3]

            inning1 = Deliveries.objects.filter(match_id_id = match_obj,inning = 1).values_list("inning","over","ball","striker","bowler","total_runs","total_runs","player_dismissed","dismissal_kind","fielder")
            inning2 = Deliveries.objects.filter(match_id_id = match_obj,inning = 2).values_list("inning","over","ball","striker","bowler","total_runs","total_runs","player_dismissed","dismissal_kind","fielder")
            return render(request,"displayMatchDetails.html",{'match' : match,'inning1':inning1,'inning2':inning2,'user':request.user,'topbat1':top3bats1,'topbat2':top3bats2,'topbowl1':top3_wicket_takers1,'topbowl2':top3_wicket_takers2})

class TeamHomePage(View):
    def get(self,request,*args,**kwargs):
        teams = {1: 'Royal Challengers Bangalore', 2: 'Mumbai Indians', 3: 'Sunrisers Hyderabad', 4: 'Rajasthan Royals',
                 5: 'Delhi Capitals',
                 6: 'Kings XI Punjab', 7: 'Chennai Super Kings', 8: 'Gujarat Lions', 9: 'Rising Pune Supergiant',
                 10: 'Pune Warriors', 11: 'Kolkata Knight Riders',
                 12: 'Kochi Tuskers Kerala', 13: 'Deccan Chargers', 14: 'Delhi Daredevils'}
        seasonStats = getTeamStats(teams[kwargs['id']])
        return render(request,'TeamHomePage.html',{'stats':seasonStats,'team':teams[kwargs['id']],'user':request.user})