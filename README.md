# Travel Itinerary Planner

## Overview

The Travel Itinerary Planner is an AI-powered application that helps users create customized travel plans. Using a multi-agent system built on the phi framework and Streamlit for the GUI, the application aggregates information from specialized agents (itinerary, weather, and travel/accommodation) to generate a detailed, day-by-day travel plan. The system tailors recommendations based on user inputs such as budget, number of people, travel dates, duration, destination, starting location, travel purpose, preferences, and additional notes.

## Features

- **Multi-Agent Integration:** Combines responses from itinerary, weather, and travel/accommodation agents.
- **Dynamic Itinerary Generation:** Produces detailed daily schedules including transportation options, accommodations, activities, and weather forecasts.
- **Demo Inputs:** Pre-filled input fields for an enhanced user experience and easier testing.
- **Streamlit GUI:** A user-friendly interface to input travel details and view the generated itinerary.
- **Accurate and Customized:** Agents retrieve data from reputable sources and include booking links, estimated costs, and source references.

## Requirements

- Python 3.7+
- [phi](https://github.com/your-org/phi) library (for agent management)
- [exa_py](https://github.com/your-org/exa_py) library (for travel data extraction)
- [Streamlit](https://streamlit.io/)
- Environment variables:
  - `EXA_API_KEY`
  - `GROQ_API_KEY`

## Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/travel-itinerary-planner.git
   cd travel-itinerary-planner
