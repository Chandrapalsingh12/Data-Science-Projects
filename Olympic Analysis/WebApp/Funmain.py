import re
import numpy as np




# def medal_tail(df,year="overall",country="overall"):
#         medal_df = df.drop_duplicates(subset=["Team","NOC","Games","Year","City","Sport","Event","Medal"])
#         flag = 0
        
#         if year== "overall" and country=="overall":
#             temp_df = medal_df
        
#         if year=="overall" and country !="overall":
#             flag = 1
#             temp_df = medal_df[medal_df.region==country]
            
#         if year!="overall" and country=="overall":
#             temp_df = medal_df[medal_df.Year==int(year)]
                
        
#         if year!="overall" and country!="overall":
#             temp_df = medal_df[(medal_df.Year==int(year)) & (medal_df.region==country) ]
            
#         if(flag==1):  
#             x = temp_df.groupby('Year').sum()[["Gold","Silver","Bronze"]].sort_values('Year').reset_index()
#         else:
#             x = temp_df.groupby('region').sum()[["Gold","Silver","Bronze"]].sort_values('Gold',ascending=False).reset_index()
        
#         x["total"] = x["Gold"] + x["Silver"] + x["Bronze"]

#         return x

class MainClass:
    def __init__(self,df):
        self.df = df

    def medalmain(self):
        
        medal_ta = self.df.drop_duplicates(subset=["Team","NOC","Games","Year","City","Sport","Event","Medal"])
        medal_ta = medal_ta.groupby('region').sum()[["Gold","Silver","Bronze"]].sort_values('Gold',ascending=False).reset_index()

        year = self.df.Year.unique().tolist()
        year.sort()
        year.insert(0,"overall")

        country = np.unique(self.df.region.dropna().values).tolist()
        country.sort()
        country.insert(0,"overall")

        return medal_ta,year,country


    def medal_tail(self,year,country):
        medal_df = self.df.drop_duplicates(subset=["Team","NOC","Games","Year","City","Sport","Event","Medal"])
        flag = 0
        
        if year== "overall" and country=="overall":
            temp_df = medal_df
        
        if year=="overall" and country !="overall":
            flag = 1
            temp_df = medal_df[medal_df.region==country]
            
        if year!="overall" and country=="overall":
            temp_df = medal_df[medal_df.Year==int(year)]
                
        
        if year!="overall" and country!="overall":
            temp_df = medal_df[(medal_df.Year==int(year)) & (medal_df.region==country) ]
            
        if(flag==1):  
            x = temp_df.groupby('Year').sum()[["Gold","Silver","Bronze"]].sort_values('Year').reset_index()
        else:
            x = temp_df.groupby('region').sum()[["Gold","Silver","Bronze"]].sort_values('Gold',ascending=False).reset_index()
        
        x["total"] = x["Gold"] + x["Silver"] + x["Bronze"]

        return x

    def overall(self):
        Edition = self.df.Year.unique().shape[0]-1
        city = self.df.City.unique().shape[0]
        sport = self.df.Sport.unique().shape[0]
        events = self.df.Event.unique().shape[0]
        athletes = self.df.Name.unique().shape[0]
        nation = self.df.region.unique().shape[0]

        return Edition,city,sport,events,athletes,nation
    
    def shoGraph(self):
        # Participating Nation Over the Years
        nation_time = self.df.drop_duplicates(["Year","region"])["Year"].value_counts().reset_index().sort_values("index")
        nation_time.rename(columns={"index":"Year","Year":"No of Country"},inplace=True)

        # Event Over Years
        No_of_Event = self.df.drop_duplicates(["Year","Event"])["Year"].value_counts().reset_index().sort_values("index")
        No_of_Event.rename(columns={"index":"Year","Year":"Evetns"},inplace=True)

        # Athletes Over the Years
        No_of_Athlete = self.df.drop_duplicates(["Year","Name"])["Year"].value_counts().reset_index().sort_values("index")
        No_of_Athlete.rename(columns={"index":"Year","Year":"Athlete"},inplace=True)



        X = nation_time.Year.values
        Y = nation_time["No of Country"].values
        E_X = No_of_Event.Year.values
        E_Y = No_of_Event.Evetns.values
        N_X = No_of_Athlete.Year.values
        N_Y = No_of_Athlete.Athlete.values


        return X,Y,E_X,E_Y,N_X,N_Y

    def most_sec(self,sport):
        tem_df = self.df.dropna(subset=["Medal"])
        
        if sport!="overall":
            tem_df = tem_df[tem_df.Sport==sport]
            
        x =  tem_df.Name.value_counts().reset_index().head(15).merge(self.df,left_on="index",right_on="Name",how="left")[["index","Name_x","Sport","region"]].drop_duplicates()
        x.rename(columns={"index":"Name","Name_x":"Medals"},inplace=True)

        sport = self.df.Sport.unique().tolist()
        sport.sort()
        sport.insert(0,"overall")
        return x,sport

    def get_country_name(self):
        country = np.unique(self.df.region.dropna().values).tolist()
        country.sort()
        country.insert(0,"overall")
        return country



    def Medal_Taily_Country(self,c_name):
        new_df = self.df.dropna(subset=["Medal"])
        new_df.drop_duplicates(subset=["Team","NOC","Games","Year","City","Sport","Event","Medal"],inplace=True)
        temp_df = new_df[new_df.region==c_name]
        final_df = temp_df.groupby("Year").count()["Medal"].reset_index()
        country_Year = final_df.Year.values
        country_Medal = final_df.Medal.values

        
        return country_Year,country_Medal



    def country_most(self,country):
        tem_df = self.df.dropna(subset=["Medal"])
        tem_df = tem_df[tem_df.region==country]
            
        x =  tem_df.Name.value_counts().reset_index().head(10).merge(self.df,left_on="index",right_on="Name",how="left")[["index","Name_x","Sport"]].drop_duplicates()
        x.rename(columns={"index":"Name","Name_x":"Medals"},inplace=True)
        return x
    
    def Athlete(self):
        ath_df = self.df.drop_duplicates(subset=["Name","region"])
        x1 = ath_df.Age.dropna().astype("int").values
        x2 = ath_df[ath_df.Medal == "Gold"]["Age"].dropna().astype("int").values
        x3 = ath_df[ath_df.Medal == "Silver"]["Age"].dropna().astype("int").values
        x4 = ath_df[ath_df.Medal == "Bronze"]["Age"].dropna().astype("int").values

        return x1,x2,x3,x4

    def male_female(self):
        man = self.df[self.df.Sex=="M"].groupby("Year").count()["Name"].reset_index()
        women =self.df[self.df.Sex=="F"].groupby("Year").count()["Name"].reset_index()
        final = man.merge(women,on='Year',how="left")
        final.rename(columns={'Name_X':"Male","Name_Y":"Female"},inplace=True)
        final.fillna(0,inplace=True)
        Y = final.Year.values
        X1 = final.Name_x.values
        X2 = final.Name_y.values

        return Y,X1,X2