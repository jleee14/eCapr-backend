from rest_framework import serializers
from .models import Bet
from django.db.models import F, Case, When
from django.db.models.lookups import GreaterThan, LessThan

class BetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    bet_url = serializers.ModelSerializer.serializer_url_field(view_name='bet_detail')

    class Meta:
        model = Bet
        fields = ('id', 'bookmaker', 'name', 'odds', 'bet_type', 'event_finish', 'wager', 'sport', 'league', 'notes', 'date_placed', 'date_resolved', 'resolved', 'bet_result', 'owner', 'bet_url', 'pot_win')