# Multi-Agent Deep Research Assistant using CrewAI

This project implements a **multi-agent research assistant** leveraging the [CrewAI](https://github.com/crewAIInc/crewAI) framework. The assistant automates the process of researching a given topic by orchestrating multiple AI agents to gather information, summarize findings, and generate comprehensive reports. Additionally, this project includes a **custom citation tool** to properly format and retrieve references for research outputs.

## Features

- **Multi-Agent Collaboration**: Multiple AI agents work together to conduct research, summarize findings, and generate reports.
- **Custom Citation Tool**: A custom CrewAI-based tool specifically designed to extract, generate, and format citations from various sources.
- **Comprehensive Reporting**: The system produces detailed reports with properly formatted citations and references.

## Agents Used in the Research Workflow

This project uses multiple CrewAI **agents**, each assigned a specific task in the research pipeline:

1. **Research Agent**:
   - Gathers data and insights from multiple sources.
   - Uses web search and document parsing tools to extract relevant content.

2. **Summarization Agent**:
   - Processes the raw research findings and condenses them into structured summaries.
   - Ensures coherence and readability of the research content.

3. **Report Generation Agent**:
   - Compiles the structured summaries into a final research report.
   - Organizes the content into sections like introduction, findings, and conclusion.

4. **Citation Generation Agent** (Custom Tool):
   - Extracts citation data from research sources.
   - Formats citations correctly based on research standards (APA, MLA, etc.).
   - Ensures all references used in the research report are correctly attributed.

## Custom Citation Tool

A **CrewAI-based citation generation tool** has been developed(by extending the CrewAI BaseTool) to automate the process of handling research citations. This tool performs the following:

- **Automatic Citation Extraction**: Extracts citation data from web sources, PDFs, and online research articles.
- **Formatted Citation Generation**: Converts raw citation data into properly formatted references (APA, MLA, Chicago, etc.).
- **Seamless Integration with Research Workflow**: The citation tool interacts with other agents to ensure that all referenced materials are included in the final report.

This ensures that the **generated research reports are well-referenced and credible**.

## Installation

### **1. Clone the Repository**

```bash
git clone https://github.com/sailajabobburi/MultiAgent_Deep-Research-Assistant_using-CrewAI.git
cd MultiAgent_Deep-Research-Assistant_using-CrewAI
```

### **2. Set Up a Virtual Environment** (Optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3. Install Dependencies**

```bash
pip install -r requirements.txt
```

## Usage

### **Run the Research Workflow**

Execute the main research pipeline:

```bash
python main.py
```

### **Interact with the Research Assistant**

- Enter a research topic when prompted.
- The agents will collaboratively generate a research report.
- Citations will be automatically extracted and formatted.
- The final report will be displayed in the terminal.

## Project Structure

- `agents.py`: Defines the AI agents and their roles.
- `tasks.py`: Contains task definitions and the logic for task execution.
- `main.py`: Executes the research workflow by coordinating agents and tasks.
- `citation_tool.py`: Implements the custom citation generation tool.

## Acknowledgments

- [CrewAI](https://github.com/crewAIInc/crewAI) for enabling multi-agent collaboration.



