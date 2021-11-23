from urllib import request
import json

r = request.urlopen("https://api.nasa.gov/planetary/apod?api_key=Bh5EFULUqcQmnVqskzAFlyrq3d4Ubw6vcIzsIq30")

d = json.loads(r.read())
print(d)

print(d["url"])
