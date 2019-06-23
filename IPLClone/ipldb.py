from django.db.models import *
from iplapp.models import *
import  click
import  openpyxl
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","IPLClone.settings")

import django
django.setup()


def ImportMatchesData():
    wb = openpyxl.load_workbook('C:\\Users\\18suryateja\\Downloads\\matches.xlsx')
    ws = wb['matches (1)']
    for row in ws:
        temp = list(map(lambda x: x.value, row))
        if (temp[0] is not None and temp[0] != "id"):
            m = Matches(matchid=int(temp[0]), season=int(temp[1]), city=temp[2], date=temp[3], team1=temp[4],
                        team2=temp[5], toss=temp[6], toss_decision=temp[7], result=temp[8], dl_applied=int(temp[9]),
                        winner=temp[10], win_by_runs=int(temp[11]), win_by_wickets=int(temp[12]), mom=temp[13],
                        venue=temp[14], umpire1=temp[15], umpire2=temp[16], umpire3=temp[17])
            m.save()

ImportMatchesData()

def ImportDeliveriesData():
    wb = openpyxl.load_workbook('C:\\Users\\18suryateja\\Downloads\\deliveries.xlsx')
    ws = wb['deliveries']
    for row in ws:
        temp = list(map(lambda x:x.value,row))
        if (temp[0] is not None and temp[0]!='match_id'):
            d = Deliveries(match_id = Matches.objects.filter(matchid = int(temp[0]))[0],inning = int(temp[1]),bat_team = str(temp[2]),bowl_team = str(temp[3]),
                           over = int(temp[4]),ball = int(temp[5]),striker = temp[6],non_striker = temp[7],
                           bowler = temp[8],is_super_over = int(temp[9]),wide_runs = int(temp[10]),bye_runs = int(temp[11]),
                           leg_byes = int(temp[12]),noball_runs = int(temp[13]),penalty = int(temp[14]),batsman_runs = int(temp[15]),
                           extras = int(temp[16]),total_runs = int(temp[17]),player_dismissed = temp[18],dismissal_kind = temp[19],fielder = temp[20])
            d.save()

ImportDeliveriesData()