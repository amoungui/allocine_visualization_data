# Import libs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
import seaborn as sb
warnings.filterwarnings("ignore")
import ast
import matplotlib.pyplot as plt

class Cleaner():
    def __init__(self, frame):
        self.df = self.load_data(frame)

    def load_data(self, frame):
        """load dataset that we pass as parameter
        Args:
            dataset (dataset)
        Returns:
            df (dataframe)
        """        
        df = pd.read_csv(frame)
        return df 
        
    def clean(self):
        """clean dataset to move the list to string in all the specific column
        Args:
            None
        Returns:
            df (dataframe)
        """        
        #Select only movies with ratings from both critics and audience
        df_s= self.df[self.df.press_rating.notnull() & self.df.spec_rating.notnull()]  
               
        df_s['genres']=df_s['genres'].apply(lambda x : x.replace('[','')) 
        df_s['genres']=df_s['genres'].apply(lambda x : x.replace(']',''))
        df_s['genres']=df_s['genres'].apply(lambda x : x.replace("'",''))

        df_s['directors']=df_s['directors'].apply(lambda x : x.replace('[','')) 
        df_s['directors']=df_s['directors'].apply(lambda x : x.replace(']',''))
        df_s['directors']=df_s['directors'].apply(lambda x : x.replace("'",''))

        df_s['actors']=df_s['actors'].apply(lambda x : x.replace('[','')) 
        df_s['actors']=df_s['actors'].apply(lambda x : x.replace(']',''))
        df_s['actors']=df_s['actors'].apply(lambda x : x.replace("'",''))

        df_s['nationality']=df_s['nationality'].apply(lambda x : x.replace('[','')) 
        df_s['nationality']=df_s['nationality'].apply(lambda x : x.replace(']',''))
        df_s['nationality']=df_s['nationality'].apply(lambda x : x.replace("'",''))  
        
        return df_s  

        
    def movie_rating_cleaner(self):
        """clean dataset to move the list to string in all the specific column and rename in english the genre 
        Args:
            None
        Returns:
            df (dataframe)
        """
        #Select only movies with ratings from both critics and audience
        df_s= self.df[self.df.press_rating.notnull() & self.df.spec_rating.notnull()] 
        df_s['press_rating'] = df_s['press_rating'].astype(str).str.strip().str.replace(',','.').str.replace('--','0').astype(float)
        df_s['spec_rating'] = df_s['spec_rating'].astype(str).str.strip().str.replace(',','.').str.replace('--','0').astype(float)
        #Define the gap between average critics' rating and audience rating
        df_s['diff']=df_s['press_rating']-df_s['spec_rating']         
        df_s['genres']=df_s['genres'].apply(lambda x : x.replace('[','')) 
        df_s['genres']=df_s['genres'].apply(lambda x : x.replace(']',''))
        df_s['genres']=df_s['genres'].apply(lambda x : x.replace("'",''))

        df_s['directors']=df_s['directors'].apply(lambda x : x.replace('[','')) 
        df_s['directors']=df_s['directors'].apply(lambda x : x.replace(']',''))
        df_s['directors']=df_s['directors'].apply(lambda x : x.replace("'",''))

        df_s['nationality']=df_s['nationality'].apply(lambda x : x.replace('[','')) 
        df_s['nationality']=df_s['nationality'].apply(lambda x : x.replace(']',''))
        df_s['nationality']=df_s['nationality'].apply(lambda x : x.replace("'",''))  
        
        #Rename in english the genre for the most populated categories
        df_s['genres']=df_s['genres'].apply(lambda x : x.replace('Drame','Drama'))
        df_s['genres']=df_s['genres'].apply(lambda x : x.replace('Comédie','Comedy'))
        df_s['genres']=df_s['genres'].apply(lambda x : x.replace('Comédie dramatique','comedy drama'))
        df_s['genres']=df_s['genres'].apply(lambda x : x.replace('Documentaire','Documentary'))
        df_s['genres']=df_s['genres'].apply(lambda x : x.replace('Policier','Crime movie'))
        df_s['genres']=df_s['genres'].apply(lambda x : x.replace('Epouvante-horreur','Horror movie'))
        df_s['genres']=df_s['genres'].apply(lambda x : x.replace('Fantastique','Fantasie movie'))
        df_s['genres']=df_s['genres'].apply(lambda x : x.replace('Aventure','Adventure movie'))
                
        df_s['genre_1']=df_s['genres'].apply(lambda x : x.split(',')[0])
        
        df_s['nationality_1']=df_s['nationality'].apply(lambda x : x.split(',')[0])
        
        return df_s
        
    def country_production(self):
        """ Rename in english the nationality for the most populated categories. 
            Create a new column variable that content the critics of press and audience of user.
        Args:
            None
        Returns:
            df (dataframe)
        """
        df_s = self.movie_rating_cleaner()
        #Work on the nationality 
        nat_group=df_s.groupby(['nationality_1'],as_index=False).count().sort_values(by="diff").tail(8)['nationality_1'].tolist()
        
        a=df_s[df_s.nationality_1.isin(nat_group)].groupby(['nationality_1'],as_index=False).mean()[['nationality_1','press_rating','spec_rating']]        
        # To make analysis of data in table easier, we can reshape the data into a more computer-friendly 
        b=pd.melt(a, id_vars=['nationality_1'], value_vars=['press_rating','spec_rating'])
        
        b['nationality_1']=b['nationality_1'].apply(lambda x : x.replace('allemand','German'))
        b['nationality_1']=b['nationality_1'].apply(lambda x : x.replace('américain','US'))
        b['nationality_1']=b['nationality_1'].apply(lambda x : x.replace('britannique','UK'))
        b['nationality_1']=b['nationality_1'].apply(lambda x : x.replace('canadien','Canadian'))
        b['nationality_1']=b['nationality_1'].apply(lambda x : x.replace('espagnol','Spanish'))
        b['nationality_1']=b['nationality_1'].apply(lambda x : x.replace('français','French'))
        b['nationality_1']=b['nationality_1'].apply(lambda x : x.replace('italien','Italian'))
        b['variable']=b['variable'].apply(lambda x : x.replace('press_rating','critics'))

        b['variable']=b['variable'].apply(lambda x : x.replace('spec_rating','audience'))
                
        return b 
        
    def insight_critics_cleaner(self, df_s):
        """ Rename in english the nationality for the most populated.
        Args:
            df (dataframe)
        Returns:
            arr (list)
        """        
        #Select only categories of genres with at least 100 movies
        select_cat=df_s.groupby(['genre_1'],as_index=False).count().query('diff>=100')['genre_1'].tolist()        
        # verify if value of genre_1 column is in select_category (select_cat)
        table=df_s[df_s.genre_1.isin(select_cat)]
        order_cat=table.groupby(['genre_1'],as_index=False).mean().sort_values(by=('diff')) # we sort value by diff column
        # we merge order_cat with table 
        table_2=table.merge(order_cat,left_on='genre_1',right_on='genre_1')

        grouped = table.loc[:,['genre_1', 'diff']] \
            .groupby(['genre_1']) \
            .median() \
            .sort_values(by='diff')        
        
        return [table, table_2, grouped]        
        
    def convert_data(self, df):
        """ convert type of columns (press_rating, spec_rating) to float
            convert type of columns (nb_press, nb_spec) to int 
        Args:
            df (dataframe)
        Returns:
            df (dataframe): return the new dataset 
        """        
        #Select only movies with ratings from both critics and audience
        df= self.df[self.df.press_rating.notnull() & self.df.spec_rating.notnull()] 
        df['press_rating'] = df['press_rating'].astype(str).str.strip().str.replace(',','.').str.replace('--','0').astype(float)
        df['spec_rating'] = df['spec_rating'].astype(str).str.strip().str.replace(',','.').str.replace('--','0').astype(float)        

        df["release_date"] = pd.to_datetime(df["release_date"])

        # drop NaN values
        df = df.dropna(subset=["press_rating", "spec_rating"]).reset_index(drop=True)
        # convert float to int 
        df['nb_press'] = df['nb_press'].astype(str).str.strip().str.replace(',','.').str.replace('--','0').astype(float)
        df['nb_spec'] = df['nb_spec'].astype(str).str.strip().str.replace(',','.').str.replace('--','0').astype(float)

        return df
