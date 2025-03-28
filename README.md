## Git Commit Message (Git Description):

```
feat: Add Travel Itinerary Planner with Multi-Agent Integration

- Implemented a Streamlit-based GUI to collect travel details (budget, people, dates, duration, destination, starting point, purpose, preferences, and notes).
- Integrated multiple phi agents (itinerary, weather, and travel/accommodation) to generate a unified travel itinerary.
- Aggregated agent responses and presented the final plan with sources, booking links, and detailed day-by-day schedules.
- Added demo inputs to guide users in providing required information.
- Enhanced agent instructions to ensure accurate, customized travel plans.

This commit lays the foundation for an AI-powered travel planner that tailors itineraries based on user inputs.
```

---

## README.md

```markdown
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
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *(Ensure that your `requirements.txt` includes phi, exa_py, streamlit, python-dotenv, etc.)*

3. **Configure Environment Variables:**
   - Create a `.env` file in the project root with:
     ```
     EXA_API_KEY=your_exa_api_key_here
     GROQ_API_KEY=your_groq_api_key_here
     ```

## Running the Application

To launch the Streamlit GUI, run:
```bash
streamlit run Traveling_AgentTeam.py
```
This command opens a web interface where you can enter your travel details. Demo inputs are provided by default. Click **Plan My Trip !!!** to generate your customized travel itinerary.

## Project Structure

```
travel-itinerary-planner/
├── Traveling_AgentTeam.py       # Main application code integrating phi agents and Streamlit GUI
├── .env                       # Environment variable file (not tracked in Git)
├── requirements.txt           # List of required Python packages
└── README.md                  # This README file
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Happy traveling, and enjoy planning your next adventure!
```

