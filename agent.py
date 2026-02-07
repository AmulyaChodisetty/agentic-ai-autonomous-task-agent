from datetime import datetime
from memory import AgentMemory
from tools import PaperSearchTool, SummarizationTool, StorageTool


class AgenticAI:
    """
    Planner + Executor Agent
    """

    def __init__(self):
        self.memory = AgentMemory()
        self.search_tool = PaperSearchTool()
        self.summarizer = SummarizationTool()
        self.storage_tool = StorageTool()

    def plan(self, goal):
        """
        Task decomposition
        """
        return [
            "Search for recent AI research papers on agriculture",
            "Select top 3 relevant papers",
            "Summarize the papers",
            "Store results in structured format"
        ]

    def execute(self, goal):
        print("🔹 Goal:", goal)
        print("🔹 Planning steps...")

        steps = self.plan(goal)
        for step in steps:
            print("  -", step)

        # Step 1: Search
        papers = self.search_tool.search("AI in Agriculture")
        self.memory.store({"searched_papers": papers})

        # Step 2 & 3: Summarize
        summaries = []
        for i, paper in enumerate(papers):
            summary = self.summarizer.summarize(paper)
            summaries.append({
                "paper_id": i + 1,
                "title": paper["title"],
                "authors": paper["authors"],
                "year": paper["year"],
                "summary": summary
            })

        self.memory.store({"summaries": summaries})

        # Step 4: Store
        final_output = {
            "goal": goal,
            "generated_on": datetime.now().isoformat(),
            "results": summaries
        }

        self.storage_tool.store(final_output)
        return final_output