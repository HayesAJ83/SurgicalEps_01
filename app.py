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


import streamlit as st
import pandas as pd
import numpy as np


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



#----------------------------------------------------------------------------------------------#
#                                                                                              #
#  Homepage                                                                                    #
# ::: Handles                                                                                  #                                                                                              #
#                                                                                              #
#----------------------------------------------------------------------------------------------#

def show_homepage():
    ''' Home / About page '''

    st.write("Hello Anne! My first webpage live :)")


if __name__ == "__main__":
    main()
