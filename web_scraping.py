import requests
from bs4 import BeautifulSoup
import io



#excercice1
#Ecrire un programme python qui récupère et affiche à la console le contenu du fichier robot.txt de
#fr.wikipedia.org

reponse0 = requests.get('http://fr.wikipedia.org/robot.txt')
print(reponse0.content)
print(reponse0.text)

#exercice2
#Ecrire un programme python qui récupère le nombre de datasets disponibles dans
requests.get('http://www.data.gov/')
reponse=requests.get('http://www.data.gov/')

soup = BeautifulSoup(reponse.text, "lxml")


print(soup.find_all('small')[0].get_text())

with io.open("dataset7.txt", "w", encoding="utf-8") as f:
    f.write(str(soup))

#exercice3
#Ecrire un programme python qui extrait le tag h1 à partir de https://www.linkedin.com/
requests.get('https://www.linkedin.com/feed/')
response=requests.get('https://www.linkedin.com/feed/')
response.content
#print(response.content)
Soup = BeautifulSoup(response.text, "lxml")
print(Soup.h1.get_text())

#exercice4
#Ecrire un programme python qui extrait et affiche tous les tags de type headers à partir de
#en.wikipedia.org/wiki/Main_Page
requests.get('https://en.wikipedia.org/wiki/Main_Page')
reponse1=requests.get('https://en.wikipedia.org/wiki/Main_Page')
print(reponse1)
soup1 = BeautifulSoup(reponse1.text, "lxml")
print(soup1.h1)

for sub_heading in soup1.find_all('h2'):
    print(sub_heading.text)

#excercice5
#Ecrire un programme python qui extrait et affiche tous les liens vers les images de la page wikipedia
#de la reine Elisabeth II.
requests.get('https://fr.wikipedia.org/wiki/Élisabeth_II')
reponse2=requests.get('https://fr.wikipedia.org/wiki/Élisabeth_II')
print(reponse2)    
soup2 = BeautifulSoup(reponse2.text, "lxml")
#print(soup2)
print(soup2.find_all('img'))

for im in soup2.find_all('img'):
    print(im['src'])


#exercice6
#Ecrire un programme python qui affiche le nombre de followers d’un compte twitter.
requests.get('https://twitter.com/u_lookme')
reponse3=requests.get('https://twitter.com/u_lookme')
print(reponse3)    
soup3 = BeautifulSoup(reponse3.text, "lxml")   
#print(soup3)
#print(soup3.a)
a = soup3.find('a', {'href':'/U_lookme/followers'})['title']
print(a)

#exercice7
#Ecrire un programme python qui affiche la météo (température, vitesse du vent, description, etc.)
#d’une ville donnée a partir de l'API.

response4 = requests.get('https://api.openweathermap.org/data/2.5/weather?q=nancy&appid=101c67a83745b21206b5be926c5c3419')
temps=response4.json()
ville=temps['name']
temperature=temps['main']['temp']
vent=temps['wind']['speed']
print(f'la meteo de  {ville} a une température de {temperature} et le vent souffle a une vitesse de {vent} km par heure')

