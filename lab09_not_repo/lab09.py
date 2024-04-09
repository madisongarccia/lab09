import pandas as pd
import plotly.express as px
import streamlit as st

st.title('Name Data App')

url = 'https://github.com/esnt/Data/raw/main/Names/popular_names.csv'
df = pd.read_csv(url)

# Expander for where this data came from
with st.expander(label = 'Data Description'):
    st.write("""
        The data used for this website contains 176,924 baby names
        from 1910 until 2021. The dataset contains the following columns:\n
             - name\n
             - sex\n
             - count\n
             - year
""")

tab1, tab2 = st.tabs(['Name Distributions', 'New Names Each Year'])

with tab1:

    name = st.text_input(label ='Enter a name', value = 'John')
    name_df = df[df['name'] == name]

# popover to select which gender to look at
    popover = st.popover("Filter sex")
    pink = popover.checkbox('Show females.', True)
    blue = popover.checkbox('Show males.', True)

    st.header(f'Popularity of \'{name}\' Over Time')

    if pink:
        st.subheader('Female Distribution')
        plot_df = name_df[name_df['sex'] =='F']
        fig_f = px.line(plot_df, x='year', y='n', color_discrete_sequence=['#FFC0CB'],
                        labels={'n':'count'})
        st.plotly_chart(fig_f)
    if blue:
        st.subheader('Male Distribution')
        plot_df = name_df[name_df['sex'] =='M']
        fig_m = px.line(plot_df, x='year', y='n',
                        labels={'n':'count'})
        st.plotly_chart(fig_m)

    with st.sidebar:
        year = st.slider('Choose a year', 1910, 2021)
        st.header(f'Top Names in {year}')
        year_df = df[df['year'] == year]
        girls_names = year_df[year_df.sex=='F'].sort_values('n', ascending=False).head(5)['name']
        boys_names = year_df[year_df.sex=='M'].sort_values('n', ascending=False).head(5)['name']

        top_names = pd.concat([girls_names.reset_index(drop=True), boys_names.reset_index(drop=True)], ignore_index=True, axis=1)
        top_names.columns = ['Girls','Boys']
        top_names.index = [1,2,3,4,5]
        st.dataframe(top_names)


with tab2:
    # how many new names came about each year
    st.header('Choose a year to see which names came about in that year.\n')

    st.write('Hint: Earlier years have more new names\n')
              
    year = st.slider('Select Year', 1910, 2021)

    # filter dataframe to only that year and prior
    year_and_older = df[df['year'] <= year]
    names_prior_years = set(df[df['year'] < year]['name'])

    # check if any name from only that year were not in other years
    only_year = df[df['year'] == year]
    filtered_df = only_year[~only_year['name'].isin(names_prior_years)]

    unique_names = filtered_df['name'].unique()

    st.write(f'New name(s) in {year}:')
    for name in unique_names:
        st.write(f'{name}')
   
    # display those names to the screen






