import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
 
from fonctions import find_informations

monkey = find_informations('od_PmtmMDV0')

zerator = find_informations('JhWZWXvN_yo')

def test_find_id_vid_video():
    assert monkey['id_vid_video'] == 'od_PmtmMDV0'

def test_find_titre():
    assert monkey['titre'] == 'Driving to the banana store'

def test_find_nom_chaine():
    assert monkey['nom_chaine'] == 'Clayton Collins'

def test_find_description():
    assert monkey['nb_likes'] >= 0

def test_find_description():
    assert monkey['description'] == 'Here we see an orangutan driving to the banana store to buy lots of bananas.'

def test_find_liens():
    assert zerator['liens_desc'] == [
            "https://www.youtube.com/user/ZeratoRSC2/?sub_confirmation=1",
            "https://www.twitch.tv/zerator",
            "https://www.twitch.tv/videos/1630581181",
            "http://www.ZeratoR.com/",
            "https://boutiquezerator.com/",
            "http://e.lga.to/ZeratoR",
            "https://www.facebook.com/ZeratoR",
            "https://twitter.com/ZeratoR",
            "https://www.instagram.com/zerator",
            "https://discord.gg/zerator",
            "https://www.tiktok.com/@ZeratoR",
            "https://www.mandatory.gg/",
            "https://twitter.com/MandatoryGG",
            "https://www.instagram.com/mandatory.gg/",
            "https://www.tiktok.com/@mandatory.gg",
            "https://discord.gg/3uHncKP",
            "https://www.twitch.tv/mandatory",
            "https://www.facebook.com/MandatoryGG/"
        ]