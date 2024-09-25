import streamlit as st
from datetime import datetime
import asyncio
import aiohttp
from api_functions import get_related_events

def render_navbar():
    col1, col2, col3 = st.columns([3,1,1])
    with col1:
        st.markdown('<h1 class="navbar-title">TechWhale Ticket Checker 🎟️</h1>', unsafe_allow_html=True)
    with col3:
        if st.button('🌓 Toggle Dark Mode'):
            st.session_state.dark_mode = not st.session_state.dark_mode
            st.rerun()

def render_sidebar():
    st.sidebar.markdown('<p class="sidebar-title">Enter Details</p>', unsafe_allow_html=True)
    api_key = st.sidebar.text_input('Enter your Ticketmaster API Key:', type="password")
    artist = st.sidebar.text_input('Enter Artist Name:')
    col1, col2 = st.sidebar.columns(2)
    start_date = col1.date_input('Start Date:', min_value=datetime.now().date())
    end_date = col2.date_input('End Date:', min_value=start_date)
    st.sidebar.markdown('---')
    search_button = st.sidebar.button('Search Tickets 🔍')
    st.sidebar.markdown('---')
    st.sidebar.info('Please enter your Ticketmaster API key, artist name, and select the date range to check for available tickets.')
    return api_key, start_date, end_date, artist, search_button

def render_event_details(event, date):
    with st.container():
        st.markdown(f"<div class='event-container'>", unsafe_allow_html=True)
        st.markdown(f"### {event['name']} on {date.strftime('%B %d, %Y')}")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            if 'images' in event and event['images']:
                st.image(event['images'][0]['url'], width=300)
            else:
                st.info("No image available for this event.")
        
        with col2:
            st.write(f"**Venue:** {event['_embedded']['venues'][0]['name']}")
            if 'priceRanges' in event:
                st.write(f"**Price Range:** £{event['priceRanges'][0]['min']} - £{event['priceRanges'][0]['max']}")
            else:
                st.write("**Price information not available**")
            if 'url' in event:
                st.markdown(f"[**Buy Tickets**]({event['url']})")
        
        st.markdown("</div>", unsafe_allow_html=True)

async def fetch_related_events(api_key, artist):
    async with aiohttp.ClientSession() as session:
        return await get_related_events(session, api_key, artist)

def render_search_history(search_history, api_key):
    for search in reversed(search_history[-5:]):  # Show last 5 searches
        st.markdown(f"**Artist:** {search['artist']}, **Dates:** {search['start_date']} to {search['end_date']}")
        
        # Fetch and display related events
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        related_events = loop.run_until_complete(fetch_related_events(api_key, search['artist']))
        
        if related_events and '_embedded' in related_events:
            st.markdown(f"### Upcoming events for {search['artist']}:")
            for event in related_events['_embedded'].get('events', [])[:3]:  # Show up to 3 related events
                st.markdown(f"- {event['name']} on {event['dates']['start']['localDate']} at {event['_embedded']['venues'][0]['name']}")
        else:
            st.markdown(f"No upcoming events found for {search['artist']}")
        
        st.markdown("---")

def render_footer():
    st.markdown(
        """
        <div class="footer">
            <p>TechWhale Ticket Checker | Created by Mayur Chavhan | <a href="https://techwhale.in" target="_blank">techwhale.in</a></p>
        </div>
        """,
        unsafe_allow_html=True
    )