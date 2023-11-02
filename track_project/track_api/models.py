from django.db import models

class Schedule(models.Model):
    game_date = models.DateField()
    home_team = models.ForeignKey('Team', on_delete=models.DO_NOTHING, related_name='home_team')
    visiting_team = models.ForeignKey('Team', on_delete=models.DO_NOTHING, related_name='visiting_team')
    confirmed = models.BooleanField()
    sanctioned = models.BooleanField()
    location = models.CharField(max_length=150, default='')


class Team(models.Model):
    name = models.CharField(max_length=100, default='')
    abbreviation = models.CharField(max_length=100, default='')
    location = models.CharField(max_length=150, default='')
    sanctioned = models.BooleanField()
    region = models.CharField(max_length=100, default='')
    logo = models.ImageField()
    schedule = models.ForeignKey(Schedule, on_delete=models.DO_NOTHING, related_name='schedule')


class Skater(models.Model):
    full_name = models.CharField(max_length=100, default='')
    skater_name = models.CharField(max_length=100, default='')
    skater_number = models.CharField(max_length=4, default='')
    birth_year = models.CharField(max_length=10, default='')
    pronouns = models.CharField(max_length=20, default='')
    insurance_number = models.CharField(max_length=10, default='')
    team = models.ForeignKey('Team', on_delete=models.DO_NOTHING, related_name='team')