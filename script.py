import os
import datetime
from PIL import Image
import pyexiv2
import requests

try:
    import json
except ImportError:
    import simplejson as json

from data import *  

# image link retrieval
link = requests.get(BING_LINK)


img_data = json.loads(link.text)

'''
{
	"images": [{
		"startdate": "20190823",
		"fullstartdate": "201908230700",
		"enddate": "20190824",
		"url": "/th?id=OHR.FarmlandLandscape_EN-US6661316442_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp",
		"urlbase": "/th?id=OHR.FarmlandLandscape_EN-US6661316442",
		"copyright": "Farmland in Washington state's Palouse region (© Art Wolfe/Getty Images)",
		"copyrightlink": "https://www.bing.com/search?q=palouse+region&form=hpcapt&filters=HpDate%3a%2220190823_0700%22",
		"title": "Harvest time in the Palouse",
		"quiz": "/search?q=Bing+homepage+quiz&filters=WQOskey:%22HPQuiz_20190823_FarmlandLandscape%22&FORM=HPQUIZ",
		"wp": true,
		"hsh": "44238c657b35ce3c11fbf3f59881474e",
		"drk": 1,
		"top": 1,
		"bot": 1,
		"hs": []
	}],
	"tooltips": {
		"loading": "Loading...",
		"previous": "Previous image",
		"next": "Next image",
		"walle": "This image is not available to download as wallpaper.",
		"walls": "Download this image. Use of this image is restricted to wallpaper only."
	}
}


Get the image URL from the response
'''


#get image url + image name + image date + image copyright and add as metadata
tmp = (img_data['images'][0]['url']).split('&')[0]

img_url = "https://bing.com" + tmp #required link is only till .jpg suffix

img_name = img_data['images'][0]['title'] + "." + tmp.split('.')[-1]

img_meta1 = img_data['images'][0]['copyright']

tmp = img_data['images'][0]['startdate']

img_meta2 = datetime.datetime(int(tmp[:4]), int(tmp[4:6]), int(tmp[6:]))

img_data = requests.get(img_url).content

##img = Image.fromarray(img_data)
##
##img.modify_exif({'Exif.Image.ImageDescription': img_meta1})
##img.write_exif()

with open(img_name,'wb') as control:
    control.write(img_data)
