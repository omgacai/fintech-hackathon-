#lines to run on terminal
#pip install st-gsheets-connection
#pip install streamlit
#pip install pandas
#streamlit run hotel1-sample.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd 

st.set_page_config(page_title = "Hotel1", page_icon=":hotel:" )
st.title("Hotel1")
st.markdown("Leave a review for Hotel1 below")

#establish google sheets connection
conn = st.connection("gsheets", type=GSheetsConnection)
##conn = GSheetsConnection("./.streamlit/secrets.toml")
#conn.connect()

#fetch existing reviews data in pandas dataframe
existing_reviews = conn.read(worksheet = "Sheet1", usecols = list(range(7)))
existing_reviews = existing_reviews.dropna(how = "all") 
#existing_reviews = conn.read(spreadsheet = "https://docs.google.com/spreadsheets/d/1KggYWjLOD0pv-N5sSFqnMdcJZtfrSxZp2x167LocoMU/edit?usp=sharing", usecols = list(range(5)), ttl = 5)

#display review
display_reviews = conn.read(worksheet = "Sheet1", usecols = list(range(5)))
display_reviews = display_reviews.dropna(how = "all") 


def calc_stars(x):     
    headers = list(existing_reviews.columns)

    incen = headers.index('Incen')
    star = headers.index('Stars')

    yes = existing_reviews[existing_reviews['Incen'] == 'yes']
    no = existing_reviews[existing_reviews['Incen'] == 'no']

    no_responses = no[headers[0]].count()
    yes_responses = yes[headers[0]].count()

    sum_yes, sum_no = yes['Stars'].sum(), no['Stars'].sum()

    if sum_yes == 0:
        final = sum_no/no_responses
    elif sum_no == 0:
        final = sum_yes/yes_responses
    else:
        final = sum_yes*(1-x)/yes_responses + sum_no*x/no_responses

    return final

rating = calc_stars(0.75)
st.subheader("current rating: " + str(rating) + "/5 :star:")



#display spreadsheet table
st.dataframe(display_reviews)

with st.container():
    st.write("---")
    st.subheader("leave a review for hotel1 here")

#submit reviews form
with st.form(key="review_form"):
    username = st.text_input(label = "Username*")
    date = st.date_input(label = "Date*")
    time = st.time_input(label = "Time*")
    stars = st.slider("Stars*", 0, 5, 1)
    comment = st.text_input(label = "Comment*")
    incen = st.selectbox("Have you been incentivised to leave a review for this place?",("yes", "no") )
    st.write('You selected:', incen)
    file = st.file_uploader("Upload proof of purchase*")
    submit_button = st.form_submit_button(label="Submit Review")

#mark mandatory fields
st.markdown("**required*")

#if the submit button is pressed
if submit_button:
    #check all mandatory fields
    if not username or not date or not time or not stars or not comment:
        st.warning("Ensure all mandatory fields are filled.")
        st.stop()
    else:
        #create a new row in the spreadsheet
        review = pd.DataFrame(
            [
                {
                    "Username": username,
                    "Date": date.strftime("%Y-%m-%d"),
                    "Time": time,
                    "Stars": stars,
                    "Comment": comment,
                    "Incen": incen,
                    "File": file,
                }
            ]
        )

        #add new review to existing reviews
        updated_df = pd.concat([existing_reviews, review], ignore_index = True)

        #update google sheets
        conn.update(worksheet="Sheet1", data = updated_df)

        st.success("Submitted")
    


#https://docs.google.com/spreadsheets/d/1KggYWjLOD0pv-N5sSFqnMdcJZtfrSxZp2x167LocoMU/edit#gid=0
