import streamlit as st
import pandas as pd
import numpy as np
#import os

@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    return df

df = load_data('../data/mega_2024_df.csv')

df['rookie'] = np.where(df['rookie'] == 1, 'Y', 'N')
df['win_prediction'] = np.where(df['win_prediction'] == 1, 'Y', 'N')
df['podium_prediction'] = np.where(df['podium_prediction'] == 1, 'Y', 'N')
df['top10_prediction'] = np.where(df['top10_prediction'] == 1, 'Y', 'N')

if 'code' not in st.session_state:
    st.session_state.code = 'CAR'

#st.image(f'../photos/{st.session_state.code}.jpg')

#st.sidebar.title("F1 Capstone Project")
st.sidebar.header("2024 Season with Predictions")
#st.sidebar.header("Round and Driver Selection")

with st.sidebar:
    
    st.header("Round and Driver Selection")

    circuit_list = df['round_long'].drop_duplicates()
    
    circuit = st.selectbox(
        label="Select round:", 
        options=circuit_list, 
        index=None, 
        placeholder="Select round...",
        disabled=False,
    )

#    st.write(circuit) #used just for troubleshooting during dev
        
    driver_list = df['name'].loc[df['round_long'] == circuit]

#take 1: driver by selecting individual options - want multiselect, I think    
#    driver = st.selectbox(
#        label="Select driver:", 
#        options=driver_list, 
#        index=None, 
#        placeholder="Select driver...", 
#        disabled=False,
#    )

#take2: multiselect
#    driver = st.multiselect(
#        label="Select drivers:",
#        options= driver_list,
#        default=None,
#        placeholder="Select drivers...",
#    )

#is there a way to 'add all'? -YES!
#take3:
    container = st.container()
    all = st.checkbox("Select all")
 
    if all:
        driver = container.multiselect("Select one or more options:",
        driver_list, driver_list)
    else:
        driver =  container.multiselect("Select one or more options:",
        driver_list)

#    st.write(driver) #used just for troubleshooting during dev

df_filtered = df.query(
    "(round_long == @circuit) and (name == @driver)"
)

df_clean = df_filtered[['name',
                        'code',
                        'number',
                        'constructor_name',
                        'rookie',
                        'wins',
                        'YTD_win_pct',
                        'previous_finish',
                        'YTD_avg_finish_pos',
                        'avg_last_4_finishes',
                        'avg_finish_pos_on_circuit',
                        'win_percentage_on_circuit',
                        'top_3_finishes_on_circuit',
                        'career_win_pct',
                        'win_prediction',
                        'podium_prediction',
                        'top10_prediction',
                        'positionOrder'
                        ]]

df_clean = df_clean.rename(columns={'name': 'Driver Name', 
                                    'code': 'Broadcast Code', 
                                    'number': 'Driver Number',
                                    'constructor_name': 'Constructor',
                                    'rookier': 'Rookie?',
                                    'wins': 'Wins YTD',
                                    'YTD_win_pct': 'YTD Win %',
                                    'previous_finish': 'Previous Race Finish',
                                    'YTD_avg_finish_pos': 'YTD Avg Finish Position',
                                    'avg_last_4_finishes': 'Avg of Last 4 Finishes',
                                    'avg_finish_pos_on_circuit': 'Avg Finish Position on Circuit',
                                    'win_percentage_on_circuit': 'Career Win % on Circuit',
                                    'top_3_finishes_on_circuit': 'Career Top 3 Finishes on Circuit',
                                    'career_win_pct': 'Career Win %',
                                    'win_prediction': 'Predicted Win',
                                    'podium_prediction': 'Predicted Podium',
                                    'top10_prediction': 'Predicted Top 10 Finish',
                                    'positionOrder': 'Actual Finish Position'
                                   })

#st.session_state.code = df_filtered['code']
#st.write(st.session_state.code)

#st.image('app/static/CAR.jpg')
image_df = 
st.image('http://localhost:8501/app/static/CAR.jpg')
#st.image(f'../photos/{st.session_state.code}.jpg')

#st.table(df_filtered)
st.dataframe(df_clean,
            hide_index=True,
            )