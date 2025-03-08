from crewai import Agent
from langchain.chat_models import ChatOpenAI
from crewai_tools import SerperDevTool
import os
from dotenv import load_dotenv
from citationtool import CitationTool
load_dotenv()
SERPER_API_KEY=os.getenv("SERPER_API_KEY")
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
# Define Research Agent
research_agent = Agent(
    role="Researcher",
    goal="Fetch relevant articles, extract key insights, and include source links.",
    backstory="A research AI expert skilled in finding reliable academic sources.",
    tools=[SerperDevTool(api_key=SERPER_API_KEY),CitationTool()],  # Uses Serper API for Google search
    verbose=True,
    llm=ChatOpenAI(model_name="gpt-4", openai_api_key=OPENAI_API_KEY)
)

# Define Summarization Agent
summarization_agent = Agent(
    role="Summarizer",
    goal="Summarize the research findings into key insights",
    backstory="An AI assistant specializing in breaking down complex information into simple summaries.",
    verbose=True,
    llm=ChatOpenAI(model_name="gpt-4",openai_api_key=OPENAI_API_KEY)
)

# Define Report Generator Agent
report_generator_agent = Agent(
    role="Report Writer",
    goal="Generate a structured research report and append references at the end.",
    backstory="An AI-powered writing assistant that ensures research integrity.",
    verbose=True,
    llm=ChatOpenAI(model_name="gpt-4", openai_api_key=OPENAI_API_KEY,max_tokens=7000)
)

