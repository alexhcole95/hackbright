import os
import requests
import bs4

res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
status = res.status_code == requests.codes.ok
print(status)

# print(len(res.text))
# print(res.text[:250])
# res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
# try:
#     res.raise_for_status()
# except Exception as exc:
#     print(f"There was a problem: {exc}")

playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()

# res = requests.get("https://nostarch.com")
# res.raise_for_status()
# no_starch_soup = bs4.BeautifulSoup(res.text, "html.parser")
# print(type(no_starch_soup))

example_file = open("example.html")
example_soup = bs4.BeautifulSoup(example_file, "html.parser")
elems = example_soup.select("#author")
print(type(elems))      # elems is a list of Tag objects.
print(len(elems))
print(type(elems[0]))
print(str(elems[0]))    # The Tag object as a string.
print(elems[0].getText())
print(elems[0].attrs)

span_elem = example_soup.select("span")[0]
print(str(span_elem))
print(span_elem.get("id"))
print(span_elem.get("some_nonexistent_addr") == None)
print(span_elem.attrs)

"""downloadXKCD.py

Download every single XKCD comic.
"""

url = "https://xkcd.com"  # starting url
os.makedirs("xkcd", exist_ok=True)  # store comics in ./xkcd
while not url.endswith("#"):

    # Download the page
    print(f"Download page {url}...")
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # Find the URL of the comic image
    comic_elem = soup.select("#comic img")
    if not comic_elem:
        print("Could not find comic image.")
    else:
        comic_url = f"https:{comic_elem[0].get('src')}"

        # Download the image
        print(f"Downloading image {comic_url}...")
        res = requests.get(comic_url)
        res.raise_for_status()

        # Save the image to ./xkcd
        image_file = open(os.path.join("xkcd", os.path.basename(comic_url)), "wb")
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()

    # Get the Prev button's url
    prev_link = soup.select('a[rel="prev"]')[0]
    url = f"https://xkcd.com{prev_link.get('href')}"

print("Done.")
