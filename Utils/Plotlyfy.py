# Import libs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
import seaborn as sb # sns
import plotly.express as px
#import ast
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")

class Plotlyfy():
    def __init__(self, df):
        pass 
    
    def average_ratings(self, data):
        sb.lineplot(data=data ,x='nationality_1',y='value',hue='variable'); 
        plt.xticks(rotation=20); 
        plt.xlabel(''); 
        plt.ylabel('average ratings'); 

    def distribution(self, df_s):
        #plot the distribution of the variable depicting the gap between critics' and audience's ratings.   
        bin_edge=np.arange(-3,3,0.1); 
        plt.hist(data=df_s,x='diff',bins=bin_edge, color='C0'); #, histtype = 'step'         

    def ratings_distributions(self, df):
        sb.set(style="white", palette="deep")

        fig, axes = plt.subplots(1, 3, figsize = (16,4))
        ax1, ax2, ax3 = fig.axes

        ax1.set_xlim([0.5,5.5])
        ax2.set_xlim([0.5,5.5])
        ax3.set_xlim([0.5,5.5])


        ax1.hist(df["press_rating"], bins = 10, range = (0,5), color='C0') # bin range = 1
        ax1.set_title('Press Ratings Distribution')
        ax1.set_xlabel('Ratings')

        ax2.hist(df["spec_rating"], bins = 10, range = (0,5), color='C1') # bin range = 1
        ax2.set_title('Users Ratings Distribution')
        ax2.set_xlabel('Ratings')

        ax3.hist(df["press_rating"], bins = 10, range = (0,5), histtype = 'step', 
                 lw=1.5, label='Press Ratings', color='C0')
        ax3.hist(df["spec_rating"], bins = 10, range = (0,5), histtype = 'step', 
                 lw=1.5, label='Users Ratings', color='C1')
        ax3.legend(loc = 'upper left')
        ax3.set_title('Comparison of Distributions')
        ax3.set_xlabel('Ratings')

        for ax in fig.axes:
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)        


    def correlation_ratings(self, allocine):
        ax = sb.jointplot(x="press_rating", y="spec_rating", 
                        data=allocine, kind="hex",
                        marginal_kws=dict(bins=20),
                        xlim=(0.8,5.1), ylim=(0.8,5.1),
                        size=7, space=0).set_axis_labels("Press Ratings", "Users Ratings")        

    def compare_to_users_ratings(self, allocine):
        five_stars = allocine[allocine["press_rating"] >= 5]

        f, ax = plt.subplots(figsize=(15,6))
        f.suptitle('Movies with Five Stars From The Press', 
                fontsize=13)
        f.subplots_adjust(top=0.85)

        sb.countplot(five_stars["spec_rating"], ax=ax)
        ax.set_xlabel("Users Ratings")
        ax.set_ylabel("")
        sb.despine(top=True, right=True, left=False, bottom=False)        
    
    def first_insight(self, data:list):
        base_color=sb.color_palette()[0]

        plt.figure(figsize=[10,5])
        sb.boxplot(data=data[1],y='genre_1',x='diff_x',order=data[2].index,color=base_color)
        plt.xticks(rotation=90)
        plt.title('gap between average ratings between critics and audiance per genre')
        plt.xlabel('gap: average rating per critics minus audience rating')
        plt.ylabel('')        


    def second_insight(self, df_s):        
        base_color=sb.color_palette()[0]
        l=df_s.groupby(['directors'],as_index=False).count().sort_values(by="diff").tail(50)['directors'].tolist()
        df_3 = df_s[df_s.directors.isin(l)].groupby(['directors'],as_index=False).mean().sort_values(by='diff')

        plt.figure(figsize=[20,6])
        sb.boxplot(data=df_3,x='directors',y='diff',color=base_color) 
        plt.xticks(rotation=90)
        plt.title('40 out of 50 top directors have average higher critics ratings than audiences')
        plt.xlabel('')
        plt.ylabel('gap: average rating per critics minus audience rating'); 
        x_coordinates = [1, 50] 
        y_coordinates = [0, 0] 
        plt.plot(x_coordinates, y_coordinates)


    def five_star_movie(self, allocine):
        five_stars = allocine[allocine["press_rating"] >= 5]
        fig, axes = plt.subplots(1, 3, figsize = (16,4))
        fig.suptitle('Movies with Five Stars From The Press', fontsize=14, fontweight='bold')
        fig.subplots_adjust(top=0.75)
        ax1, ax2, ax3 = fig.axes

        # fig 1
        ax1.set_xlim([1925,2017])
        ax1.set_title("Distribution of Movies\nby Year of Release\n")
        # years distribution of the five stars
        sb.distplot(five_stars["release_date"].dt.year.dropna(), ax=ax1, 
                    axlabel="Year of Release", label="Five Stars Movies", bins=10, 
                    norm_hist=True, kde=False,
                    hist_kws={"alpha": 0.9, "color": "C5"})

        # years distribution of all the data
        sb.distplot(allocine["release_date"].dt.year.dropna(), ax=ax1, 
                    axlabel="Year of Release", label="Full Dataset", bins=10, 
                    norm_hist=True, kde=False,
                    hist_kws={"alpha": 0.85, "color": "C1"})

        ax1.axvline(x=1997, color="C0", label="Launch of AlloCiné", linestyle="--", linewidth=1.5)
        ax1.legend(loc = "upper left")

        # fig 2
        sb.countplot(five_stars["nb_press"], ax=ax2)
        ax2.set_xlabel("Number of Press Votes")
        ax2.set_title("Distribution of Movies\nby the Number of Press Votes\n")
        sb.despine(top=True, right=True, left=False, bottom=False)
        
        # fig 3
        # years distribution of all the data
        ax3.set_xlim([1935,2017])
        ax3.set_title("Distribution of Movies\nwith only one Press Vote\nby Year of Release")
        # years distribution of the view
        fs_nbp = five_stars[five_stars["nb_press"] == 1]
        left97 = len(fs_nbp[fs_nbp["release_date"].dt.year < 1997])
        right97 = len(fs_nbp[fs_nbp["release_date"].dt.year >= 1997])
        sb.distplot(fs_nbp["release_date"].dt.year.dropna(), ax=ax3, 
                    axlabel="Year of Release", label="Five Stars Movies", bins=4, 
                    norm_hist=False, kde=False,
                    hist_kws={"alpha": 0.9, "color": "C5"})

        ax3.text(1967, 10, '{}%'.format(round((left97 / (left97 + right97)) * 100, 1)), ha='center', va='bottom', color='C0')
        ax3.text(2007, 10, '{}%'.format(round((right97 / (left97 + right97)) * 100, 1)), ha='center', va='bottom', color='C0')
        ax3.axvline(x=1997, color="C0", label="Launch of AlloCiné", linestyle="--", linewidth=1.5)
        ax3.legend(loc = "upper left"); 


        
    def ploting_the_distribution(self, allocine):
        allocine["diff_rating"] = (allocine["press_rating"] - allocine["spec_rating"]).abs()
        f, ax = plt.subplots(1, 3, figsize = (16,4))
        f.suptitle('Distribution of Difference Between Ratings', 
                fontsize=14, fontweight='bold')
        f.subplots_adjust(top=0.75)
        ax1, ax2, ax3 = f.axes

        ax1.set_xlim([0,3])
        ax1.set_title("Distribution for\nUsers Ratings < Press Ratings")
        sb.distplot(allocine.loc[allocine["spec_rating"] < allocine["press_rating"], "diff_rating"], ax=ax1, bins=7, 
                    norm_hist=True, kde=False,
                    hist_kws={"alpha": 0.85, "color": "C0"})

        ax1.set_xlabel("Absolute Difference")

        ax2.set_xlim([0,3])
        ax2.set_title("Distribution for\nUsers Ratings > Press Ratings")
        sb.distplot(allocine.loc[allocine["spec_rating"] > allocine["press_rating"], "diff_rating"], ax=ax2, bins=7, 
                    norm_hist=True, kde=False,
                    hist_kws={"alpha": 0.85, "color": "C2"})
        ax2.set_xlabel("Absolute Difference")

        ax3.set_xlim([0,3])
        ax3.set_title("Distribution of absolute difference for\nall the data")
        sb.distplot(allocine.loc[:, "diff_rating"], ax=ax3, bins=7, 
                    norm_hist=True, kde=False,
                    hist_kws={"alpha": 0.85, "color": "C1"})
        ax3.set_xlabel("Absolute Difference")

        sb.despine(top=True, right=True, left=False, bottom=False)
