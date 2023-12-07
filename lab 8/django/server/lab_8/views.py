from django.shortcuts import render
from django.core.serializers import serialize
import json
from .models import Player, Profession, Race
# Create your views here.
def index(request):
    player = Player.objects.all().values('id', 'name', 'title', 'rase__race', 'profession__profession', 'birthday', 'banned', 'level')
    player_list = list(player)
    for player in player_list:
        player['birthday'] = player['birthday'].strftime('%Y-%m-%d')
    with open('lab_8/static/json/data_users.json', 'w') as file:
        json.dump(player_list, file)
    return render(request,"lab_8/index.html")