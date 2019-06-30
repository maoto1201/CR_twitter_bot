import tweepy
import crl_image

# crl_scrap.sta
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np


#ファイル名の辞書作成
card=["Baby Dragon","Minions","Balloon","Goblin Barrel", "Miner","Ice Wizard","Mega Minion", "Goblin Gang", "Bats","Barbarians", "Lava Hound",
        "Giant","Guards", "Dark Prince", "Electro Wizard","Bandit", "Battle Ram","Executioner","Hog Rider", "Ice Spirit", "Golem",
        "Fire Spirit","Three Musketeers","Royal Giant","P.E.K.K.A","Mega Knight","Elite Barbarians","Giant Skeleton","Goblin Giant","Sparky","Ice Gorem",
       "Minion Horde","Rascals","Witch","Prince","Bowler","Cannon Cart","Electro Dragon","Ram Rider","Royal Hogs","Hunter","Royal Recruits",
       "Lumberjack","Inferno Dragon","Night Witch","Magic Archer","Valkyrie","Musketeer","Mini P.E.K.K.A","Zappies","Flying Machine","Knight","Archers",
       "Bomber","Skeleton Barrel","Skeleton Army","Wall Breakers","Princess","Royal Ghost","Dart Goblin","Goblins","Spear Goblins","Skeletons","Bomb Tower",
       "Cannon","Inferno Tower","Mortar","Tesla","X-Bow","Barbarian Hut","Elixir Collector","Furnace","Goblin Hut","Tombstone","Goblin Cage","Arrows",
       "Barbarian Barrel","Fireball","Rocket", "Giant Snowball","Lightning","Poison","The Log","Tornado","Zap","Clone","Earthquake","Graveyard","Freeze",
     "Rage","Mirror","Heal"]

img = {'Baby Dragon': 'baby_dragon.png', 'Goblin Gang': 'goblin_gang.png', 'Minions': 'minion.png"', 'Balloon': 'chr_balloon.png', 'Goblin Barrel': 'goblin_barrel.png', 'Miner': 'miner.png', 'Ice Wizard': 'ice_wizard.png', 'Mega Minion': 'mega_minion.png', 'Bats': 'bats.png', 'Barbarians': 'barbarians.png', 'Lava Hound': 'lava_hound.png', 'Giant': 'giant.png', 'Guards': 'skeleton_warriors.png', 'Dark Prince': 'dark_prince.png', 'Electro Wizard': 'electro_wizard.png', 'Bandit': 'bandit.png', 'Battle Ram': 'battle_ram.png', 'Executioner': 'executioner.png', 'Hog Rider': 'hog_rider.png', 'Ice Spirit': 'snow_spirits.png', 'Golem': 'chr_golem.png', 'Fire Spirit': 'fire_spirits.png', 'Three Musketeers': 'three_musketeers.png', 'Royal Giant': 'royal_giant.png', 'P.E.K.K.A': 'pekka.png', 'Mega Knight': 'mega_knight.png', 'Elite Barbarians': 'angry_barbarian.png', 'Giant Skeleton': 'giant_skeleton.png', 'Goblin Giant': 'goblin_giant.png', 'Sparky': 'zapMachine.png', 'Ice Gorem': 'ice_golem.png', 'Minion Horde': 'minion_horde.png', 'Rascals': 'rascals.png', 'Witch': 'chr_witch.png', 'Prince': 'prince.png', 'Bowler': 'bowler.png', 'Cannon Cart': 'cannon_cart.png', 'Electro Dragon': 'electro_dragon.png', 'Ram Rider': 'ram_rider.png', 'Royal Hogs': 'royal_hog.png', 'Hunter': 'hunter.png', 'Royal Recruits': 'royal_recruits.png', 'Lumberjack': 'rage_barbarian.png', 'Inferno Dragon': 'inferno_dragon.png', 'Night Witch': 'dark_witch.png', 'Magic Archer': 'magic_archer.png', 'Valkyrie': 'valkyrie.png', 'Musketeer': 'musketeer.png', 'Mini P.E.K.K.A': 'mini_pekka.png', 'Zappies': 'zappies.png', 'Flying Machine': 'flying_machine.png', 'Knight': 'knight.png', 'Archers': 'archers.png', 'Bomber': 'bomber.png', 'Skeleton Barrel': 'skeleton_balloon.png', 'Skeleton Army': 'skeleton_horde.png', 'Wall Breakers': 'wallbreaker.png', 'Princess': 'princess.png', 'Royal Ghost': 'ghost.png', 'Dart Goblin': 'blowdart_goblin.png', 'Goblins': 'goblins.png', 'Spear Goblins': 'goblin_archer.png', 'Skeletons': 'skeletons.png', 'Bomb Tower': 'bomb_tower.png', 'Cannon': 'chaos_cannon.png', 'Inferno Tower': 'building_inferno.png', 'Mortar': 'building_mortar.png', 'Tesla': 'building_tesla.png', 'X-Bow': 'building_xbow.png', 'Barbarian Hut': 'barbarian_hut.png', 'Elixir Collector': 'building_elixir_collector.png', 'Furnace': 'firespirit_hut.png', 'Goblin Hut': 'fire_furnace.png', 'Tombstone': 'tombstone.png', 'Goblin Cage': 'goblin_cage.png', 'Arrows': 'order_volley.png', 'Barbarian Barrel': 'barb_barrel.png', 'Fireball': 'fire_fireball.png', 'Rocket': 'rocket.png', 'Giant Snowball': 'snowball.png', 'Lightning': 'lightning.png', 'Poison': 'poison.png', 'The Log': 'the_log.png', 'Tornado': 'tornado.png', 'Zap': 'zap.png', 'Clone': 'copy.png', 'Earthquake': 'earthquake.png', 'Graveyard': 'graveyard.png', 'Freeze': 'freeze.png', 'Rage': 'rage.png', 'Mirror': 'mirror.png', 'Heal': 'heal.png'}

# 後で修正


# dfを作成し、データを収集し格納
list = []
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []

df = pd.DataFrame()

url = "https://royaleapi.com/decks/popular?time=1d&sort=win&size=30&players=PvP&min_trophies=6300&max_trophies=10000&mode=detail&type=TopLadder&&&global_exclude=false"
# トッププレーヤーマルチ勝率

html_doc = requests.get(url).text
soup=BeautifulSoup(html_doc,"html.parser")

#print(soup)
tags = soup.find_all("img")

for tag in tags:
  a = tag.get("alt")
  if a == None:
    pass
  else:
    list.append(a)
list1 = [list[idx:idx + 8] for idx in range(0,len(list), 8)]

df["card"]=list1

tags2 = soup.find_all("td",{"class":"right aligned strong"})
for tag2 in tags2:
  b = tag2.text
  list2.append(b)

df["winrate"] = list2

tags3 = soup.find_all("div",{"class":"ui black inverted label margin0"})
for tag3 in tags3:
  c = tag3.text[1:5]
  list3.append(c)

df["userate"] = list3

tags4 = soup.find_all("div",{"class":"header item mobile-hide tablet-hide"})
for tag4 in tags4:
  d = tag4.text.strip("\n")
  list4.append(d)

df["deckname"] = list4

tags5 = soup.find_all("a",{"class":"ui blue icon circular button button_popup"})
for tag5 in tags5:
  e = tag5.get("href")
  list5.append(e)

df["link"] = list5

###crl_scrap.fin

CK = "secret" #(API key)
CS = "secret" #(API secret key)
AT = "secret" #(Access token)
AS = "secret" #(Access token secret)

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)

# ツイート
#api.update_status("自動投稿テスト")

#画像付きツイート
winrate = df.iloc[0,1]
userate = df.iloc[0,2]
deckname = df.iloc[0,3]
link = df.iloc[0,4]

api.update_with_media(status = '【マルチ勝率1位デッキ】\n \n ■Deck:%s \n ■Win rate:%s \n ■Use rate:%s \n ■Link:%s ' % ( deckname,winrate,userate,link ), filename = 'test.png')#画像のファイル名いれる


#検索で引っかかった人をフォロー&ふぁぼ
q = "クラロワリーグ" #ここに検索キーワードを設定
count = 50
search_results = api.search(q=q, count=count)

for result in search_results:
    username = result.user._json['screen_name']
    user_id = result.id #ツイートのstatusオブジェクトから、ツイートidを取得
    print(user_id)
    user = result.user.name #ツイートのstatusオブジェクトから、userオブジェクトを取り出し、名前を取得する
    print(user)
    tweet = result.text
    print(tweet)
    time = result.created_at
    print(time)
    try:
        api.create_favorite(user_id) #ファボする
        print(user)
        print("をライクしました")
        api.create_friendship(user_id)
        print("をフォローしました")
    except:
        print("もうすでにふぁぼかフォローしてます")
    print("##################")
