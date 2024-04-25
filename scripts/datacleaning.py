#data cleaning script

#import librairies
import gdown
import pandas as pd

#download dasaset
url = 'https://drive.google.com/uc?id=11OjUiB8FBZSYyGAD_b6nTFtI5zln5XCH'
output = 'insta_v0.csv'
gdown.download(url, output,quiet=False)

df = pd.read_csv(output)

#rename the columns
df= df.rename(columns={'0':"date"})
df= df.rename(columns={'1':"nombre de like"})
df= df.rename(columns={'2':"description"})
df_true= df.rename(columns={'3':"url"})

#split "date" and "heure" 
df_true[["date","heure"]]=df.date.str.split(pat="T",expand=True)



