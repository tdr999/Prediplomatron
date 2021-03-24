LICENSE_NOTICE = '
    Prediplomatron is a horrible program for automatic diploma generation
    Copyright (C) 2021  Predună Tudor-Gabriel

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'



import csv
import os
from pytesseract import pytesseract
from PIL import Image, ImageDraw, ImageFont
fontudor = ImageFont.truetype("liberation/LiberationMono-Bold.ttf", 100, encoding="unic")


image  = Image.open('eval.jpg').convert('RGB')
BACKUP_IMAGE = image
w, h = image.size

#retardeala cu pytesseract de a afla locatia lui W
boxes = pytesseract.image_to_boxes(image)
print(boxes)
casete = boxes.split('\n')
j = 0
z = 0
iteratudor = 0

#cauta locurile unde trebe sa scriem
for i in casete:
	vectudor = i.split(' ')
	if vectudor[0] == 'Q':
		j = iteratudor
	if vectudor[0] == 'K':
		z = iteratudor
	iteratudor = iteratudor + 1


print(casete[j])
print(casete[z])
#codul initial schimba doar numele, nu si nume de echipa, de aia arata ciudat
#patratul definit prin coltul stanga jos si dreapta sus
stangax = int(casete[j].split()[1]) #locatia din string
stangay = h - int(casete[j].split()[2])
dreaptax = int(casete[j].split()[3])
dreaptay = h - int(casete[j].split()[4]) #niste matematica de fotografii. Colt stanga sus e 00
#casete[j] este acum locul unde e W

stangaxx = int(casete[z].split()[1]) #locatia din string
stangayy = h - int(casete[z].split()[2])
dreaptaxx = int(casete[z].split()[3])
dreaptayy = h - int(casete[z].split()[4])
#casete[z] e locul unde e d





#acum vom sterge W si vom calcula in functie de numele persoanei cum sa centram
draw_obj = ImageDraw.Draw(image) #creeam obiectul draw, care mi se pare absolut cretin din punct de vedere stilistic al librariei
#ideea e ca vom vrea ca mijlocul numelui persoanei sa fie unde era w
draw_obj.rectangle( [(stangax, stangay), (dreaptax, dreaptay)], outline='white',fill='white', width=10 )#stergem Q-ul
#ideea e ca vom vrea ca mijlocul numelui persoanei sa fie unde era d
draw_obj.rectangle( [(stangaxx, stangayy), (dreaptaxx, dreaptayy)], outline='white',fill='white', width=10 )#stergem d-ul
#DE IMPLEMENTAT ESANTIONAREA CULORII DIPLOMEI LANGA LOCUL MARCAT

imagine_curata = image #un backup curat

def fa_diplome(im, Nume, Echipa):
	drw = ImageDraw.Draw(im)
	W, H = drw.textsize(Nume, font=fontudor)
	drw.text(((w-W)/2, stangay-100), Nume, font=fontudor,fill='black')#nu mai stiu de ce merge dar are sens
	W, H = drw.textsize(Echipa, font=fontudor)
	drw.text(((w-W)/2, stangayy-100), Echipa, font=fontudor,fill='black')#nu mai stiu de ce merge dar are sens

	im.save(Nume +'.pdf')
	im = im.resize((600, 600))
	im.show()



deskidem = open('date.csv')
reader = csv.reader(deskidem, delimiter = ',')


os.mkdir('Diplome')
os.chdir('Diplome')

for roww in reader:
	print(roww[0], roww[1], roww[2])
	print('AM AJUNS')
	echipa = roww[3]
	club = roww[4]
	print(echipa)
	print(club)
	try:
		os.mkdir(club)
	except:
		pass
	os.chdir(club)
	try:
		os.mkdir(echipa)
	except:
		pass
	os.chdir(echipa)
	
	fa_diplome(imagine_curata.copy(), roww[0], echipa)
	fa_diplome(imagine_curata.copy(), roww[1], echipa)
	fa_diplome(imagine_curata.copy(), roww[2], echipa)
	
	os.chdir('..')
	os.chdir('..')
	



