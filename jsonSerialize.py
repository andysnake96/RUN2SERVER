#serialize races info in json by json lib & python dict into jsonGare.txt
#dict <--->json			-> = json.dump(dict,filePointer)
#				<- = json.loads(jsonStr)-> list of dict....

import json

races=list()					#glbl list of race to serialize in json...
raceKeys=('dateRace', 'description', 'distance','id_race', 'locality', 'n_max_runner', 'name', 'note', 'prenExpire', 'urlImage', 'urlRace')

jsonFile=open("jsonGare.txt","w")		#dest output file with serialized json

def addRace(dateRace, description, distance, id_race, locality, n_max_runner, name, note, prenExpire, urlImage, urlRace):
	#create dict rappresenting race entity from values...
	print(raceKeys)
	race=dict()
	race['dateRace']=dateRace
	race['description']=description
	race['distance']=distance
	race['id_race']=id_race
	race['locality']=locality
	race['n_max_runner']=n_max_runner
	race['name']=name
	race['note']=note
	race['prenExpire']=prenExpire
	race['urlImage']=urlImage
	race['urlRace']=urlRace
	
	races.append(race)			#added to races to serialize


def serialize():
	#serialize writted race into json file pointed from jsonFile 
	json.dump(races,jsonFile)
	jsonFile.close()

if __name__=="__main__":
	#adding races...
	addRace("2018-09-23-09:00","2nda ed. mezza maratona via pacis",21.097,0,"Roma",300,"Rome Half Marathon Via Pacis 2nda edizione","occhio alle buche","2018-09-17-00:00","http://www.fidal.it/funzioni/phpThumb/phpThumb.php?src=http://www.fidal.it/upload/Viapacis/20170914_1_giorno_0004.JPG&w=940&h=460&zc=1&hash=f592be057557474f87d868d5dc9ce5d2","http://www.romahalfmarathon.org")
	
	addRace("2018-09-30-09:30","quarta ed. cardio race ",16.092,1,"Roma",300,"cardio race ed.4 2018","corri per la salute","2018-09-19-00:00","http://www.cardiorace.it/","https://www.cardiorace.it/wp-content/uploads/2018/04/logo-cardiorace.png")

	serialize()
