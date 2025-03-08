from crewai.tools import BaseTool

class CitationTool(BaseTool):
    name: str = "Citation Extractor"
    description: str = "Extracts sources and formats them for research reports."

    def _run(self, extracted_text: str) -> list:
        """
        Extracts sources (URLs) from the given research text.
        Returns a formatted list of citations.
        """
        sources = []
        for line in extracted_text.split("\n"):
            if "http" in line:  # Simple logic to extract URLs
                sources.append(line.strip())

        return sources if sources else ["No sources found."]
