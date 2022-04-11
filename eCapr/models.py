from django.db import models
import datetime, django

class Bet(models.Model):
    bookmaker = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    odds = models.IntegerField()
    bet_type = models.CharField(max_length=75)
    event_finish = models.DateField(default=datetime.date.today())
    wager = models.IntegerField()
    sport = models.CharField(max_length=50)
    league = models.CharField(max_length=50)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE) 
    notes = models.TextField()
    date_placed = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_resolved = models.DateTimeField(auto_now_add=False, auto_now=True) # need to update using queryset.update() - ask in issue.
    resolved = models.BooleanField()
    bet_result = models.CharField(max_length=10, default='None')
    pot_win = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


    def __str__(self):
        return self.name
