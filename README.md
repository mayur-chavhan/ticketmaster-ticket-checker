# TechWhale Ticket Checker

TechWhale Ticket Checker is a Streamlit-based web application that allows users to search for and monitor ticket availability for various events using the Ticketmaster API. It features a user-friendly interface with dark mode support and a search history function.

## Features

- Search for events by artist name and date range
- Display event details including venue, date, and ticket price range
- Toggle between light and dark mode
- View search history and related upcoming events
- Responsive design for both desktop and mobile devices

## Prerequisites

- Python 3.7+
- Ticketmaster API key (obtainable from [Ticketmaster Developer Portal](https://developer.ticketmaster.com/))

## Installation

### Local Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/techwhale-ticket-checker.git
   cd techwhale-ticket-checker
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```
   streamlit run main.py
   ```

5. Open your web browser and navigate to `http://localhost:8501`

### Docker Installation

1. Make sure you have Docker and Docker Compose installed on your system.

2. Clone the repository:
   ```
   git clone https://github.com/yourusername/techwhale-ticket-checker.git
   cd techwhale-ticket-checker
   ```

3. Build and run the Docker container:
   ```
   docker-compose up --build
   ```

4. Open your web browser and navigate to `http://localhost:8501`

## Usage

1. Enter your Ticketmaster API key in the sidebar.
2. Input the artist name you want to search for.
3. Select the date range for your search.
4. Click the "Search Tickets" button.
5. View the search results and related upcoming events.
6. Toggle between light and dark mode using the button in the navbar.

## Project Structure

- `main.py`: The main Streamlit application file
- `api_functions.py`: Contains functions for interacting with the Ticketmaster API
- `ui_components.py`: Defines the UI components used in the application
- `search_history.py`: Manages the search history functionality
- `styles.css`: Contains custom CSS styles for the application
- `requirements.txt`: Lists all Python dependencies
- `Dockerfile`: Defines the Docker image for the application
- `docker-compose.yaml`: Configures the Docker container for easy deployment

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing web app framework
- [Ticketmaster](https://developer.ticketmaster.com/) for providing the API

## Contact

Mayur Chavhan - [techwhale.in](https://techwhale.in)

Project Link: [https://github.com/yourusername/techwhale-ticket-checker](https://github.com/yourusername/techwhale-ticket-checker)
```

Now, let's create a `docker-compose.yaml` file for easy Docker deployment:

```yaml
version: '3.8'

services:
  techwhale-ticket-checker:
    build: .
    ports:
      - "8501:8501"
    volumes:
      - .:/app
    environment:
      - STREAMLIT_SERVER_PORT=8501
      - STREAMLIT_SERVER_HOST=0.0.0.0

volumes:
  techwhale-ticket-checker:
```

To use this docker-compose file, you'll need to create a `Dockerfile` in your project root:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["streamlit", "run", "main.py"]
```

Lastly, ensure you have a `requirements.txt` file in your project root with all the necessary dependencies:

```
streamlit
aiohttp
```

These files will allow users to easily set up and run your TechWhale Ticket Checker application using either local installation or Docker. The README provides clear instructions for both methods, along with usage guidelines and project structure information.