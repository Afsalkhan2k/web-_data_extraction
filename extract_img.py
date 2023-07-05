import urllib.request
from bs4 import BeautifulSoup
from os.path  import basename
import os
import re
import requests
import cv2
import pytesseract


BASE_DIR="C:\\xampp\\htdocs\\web_data_extraction\\images"
DIR = os.listdir(BASE_DIR)

"""
for i in DIR:
	os.remove(BASE_DIR+'\\'+i)


file=open("url.txt","r",encoding='utf-8')
url=file.read()
file.close()

try:
	html = urllib.request.urlopen(url)
except:
	print("url not supported for web scrapping")
	exit()

htmlParse = BeautifulSoup(html, 'html.parser')

images = []
for img in htmlParse.findAll('img'):
    images.append(img.get('src'))
	

for i in images:
	print(i)
	try:
		with open("images\\"+basename(re.sub("\n","",str(i))), "wb") as f:
			f.write(requests.get(i).content)
	except:
		pass

print(images)"""

###
"""
extracted_text_data=[]	


for i in DIR:
	#pytesseract.pytesseract.tesseract_cmd=r'C:Program FilesTesseract-OCRtesseract.exe'
	try:
		img_path=BASE_DIR+'\\'+i
		#print(img_path)
		img = cv2.imread(BASE_DIR+'\\'+i)
		img = cv2.resize(img, (400, 450))
		#cv2.imshow("Image", img)
		#cv2.waitKey(0)
		text = pytesseract.image_to_string(img)
		extracted_text_data.append(text)
		#print(text)
		cv2.destroyAllWindows
	except:
		pass
print(extracted_text_data)"""

text=""
try:
		img_path=BASE_DIR+'\\'+"test.jpg"
		#print(img_path)
		img = cv2.imread(BASE_DIR+'\\'+"test.jpg")
		img = cv2.resize(img, (400, 450))
		#cv2.imshow("Image", img)
		#cv2.waitKey(0)
		text = pytesseract.image_to_string(img)
		#extracted_text_data.append(text)
		#print(text)
		cv2.destroyAllWindows
except:
		pass	
        
print(text)