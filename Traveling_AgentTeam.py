from phi.agent import Agent ,RunResponse
# from phi.run.response import RunResponse
from phi.tools.googlesearch import GoogleSearch
from phi.utils.pprint import pprint_run_response
from phi.model.groq import Groq
from exa_py import Exa
import streamlit as st
from phi.tools.exa import ExaTools
import os
from dotenv import load_dotenv , find_dotenv
load_dotenv(find_dotenv())
exa = Exa(os.getenv('EXA_API_KEY'))
api_key1 = os.getenv('GROQ_API_KEY')

ggl_agent = Agent(
    tools=[GoogleSearch()],
    model=Groq(id="deepseek-r1-distill-llama-70b",
               api_key=api_key1),
    description="You are an expert itinerary planning agent. Your role is to assist users in creating detailed, customized travel plans tailored to their preferences and needs.",
    instructions=[
                "Collect information on travels,weather conditions, accommodations (count for all given days by user and make sure to keep it in budget and give at-least name of some hotels / dharamshala),  activity recommendations (e.g., sightseeing,must visit sites, latest happening events [search from online]), attractions, and estimated costs from these sources of given days.",
        "Ensure that the gathered data is accurate and tailored to the user's preferences, such as destination,purpose and preference of user ",
    ],
    show_tool_calls=True,
    debug_mode=True,
)
weather_agent = Agent(
    tools=[GoogleSearch()],
    model=Groq(id="deepseek-r1-distill-llama-70b",
               api_key=api_key1),
    description="You are an expert Weather reporter. Your role is to check weather of given destination at given dates by the user and plan the extras of trip ",
    instructions=[
        "Collect information on weather condition of given location and destination keep track of temperature , wind , humidity ,etc",
        "Ensure to use the weather data and send to other llm for them to curate the plane of trip accordingly ",
        "if there is some unforeseen natural conditions or harsh climate warn the user accordingly"
        "Ensure that the gathered data is accurate and reliable",
    ],
    show_tool_calls=True,
    debug_mode=True,
)

travel_accommodation_agent = Agent(
    name="Globe Hopper",
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    tools=[ExaTools()],
    markdown=True,
    description="You are an expert Travel planning agent. Your role is to assist users in creating detailed customized flight travel plans or cab or trains tailored and recommend flights and hotels for given location and destination",
    instructions=[
        "Use Exa to search and extract relevant data from reputable travel platforms. Give alternatives Traveling accommodation",
        "Collect travel information based on user's destination, purpose, and budget. Ensure recommendations are customized to user preferences (e.g., adventure, family-friendly, luxury, budget travel). Provide specific names and links for hotels and flights.",
        "Collect information on flights , cabs and accommodations and estimated costs from these sources.",
        "Create a clear and concise itinerary that includes: detailed travel plan, suggested transportation and accommodation options and an estimated cost breakdown (covering transportation, accommodation, food, and activities).",
        "If a particular website or travel option is unavailable, provide alternatives from other trusted sources.",
        "Do include direct links to external websites or booking platforms in the response."
    ],
)
agent_team = Agent(
    model=Groq(id="deepseek-r1-distill-llama-70b",
               api_key=api_key1),
    team=[weather_agent , ggl_agent , travel_accommodation_agent],
    instructions=[
        "Use all the agents at your dispose to get response and tailor it together",
        "Ensure to keep things in budget",
        "Always include sources",   "Create a detailed itinerary that includes: detailed day-by-day activity , weather  conditions, events , travel plan, suggested transportation and accommodation options with prices and booking sources, an estimated cost breakdown (covering transportation, accommodation[for all given days] and food).",
        "If a particular website or travel option is unavailable, provide alternatives from other trusted sources.",
        "Show web results and weblinks and give source of booking and details"],
    show_tool_calls=True,
    markdown=True,
)


# agent_team.print_response("I want to have 2 days tour in ahmedabad from 28 March 2025 to 30 March 2025 with budget of Rs. 6000 and i am expecting some great memories from this trip with lots of events", stream=True)
# agent_team.print_response("I want to have 3 days honeymoon tour with my wife in ahmedabad from 28 March 2025 to 30 March 2025 with budget of Rs. 10000 and i am expecting some great memories from this trip with lots of memories", stream=True)
# agent_team.print_response("I want to have 2 days trip from ahmedabad to taranga hills from 28 March 2025 to 30 March 2025 with budget of Rs. 3000 and i wish stay in dharamshala and explore hills as well as temples too and also want to relax from stressed life", stream=True)
#
# budget = input("Enter your budget")
# people = input("number of people")
# dates = input("Enter the dates ")
# duration = input("Trip duration in days")
# destination = input("Enter your destination to travel")
# starting = input("Enter your starting destination ")
# purpose = input("Enter your purpose of travel ")
# preference = input("What are you expecting from this trip or reasons to do this trip")
# agent_team.print_response(    f"I want you to plan a trip the {duration} days from {starting} to {destination} from {dates} with budget of Rs. {budget} with in mind purpose of {purpose} and i have some preference {preference} take care of my transportation and activities", stream=True)
# Collecting user inputs
# budget = input("Enter your budget: ")
# people = input("Number of people: ")
# dates = input("Enter the dates: ")
# duration = input("Trip duration in days: ")
# destination = input("Enter your destination to travel: ")
# starting = input("Enter your starting destination: ")
# purpose = input("Enter your purpose of travel: ")
# preference = input("What are you expecting from this trip or reasons to do this trip:  (e.g.,'Hidden Gems').  ")
# Note = input("Enter something to be noted or taken in consideration about eg: (Dietary preferences, Specific interests within the given preferences ,Accommodation preferences (luxury, budget, central location, etc.))")
# # Construct the prompt for the agent
# print(f"this is note {Note}")
# prompt = (
#     f"Plan a trip for {duration} days from {starting} to {destination} starting on {dates}. "
#     f"The budget is Rs. {budget} for {people} people. "
#     f"The purpose of travel is '{purpose}', and the traveler is expecting '{preference}'. "
#     f"Make sure to follow and  use this information to curate the travel trip without fail:{Note}  "
#     "Ensure the itinerary covers transportation options, accommodation, activities and weather forecasts . "
#     "make sure to keep preferences and needs in mind when creating plans"
#     "Tailor the plan to fit the budget and preferences, including detailed daily schedules with relevant sources and booking links."
# )

# Pass the constructed prompt to the agent team for processing
# agent_team.print_response(prompt, stream=True)

st.title("Travel Itinerary Planner")
st.write("Enter your travel details below to generate a customized itinerary.")

st.subheader("Demo Inputs")
st.write("The following demo values are pre-filled. You can modify them as needed.")

# Collect user inputs with demo default values
budget = st.text_input("Enter your budget (Rs):", value="7000")
people = st.text_input("Number of people to travel with:", value="2")
dates = st.date_input("Enter the dates (e.g., 28 March to 31 March):")
duration = st.text_input("Trip duration in days:", value="3")

destination = st.text_input("Enter your destination to travel:", value="Rajasthan")
starting = st.text_input("Enter your starting destination:", value="Ahmedabad")
purpose = st.text_input("Enter your purpose of travel:", value="enjoying with friends")
preference = st.text_input("What are your Preference or purpose or expectations for this trip?  (e.g.,'Hidden Gems')",
                           value="Cultural exploration, sightseeing, and finding hidden gem")
Notes = st.text_input(
    "Enter something to be noted or taken in consideration about eg: (Dietary preferences, Specific interests within the given preferences ,Accommodation preferences (luxury, budget, central location, etc.))",
    value="I am person with less mobility make sure to use this information to curate the travel trip")

if st.button("Plan My Trip !!!"):
    # Construct a concise prompt incorporating user inputs
    prompt = (
        f"Plan a trip for {duration} days from {starting} to {destination} starting on {dates}. "
        f"The budget is Rs. {budget} for {people} people. "
        f"The purpose of travel is '{purpose}', and the traveler is expecting '{preference}'. "
        f"Make sure to follow and  use this information to curate the travel trip without fail:{Notes}  "
        "Ensure the itinerary covers transportation options, accommodation, activities, and weather forecasts. "
        "Tailor the plan to fit the budget and preferences, including detailed daily schedules with relevant sources and booking links."
    )

    st.write("Generating itinerary... (It may takes upto 30-40 seconds at-least ⌛ please be patient)")
    # Get the aggregated itinerary from the agent team
    response: RunResponse =agent_team.run(prompt)
    pprint_run_response(response, markdown=True)
    st.write(response.content )

    # st.text_area("Your Customized Itinerary Travel plan is ready Enjoy Your Trip!!!", value=itinerary, height=400)
