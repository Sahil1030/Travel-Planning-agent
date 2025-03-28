# Travel Itinerary Planner

## Overview
The Travel Itinerary Planner is an AI-powered tool designed to create detailed and customized travel plans. It utilizes multiple agents to provide itinerary recommendations, weather forecasts, transportation, accommodation suggestions, and budget-conscious activity planning.

## Features
- **AI-powered Travel Planning:** Generates personalized itineraries based on user input.
- **Multi-Agent System:** Uses different agents for weather, travel, and activity planning.
- **Budget-Friendly Recommendations:** Suggests accommodations, transport, and activities within the specified budget.
- **Real-Time Web Searches:** Fetches the latest events, attractions, and weather conditions.
- **Streamlit UI:** Provides an interactive interface for users to input their trip details.

## Installation
1. Clone the repository:
   ```sh
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```sh
   cd Travel_Itinerary_Planner
   ```
3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up the required API keys in a `.env` file:
   ```sh
   EXA_API_KEY=your_exa_api_key
   GROQ_API_KEY=your_groq_api_key
   ```

## Usage
1. Run the Streamlit application:
   ```sh
   streamlit run app.py
   ```
2. Enter your trip details such as budget, destination, duration, and preferences.
3. Receive a detailed travel plan with activities, accommodations, transport, and weather insights.

## Agents in Use
- **Google Search Agent:** Fetches real-time travel data.
- **Weather Agent:** Provides weather forecasts for the trip duration.
- **Travel & Accommodation Agent:** Suggests transport and hotels based on budget and preference.
- **Itinerary Planning Agent:** Compiles the final travel plan with day-by-day schedules.

## Future Improvements
- Integration with flight and hotel booking APIs.
- Enhanced UI/UX for better user interaction.
- More AI-powered personalization for recommendations.

## Contributing
Feel free to submit issues and pull requests to improve the project.

## License
This project is licensed under the MIT License.

