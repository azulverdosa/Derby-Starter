from django.shortcuts import render
from rest_framework import viewsets

from track_api.serializers import ScheduleSerializer, TeamSerializer, SkaterSerializer
from track_api.models import Schedule, Team, Skater


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class SkaterViewSet(viewsets.ModelViewSet):
    queryset = Skater.objects.all()
    serializer_class = SkaterSerializer