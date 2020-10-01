#Copyright [2020] [Alastair Hayes]
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.

'''
Author: Alastair Hayes #
Source: [Github] (http://github.com
'''

#Imports
import streamlit as st               #[v 0.61.0]
import streamlit.components.v1 as components
import pandas as pd                  #[v 1.0.4]
pd.options.display.max_colwidth = 1000000
import numpy as np                   #[v 1.18.5]
import matplotlib.pyplot as plt      #[v 3.2.1]
import plotly.express as px          #[v 0.4.1]
import plotly.graph_objects as go    #[v 4.8.1]
import plotly.figure_factory as ff
import bokeh                         #[v ?]
from bokeh.plotting import ColumnDataSource, figure, output_file, show
import ipywidgets as widgets
from PIL import ImageTk, Image
px.set_mapbox_access_token(open("/Users/alastairhayes/desktop/Eponyms/ajhayes83_1.mapbox_token").read())

st.write(
        """
        <style type="text/css" media="screen">
        div[role="listbox"] ul {
            height:250px;
        }
        </style>
        """
        ,
        unsafe_allow_html=True,
    )

#----------------------------------------------------------------------------------------------#
#                                                                                              #
# Read in data                                                                                 #
#                                                                                              #
#----------------------------------------------------------------------------------------------#

#Data read and arrange
df1A2Z = pd.read_csv('/Users/alastairhayes/desktop/Eponyms/Eponyms4python_Lite_A2Z.csv',dtype={'PMID':str,'Year':str})
df2A2Z = df1A2Z.sort_values(by=['Year'],ascending=True)
df3A2Z = df2A2Z.drop(['Lat_A1', 'Long_A1','Year','ISO_country_A1','CityOfEponym_A1',
               'Author_2','Pubmed_results','Type',
               'Societies','ICD11','PMID','Google_results','Class'], axis=1)
df3A2Z.rename(columns={'Author_1': 'Main Person'}, inplace=True)
df4A2Z = df3A2Z.drop_duplicates(subset='Eponym', keep="first")
df_A2Z = df4A2Z.sort_values(by=['Eponym'], ascending=True)

df1 = pd.read_csv('/Users/alastairhayes/desktop/Eponyms/Eponyms4python_Lite.csv',dtype={'PMID':str,'Year':str})
df2 = df1.sort_values(by=['Year'],ascending=True)
df3 = df2.drop(['Lat_A1', 'Long_A1','Year','ISO_country_A1','CityOfEponym_A1',
               'Author_2','Pubmed_results','Type',
               'Societies','ICD11','PMID','Google_results','Class'], axis=1)
df3.rename(columns={'Author_1': 'Main Person'}, inplace=True)
df4 = df3.drop_duplicates(subset='Eponym', keep="first")

df5 = df2.drop(['Alphabet','Lat_A1', 'Long_A1','ISO_country_A1','CityOfEponym_A1',
               'CountryOfEponym_A1','Author_2','Pubmed_results','Type',
               'Societies','ICD11','PMID','Google_results','Class'], axis=1)

df5.rename(columns={'Author_1': 'Main Person'}, inplace=True)
df6 = df5.drop_duplicates(subset='Eponym', keep="first")
df_Yr = df6[['Year','Eponym','Main Person','Subclass']]

df_countries = pd.read_csv('/Users/alastairhayes/desktop/Eponyms/Countries.csv') #Import all countries as count = 0
df_country = df2.groupby(['CountryOfEponym_A1','ISO_country_A1']).size().reset_index(name='counts')
df_countries.set_index('CountryOfEponym_A1').head(1)
df_country.set_index('CountryOfEponym_A1').head(1)
df_country_comb = pd.concat([df_countries, df_country], ignore_index=False)
df_country_comb_fini = df_country_comb.groupby(['CountryOfEponym_A1', 'ISO_country_A1']).sum()
df_C = df_country_comb_fini.reset_index()

# New dataframe for timeslider data
df1_TS = pd.read_csv('/Users/alastairhayes/desktop/Eponyms/Eponyms4python_Lite_Timeline10.csv')
df2_TS = df1_TS.sort_values(by=['Year'],ascending=True)


#----------------------------------------------------------------------------------------------#
#                                                                                              #
#  Main                                                                                        #
# ::: Handles the navigation / routing and data loading / caching                              #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#

def main():
    df = load_data()
#    st.sidebar.markdown('''**Advertisement**''')
#    st.sidebar.markdown('''[Advert space for Google AdSense]''')
#    st.sidebar.markdown("---")
    st.sidebar.title('Navigator')
    page = st.sidebar.radio("""Go to""",
                            ["Homepage",
                             "Surgical Eponym Explorer ©",
                             "App Team"])

    if page   == "Homepage":                   show_homepage()
    elif page == "Surgical Eponym Explorer ©": show_explore()
    elif page == "App Team":                   show_the_app_team()


st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
        max-width: {1160}px;
        padding-top: {2}rem;
        padding-right: {3}rem;
        padding-left: {1}rem;
        padding-bottom: {1}rem;
    }}
</style>
""",
        unsafe_allow_html=True,
    )


#----------------------------------------------------------------------------------------------#
#                                                                                              #
#  Homepage                                                                                    #
# ::: Handles                                                                                  #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#

def show_homepage():
    ''' Home / About page '''
    st.markdown('''# Learning Surgical Eponyms App''')
    st.subheader('Welcome')
    st.write('''There are a hundreds of eponyms used in daily surgical practice.
    We hope that you will find this app helpful in understanding what these terms mean, their history, and how they relate to one another using the **Eponym Explorer**.''')
    st.markdown('''We suggest starting with **Operations** of interest, or eponyms related to **Anatomy**.
    To explore their origins, check out the **Year** and **Geography** options. See **Journals** for eponyms that can be traced back to a famous publication.
    To gauge eponym usage see **Google hits**, and choose **Surgical instruments** to find eponymously named equipment.''')
    st.markdown('''We include **direct links to primary papers**, as well as useful webpages in **Wikipedia**, **Whonamedit?**, **ICD-11** and **TeachMeSurgery**. To simply search **A to Z** use the search box (below).''')
    st.markdown("---")
    st.subheader('Who is this App for?')
    st.write('''Doctors, nurses, secretaries, theatre staff, physician assistants, allied health professionals and students''')
    st.markdown("---")
    st.subheader('Disclaimer')
    st.write('''Educational purposes''')
    st.sidebar.markdown("---")
    st.sidebar.markdown('''**Latest News**''')
    st.sidebar.info("App will be launched Dec 2020")
    st.sidebar.markdown('''**About**''')
    st.sidebar.info("This App is maintained by Alastair Hayes, a Surgeon and Coder based in Edinburgh UK, supported by the App Team")
    st.sidebar.markdown('''**Contact details**''')
    st.sidebar.info("Please get in touch with any contributions or comments: surgicaleponyms@gmail.com")

#----------------------------------------------------------------------------------------------#
#                                                                                              #
#  About the team                                                                              #
# :::                                                                                          #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#

def show_the_app_team():
    st.title("Surgical App Development Team")
    st.markdown('''<br>We are group of General Surgeons based in Edinburgh developing app software to improve surgical **data systems**,
             **research** and **education**.''',unsafe_allow_html=True)

    st.sidebar.markdown("---")
    st.sidebar.markdown('''**Contact details**''')
    st.sidebar.info("Get in touch with any comments, queries or suggestions: surgicaleponyms@gmail.com")
    
    st.subheader("Project Lead & App Developer")
    about1 = st.checkbox("Alastair Hayes")
    if about1:
        st.markdown('''Alastair is a Specialty Training Registrar in Edinburgh with interests in Upper GI, Endocrine and Emergency General Surgery.
    His qualifications consist of BSc(Hons), MBChB, MRCS(Ed), MSc, PhD.
    He is working to develop data science and software solutions for clinical data systems, research and education in surgical practice.''')

    st.subheader("Associate Project Lead")
    about2 = st.checkbox('''Anne Ewing''')
    if about2:
        st.markdown('''Anne is a Specialty Training Registrar in Edinburgh with interests in Upper GI, Hernias and Emergency General Surgery.
    She is passionate about surgical teaching and outside work Anne is **_really_** :sports_medal: good at :woman-biking::woman-swimming::woman-running:''')

    st.markdown("---")
    st.subheader("Contributors")
    about3 = st.checkbox('''Show Contributors''')
    if about3:
        st.markdown('''Maria Drogouti, Surgical Registrar''')
        st.markdown('''Michael Ramage, Surgical Registrar''')
    
    st.subheader("Collaborators")
    about4 = st.checkbox('''Show Collaborators''')
    if about4:
        st.markdown('''[Chris Deans](https://www.ed.ac.uk/surgery/staff/profiles/chris-deans), Consultant Surgeon''')
        st.markdown('''[Dimitrios Damaskos](https://www.ed.ac.uk/surgery/staff/profiles/dimitrios-damaskos), Consultant Surgeon''')

    st.subheader("Acknowledgements")
    st.markdown('''[Google](https://www.google.com/search/howsearchworks/?fg=1),
    [Mapbox](https://www.mapbox.com),
    [Pandas](https://pandas.pydata.org), [Plotly](https://plotly.com/python/), [PubMed&reg;](http://www.ncbi.nlm.nih.gov/pubmed),
    [Streamlit](https://www.streamlit.io)''')
    #[TeachMeSurgery](https://teachmesurgery.com)
    st.sidebar.markdown("---")


#----------------------------------------------------------------------------------------------#
#                                                                                              #
#  Explorer                                                                                    #
# ::: Handles the navigation                                                                   #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#

def show_explore():
    st.sidebar.markdown("---")
    st.sidebar.title("**Explorer**")
    exp = st.sidebar.radio('Select',
                                ["About",
                                 "By Operation",
                                 "Type of Eponym",
                                 "Geographical",
                                 "Journal of Publication",
                                 "People",
                                 "Time Travel",
                                 "Exam Favourites",
                                 "A to Z",
                                 ])
    if   exp == "About":                    exp_about()             #1
    elif exp == "By Operation":             exp_operation()         #2
    elif exp == "Type of Eponym":           exp_type()              #3
    elif exp == "Geographical":             exp_geography()         #4         
    elif exp == "Journal of Publication":   exp_journals()          #5
    elif exp == "People":                   exp_people()            #6
    elif exp == "Time Travel":              exp_year()              #7
    elif exp == "Exam Favourites":          exp_exam()              #8
    elif exp == "A to Z":                   exp_A2Z()               #9


#----------------------------------------------------------------------------------------------#
#                                                                                              #
#  About (1)                                                                     #
# ::: Handles                                                                                  #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#

def exp_about():

    st.markdown(
        """
        <style type="text/css" media="screen">
        .hovertext text {
        font-size: 20px !important;}
        </style>
        """
        ,
        unsafe_allow_html=True,
    )

    #Sidebar
    st.sidebar.markdown("---")

    #Page

    st.markdown('''# About - Surgical Eponym Explorer''')
    st.markdown("""<br>Use the **Explorer** select options in the sidebar to explore eponyms related to surgery.""",
        unsafe_allow_html=True)
    st.markdown('''<br><span style="font-size:14pt;font-weight:bold;color:black;text-decoration:underline;">By Operation</span>''', unsafe_allow_html=True)
    st.write('''Here you can choose an operation type, and then access all the common eponyms related to that procedure.''')
    st.markdown('''<br><span style="font-size:14pt;font-weight:bold;color:black;text-decoration:underline;">Type of Eponym</span>''', unsafe_allow_html=True)
    st.write('''Choose from anatomical structures, clinical scores or signs, operations,
                pathology, patient positioning, research trials, incisions, instruments,
                surgical maneouvers & techniques.''')
    st.markdown('''<br><span style="font-size:14pt;font-weight:bold;color:black;text-decoration:underline;">Geographical</span>''', unsafe_allow_html=True)
    st.write('''Choose a region of the world to find eponyms. Select a country or famous city.''')
    st.markdown('''<br><span style="font-size:14pt;font-weight:bold;color:black;text-decoration:underline;">Journal of Publication</span>''', unsafe_allow_html=True)

    st.write('''In this section, journals can be selected to find which eponyms can be traced to their archives.''')
    st.markdown('''<br><span style="font-size:14pt;font-weight:bold;color:black;text-decoration:underline;">People</span>''', unsafe_allow_html=True)

    st.write('''Some famous people have been attributed to many eponyms.''')
    st.markdown('''<br><span style="font-size:14pt;font-weight:bold;color:black;text-decoration:underline;">Time Travel</span>''', unsafe_allow_html=True)

    st.write('''Explore through time using the time travel function.''')
    st.markdown('''<br><span style="font-size:14pt;font-weight:bold;color:black;text-decoration:underline;">Exam Favourites</span>''', unsafe_allow_html=True)
    st.write('''Select from those often found in exams. Explore by speciality.''')
    st.markdown('''<br><span style="font-size:14pt;font-weight:bold;color:black;text-decoration:underline;">A to Z</span>''', unsafe_allow_html=True)
    st.write('''Explore the eponym library alphabetically.''')
 


#----------------------------------------------------------------------------------------------#
#                                                                                              #
#  Surgical Operations (2)                                                                     #
# ::: Handles                                                                                  #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#

def exp_operation():
    st.markdown(
        """
        <style type="text/css" media="screen">
        .hovertext text {
        font-size: 20px !important;}
        </style>
        """
        ,
        unsafe_allow_html=True,)
    
    #Sidebar
    st.sidebar.markdown("---")

    #Page
    df1 = pd.read_csv('/Users/alastairhayes/desktop/Eponyms/Eponyms4python_Lite.csv',dtype={'PMID':str,'Year':int})
    df2 = df1.sort_values(by=['Year'],ascending=True)
    df3 = df2.sort_values(by=['Operation'],ascending=True)  #Gives eponyms by operation alphabetically
    df4 = df3['Operation'].dropna()
    string = df4.str.cat(sep=',')
    splits = string.split(",")
    S = set(splits)
    T = np.array(list(S)).astype(object)
    U = np.sort(T)

    st.markdown('''[Advert space for Google AdSense1]''')
    st.subheader('''First, choose operation(s) of interest:''')
    eponymByOp = st.multiselect('',options=list(U), format_func=lambda x: ' ' if x == '1' else x)
    new_df = df1.loc[df1['Operation'].str.contains('|'.join(eponymByOp)) == True]
    new_df2 = new_df.sort_values(by=['Eponym'],ascending=True)
 
    if not eponymByOp == None:
        st.subheader('''Then, search this list of relevant eponyms:''')
        Op_options = st.selectbox('',
                                  new_df2['Eponym_easy'].unique(), format_func=lambda x: ' ' if x == '1' else x)   #selectbox

        if Op_options == "Allis forceps":
            st.markdown("---")
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/Instruments/Allis_Tissue_Forceps.jpg'
            st.image(image, width=500)
        if Op_options == "Amyand hernia":
            st.markdown("---")
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Claudius_Amyand.png'
            st.image(image, width=180)
        if Op_options == "Allison repair":
            st.markdown("---")
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Philip_Rowland_Allison.png'
            st.image(image, width=180)
        if Op_options == "Altemeier procedure":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/William_A_Altemeier.png'
            st.image(image, width=180)
        if Op_options == "Alvarado score":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Alfredo_Alvarado.png'
            st.image(image, width=180)
        if Op_options == "Babcock forceps":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/Instruments/Babcock_Forceps.png'
            st.image(image, width=650) 
        if Op_options == "Barrett's oesophagus":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Norman_Rupert_Barrett.png'
            st.image(image, width=180)
        if Op_options == "Bassini hernia repair":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Edoardo_Bassini_Wellcome.jpg'
            st.image(image, width=200)
        if Op_options == "Battle's incision":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/William_Henry_Battle.png'
            st.image(image, width=180)
        if Op_options == "Beger procedure":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Hans_Gunther_Beger.png'
            st.image(image, width=180)
        if Op_options == "Belsey Mark IV operation":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Ronald_Belsey.png'
            st.image(image, width=180)
        if Op_options == "Berry's ligament":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/James_Berry.png'
            st.image(image, width=180)
        if Op_options == "Brooke ileostomy":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Bryan_Nicholas_Brooke.png'
            st.image(image, width=180)
        if Op_options == "Calot's triangle":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Calot2.png'
            st.image(image, width=600)
        if Op_options == "Charcot's triad":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Jean-Martin Charcot.png'
            st.image(image, width=180)
        if Op_options == "Crohn's disease":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Burrill_Bernard_Crohn.png'
            st.image(image, width=180)
        if Op_options == "Collis gastroplasty":  #universally known as Jack
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/John_Leigh_Collis.png'
            st.image(image, width=180)
        if Op_options == "Cushing's ulcer":  #universally known as Jack
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Harvey_Cushing.png'
            st.image(image, width=180)
        if Op_options == "Delorme's procedure":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Edmond_Delorme.png'
            st.image(image, width=180)
        if Op_options == "Fallopian tube":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Gabriele_Falloppio.png'
            st.image(image, width=180)
        if Op_options == "Fowler-Weir approach":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Fowler_Weir2.png'
            st.image(image, caption='George Ryerson Fowler &  Robert Fulton Weir', width=400)
        if Op_options == "De Garengeot's hernia":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Rene_De_Garengeot.png'
            st.image(image, width=180)
        if Op_options == "Graves disease":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Robert_J_Graves.png'
            st.image(image, width=180)
        if Op_options == "Hartmann's operation":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Henri_Hartmann_1920.jpg'
            st.image(image, width=180)
        if Op_options == "Hartmann's pouch":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/Anatomy/Hartmanns_Pouch.png'
            st.image(image, width=450)
        if Op_options == "Hasson technique":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Harrith_Hasson.png'
            st.image(image, width=180)
        if Op_options == "Heineke–Mikulicz pyloroplasty":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Heineke_Mikulicz.png'
            st.image(image, caption='Walter Hermann von Heineke  &  Jan Mikulicz-Radecki', width=400)
        if Op_options == "Spiral valves of Heister":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Lorenz_Heister.png'
            st.image(image, width=180)
        if Op_options == "Fanelli catheter":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Fanelli.png'
            st.image(image, width=500)
        if Op_options == "Hashimoto's thyroiditis":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Hakaru_Hashimoto.png'
            st.image(image, width=180)
        if Op_options == "Ivor Lewis oesophagectomy":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Ivor_Lewis.png'
            st.image(image, width=180)
        if Op_options == "Joll's retractor":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/Instruments/JollsRetractor.png'
            st.image(image, width=538)
        if Op_options == "Joll's triangle":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/Anatomy/JollsTriangle.png'
            st.image(image, width=460)
        if Op_options == "Kierner classification":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/Anatomy/Kierner_classification.png'
            st.image(image, width=700)
        if Op_options == "Kocher's incision of the abdomen":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Emil_Theodor_Kocher.png'
            st.image(image, width=180)
        if Op_options == "Meckel's diverticulum":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Johann_F_Meckel.png'
            st.image(image, width=180)
        if Op_options == "Merendino jejunal interposition":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/K_Alvin_Merendino.png'
            st.image(image, width=180)
        if Op_options == "Morrison's pouch":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/James_Rutherford_Morrison.png'
            st.image(image, width=180)
        if Op_options == "Murphy's sign":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/John_Benjamin_Murphy.png'
            st.image(image, width=180)
        if Op_options == "Ducts of Luschka":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Hubert_Von_Luschka.png'
            st.image(image, width=180)
        if Op_options == "Mirizzi's syndrome":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Pablo_Luis_Mirizzi.png'
            st.image(image, width=180)
        if Op_options == "Sphincter of Oddi":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Ruggero_Oddi.png'
            st.image(image, width=180)
        if Op_options == "Olsen-Reddick cholangiography clamp":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/Instruments/Olsen_Reddick.png'
            st.image(image, width=600)
        if Op_options == "Riedel's lobe":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Bernhard_Riedel.png'
            st.image(image, width=180)
        if Op_options == "Riedel's thyroiditis":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Bernhard_Riedel.png'
            st.image(image, width=180)
        if Op_options == "Rouviere's sulcus":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Henri_Rouviere.png'
            st.image(image, width=180)
        if Op_options == "Shouldice hernia repair":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Edward_E_Shouldice.png'
            st.image(image, width=180)
        if Op_options == "Strasberg's critical view of safety":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Steven_Strasberg.png'
            st.image(image, width=180)
        if Op_options == "Ligament of Treitz":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Vaclav_Treitz.png'
            st.image(image, width=180)
        if Op_options == "Valsalva maneuver":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Antonio_M_Valsalva.png'
            st.image(image, width=180)
        if Op_options == "Ampulla of Vater":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Abraham_Vater.png'
            st.image(image, width=180)
        if Op_options == "Whipple's operation":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Allen_O_Whipple.png'
            st.image(image, width=180)
        if Op_options == "Foramen of Winslow":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Jacob_Benignus_Winslow.png'
            st.image(image, width=180)
        if Op_options == "Witzel tunnel technique":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Oskar_Witzel.png'
            st.image(image, width=180)
        if Op_options == "Zollinger-Ellison syndrome":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Zollinger_Ellison.png'
            st.image(image, width=400)
        if Op_options == "Tubercle of Zuckerkandl":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Emil_Zuckerkandl.png'
            st.image(image, width=180)


        df_ep_info2 = new_df[new_df['Eponym_easy'].str.match(Op_options)]
        ep_yr = df_ep_info2['Year'].to_string(index=False)

        if not df_ep_info2['Who'].isnull().all():
            st.write('*_Who_*:', df_ep_info2['Who'].to_string(index=False))

        if not df_ep_info2['Year_str'].isnull().all():
            st.write('*_When_*:', df_ep_info2['Year_str'].to_string(index=False))

        if not df_ep_info2['Where'].isnull().all():
            st.write('*_Where_*:', df_ep_info2['Where'].to_string(index=False))
    
        description = df_ep_info2['Description'].to_string(index=False)
        history = df_ep_info2['History'].to_string(index=False)

        if not df_ep_info2['Description'].isnull().all():
            st.markdown(description, unsafe_allow_html=True)
        if not df_ep_info2['History'].isnull().all():
            st.write('**_History_**:', history)
            st.markdown("---")

        if not df_ep_info2['Who'].isnull().all():
            st.write('**External links**')
        ref_link = df_ep_info2['Pubmed'].to_string(index=False)
        if not df_ep_info2['Pubmed'].isnull().all():
           st.markdown(f"[PubMed.gov]({ref_link})")

        wiki_link = df_ep_info2['Wiki_link'].to_string(index=False)
        if not df_ep_info2['Wiki_link'].isnull().all():
            st.markdown(f"[wikipedia.org]({wiki_link})")

        wni_link = df_ep_info2['WNI_link'].to_string(index=False)
        if not df_ep_info2['WNI_link'].isnull().all():
           st.markdown(f"[whonamedit.com]({wni_link})")

        icd_link = df_ep_info2['ICD11_link'].to_string(index=False)
        if not df_ep_info2['ICD11_link'].isnull().all():
           st.markdown(f"[Internatinal Classification of Diseases 11th Revision]({icd_link})")
           

#----------------------------------------------------------------------------------------------#
#                                                                                              #
#  Types (eg. Incisions, Instruments) (3)                                                      #
# ::: Handles the                                                                              #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#

def exp_type():
    st.markdown('''[Advert space for Google AdSense2]''')
    st.subheader('''First, select type:''')
    st.sidebar.markdown("---")
    
    types = st.selectbox(""" """,
                            ["Anatomical structures",
                             "Clinical scores",
                             "Clinical signs",
                             "Operations",
                             "Pathology",
                             "Patient positioning",
                             "Research trials",
                             "Surgical incisions",
                             "Surgical instruments",
                             "Surgical maneuvers & techniques",
                             ], index=0)

    if types   == "Anatomical structures":              show_anatomical()       #1
    elif types == "Clinical scores":                    show_scores()           #2
    elif types == "Clinical signs":                     show_signs()            #3
    elif types == "Operations":                         show_opNames()          #4
    elif types == "Pathology":                          show_path()             #5
    elif types == "Patient positioning":                show_positions()        #6
    elif types == "Research trials":                    show_trials()           #7
    elif types == "Surgical incisions":                 show_cuts()             #8
    elif types == "Surgical instruments":               show_instruments()      #9
    elif types == "Surgical maneuvers & techniques":    show_maneuvers()        #10

#1
def show_anatomical():
    st.markdown(
        """
        <style type="text/css" media="screen">
        div[role="listbox"] ul {height:430px}
        </style>
        """
        ,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <style type="text/css" media="screen">
        .hovertext text {
        font-size: 20px !important;}
        </style>
        """
        ,
        unsafe_allow_html=True,
    )

    df = pd.read_csv('/Users/alastairhayes/desktop/Eponyms/Eponyms4python_Lite.csv')
    df1 = df.rename(columns={"Eponym": "Eponym_OLD", "Eponym_easy": "Eponym"})
    Anat_df = df1[(df1['Type'].str.match('Structures'))]
    if not Anat_df['Type'].isnull().all():
        Table = ff.create_table(Anat_df.drop(['Alphabet','CityOfEponym_A1','ISO_country_A1','Author_1_Role','WhoNamedIt',
                    'Author_1', 'Author_2','Pubmed_results','Google_results','Operation','GxP','Log2_GxP','Societies',
                    'ICD11','WNI_link', 'Reference', 'Wiki_link','PMID','Type','Journal','History','ICD11_link','Year',
                    'CountryOfEponym_A1','Class','Subclass','Description','Sex_A1','Lat_A1','Long_A1'],
                             axis=1).sort_values(by=['Eponym_OLD'],
                                                 ascending=True).reindex(columns=['Eponym']).reset_index(drop=True))

    worldMap = st.checkbox('''Show by world map''', value=False)
    if worldMap:
        Year = st.slider('Time traveler function - Year:', 1560, 2020, value=2020)
        mapbox_access_token = open("/Users/alastairhayes/desktop/Eponyms/ajhayes83_1.mapbox_token").read()  

        dfT = Anat_df.sort_values(by=['Year'],ascending=True)
        time_df = Anat_df.loc[Anat_df['Year'] <= Year]
        site_lat = time_df['Lat_A1']                           
        site_lon = time_df['Long_A1']           
        text = time_df['Eponym'] + ', ' + time_df['CityOfEponym_A1'] + ', ' + time_df['Year'].astype(str)
        locations_name = time_df['Eponym']

        fig = go.Figure()
        fig.add_trace(go.Scattermapbox(
                lat=site_lat,lon=site_lon,
                mode='markers',
                marker=go.scattermapbox.Marker(
                    color='yellow',
                    opacity=0.7,
                    size=12,
                ),
                text=text,
            hoverinfo='text'
            ))
        fig.update_layout(
            autosize=True,
            hovermode='closest',
            showlegend=False,
            width=1100,
            height=570,
            mapbox=dict(
                accesstoken=mapbox_access_token,
                bearing=0,
                center=dict(lat=25,lon=8),
                pitch=0,
                zoom=1.08,
                style='dark'),
            )
        fig.update_layout(margin=dict(l=2, r=2, t=0, b=0))
        st.write(fig) 

    st.markdown('---')
    st.subheader('''Then, search list of named anatomical structures:''')
    Anat_options2 = st.selectbox('', Anat_df['Eponym'].unique(), format_func=lambda x: ' ' if x == '1' else x)
    Anat_options2_info = df2[df2['Eponym'].str.match(Anat_options2)]


    if Anat_options2 == "Berry's ligament":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/James_Berry.png'
            st.image(image, width=180)
    if Anat_options2 == "Calot's triangle":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Calot2.png'
            st.image(image, width=600)

    if Anat_options2 == "Hartmann's pouch":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/Anatomy/Hartmanns_Pouch.png'
            st.image(image, width=450)
        
    if not Anat_options2_info['Who'].isnull().all():
        st.write('*_Who_*:', Anat_options2_info['Who'].to_string(index=False))
            
    if not Anat_options2_info['Year_str'].isnull().all():
        st.write('*_When_*:', Anat_options2_info['Year_str'].to_string(index=False))

    if not Anat_options2_info['Where'].isnull().all():
        st.write('*_Where_*:', Anat_options2_info['Where'].to_string(index=False))

        st.markdown("---")
    
    description = Anat_options2_info['Description'].to_string(index=False)
    history = Anat_options2_info['History'].to_string(index=False)
    if not Anat_options2_info['Description'].isnull().all():
        st.markdown(description, unsafe_allow_html=True)
    if not Anat_options2_info['History'].isnull().all():
        st.write('**_History_**:', history)
    st.markdown("---")

    st.write('**External links**')
    ref_link = Anat_options2_info['Reference'].to_string(index=False)
    if not Anat_options2_info['Reference'].isnull().all():
        st.markdown(f"[Link to primary paper]({ref_link})")

    wiki_link = Anat_options2_info['Wiki_link'].to_string(index=False)
    if not Anat_options2_info['Wiki_link'].isnull().all():
        st.markdown(f"[Link to Wikipedia webpage]({wiki_link})")

    wni_link = Anat_options2_info['WNI_link'].to_string(index=False)
    if not Anat_options2_info['WNI_link'].isnull().all():
        st.markdown(f"[Link to Whonamedit webpage]({wni_link})")

    icd_link = Anat_options2_info['ICD11_link'].to_string(index=False)
    if not Anat_options2_info['ICD11_link'].isnull().all():
        st.markdown(f"[Link to ICD-11 webpage]({icd_link})")
           
#2
def show_scores():
    st.markdown(
        """
        <style type="text/css" media="screen">
        div[role="listbox"] ul {height:430px}
        </style>
        """
        ,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <style type="text/css" media="screen">
        .hovertext text {
        font-size: 20px !important;}
        </style>
        """
        ,
        unsafe_allow_html=True,
    )
    
    df = pd.read_csv('/Users/alastairhayes/desktop/Eponyms/Eponyms4python_Lite.csv')
    Scores_df = df[(df['Type'].str.match('Scores'))]
    if not Scores_df['Type'].isnull().all():
        Table = ff.create_table(Scores_df.drop(['Alphabet','CityOfEponym_A1','ISO_country_A1','Author_1_Role','WhoNamedIt',
                    'Author_1', 'Author_2','Pubmed_results', 'Google_results','Operation','GxP', 'Log2_GxP','Societies',
                    'ICD11','WNI_link', 'Reference', 'Wiki_link','PMID', 'Type','Journal','History','ICD11_link','Year',
                    'CountryOfEponym_A1','Class','Subclass','Description','Sex_A1','Lat_A1','Long_A1'],
                             axis=1).sort_values(by=['Eponym'],
                                                 ascending=True).reindex(columns=['Eponym']).reset_index(drop=True))

        worldMap = st.checkbox('''Show by world map''', value=False)
        if worldMap:
            Year = st.slider('Time traveler function - Year:', 1560, 2020, value=2020)
            mapbox_access_token = open("/Users/alastairhayes/desktop/Eponyms/ajhayes83_1.mapbox_token").read()  
            dfT = Scores_df.sort_values(by=['Year'],ascending=True)
            time_df = dfT.loc[dfT['Year'] <= Year]
            site_lat = time_df['Lat_A1']            #df3['Lat_A1']                
            site_lon = time_df['Long_A1']           #df3['Long_A1']
            text = time_df['Eponym_easy'] + ', ' + time_df['CityOfEponym_A1'] + ', ' + time_df['Year'].astype(str)
            locations_name = time_df['Eponym_easy'] #df3['Eponym_easy']

            fig = go.Figure()
            fig.add_trace(go.Scattermapbox(
                    lat=site_lat,lon=site_lon,
                    mode='markers',
                    marker=go.scattermapbox.Marker(
                        color='yellow',
                        opacity=0.7,
                        size=12,
                    ),
                    text=text,
                hoverinfo='text'
                ))
            fig.update_layout(
                autosize=True,
                hovermode='closest',
                showlegend=False,
                width=1100,
                height=570,
                mapbox=dict(
                    accesstoken=mapbox_access_token,
                    bearing=0,
                    center=dict(lat=25,lon=8),
                    pitch=0,
                    zoom=1.08,
                    style='dark'),
                )
            fig.update_layout(margin=dict(l=2, r=2, t=0, b=0))
            st.write(fig) 

        st.markdown('---')
        st.subheader('''Then, search list of clinical scores:''')
        Scores_options2 = st.selectbox('', Scores_df['Eponym'].unique())

        Scores_options2_info = df2[df2['Eponym'].str.match(Scores_options2)]

        if Scores_options2 == "Alvarado score":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Alfredo_Alvarado.png'
            st.image(image, width=180)
        
        if not Scores_options2_info['Who'].isnull().all():
            st.write('*_Who_*:', Scores_options2_info['Who'].to_string(index=False))
            
        if not Scores_options2_info['Year_str'].isnull().all():
            st.write('*_When_*:', Scores_options2_info['Year_str'].to_string(index=False))

        if not Scores_options2_info['Where'].isnull().all():
            st.write('*_Where_*:', Scores_options2_info['Where'].to_string(index=False))

        ref_link = Scores_options2_info['Reference'].to_string(index=False)
        if not Scores_options2_info['Reference'].isnull().all():
           st.markdown(f"[Link to primary paper]({ref_link})")
        st.markdown("---")
    
        description = Scores_options2_info['Description'].to_string(index=False)
        history = Scores_options2_info['History'].to_string(index=False)
        if not Scores_options2_info['Description'].isnull().all():
            st.markdown(description, unsafe_allow_html=True)
        if not Scores_options2_info['History'].isnull().all():
            st.write('*_History_*:', history)
        st.markdown("---")

        wiki_link = Scores_options2_info['Wiki_link'].to_string(index=False)
        if not Scores_options2_info['Wiki_link'].isnull().all():
            st.write('**External links**')
            st.markdown(f"[Link to Wikipedia webpage]({wiki_link})")

        wni_link = Scores_options2_info['WNI_link'].to_string(index=False)
        if not Scores_options2_info['WNI_link'].isnull().all():
           st.markdown(f"[Link to Whonamedit webpage]({wni_link})")

        icd_link = Scores_options2_info['ICD11_link'].to_string(index=False)
        if not Scores_options2_info['ICD11_link'].isnull().all():
           st.markdown(f"[Link to ICD-11 webpage]({icd_link})")

#3
def show_signs():
    st.markdown(
        """
        <style type="text/css" media="screen">
        div[role="listbox"] ul {height:430px}
        </style>
        """
        ,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <style type="text/css" media="screen">
        .hovertext text {
        font-size: 20px !important;}
        </style>
        """
        ,
        unsafe_allow_html=True,
    )
    df = pd.read_csv('/Users/alastairhayes/desktop/Eponyms/Eponyms4python_Lite.csv')
    Sign_df = df[(df['Type'].str.match('Signs'))]
    if not Sign_df['Type'].isnull().all():
        Table = ff.create_table(Sign_df.drop(['Alphabet','CityOfEponym_A1','ISO_country_A1','Author_1_Role','WhoNamedIt',
                    'Author_1', 'Author_2','Pubmed_results', 'Google_results','Operation','GxP', 'Log2_GxP','Societies',
                    'ICD11','WNI_link', 'Reference', 'Wiki_link','PMID', 'Type','Journal','History','ICD11_link','Year',
                    'CountryOfEponym_A1','Class','Subclass','Description','Sex_A1','Lat_A1','Long_A1'],
                             axis=1).sort_values(by=['Eponym'],
                                                 ascending=True).reindex(columns=['Eponym']).reset_index(drop=True))
        worldMap = st.checkbox('''Show by world map''', value=False)
        if worldMap:
            Year = st.slider('Time traveler function - Year:', 1560, 2020, value=2020)
            mapbox_access_token = open("/Users/alastairhayes/desktop/Eponyms/ajhayes83_1.mapbox_token").read()  
            dfT = Sign_df.sort_values(by=['Year'],ascending=True)
            time_df = dfT.loc[dfT['Year'] <= Year]
            site_lat = time_df['Lat_A1']            
            site_lon = time_df['Long_A1']           
            text = time_df['Eponym_easy'] + ', ' + time_df['CityOfEponym_A1'] + ', ' + time_df['Year'].astype(str)
            locations_name = time_df['Eponym_easy'] #df3['Eponym_easy']

            fig = go.Figure()
            fig.add_trace(go.Scattermapbox(
                lat=site_lat,lon=site_lon,
                mode='markers',
                marker=go.scattermapbox.Marker(
                        color='yellow',
                        opacity=0.7,
                        size=12,
                        ),
                text=text,
                hoverinfo='text'
                ))
            fig.update_layout(
                autosize=True,
                hovermode='closest',
                showlegend=False,
                width=1100,height=570,
                mapbox=dict(
                    accesstoken=mapbox_access_token,
                    bearing=0,
                    center=dict(lat=25,lon=8),
                    pitch=0,
                    zoom=1.08,
                    style='dark'),
                    )
            fig.update_layout(margin=dict(l=2, r=2, t=0, b=0))
            st.write(fig) 

        st.markdown('---')
        st.subheader('''Then, search list of clinical signs:''')
        
        Sign_options2 = st.selectbox('', Sign_df['Eponym'].unique())

        Sign_options2_info = df2[df2['Eponym'].str.match(Sign_options2)]

        if Sign_options2 == "Murphy's sign":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/John_Benjamin_Murphy.png'
            st.image(image, width=180)

        if Sign_options2 == "Charcot's triad":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Jean-Martin Charcot.png'
            st.image(image, width=180)

        
        if not Sign_options2_info['Who'].isnull().all():
            st.write('*_Who_*:', Sign_options2_info['Who'].to_string(index=False))
            
        if not Sign_options2_info['Year_str'].isnull().all():
            st.write('*_When_*:', Sign_options2_info['Year_str'].to_string(index=False))

        if not Sign_options2_info['Where'].isnull().all():
            st.write('*_Where_*:', Sign_options2_info['Where'].to_string(index=False))
    
        description = Sign_options2_info['Description'].to_string(index=False)
        history = Sign_options2_info['History'].to_string(index=False)
        if not Sign_options2_info['Description'].isnull().all():
            st.markdown(description, unsafe_allow_html=True)
        if not Sign_options2_info['History'].isnull().all():
            st.write('*_History_*:', history)
        st.markdown("---")

        ref_link = Sign_options2_info['Reference'].to_string(index=False)
        if not Sign_options2_info['Reference'].isnull().all():
           st.markdown(f"[Link to primary paper]({ref_link})")

        wiki_link = Sign_options2_info['Wiki_link'].to_string(index=False)
        if not Sign_options2_info['Wiki_link'].isnull().all():
            st.write('**External links**')
            st.markdown(f"[Link to Wikipedia webpage]({wiki_link})")

        wni_link = Sign_options2_info['WNI_link'].to_string(index=False)
        if not Sign_options2_info['WNI_link'].isnull().all():
           st.markdown(f"[Link to Whonamedit webpage]({wni_link})")

        icd_link = Sign_options2_info['ICD11_link'].to_string(index=False)
        if not Sign_options2_info['ICD11_link'].isnull().all():
           st.markdown(f"[Link to ICD-11 webpage]({icd_link})")
       
#4
def show_opNames():
    st.markdown(
        """
        <style type="text/css" media="screen">
        div[role="listbox"] ul {height:430px}
        </style>
        """
        ,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <style type="text/css" media="screen">
        .hovertext text {
        font-size: 20px !important;}
        </style>
        """
        ,
        unsafe_allow_html=True,
    )

    df = pd.read_csv('/Users/alastairhayes/desktop/Eponyms/Eponyms4python_Lite.csv')
    OpName_df = df[(df['Type'].str.match('Operations'))]
    if not OpName_df['Type'].isnull().all():
        Table = ff.create_table(OpName_df.drop(['Alphabet','CityOfEponym_A1','ISO_country_A1','Author_1_Role',
                    'WhoNamedIt','Author_1', 'Author_2','Pubmed_results', 'Google_results','Operation',
                    'GxP', 'Log2_GxP','Societies','ICD11','WNI_link', 'Reference', 'Wiki_link','PMID', 'Type',
                    'Journal','History','ICD11_link','Year', 'CountryOfEponym_A1','Class','Subclass','Description',
                    'Sex_A1','Lat_A1','Long_A1'],
                             axis=1).sort_values(by=['Eponym'],
                                                 ascending=True).reindex(columns=['Eponym']).reset_index(drop=True))

        worldMap = st.checkbox('''Show by world map''', value=False)
        if worldMap:
            Year = st.slider('Time traveler function - Year:', 1560, 2020, value=2020)
            mapbox_access_token = open("/Users/alastairhayes/desktop/Eponyms/ajhayes83_1.mapbox_token").read()  
            dfT = OpName_df.sort_values(by=['Year'],ascending=True)
            time_df = dfT.loc[dfT['Year'] <= Year]
            site_lat = time_df['Lat_A1']            #df3['Lat_A1']
            site_lon = time_df['Long_A1']           #df3['Long_A1']
            text = time_df['Eponym_easy'] + ', ' + time_df['CityOfEponym_A1'] + ', ' + time_df['Year'].astype(str)
            locations_name = time_df['Eponym_easy'] #df3['Eponym_easy']

            fig = go.Figure()
            fig.add_trace(go.Scattermapbox(
                lat=site_lat,lon=site_lon,
                mode='markers',
                marker=go.scattermapbox.Marker(
                        color='yellow',
                        opacity=0.7,
                        size=12,
                        ),
                text=text,
                hoverinfo='text'
                ))
            fig.update_layout(
                autosize=True,
                hovermode='closest',
                showlegend=False,
                width=1100,height=570,
                mapbox=dict(
                    accesstoken=mapbox_access_token,
                    bearing=0,
                    center=dict(lat=25,lon=8),
                    pitch=0,
                    zoom=1.08,
                    style='dark'),
                    )
            fig.update_layout(margin=dict(l=2, r=2, t=0, b=0))
            st.write(fig) 

        st.markdown('---')
        st.subheader('''Then, search list of named operations:''')
        OpName_options2 = st.selectbox('', OpName_df['Eponym'].unique())
        OpName_options2_info = df2[df2['Eponym'].str.match(OpName_options2)]

        if OpName_options2 == "Allison repair":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Philip_Rowland_Allison.png'
            st.image(image, width=180)
        if OpName_options2 == "Altemeier procedure":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/William_A_Altemeier.png'
            st.image(image, width=180)
        if OpName_options2 == "Bassini hernia repair":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Edoardo_Bassini_Wellcome.jpg'
            st.image(image, width=200)
        if OpName_options2 == "Battle's operation":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/William_Henry_Battle.png'
            st.image(image, width=180)
        if OpName_options2 == "Beger procedure":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Hans_Gunther_Beger.png'
            st.image(image, width=180)
        if OpName_options2 == "Belsey Mark IV operation":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Ronald_Belsey.png'
            st.image(image, width=180)
        if OpName_options2 == "Brooke ileostomy":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Bryan_Nicholas_Brooke.png'
            st.image(image, width=180)
        if OpName_options2 == "Collis gastroplasty":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/John_Leigh_Collis.png'
            st.image(image, width=180)
        if OpName_options2 == "Delorme's procedure":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Edmond_Delorme.png'
            st.image(image, width=180)
        if OpName_options2 == "Hartmann's operation":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Henri_Hartmann_1920.jpg'
            st.image(image, width=180)
        if OpName_options2 == "Heineke–Mikulicz pyloroplasty":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Heineke_Mikulicz.png'
            st.image(image, width=400)
        if OpName_options2 == "Ivor Lewis oesophagectomy":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Ivor_Lewis.png'
            st.image(image, width=180)
        if OpName_options2 == "Merendino jejunal interposition":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/K_Alvin_Merendino.png'
            st.image(image, width=180)

        
        if not OpName_options2_info['Who'].isnull().all():
            st.write('*_Who_*:', OpName_options2_info['Who'].to_string(index=False))
            
        if not OpName_options2_info['Year_str'].isnull().all():
            st.write('*_When_*:', OpName_options2_info['Year_str'].to_string(index=False))

        if not OpName_options2_info['Where'].isnull().all():
            st.write('*_Where_*:', OpName_options2_info['Where'].to_string(index=False))

        ref_link = OpName_options2_info['Reference'].to_string(index=False)
        if not OpName_options2_info['Reference'].isnull().all():
           st.markdown(f"[Link to primary paper]({ref_link})")
        st.markdown("---")
    
        description = OpName_options2_info['Description'].to_string(index=False)
        history = OpName_options2_info['History'].to_string(index=False)
        if not OpName_options2_info['Description'].isnull().all():
            st.markdown(description, unsafe_allow_html=True)
        if not OpName_options2_info['History'].isnull().all():
            st.write('**_History_**:', history)
        st.markdown("---")

        wiki_link = OpName_options2_info['Wiki_link'].to_string(index=False)
        if not OpName_options2_info['Wiki_link'].isnull().all():
            st.write('**External links**')
            st.markdown(f"[Link to Wikipedia webpage]({wiki_link})")

        wni_link = OpName_options2_info['WNI_link'].to_string(index=False)
        if not OpName_options2_info['WNI_link'].isnull().all():
           st.markdown(f"[Link to Whonamedit webpage]({wni_link})")

        icd_link = OpName_options2_info['ICD11_link'].to_string(index=False)
        if not OpName_options2_info['ICD11_link'].isnull().all():
           st.markdown(f"[Link to ICD-11 webpage]({icd_link})")
       
#5
def show_path():
    st.markdown(
        """
        <style type="text/css" media="screen">
        div[role="listbox"] ul {height:430px}
        </style>
        """
        ,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <style type="text/css" media="screen">
        .hovertext text {
        font-size: 20px !important;}
        </style>
        """
        ,
        unsafe_allow_html=True,
    )
    df = pd.read_csv('/Users/alastairhayes/desktop/Eponyms/Eponyms4python_Lite.csv')
    Path_df = df[(df['Type'].str.match('Pathology'))]
    if not Path_df['Type'].isnull().all():
        Table = ff.create_table(Path_df.drop(['Alphabet','CityOfEponym_A1','ISO_country_A1','Author_1_Role',
                    'WhoNamedIt','Author_1', 'Author_2','Pubmed_results', 'Google_results','Operation','GxP',
                    'Log2_GxP','Societies','ICD11','WNI_link', 'Reference', 'Wiki_link','PMID', 'Type','Journal',
                    'History','ICD11_link','Year', 'CountryOfEponym_A1','Class','Subclass','Description',
                    'Sex_A1','Lat_A1','Long_A1'],
                             axis=1).sort_values(by=['Eponym'],
                                                 ascending=True).reindex(columns=['Eponym']).reset_index(drop=True))
        worldMap = st.checkbox('''Show by world map''', value=False)
        if worldMap:
            Year = st.slider('Time traveler function - Year:', 1560, 2020, value=2020)
            mapbox_access_token = open("/Users/alastairhayes/desktop/Eponyms/ajhayes83_1.mapbox_token").read()  
            dfT = Path_df.sort_values(by=['Year'],ascending=True)
            time_df = dfT.loc[dfT['Year'] <= Year]
            site_lat = time_df['Lat_A1']            #df3['Lat_A1']
            site_lon = time_df['Long_A1']           #df3['Long_A1']
            text = time_df['Eponym_easy'] + ', ' + time_df['CityOfEponym_A1'] + ', ' + time_df['Year'].astype(str)
            locations_name = time_df['Eponym_easy'] #df3['Eponym_easy']

            fig = go.Figure()
            fig.add_trace(go.Scattermapbox(
                lat=site_lat,lon=site_lon,
                mode='markers',
                marker=go.scattermapbox.Marker(
                        color='yellow',
                        opacity=0.7,
                        size=12,
                        ),
                text=text,
                hoverinfo='text'
                ))
            fig.update_layout(
                autosize=True,
                hovermode='closest',
                showlegend=False,
                width=1100,
                height=570,
                mapbox=dict(
                    accesstoken=mapbox_access_token,
                    bearing=0,
                    center=dict(lat=25,lon=8),
                    pitch=0,
                    zoom=1.08,
                    style='dark'),
                    )
            fig.update_layout(margin=dict(l=2, r=2, t=0, b=0))
            st.write(fig) 

        st.markdown('---')
        st.subheader('''Then, choose from pathological condition, classification, rule or score:''')
        Paths_options2 = st.selectbox('', Path_df['Eponym'].unique())

        Paths_options2_info = df2[df2['Eponym'].str.match(Paths_options2)]

        if Paths_options2 == "Barrett's oesophagus":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Norman_Rupert_Barrett.png'
            st.image(image, width=180)

        if Paths_options2 == "Crohn's disease":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Burrill_Bernard_Crohn.png'
            st.image(image, width=180)
        
        if not Paths_options2_info['Who'].isnull().all():
            st.write('*_Who_*:', Paths_options2_info['Who'].to_string(index=False))
            
        if not Paths_options2_info['Year_str'].isnull().all():
            st.write('*_When_*:', Paths_options2_info['Year_str'].to_string(index=False))

        if not Paths_options2_info['Where'].isnull().all():
            st.write('*_Where_*:', Paths_options2_info['Where'].to_string(index=False))

        ref_link = Paths_options2_info['Reference'].to_string(index=False)
        if not Paths_options2_info['Reference'].isnull().all():
           st.markdown(f"[Link to primary paper]({ref_link})")
        st.markdown("---")
    
        description = Paths_options2_info['Description'].to_string(index=False)
        history = Paths_options2_info['History'].to_string(index=False)
        if not Paths_options2_info['Description'].isnull().all():
            st.write(description)
        if not Paths_options2_info['History'].isnull().all():
            st.write('*_History_*:', history)
        st.markdown("---")

        wiki_link = Paths_options2_info['Wiki_link'].to_string(index=False)
        if not Paths_options2_info['Wiki_link'].isnull().all():
            st.write('**External links**')
            st.markdown(f"[Link to Wikipedia webpage]({wiki_link})")

        wni_link = Paths_options2_info['WNI_link'].to_string(index=False)
        if not Paths_options2_info['WNI_link'].isnull().all():
           st.markdown(f"[Link to Whonamedit webpage]({wni_link})")

        icd_link = Paths_options2_info['ICD11_link'].to_string(index=False)
        if not Paths_options2_info['ICD11_link'].isnull().all():
           st.markdown(f"[Link to ICD-11 webpage]({icd_link})")
           
#6
def show_positions():
    st.markdown(
        """
        <style type="text/css" media="screen">
        div[role="listbox"] ul {height:430px}
        </style>
        """
        ,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <style type="text/css" media="screen">
        .hovertext text {
        font-size: 20px !important;}
        </style>
        """
        ,
        unsafe_allow_html=True,
    )
    df = pd.read_csv('/Users/alastairhayes/desktop/Eponyms/Eponyms4python_Lite.csv')
    Positions_df = df[(df['Type'].str.match('Positions'))]
    if not Positions_df['Type'].isnull().all():
        Table = ff.create_table(Positions_df.drop(['Alphabet','CityOfEponym_A1','ISO_country_A1','Author_1_Role',
                    'WhoNamedIt','Author_1', 'Author_2','Pubmed_results', 'Google_results','Operation','GxP',
                    'Log2_GxP','Societies','ICD11','WNI_link', 'Reference', 'Wiki_link','PMID', 'Type','Journal',
                    'History','ICD11_link','Year', 'CountryOfEponym_A1','Class','Subclass','Description',
                    'Sex_A1','Lat_A1','Long_A1'],
                             axis=1).sort_values(by=['Eponym'],
                                                 ascending=True).reindex(columns=['Eponym']).reset_index(drop=True))
        worldMap = st.checkbox('''Show by world map''', value=False)
        if worldMap:
            Year = st.slider('Time traveler function - Year:', 1560, 2020, value=2020)
            mapbox_access_token = open("/Users/alastairhayes/desktop/Eponyms/ajhayes83_1.mapbox_token").read()  
            dfT = Positions_df.sort_values(by=['Year'],ascending=True)
            time_df = dfT.loc[dfT['Year'] <= Year]
            site_lat = time_df['Lat_A1']            #df3['Lat_A1']
            site_lon = time_df['Long_A1']           #df3['Long_A1']
            text = time_df['Eponym_easy'] + ', ' + time_df['CityOfEponym_A1'] + ', ' + time_df['Year'].astype(str)
            locations_name = time_df['Eponym_easy'] #df3['Eponym_easy']

            fig = go.Figure()
            fig.add_trace(go.Scattermapbox(
                lat=site_lat,lon=site_lon,
                mode='markers',
                marker=go.scattermapbox.Marker(
                        color='yellow',
                        opacity=0.7,
                        size=12,
                        ),
                text=text,
                hoverinfo='text'
                ))
            fig.update_layout(
                autosize=True,
                hovermode='closest',
                showlegend=False,
                width=1100,height=570,
                mapbox=dict(
                    accesstoken=mapbox_access_token,
                    bearing=0,
                    center=dict(lat=25,lon=8),
                    pitch=0,
                    zoom=1.08,
                    style='dark'),
                    )
            fig.update_layout(margin=dict(l=2, r=2, t=0, b=0))
            st.write(fig) 

        st.markdown('---')
        st.subheader('''Choose named patient position:''')
        Positions_options2 = st.selectbox('', Positions_df['Eponym'].unique())

        Positions_options2_info = df2[df2['Eponym'].str.match(Positions_options2)]
        
        if not Positions_options2_info['Who'].isnull().all():
            st.write('*_Who_*:', Positions_options2_info['Who'].to_string(index=False))
            
        if not Positions_options2_info['Year_str'].isnull().all():
            st.write('*_When_*:', Positions_options2_info['Year_str'].to_string(index=False))

        if not Positions_options2_info['Where'].isnull().all():
            st.write('*_Where_*:', Positions_options2_info['Where'].to_string(index=False))

        ref_link = Positions_options2_info['Reference'].to_string(index=False)
        if not Positions_options2_info['Reference'].isnull().all():
           st.markdown(f"[Link to primary paper]({ref_link})")
        st.markdown("---")
    
        description = Positions_options2_info['Description'].to_string(index=False)
        history = Positions_options2_info['History'].to_string(index=False)
        if not Positions_options2_info['Description'].isnull().all():
            st.write('**_Description_**:', description)
        if not Positions_options2_info['History'].isnull().all():
            st.write('**_History_**:', history)
        st.markdown("---")

        wiki_link = Positions_options2_info['Wiki_link'].to_string(index=False)
        if not Positions_options2_info['Wiki_link'].isnull().all():
            st.write('**External links**')
            st.markdown(f"[Link to Wikipedia webpage]({wiki_link})")

        wni_link = Positions_options2_info['WNI_link'].to_string(index=False)
        if not Positions_options2_info['WNI_link'].isnull().all():
           st.markdown(f"[Link to Whonamedit webpage]({wni_link})")

        icd_link = Positions_options2_info['ICD11_link'].to_string(index=False)
        if not Positions_options2_info['ICD11_link'].isnull().all():
           st.markdown(f"[Link to ICD-11 webpage]({icd_link})")


#7
def show_trials():
    st.markdown(
        """
        <style type="text/css" media="screen">
        div[role="listbox"] ul {height:430px}
        </style>
        """
        ,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <style type="text/css" media="screen">
        .hovertext text {
        font-size: 20px !important;}
        </style>
        """
        ,
        unsafe_allow_html=True,
    )
    df = pd.read_csv('/Users/alastairhayes/desktop/Eponyms/Eponyms4python_Lite.csv')
    Trial_df = df[(df['Type'].str.match('Trials'))]
    if not Trial_df['Type'].isnull().all():
        Table = ff.create_table(Trial_df.drop(['Alphabet','CityOfEponym_A1','ISO_country_A1','Author_1_Role','WhoNamedIt',
                    'Author_1', 'Author_2','Pubmed_results', 'Google_results','Operation','GxP', 'Log2_GxP','Societies',
                    'ICD11','WNI_link', 'Reference', 'Wiki_link','PMID', 'Type','Journal','History','ICD11_link','Year',
                    'CountryOfEponym_A1','Class','Subclass','Description','Sex_A1','Lat_A1','Long_A1'],
                             axis=1).sort_values(by=['Eponym'],
                                                 ascending=True).reindex(columns=['Eponym']).reset_index(drop=True))
        worldMap = st.checkbox('''Show by world map''', value=False)
        if worldMap:
            Year = st.slider('Time traveler function - Year:', 1560, 2020, value=2020)
            mapbox_access_token = open("/Users/alastairhayes/desktop/Eponyms/ajhayes83_1.mapbox_token").read()  
            dfT = Trial_df.sort_values(by=['Year'],ascending=True)
            time_df = dfT.loc[dfT['Year'] <= Year]
            site_lat = time_df['Lat_A1']            
            site_lon = time_df['Long_A1']           
            text = time_df['Eponym_easy'] + ', ' + time_df['CityOfEponym_A1'] + ', ' + time_df['Year'].astype(str)
            locations_name = time_df['Eponym_easy'] #df3['Eponym_easy']

            fig = go.Figure()
            fig.add_trace(go.Scattermapbox(
                lat=site_lat,lon=site_lon,
                mode='markers',
                marker=go.scattermapbox.Marker(
                        color='yellow',
                        opacity=0.7,
                        size=12,
                        ),
                text=text,
                hoverinfo='text'
                ))
            fig.update_layout(
                autosize=True,
                hovermode='closest',
                showlegend=False,
                width=1100,height=570,
                mapbox=dict(
                    accesstoken=mapbox_access_token,
                    bearing=0,
                    center=dict(lat=25,lon=8),
                    pitch=0,
                    zoom=1.08,
                    style='dark'),
                    )
            fig.update_layout(margin=dict(l=2, r=2, t=0, b=0))
            st.write(fig) 

        st.markdown('---')
        st.subheader('''Then, search list of research trials:''')
        
        Trial_options2 = st.selectbox('', Trial_df['Eponym'].unique())

        Trial_options2_info = df2[df2['Eponym'].str.match(Trial_options2)]

        
        if not Trial_options2_info['Who'].isnull().all():
            st.write('*_Who_*:', Trial_options2_info['Who'].to_string(index=False))
            
        if not Trial_options2_info['Year_str'].isnull().all():
            st.write('*_When_*:', Trial_options2_info['Year_str'].to_string(index=False))

        if not Trial_options2_info['Where'].isnull().all():
            st.write('*_Where_*:', Trial_options2_info['Where'].to_string(index=False))
    
        description = Trial_options2_info['Description'].to_string(index=False)
        history = Trial_options2_info['History'].to_string(index=False)
        if not Trial_options2_info['Description'].isnull().all():
            st.markdown(description, unsafe_allow_html=True)
        if not Trial_options2_info['History'].isnull().all():
            st.write('*_History_*:', history)
        st.markdown("---")

        ref_link = Trial_options2_info['Reference'].to_string(index=False)
        if not Trial_options2_info['Reference'].isnull().all():
           st.markdown(f"[Link to primary paper]({ref_link})")

        wiki_link = Trial_options2_info['Wiki_link'].to_string(index=False)
        if not Trial_options2_info['Wiki_link'].isnull().all():
            st.write('**External links**')
            st.markdown(f"[Link to Wikipedia webpage]({wiki_link})")

        wni_link = Trial_options2_info['WNI_link'].to_string(index=False)
        if not Trial_options2_info['WNI_link'].isnull().all():
           st.markdown(f"[Link to Whonamedit webpage]({wni_link})")

        icd_link = Trial_options2_info['ICD11_link'].to_string(index=False)
        if not Trial_options2_info['ICD11_link'].isnull().all():
           st.markdown(f"[Link to ICD-11 webpage]({icd_link})")



#8
def show_cuts():
    st.markdown(
        """
        <style type="text/css" media="screen">
        div[role="listbox"] ul {height:430px}
        </style>
        """
        ,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <style type="text/css" media="screen">
        .hovertext text {
        font-size: 20px !important;}
        </style>
        """
        ,
        unsafe_allow_html=True,
    )
    df = pd.read_csv('/Users/alastairhayes/desktop/Eponyms/Eponyms4python_Lite.csv')
    Cuts_df = df[(df['Type'].str.match('Incisions'))]
    if not Cuts_df['Type'].isnull().all():
        Table = ff.create_table(Cuts_df.drop(['Alphabet','CityOfEponym_A1','ISO_country_A1','Author_1_Role',
                    'WhoNamedIt','Author_1', 'Author_2','Pubmed_results', 'Google_results','Operation','GxP',
                    'Log2_GxP','Societies','ICD11','WNI_link', 'Reference', 'Wiki_link','PMID', 'Type','Journal',
                    'History','ICD11_link','Year', 'CountryOfEponym_A1','Class','Subclass','Description',
                    'Sex_A1','Lat_A1','Long_A1'],
                             axis=1).sort_values(by=['Eponym'],
                                                 ascending=True).reindex(columns=['Eponym']).reset_index(drop=True))
        worldMap = st.checkbox('''Show by world map''', value=False)
        if worldMap:
            Year = st.slider('Time traveler function - Year:', 1560, 2020, value=2020)
            mapbox_access_token = open("/Users/alastairhayes/desktop/Eponyms/ajhayes83_1.mapbox_token").read()  
            dfT = Cuts_df.sort_values(by=['Year'],ascending=True)
            time_df = dfT.loc[dfT['Year'] <= Year]
            site_lat = time_df['Lat_A1']            #df3['Lat_A1']
            site_lon = time_df['Long_A1']           #df3['Long_A1']
            text = time_df['Eponym_easy'] + ', ' + time_df['CityOfEponym_A1'] + ', ' + time_df['Year'].astype(str)
            locations_name = time_df['Eponym_easy'] #df3['Eponym_easy']

            fig = go.Figure()
            fig.add_trace(go.Scattermapbox(
                lat=site_lat,lon=site_lon,
                mode='markers',
                marker=go.scattermapbox.Marker(
                        color='yellow',
                        opacity=0.7,
                        size=12,
                        ),
                text=text,
                hoverinfo='text'
                ))
            fig.update_layout(
                autosize=True,
                hovermode='closest',
                showlegend=False,
                width=1100,height=570,
                mapbox=dict(
                    accesstoken=mapbox_access_token,
                    bearing=0,
                    center=dict(lat=25,lon=8),
                    pitch=0,
                    zoom=1.08,
                    style='dark'),
                    )
            fig.update_layout(margin=dict(l=2, r=2, t=0, b=0))
            st.write(fig) 

        st.markdown('---')
        st.subheader('''Choose from list of incisions:''')
        Cuts_options2 = st.selectbox('', Cuts_df['Eponym'].unique())
        Cuts_options2_info = df2[df2['Eponym'].str.match(Cuts_options2)]

        if Cuts_options2 == "Kocher's incision of the abdomen":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Emil_Theodor_Kocher.png'
            st.image(image, width=180)

        if not Cuts_options2_info['Who'].isnull().all():
            st.write('*_Who_*:', Cuts_options2_info['Who'].to_string(index=False))
            
        if not Cuts_options2_info['Year_str'].isnull().all():
            st.write('*_When_*:', Cuts_options2_info['Year_str'].to_string(index=False))

        if not Cuts_options2_info['Where'].isnull().all():
            st.write('*_Where_*:', Cuts_options2_info['Where'].to_string(index=False))

        ref_link = Cuts_options2_info['Reference'].to_string(index=False)
        if not Cuts_options2_info['Reference'].isnull().all():
           st.markdown(f"[Link to primary paper]({ref_link})")
        st.markdown("---")
    
        description = Cuts_options2_info['Description'].to_string(index=False)
        history = Cuts_options2_info['History'].to_string(index=False)
        if not Cuts_options2_info['Description'].isnull().all():
            st.write('**_Description_**:', description)
        if not Cuts_options2_info['History'].isnull().all():
            st.write('**_History_**:', history)
        st.markdown("---")

        wiki_link = Cuts_options2_info['Wiki_link'].to_string(index=False)
        if not Cuts_options2_info['Wiki_link'].isnull().all():
            st.write('**External links**')
            st.markdown(f"[Link to Wikipedia webpage]({wiki_link})")

        wni_link = Cuts_options2_info['WNI_link'].to_string(index=False)
        if not Cuts_options2_info['WNI_link'].isnull().all():
           st.markdown(f"[Link to Whonamedit webpage]({wni_link})")

        icd_link = Cuts_options2_info['ICD11_link'].to_string(index=False)
        if not Cuts_options2_info['ICD11_link'].isnull().all():
           st.markdown(f"[Link to ICD-11 webpage]({icd_link})")
        
#9    
def show_instruments():
    st.markdown(
        """
        <style type="text/css" media="screen">
        div[role="listbox"] ul {height:430px}
        </style>
        """
        ,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <style type="text/css" media="screen">
        .hovertext text {
        font-size: 20px !important;}
        </style>
        """
        ,
        unsafe_allow_html=True,
    )
    df = pd.read_csv('/Users/alastairhayes/desktop/Eponyms/Eponyms4python_Lite.csv', dtype={'Image':str})
    Instrum_df = df[(df['Type'].str.match('Instruments'))]
    if not Instrum_df['Type'].isnull().all():
        Table = ff.create_table(Instrum_df.drop(['Alphabet','CityOfEponym_A1','ISO_country_A1','Author_1_Role',
                    'WhoNamedIt','Author_1', 'Author_2','Pubmed_results', 'Google_results','Operation','GxP',
                    'Log2_GxP','Societies','ICD11','WNI_link', 'Reference', 'Wiki_link','PMID', 'Type','Journal',
                    'History','ICD11_link','Year', 'CountryOfEponym_A1','Class','Subclass','Description',
                    'Sex_A1','Lat_A1','Long_A1'],
                             axis=1).sort_values(by=['Eponym'],
                                                 ascending=True).reindex(columns=['Eponym']).reset_index(drop=True))
        worldMap = st.checkbox('''Show by world map''', value=False)
        if worldMap:
            Year = st.slider('Time traveler function - Year:', 1560, 2020, value=2020)
            mapbox_access_token = open("/Users/alastairhayes/desktop/Eponyms/ajhayes83_1.mapbox_token").read()  
            dfT = Instrum_df.sort_values(by=['Year'],ascending=True)
            time_df = dfT.loc[dfT['Year'] <= Year]
            site_lat = time_df['Lat_A1']            #df3['Lat_A1']
            site_lon = time_df['Long_A1']           #df3['Long_A1']
            text = time_df['Eponym_easy'] + ', ' + time_df['CityOfEponym_A1'] + ', ' + time_df['Year'].astype(str)
            locations_name = time_df['Eponym_easy'] #df3['Eponym_easy']

            fig = go.Figure()
            fig.add_trace(go.Scattermapbox(
                lat=site_lat,lon=site_lon,
                mode='markers',
                marker=go.scattermapbox.Marker(
                        color='yellow',
                        opacity=0.7,
                        size=12,
                        ),
                text=text,
                hoverinfo='text'
                ))
            fig.update_layout(
                autosize=True,
                hovermode='closest',
                showlegend=False,
                width=1100,height=570,
                mapbox=dict(
                    accesstoken=mapbox_access_token,
                    bearing=0,
                    center=dict(lat=25,lon=8),
                    pitch=0,
                    zoom=1.08,
                    style='dark'),
                    )
            fig.update_layout(margin=dict(l=2, r=2, t=0, b=0))
            st.write(fig) 

        st.markdown('---')
        st.subheader('''Choose from list of surgical instruments:''')
        Instrum_options2 = st.selectbox('', Instrum_df['Eponym'].unique())

        Instrum_options2_info = df2[df2['Eponym'].str.match(Instrum_options2)]

        if Instrum_options2 == "Allis forceps":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/Instruments/Allis_Tissue_Forceps.jpg'
            st.image(image, width=500,
            #caption=Philip Allison
                    )
            
        if Instrum_options2 == "Babcock forceps":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/Instruments/Babcock_Tissue_Forceps.jpg'
            st.image(image, width=500)

        if Instrum_options2 == "Deaver retractor":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/Instruments/Deaver_Retractor.jpg'
            st.image(image, width=500)

        if Instrum_options2 == "DeBakey forceps":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/Instruments/DeBakey_Forceps.jpg'
            st.image(image, width=500)

        if Instrum_options2 == "Fanelli catheter":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Fanelli.png'
            st.image(image, width=500)

        if Instrum_options2 == "Foley catheter":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Frederic_EB_Foley.png'
            st.image(image, width=200)

        if Instrum_options2 == "Joll's retractor catheter":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/Instruments/JollsRetractor.png'
            st.image(image, width=400)
            
        if not Instrum_options2_info['Who'].isnull().all():
            st.write('*_Who_*:', Instrum_options2_info['Who'].to_string(index=False))

        if not Instrum_options2_info['Where'].isnull().all():
            st.write('*_Where_*:', Instrum_options2_info['Where'].to_string(index=False))

        ref_link = Instrum_options2_info['Reference'].to_string(index=False)
        if not Instrum_options2_info['Reference'].isnull().all():
           st.markdown(f"[Link to primary paper]({ref_link})")
        st.markdown("---")
    
        description = Instrum_options2_info['Description'].to_string(index=False)
        history = Instrum_options2_info['History'].to_string(index=False)
        if not Instrum_options2_info['Description'].isnull().all():
            st.markdown(description, unsafe_allow_html=True)
        if not Instrum_options2_info['History'].isnull().all():
            st.write('**_History_**:', history)
        st.markdown("---")

        wiki_link = Instrum_options2_info['Wiki_link'].to_string(index=False)
        if not Instrum_options2_info['Wiki_link'].isnull().all():
            st.write('**External links**')
            st.markdown(f"[Link to Wikipedia webpage]({wiki_link})")

        wni_link = Instrum_options2_info['WNI_link'].to_string(index=False)
        if not Instrum_options2_info['WNI_link'].isnull().all():
           st.markdown(f"[Link to Whonamedit webpage]({wni_link})")

        icd_link = Instrum_options2_info['ICD11_link'].to_string(index=False)
        if not Instrum_options2_info['ICD11_link'].isnull().all():
           st.markdown(f"[Link to ICD-11 webpage]({icd_link})")

#10
def show_maneuvers():
    st.markdown(
        """
        <style type="text/css" media="screen">
        div[role="listbox"] ul {height:430px}
        </style>
        """
        ,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <style type="text/css" media="screen">
        .hovertext text {
        font-size: 20px !important;}
        </style>
        """
        ,
        unsafe_allow_html=True,
    )
    df = pd.read_csv('/Users/alastairhayes/desktop/Eponyms/Eponyms4python_Lite.csv')
    Maneuv_df = df[(df['Type'].str.match('Surgical Maneuvers & Techniques'))]
    if not Maneuv_df['Type'].isnull().all():
        Table = ff.create_table(Maneuv_df.drop(['Alphabet','CityOfEponym_A1','ISO_country_A1','Author_1_Role',
                    'WhoNamedIt','Author_1', 'Author_2','Pubmed_results','Google_results','Operation','GxP',
                    'Log2_GxP','Societies','ICD11','WNI_link', 'Reference', 'Wiki_link','PMID', 'Type','Journal',
                    'History','ICD11_link','Year', 'CountryOfEponym_A1','Class','Subclass','Description',
                    'Sex_A1','Lat_A1','Long_A1'],
                             axis=1).sort_values(by=['Eponym'],
                                                 ascending=True).reindex(columns=['Eponym']).reset_index(drop=True))
        worldMap = st.checkbox('''Show by world map''', value=False)
        if worldMap:
            Year = st.slider('Time traveler function - Year:', 1560, 2020, value=2020)
            mapbox_access_token = open("/Users/alastairhayes/desktop/Eponyms/ajhayes83_1.mapbox_token").read()  
            dfT = Maneuv_df.sort_values(by=['Year'],ascending=True)
            time_df = dfT.loc[dfT['Year'] <= Year]
            site_lat = time_df['Lat_A1']            #df3['Lat_A1']
            site_lon = time_df['Long_A1']           #df3['Long_A1']
            text = time_df['Eponym_easy'] + ', ' + time_df['CityOfEponym_A1'] + ', ' + time_df['Year'].astype(str)
            locations_name = time_df['Eponym_easy'] #df3['Eponym_easy']

            fig = go.Figure()
            fig.add_trace(go.Scattermapbox(
                lat=site_lat,lon=site_lon,
                mode='markers',
                marker=go.scattermapbox.Marker(
                        color='yellow',
                        opacity=0.7,
                        size=12,
                        ),
                text=text,
                hoverinfo='text'
                ))
            fig.update_layout(
                autosize=True,
                hovermode='closest',
                showlegend=False,
                width=1100,height=570,
                mapbox=dict(
                    accesstoken=mapbox_access_token,
                    bearing=0,
                    center=dict(lat=25,lon=8),
                    pitch=0,
                    zoom=1.08,
                    style='dark'),
                    )
            fig.update_layout(margin=dict(l=2, r=2, t=0, b=0))
            st.write(fig) 

        st.markdown('---')
        st.subheader('''Choose from list of surgical maneuvers or techniques:''')
        Maneuv_options2 = st.selectbox('', Maneuv_df['Eponym'].unique())

        Maneuv_options2_info = df2[df2['Eponym'].str.match(Maneuv_options2)]

        if Maneuv_options2 == "Hasson technique":
            image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Harrith_Hasson.png'
            st.image(image, width=180)

        if not Maneuv_options2_info['Who'].isnull().all():
            st.write('*_Who_*:', Maneuv_options2_info['Who'].to_string(index=False))
            
        if not Maneuv_options2_info['Year_str'].isnull().all():
            st.write('*_When_*:', Maneuv_options2_info['Year_str'].to_string(index=False))

        if not Maneuv_options2_info['Where'].isnull().all():
            st.write('*_Where_*:', Maneuv_options2_info['Where'].to_string(index=False))

        st.markdown("---")
    
        description = Maneuv_options2_info['Description'].to_string(index=False)
        history = Maneuv_options2_info['History'].to_string(index=False)
        if not Maneuv_options2_info['Description'].isnull().all():
            st.markdown(description, unsafe_allow_html=True)
        if not Maneuv_options2_info['History'].isnull().all():
            st.write('**_History_**:', history)
        st.markdown("---")

        ref_link = Maneuv_options2_info['Reference'].to_string(index=False)
        if not Maneuv_options2_info['Reference'].isnull().all():
           st.markdown(f"[Link to primary paper]({ref_link})")

        wiki_link = Maneuv_options2_info['Wiki_link'].to_string(index=False)
        if not Maneuv_options2_info['Wiki_link'].isnull().all():
            st.write('**External links**')
            st.markdown(f"[Link to Wikipedia webpage]({wiki_link})")

        wni_link = Maneuv_options2_info['WNI_link'].to_string(index=False)
        if not Maneuv_options2_info['WNI_link'].isnull().all():
           st.markdown(f"[Link to Whonamedit webpage]({wni_link})")

        icd_link = Maneuv_options2_info['ICD11_link'].to_string(index=False)
        if not Maneuv_options2_info['ICD11_link'].isnull().all():
           st.markdown(f"[Link to ICD-11 webpage]({icd_link})")


#----------------------------------------------------------------------------------------------#
#                                                                                              #
#  Geographical Origins (3)                                                                    #
# ::: Handles the                                                                              #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#

def exp_geography():
    st.markdown(
        """
        <style type="text/css" media="screen">
        div[role="listbox"] ul {height:53px}
        </style>
        """
        ,
        unsafe_allow_html=True,
    )

    st.sidebar.markdown("---")
    st.markdown('''[Advert space for Google AdSense3]''')
    st.subheader('''Type in box for geographical location:''')
#    st.error('This is an error')
#    options = st.selectbox(' ', [" ",
#                                 "   ",
#                                 "All",
#                                 "Argentina",
#                                 "Austria",
#                                 "Brazil",
#                                 "Canada",
#                                 "Chicago",
#                                 "Denmark",
#                                 "Edinburgh",
#                                 "Europe",
#                                 "France",
#                                 "Germany",
#                                 "Hawaii",
#                                 "Ireland",
#                                 "Italy",
#                                 "Japan",
#                                 "London",
#                                 "Netherlands",
#                                 "New York City",
#                                 "North America",
#                                 "Paris",
#                                 "Poland",
#                                 "South America",
#                                 "Sweden",
#                                 "Switzerland",
#                                 "UK",
#                                 "United Kingdom",
#                                 "USA",
#                                 "World",
#                                 ])
    
    
 #   st.subheader('To travel through history - use the red dot slider:')

    options1 = st.text_input('','World')
#    st.write('Map zoomed to:', options1)
    Year = st.slider('Use the red dot slider to travel back in time:', 1560, 2020, value=2020)
    
    df1 = pd.read_csv('/Users/alastairhayes/desktop/Eponyms/Eponyms4python_Lite.csv',dtype={'PMID':str,'Year':int})
    df2 = df1.sort_values(by=['Year'],ascending=True)
    mapbox_access_token = open("/Users/alastairhayes/desktop/Eponyms/ajhayes83_1.mapbox_token").read()  
    df3 = df2.sort_values(by=['CountryOfEponym_A1'],ascending=True)  #Gives eponyms by operation alphabetically
    dfT = df3.sort_values(by=['Year'],ascending=True)
    time_df = dfT.loc[dfT['Year'] <= Year]
    site_lat = time_df['Lat_A1']            #df3['Lat_A1']                
    site_lon = time_df['Long_A1']           #df3['Long_A1']
    text = time_df['Eponym_easy'] + ', ' + time_df['CityOfEponym_A1'] + ', ' + time_df['Year'].astype(str)
    locations_name = time_df['Eponym_easy'] #df3['Eponym_easy']

    if   options1 == " ":              lat_country  = 25.0;  lon_country  =8.0;    zoom_country = 1.08;  markersize = 12
    if   options1 == "london":         lat_country  = 51.52; lon_country  = -0.1; zoom_country = 9.8; markersize = 18
    if   options1 == "london":         lat_country  = 51.52; lon_country  = -0.1; zoom_country = 9.8; markersize = 18
    if   options1 == "Paris":          lat_country  = 48.85; lon_country  = 2.36;   zoom_country = 10.4; markersize = 18

    if   options1 == "World":          lat_country  = 25.0;  lon_country  =8.0;    zoom_country = 1.08;  markersize = 12
    if   options1 == "All":            lat_country  = 25.0;  lon_country  =8.0;    zoom_country = 1.08;  markersize = 12
    if   options1 == "Europe":         lat_country  = 54.0;  lon_country  = 10.0;   zoom_country = 2.85; markersize = 12
    if   options1 == "Austria":        lat_country  = 47.2;  lon_country  = 13.4;   zoom_country = 6.5; markersize = 16
    if   options1 == "Denmark":        lat_country  = 56.0;  lon_country  = 9.8;    zoom_country = 4.0; markersize = 16
    if   options1 == "France":         lat_country  = 47.0;  lon_country  = 4.0;    zoom_country = 4.5; markersize = 16
    if   options1 == "Germany":        lat_country  = 51.25;  lon_country  = 10.5;   zoom_country = 5.2; markersize = 16
    if   options1 == "Ireland":        lat_country  = 53.5;  lon_country  = -6.2;   zoom_country = 5.0; markersize = 16
    if   options1 == "Italy":          lat_country  = 41.5;  lon_country  = 14.0;   zoom_country = 4.0; markersize = 16
    if   options1 == "Japan":          lat_country  = 37.4;  lon_country  = 135.0;  zoom_country = 4.4; markersize = 16
    if   options1 == "Netherlands":    lat_country  = 52.0;  lon_country  =  5.0;   zoom_country = 4.8; markersize = 16
    if   options1 == "Poland":         lat_country  = 52.0;  lon_country  = 19.0;   zoom_country = 4.0; markersize = 16
    if   options1 == "Sweden":         lat_country  = 62.5;  lon_country  = 18.5;   zoom_country = 3.0; markersize = 16
    if   options1 == "Switzerland":    lat_country  = 47.0;  lon_country  =  8.0;   zoom_country = 4.5; markersize = 16
    if   options1 == "UK":             lat_country  = 53.0;  lon_country  = -3.2; zoom_country = 3.8; markersize = 18
    if   options1 == "Edinburgh":      lat_country  = 55.8;  lon_country  = -3.2;   zoom_country = 6.8; markersize = 18
    if   options1 == "London":         lat_country  = 51.52; lon_country  = -0.1; zoom_country = 9.8; markersize = 18
    if   options1 == "North America":  lat_country  = 52.0;  lon_country  = -100;   zoom_country = 1.8; markersize = 10
    if   options1 == "Canada":         lat_country  = 59.0;  lon_country  = -95.0;  zoom_country = 2.5; markersize = 16
    if   options1 == "USA":            lat_country  = 37.0;  lon_country  = -113;   zoom_country = 2.9; markersize = 16
    if   options1 == "Chicago":        lat_country  = 42.0;  lon_country  = -88.0;  zoom_country = 8.0; markersize = 18
    if   options1 == "New York":       lat_country  = 40.8;  lon_country  = -73.9;  zoom_country = 9.8; markersize = 18
    if   options1 == "Hawaii":         lat_country  = 20.5;  lon_country  = -157.4; zoom_country = 6.1; markersize = 18
    if   options1 == "South America":  lat_country  =-28.0;  lon_country  = -65.0;  zoom_country = 1.8; markersize = 12
    if   options1 == "Argentina":      lat_country  =-40.0;  lon_country  = -65.0;  zoom_country = 2.5; markersize = 16
    if   options1 == "Brazil":         lat_country  =-10.0;  lon_country  = -55.0;  zoom_country = 3.0; markersize = 16

    st.markdown(
        """
        <style type="text/css" media="screen">
        .hovertext text {
        font-size: 20px !important;}
        </style>
        """
        ,
        unsafe_allow_html=True,
    )


    fig3 = go.Figure()
    fig3.add_trace(go.Scattermapbox(
            lat=site_lat,
            lon=site_lon,
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=markersize,
                color='yellow', #'rgb(255, 0, 0)',
                opacity=0.7
            ),
            text=text,
            hoverinfo='text',
        ))

    fig3.update_layout(
        autosize=True,
        hovermode='closest',
        showlegend=False,
        width=850,
        height=570,
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(lat=lat_country,lon=lon_country),
            pitch=0,
            zoom=zoom_country,
            style='satellite-streets'), #'dark'
    )
    fig3.update_layout(margin=dict(l=2, r=2, t=0, b=0))
    st.write(fig3)
    st.write('''To **zoom in**: first click on the map then use **=** key. Use **-** key to pan out.''')

    df4 = df3.sort_values(by=['Eponym'],ascending=True)
    Geo_options = st.selectbox('', df4['Eponym_easy'].unique())

#'open-street-map','white-bg','carto-positron','carto-darkmatter','stamen- terrain','stamen-watercolor', 'basic', 'streets',
    #'outdoors', 'light', 'dark',
    #'satellite', 'satellite-streets'


#----------------------------------------------------------------------------------------------#
#                                                                                              #
#  Journals (4)                                                                                 #
# ::: Handles                                                                                  #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#

def exp_journals():
    st.markdown(
        """
        <style type="text/css" media="screen">
        div[role="listbox"] ul {height:350px}
        </style>
        """
        ,
        unsafe_allow_html=True,
    )
    st.markdown('''[Advert space for Google AdSense4]''')
    st.subheader('''Select a journal to explore related eponyms:''')
    st.write('''**Zoom in** by clicking on journal name. **Zoom out** by clicking the center of the circle.''')
    st.sidebar.markdown("---")
    
    dfY = pd.read_csv('/Users/alastairhayes/desktop/Eponyms/Eponyms4python_Lite4Journals.csv')
    dfY1 = dfY.dropna()
    dfY1["JOURNALS"] = "JOURNALS"
    figZ = px.sunburst(dfY1, path=['JOURNALS', 'journal', 'year', 'eponym'],
                      values='Log10 Google hits',
                      color='Log2 Google hits',
                      hover_data=['eponym'],
                      color_continuous_scale='RdBu', #inferno,thermal,Magma,Cividis,deep,Viridis,icefire,ylgnbu,'portland','agsunset'
                      width=1000, height=900,
                    )
    figZ.update_layout(margin=dict(l=0, r=0, t=0, b=0))
    figZ.update_traces(hovertemplate=None, hoverinfo='skip')
    st.write(figZ)
    
    st.subheader('''For details, find eponym of interest:''')
    dfY2 = dfY1.sort_values(by=['eponym'],ascending=True)
    Journ_options = st.selectbox('', dfY2['eponym'].unique())

    Journ_options2_info = df2[df2['Eponym'].str.match(Journ_options)]

    if not Journ_options2_info['Who'].isnull().all():
        st.write('**_Who_**:', Journ_options2_info['Who'].to_string(index=False))
            
    if not Journ_options2_info['Year'].isnull().all():
        st.write('**_When_**:', Journ_options2_info['Year'].to_string(index=False))

    if not Journ_options2_info['Where'].isnull().all():
        st.write('**_Where_**:', Journ_options2_info['Where'].to_string(index=False))

    ref_link = Journ_options2_info['Reference'].to_string(index=False)
    if not Journ_options2_info['Reference'].isnull().all():
        st.markdown(f"[Link to primary paper]({ref_link})")
        st.markdown("---")
    
    description = Journ_options2_info['Description'].to_string(index=False)
    history = Journ_options2_info['History'].to_string(index=False)
    if not Journ_options2_info['Description'].isnull().all():
        st.write('**_Description_**:', description)
    if not Journ_options2_info['History'].isnull().all():
        st.write('**_History_**:', history)
        st.markdown("---")

 #   if not 

    wiki_link = Journ_options2_info['Wiki_link'].to_string(index=False)
    if not Journ_options2_info['Wiki_link'].isnull().all():
        st.write('**External links**')
        st.markdown(f"[Link to Wikipedia webpage]({wiki_link})")

    wni_link = Journ_options2_info['WNI_link'].to_string(index=False)
    if not Journ_options2_info['WNI_link'].isnull().all():
        st.markdown(f"[Link to Whonamedit webpage]({wni_link})")

    icd_link = Journ_options2_info['ICD11_link'].to_string(index=False)
    if not Journ_options2_info['ICD11_link'].isnull().all():
        st.markdown(f"[Link to ICD-11 webpage]({icd_link})")


#----------------------------------------------------------------------------------------------#
#                                                                                              #
#  People (5)                                                                                  #
# ::: Handles the                                                                              #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#

def exp_people():
    st.markdown(
        """
        <style type="text/css" media="screen">
        div[role="listbox"] ul {height:300px}
        </style>
        """
        ,
        unsafe_allow_html=True,
    )
    st.markdown('''[Advert space for Google AdSense5]''')
    st.subheader('''Choose person to find related eponyms:''')
    st.sidebar.markdown("---")

    #Data read and arrange
    dfY = pd.read_csv('/Users/alastairhayes/desktop/Eponyms/Eponyms4python_Lite4People.csv', dtype={'PMID':str,'Year':str})
    dfY1 = dfY.sort_values(by=['Surname'],ascending=True)
    options = st.selectbox('', dfY1['Who'].unique(),
                           format_func=lambda x: ' ' if x == '1' else x) #use '1's for first row in CSV file to create empty row
    df_ep_info = dfY1[dfY1['Who'].str.match(options)]

    if options == "Charles Dettie Aaron":
        image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Charles_Dettie_Aaron.png'
        st.image(image, width=200)

    if options == "Oscar Huntington Allis":
        image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Oscar_Huntington_Allis.jpg'
        st.image(image, width=200)

    if options == "Philip R Allison":
        image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Philip_Rowland_Allison.png'
        st.image(image, width=200)

    if options == "William A Altemeier":
        image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/William_A_Altemeier.png'
        st.image(image, width=200)

    if options == "Alfredo Alvarado":
        image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Alfredo_Alvarado.png'
        st.image(image, width=200)

    if options == "Claudius Amyand":
        image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Claudius_Amyand.png'
        st.image(image, width=200)
        
    if options == "Norman Rupert Barrett":
        image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Norman_Rupert_Barrett.png'
        st.image(image, width=200)

    if options == "Emil Theodor Kocher":
        image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Emil_Theodor_Kocher.png'
        st.image(image, width=200)

#    if options == "  ":
#        image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/    .png'
#        st.image(image, width=200)

#    if options == "  ":
#        image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/    .png'
#        st.image(image, width=200)

#    if options == "  ":
#        image =
#        st.image(image, width=200)

#    if options == "  ":
#        image =
#        st.image(image, width=200)

#    if options == "  ":
#        image =
#        st.image(image, width=200)

#    if options == "  ":
#        image =
#        st.image(image, width=200)

#    if options == "  ":
#        image =
#        st.image(image, width=200)

#    if options == "  ":
#        image =
#        st.image(image, width=200)

#    if options == "  ":
#        image =
#        st.image(image, width=200)

#    if options == "  ":
#        image =
#        st.image(image, width=200)


    if options == "Edoardo Bassini":
        image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Edoardo_Bassini_Wellcome.jpg'
        st.image(image, width=200)

    if options == "Henri A C A Hartmann":
        image = '/Users/alastairhayes/Desktop/Eponyms/Pics/People/Henri_Hartmann_1920.jpg'
        st.image(image, width=200)
                    #caption=Instrum_options2

#----------------------------------------------------------------------------------------------#
#                                                                                              #
#  Year (6) -                                                                                  #
# :::                                                                                          #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#

def exp_year():
    st.markdown('''[Advert space for Google AdSense6]''')
    st.subheader('''Eponyms by year of origin''')
    st.sidebar.markdown("---")
#    st.write('Eponyms in the year:', Year)

    df1 = pd.read_csv('/Users/alastairhayes/desktop/Eponyms/Eponyms4python_Lite.csv',dtype={'PMID':str,'Year':int})
    df2 = df1.sort_values(by=['Year'],ascending=True)
    mapbox_access_token = open("/Users/alastairhayes/desktop/Eponyms/ajhayes83_1.mapbox_token").read()  
    df3 = df2.sort_values(by=['CountryOfEponym_A1'],ascending=True)  #Gives eponyms by operation alphabetically
    dfT = df3.sort_values(by=['Year'],ascending=True)
    Cent = st.selectbox('Century', ('1500 - 1599', '1600 - 1699', '1700 - 1799',
                                    '1800 - 1899', '1900 - 1999', '2000 - now'), index=4)

    if Cent == "1500 - 1599": Year = st.slider('Click red dot and use right and left arrow keys to change the date', 1500, 1599, value=1500)
    if Cent == "1600 - 1699": Year = st.slider('Click red dot and use right and left arrow keys to change the date', 1600, 1699, value=1600)
    if Cent == "1700 - 1799": Year = st.slider('Click red dot and use right and left arrow keys to change the date', 1700, 1799, value=1700)
    if Cent == "1800 - 1899": Year = st.slider('Click red dot and use right and left arrow keys to change the date', 1800, 1899, value=1800)
    if Cent == "1900 - 1999": Year = st.slider('Click red dot and use right and left arrow keys to change the date', 1900, 1999, value=1900)
    if Cent == "2000 - now":  Year = st.slider('Click red dot and use right and left arrow keys to change the date', 2000, 2020, value=2000)
 
    time_df = dfT.loc[dfT['Year'] == Year]
#    st.write(time_df)
    site_lat = time_df['Lat_A1']                           
    site_lon = time_df['Long_A1']       
    text = time_df['Eponym_easy'] + ', ' + time_df['Year'].astype(str)
    locations_name = time_df['Eponym_easy']
    locations = dict(at=site_lat, lon=site_lon)

    fig = go.Figure(
        data=go.Scattergeo(
            lat = site_lat,
            lon = site_lon,
            mode = 'markers+text',
            text = text,
            textposition=time_df['Text_position'],
            textfont=dict(size=15, color='yellow'),
            hoverinfo = 'skip',        
            marker = dict(
                size=8,
                color='yellow',
                opacity=0.8,
                ),
            ))

    fig.update_layout(
        geo = dict(
            scope ='world',
            showland = True,
            landcolor = "rgb(30,30,30)",
            showcountries = True,
            projection = dict(type = 'miller'),
            )
        )
    fig.update_layout(margin=dict(l=0, r=0, t=0, b=0),
                      template="plotly_dark",
                      paper_bgcolor="White",
                      height=500,width=696)                      
    st.write(fig)

#'natural earth','mercator','winkel tripel','kavrayskiy7','miller','robinson','eckert4'
#[str(i).zfill(1) for i in range(1900,2000)]


#----------------------------------------------------------------------------------------------#
#                                                                                              #
#  Exam Favourites (7)                                                                                 #
# ::: Handles                                                                                  #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#

def exp_exam():
    st.markdown(
        """
        <style type="text/css" media="screen">
        div[role="listbox"] ul {height:350px}
        </style>
        """
        ,
        unsafe_allow_html=True,
    )
    st.markdown('''[Advert space for Google AdSense7]''')
    st.subheader("Exam Favourites")
    st.sidebar.markdown("---")   
    
    options = st.selectbox('Choose specialty', df_A2Z['Eponym_easy'], format_func=lambda x: ' ' if x == '1' else x)
    df_ep_info = df2[df2['Eponym_easy'].str.match(options)]

    if not df_ep_info['Who'].isnull().all():
        st.markdown("---")
        st.write('*_Who_*:', df_ep_info['Who'].to_string(index=False))

    ep_yr = df_ep_info['Year'].to_string(index=False)
#    if not df_ep_info['Year'].isnull().all():
#        st.write('*_When_*:', df_ep_info['Year_str'].to_string(index=False))

    if not df_ep_info['Where'].isnull().all():
        st.write('*_Where_*:', df_ep_info['Where'].to_string(index=False))

    
    description = df_ep_info['Description'].to_string(index=False)
    if not df_ep_info['Description'].isnull().all():
        st.write(description)

    history = df_ep_info['History'].to_string(index=False)
    if not df_ep_info['History'].isnull().all():
        st.write('*_History_*:', history)
        st.markdown("---")

 #   st.write('**External links**')

    ref_link = df_ep_info['Reference'].to_string(index=False)
    if not df_ep_info['Reference'].isnull().all():
        st.markdown(f"[Link to primary paper]({ref_link})")

    wiki_link = df_ep_info['Wiki_link'].to_string(index=False)
    if not df_ep_info['Wiki_link'].isnull().all():
        st.markdown(f"[Link to Wikipedia webpage]({wiki_link})")

    tms_link = df_ep_info['TMS_link'].to_string(index=False)
    if not df_ep_info['TMS_link'].isnull().all():
       st.markdown(f"[Link to TeachMeSurgery webpage]({tms_link})")

    wni_link = df_ep_info['WNI_link'].to_string(index=False)
    if not df_ep_info['WNI_link'].isnull().all():
       st.markdown(f"[Link to Whonamedit webpage]({wni_link})")

    icd_link = df_ep_info['ICD11_link'].to_string(index=False)
    if not df_ep_info['ICD11_link'].isnull().all():
       st.markdown(f"[Link to ICD-11 webpage]({icd_link})")

    epictionary_link = df_ep_info['Eponymictionary'].to_string(index=False)
    if not df_ep_info['Eponymictionary'].isnull().all():
       st.markdown(f"[Link to Eponymictionary]({epictionary_link})")


    
#----------------------------------------------------------------------------------------------#
#                                                                                              #
#  A - Z (8)                                                                                 #
# ::: Handles                                                                                  #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#

def exp_A2Z():
    st.markdown(
        """
        <style type="text/css" media="screen">
        div[role="listbox"] ul {height:350px}
        </style>
        """
        ,
        unsafe_allow_html=True,
    )
    st.markdown('''[Advert space for Google AdSense8]''')
    st.subheader("Eponyms A - Z:")
    st.sidebar.markdown("---")   
    
    options = st.selectbox('Begin typing here', df_A2Z['Eponym_easy'], format_func=lambda x: ' ' if x == '1' else x)
    df_ep_info = df2[df2['Eponym_easy'].str.match(options)]

    if not df_ep_info['Who'].isnull().all():
        st.markdown("---")
        st.write('*_Who_*:', df_ep_info['Who'].to_string(index=False))

    ep_yr = df_ep_info['Year'].to_string(index=False)
    if not df_ep_info['Year'].isnull().all():
        st.write('*_When_*:', df_ep_info['Year'].to_string(index=False))

    if not df_ep_info['Where'].isnull().all():
        st.write('*_Where_*:', df_ep_info['Where'].to_string(index=False))

    
    description = df_ep_info['Description'].to_string(index=False)
    if not df_ep_info['Description'].isnull().all():
        st.write(description)

    history = df_ep_info['History'].to_string(index=False)
    if not df_ep_info['History'].isnull().all():
        st.write('*_History_*:', history)
        st.markdown("---")

    st.write('**External links**')

    ref_link = df_ep_info['Reference'].to_string(index=False)
    if not df_ep_info['Reference'].isnull().all():
        st.markdown(f"[Link to primary paper]({ref_link})")

    wiki_link = df_ep_info['Wiki_link'].to_string(index=False)
    if not df_ep_info['Wiki_link'].isnull().all():
        st.markdown(f"[Link to Wikipedia webpage]({wiki_link})")

    tms_link = df_ep_info['TMS_link'].to_string(index=False)
    if not df_ep_info['TMS_link'].isnull().all():
       st.markdown(f"[Link to TeachMeSurgery webpage]({tms_link})")

    wni_link = df_ep_info['WNI_link'].to_string(index=False)
    if not df_ep_info['WNI_link'].isnull().all():
       st.markdown(f"[Link to Whonamedit webpage]({wni_link})")

    icd_link = df_ep_info['ICD11_link'].to_string(index=False)
    if not df_ep_info['ICD11_link'].isnull().all():
       st.markdown(f"[Link to ICD-11 webpage]({icd_link})")

    epictionary_link = df_ep_info['Eponymictionary'].to_string(index=False)
    if not df_ep_info['Eponymictionary'].isnull().all():
       st.markdown(f"[Link to Eponymictionary]({epictionary_link})")


#-----------------------------------------------------------------------------------------------#
@st.cache
def load_data():
    df = pd.read_csv('/Users/alastairhayes/desktop/Eponyms/Eponyms4python.csv',
                  dtype={'Year':str})
    return df

if __name__ == "__main__":
    main()
