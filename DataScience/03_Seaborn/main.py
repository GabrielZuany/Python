import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df_videos = pd.DataFrame()
df_videos = pd.read_excel("videosYT.xlsx", sheet_name="videos")

#fig = sns.scatterplot(data=df_videos, x="Nº de Views", y="Nº de Likes", hue="Responsável", style= "Responsável")

#rel = sns.relplot(data=df_videos, x="Nº de Views", y="Nº de Likes", hue="Categoria", col="Responsável")

hist = sns.displot(data=df_videos, x="Nº de Views")

plt.show()