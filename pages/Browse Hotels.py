import streamlit as st
import pandas as pd


st.set_page_config(page_title = "Browse Hotels", page_icon=":heart:", layout = "wide" )
st.title("Browse Hotels")


import streamlit as st
import pandas as pd

# Sample hotel data 
data = {
    'Hotel Name': ['Hotel A', 'Hotel B', 'Hotel C'],
    'Location': ['City X', 'City Y', 'City Z'],
    'Rating': [4.5, 3.8, 4.2],
    'Price': ['$100', '$80', '$120']
}
df = pd.DataFrame(data)

# Function to get reviews for a specific hotel
def get_reviews(hotel_name):
    # function to fetch reviews for a specific hotel
    # replace this with actual code to fetch reviews from a database or API
    
    #need to link this to a database that will constantly update
    reviews_data = {
        'Hotel Name': [hotel_name, hotel_name, hotel_name],
        'Reviewer': ['User1', 'User2', 'User3'],
        'Rating': [4, 5, 3],
        'Comment': ['Great hotel!', 'Enjoyed my stay.', 'Could improve cleanliness.']
    }
    return pd.DataFrame(reviews_data)

# Sidebar search + review submission
st.sidebar.header('Search Hotels')
search_query = st.sidebar.text_input('Enter Hotel Name', '')

st.sidebar.header('Leave a Review')
hotel_review = st.sidebar.selectbox('Select Hotel', df['Hotel Name'])
reviewer_name = st.sidebar.text_input('Your Name', '')
review_rating = st.sidebar.slider('Rating', min_value=1, max_value=5, step=1)
review_comment = st.sidebar.text_area('Comment', '')

if st.sidebar.button('Submit Review'):
    # Save the review to a database or perform other actions
    st.sidebar.success('Review submitted successfully!') #message after review submitted

# Filter hotels based on search query
filtered_df = df[df['Hotel Name'].str.contains(search_query, case=False)]

# Display filtered hotels
st.header('Search Results')
if filtered_df.empty:
    st.warning('No hotels match the search criteria.')
else:
    st.write(filtered_df)

# Display reviews for the selected hotel
if search_query == '':
    st.header('Hotel Reviews')
    reviews_df = get_reviews(hotel_review)
    st.write(reviews_df)



# https://docs.google.com/spreadsheets/d/1iwuQ-7p9HlGKoUhQEYj8HXiuEF4TOi-yxUriyNDLdnQ/edit?usp=sharing
