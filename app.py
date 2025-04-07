from praisonaiagents import Agent, Agents, MCP
import os
from dotenv import load_dotenv
load_dotenv()
api_key=os.getenv("GROQ_API_KEY")
brave_api=os.getenv("BRAVE_API_KEY")

research_agent= Agent(
    instructions="Research about travel destinations, attractions, local customs and travel requirements.",
    llm="groq/meta-llama/llama-4-scout-17b-16e-instruct",
    tools=MCP("npx -y @modelcontextprotocol/server-brave-search",env={"BRAVE_API_KEY":brave_api})
)
flight_agent=Agent(
    instructions="Search for available flights, compare prices and recommend optimal flight choices",
    llm="groq/meta-llama/llama-4-scout-17b-16e-instruct",
    tools=MCP("npm -y @modelcontextprotocol/server-brave-search",env={"BRAVE_API_KEY": brave_api})
)
hotel_agent=Agent(
    instructions="Research hotel and accomodations based on budget and preferences",
    llm="groq/meta-llama/llama-4-scout-17b-16e-instruct",
    tools=MCP("npm -y @modelcontextprotocol/server-brave-search",env={"BRAVE_API_KEY": brave_api})
)

planning_agent=Agent(
    instructions="Design detailed day-by-day travel plans incorporating activities,transport and rest times",
    llm="groq/meta-llama/llama-4-scout-17b-16e-instruct",
    tools=MCP("npm -y @modelcontextprotocol/server-brave-search",env={"BRAVE_API_KEY": brave_api})
)

destination="Delhi,India"
dates="May 1-10th 2025"
budget="Low budget(15000-20000 INR)"
preferences="Historical sites, local cuisine, avoiding crowded tourist traps"
travel_query=f"What are the best attractions to visit in {destination} during {dates} on a budget of {budget} with preferences od {preferences}"
agents =  Agents(agents=[research_agent,planning_agent,flight_agent,hotel_agent,planning_agent])
result = agents.start(travel_query)
print(f"\n=== DESTINATION RESEARCH: {destination} ====\n")
print(result)
#research_agent.start("What are the best attractions to visit in Delhi, India. During May 1-20th, 2025 on a budget of 20K INR")