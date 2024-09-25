import asyncio
import aiohttp
from datetime import timedelta, datetime

async def fetch_event(session, api_key, artist, date):
    BASE_URL = 'https://app.ticketmaster.com/discovery/v2/events.json'
    params = {
        'apikey': api_key,
        'keyword': artist,
        'startDateTime': f"{date}T00:00:00Z",
        'endDateTime': f"{date}T23:59:59Z"
    }
    async with session.get(BASE_URL, params=params) as response:
        if response.status == 200:
            return await response.json()
        else:
            return None

async def get_events(api_key, artist, start_date, end_date):
    dates = [start_date + timedelta(days=x) for x in range((end_date-start_date).days + 1)]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_event(session, api_key, artist, date) for date in dates]
        results = await asyncio.gather(*tasks)
    return list(zip(dates, results))

async def get_related_events(session, api_key, artist):
    BASE_URL = 'https://app.ticketmaster.com/discovery/v2/events.json'
    params = {
        'apikey': api_key,
        'keyword': artist,
        'startDateTime': datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
        'size': 5  # Limit to 5 related events
    }
    async with session.get(BASE_URL, params=params) as response:
        if response.status == 200:
            return await response.json()
        else:
            return None