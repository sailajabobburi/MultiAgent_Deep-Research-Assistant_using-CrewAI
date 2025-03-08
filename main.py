from crewai import Crew
from tasks import create_research_task, create_summarization_task, create_report_task


def run_research_workflow(topic):
    print(f"\n🔍 Researching topic: {topic}")

    # Dynamically create tasks based on the topic
    research_task = create_research_task(topic)
    summarization_task = create_summarization_task(research_task)
    report_task = create_report_task(summarization_task)

    # Define Crew
    research_crew = Crew(
        agents=[research_task.agent, summarization_task.agent, report_task.agent],
        tasks=[research_task, summarization_task, report_task],
        verbose=True
    )

    # Execute workflow
    final_report = research_crew.kickoff()

    print("\n Research Completed. Generated Report:\n")
    print(final_report)


if __name__ == "__main__":
    # You can hardcode a topic or ask for user input
    topic = input("Enter the research topic: ")
    run_research_workflow(topic)

