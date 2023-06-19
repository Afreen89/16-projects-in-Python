import bs4
import requests

result = requests.get("https://www.videoschool.com/")

soup = bs4.BeautifulSoup(result.text, "html.parser")

#my_p = soup.select("p")[6].getText()
# central_block = soup.select(".fusion-text.fusion-text-1 h5")
#
# for h in central_block:
#     print(h.getText())

images = soup.select('.img-responsive')[0]["src"]

image1 = requests.get(images)

f = open("my_image.jpg", "wb")
f.write(image1.content)
f.close()


 