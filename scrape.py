import os
from lxml import objectify
import pandas as pd
import pickle
path = './episodes'

df = pd.DataFrame(columns=('genres', 'synopsis'))

i = 0
for filename in os.listdir(path):
    path_filename = path + '/' + filename
    i = i + 1
    print (str(i) + " " + path_filename)

    xml = objectify.parse(open(path_filename))
    root = xml.getroot()

    pid = root.pid.text

    if hasattr(root, "synopses"):
        synopsis = root.synopses.short.text
    else:
        synopsis = ""

    if hasattr(root, "genre_groupings"):
        genres = root.genre_groupings.genre_group.genres.genre
    else:
        genres = ""

    for g in genres:
        row = dict(zip(['genres', 'synopsis'], [g.get("id"), synopsis]))
        print row
        row_s = pd.Series(row)
        row_s.name = filename
        df = df.append(row_s)



with open("df.pickle",'wb') as f:
    pickle.dump(df, f)