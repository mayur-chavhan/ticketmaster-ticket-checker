import streamlit as st
import asyncio
from api_functions import get_events, get_related_events
from ui_components import render_sidebar, render_event_details, render_footer, render_search_history, render_navbar
from search_history import load_search_history, save_search_history


st.set_page_config(page_title="TechWhale Ticket Checker", page_icon="🎟️", layout="wide")

# Initialize session state for dark mode
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

# Render navbar (which now includes the title)
render_navbar()

# Load custom CSS
with open("styles.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

api_key, start_date, end_date, artist, search_button = render_sidebar()

# Load search history
search_history = load_search_history()

if search_button:
    if not api_key or not artist:
        st.error("Please enter your Ticketmaster API Key and Artist name.")
    else:
        with st.spinner('Searching for tickets...'):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            results = loop.run_until_complete(get_events(api_key, artist, start_date, end_date))

        found_events = False
        for date, data in results:
            if data and '_embedded' in data:
                events = data['_embedded'].get('events', [])
                if events:
                    for event in events:
                        found_events = True
                        render_event_details(event, date)

        if not found_events:
            st.warning(f"No {artist} events found for the selected dates.")
        else:
            # Add search to history
            search_history.append({'artist': artist, 'start_date': str(start_date), 'end_date': str(end_date)})
            save_search_history(search_history)

# Display search history and related events
st.markdown("## Search History and Related Events")
render_search_history(search_history, api_key)

render_footer()

# Apply dark mode if enabled
if st.session_state.dark_mode:
    st.markdown("""
        <style>
        .stApp {
            background-color: #1E1E1E;
            color: #FFFFFF;
        }
        .event-container {
            background-color: #2D2D2D;
            color: #FFFFFF;
        }
        .stSidebar {
            background-color: #2D2D2D;
            color: #FFFFFF;
        }
        .stSidebar .stTextInput>div>div>input {
            color: #FFFFFF;
        }
        .stSidebar .stDateInput>div>div>input {
            color: #FFFFFF;
        }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        .stApp {
            background-color: #FFFFFF;
            color: #000000;
        }
        .event-container {
            background-color: #F0F0F0;
            color: #000000;
        }
        </style>
    """, unsafe_allow_html=True)