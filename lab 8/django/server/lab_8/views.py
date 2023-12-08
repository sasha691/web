from django.shortcuts import render
from django.core.serializers import serialize
import json
from .models import Player, Profession, Race
# Create your views here.
def index(request):
    if request.method == 'POST':
        race_id = request.POST.get('race')
        profession_id = request.POST.get('profession')

        race = Race.objects.get(pk=race_id)
        profession = Profession.objects.get(pk=profession_id)

        banned=request.POST.get('banned')
        banned = banned == 'on'

        new_player = Player(
            name=request.POST.get('name'),
            title=request.POST.get('title'),
            rase=race,
            profession=profession,
            level=request.POST.get('level'),
            birthday=request.POST.get('birthday'),
            banned=banned
        )
        new_player.save()
    player = Player.objects.all().values('id', 'name', 'title', 'rase__race', 'profession__profession', 'birthday', 'banned', 'level')
    player_list = list(player)
    for player in player_list:
        player['birthday'] = player['birthday'].strftime('%Y-%m-%d')
    with open('lab_8/static/json/data_users.json', 'w') as file:
        json.dump(player_list, file)
    return render(request,"lab_8/index.html")