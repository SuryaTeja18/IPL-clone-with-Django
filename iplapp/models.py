from django.db import models

# Create your models here.

class Matches(models.Model):
    matchid = models.IntegerField()
    season = models.IntegerField()
    city = models.CharField(max_length=128,null=True)
    date = models.DateField()
    team1 = models.CharField(max_length=128)
    team2 = models.CharField(max_length=128)
    toss = models.CharField(max_length=128)
    toss_decision = models.CharField(max_length=128)
    result = models.CharField(max_length=128)
    dl_applied = models.IntegerField()
    winner = models.CharField(max_length=128,null=True)
    win_by_runs = models.IntegerField()
    win_by_wickets = models.IntegerField()
    mom = models.CharField(max_length=128,null=True)
    venue = models.CharField(max_length=128)
    umpire1 = models.CharField(max_length=128,null=True)
    umpire2 = models.CharField(max_length=128,null=True)
    umpire3 = models.CharField(max_length=128,null=True)

    def __str__(self):
        return (f"Season {self.season}, {self.team1} Vs {self.team2}" )


class Deliveries(models.Model):
    match_id = models.ForeignKey(Matches,on_delete=models.CASCADE)
    inning = models.IntegerField()
    bat_team = models.CharField(max_length=128)
    bowl_team = models.CharField(max_length=128)
    over = models.IntegerField()
    ball = models.IntegerField()
    striker = models.CharField(max_length=128)
    non_striker = models.CharField(max_length=128)
    bowler = models.CharField(max_length=128)
    is_super_over = models.IntegerField()
    wide_runs = models.IntegerField()
    bye_runs = models.IntegerField()
    leg_byes = models.IntegerField()
    noball_runs = models.IntegerField()
    penalty = models.IntegerField()
    batsman_runs = models.IntegerField()
    extras = models.IntegerField()
    total_runs = models.IntegerField()
    player_dismissed = models.CharField(max_length=128,null=True)
    dismissal_kind = models.CharField(max_length=128,null=True)
    fielder = models.CharField(max_length=128,null=True)

    def __str__(self):
        return (f"Over:{self.over}.{self.ball}, runs:{self.total_runs}")