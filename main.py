import os, csv
with open("100MostStreamedSongs.csv") as file:
  reader = csv.DictReader(file)
  for row in reader:
    dir = os.listdir()
    #print(os.listdir())
    artist = row["Artist(s)"].title()
    print(artist)
    if artist not in dir:
      os.mkdir(artist)
    song = row["Song"]
    print(song)
    path = os.path.join(f"{artist}/", song)
    f = open(path, "w")
    f.close()
    


