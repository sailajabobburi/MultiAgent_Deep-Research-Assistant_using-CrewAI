from crewai import Task
from agents import research_agent, summarization_agent, report_generator_agent

def create_research_task(topic):
    return Task(
        description=f"Search the web for '{topic}', extract key insights, and store the source links.",
        expected_output="A structured list of research insights with citations (source URLs).",
        agent=research_agent
    )

def create_summarization_task(researchtask):
    return Task(
        description="Summarize the findings from the research agent into concise points.",
        expected_output="A summarized version of the research, highlighting key takeaways.",
        agent=summarization_agent
    )

def create_report_task(summarization_task):
    return Task(
        description="Format the summarized insights into a structured research report, and add citations at the end.",
        expected_output="A well-structured research report with references.",
        agent=report_generator_agent
    )

