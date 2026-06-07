from rest_framework import serializers
from .models import DailyPulses

class DailyPulseSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source = 'user.email', read_only = True)

    class Meta:
        model = DailyPulses
        fields = ['id', 'user_email', 'energy_score', 'has_blocker', 'comment', 'created_at']
        read_only_fields = ['id', 'created_at']


    def validate_energy_score(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Energy score must strictly fall between 1 and 5.")
        return value