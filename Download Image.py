import random
import urllib.request

def download_image(url):
    name = str(random.randrange(1, 100)) + ".jpg"
    urllib.request.urlretrieve(url, name)

download_image("https://www.thenewboston.com/photos/users/2/resized/23471ba4417d650505928a0b1f1fd8b1.jpg")
