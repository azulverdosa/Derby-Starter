from rest_framework import serializers

from track_api.models import Schedule, Team, Skater

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('game_date', 'home_team', 'visiting_team', 'confirmed', 'sanctioned', 'location', )


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('name', 'abbreviation', 'location', 'sanctioned', 'region', 'logo', 'schedule')

class SkaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skater
        fields = ('full_name', 'skater_name', 'skater_number', 'birth_year', 'pronouns', 'insurance_number', 'team')