import json

# ---------------- SEARCH TOOL ----------------
class PaperSearchTool:
    def search(self, query):
        """
        Simulated search for recent AI + Agriculture papers
        """
        return [
            {
                "title": "Deep Learning for Crop Yield Prediction",
                "authors": "A. Sharma et al.",
                "year": 2024,
                "abstract": "Uses deep neural networks with satellite imagery and climate data."
            },
            {
                "title": "AI-Based Pest Detection in Smart Agriculture",
                "authors": "L. Wang et al.",
                "year": 2023,
                "abstract": "CNN-based pest detection system for crops."
            },
            {
                "title": "Reinforcement Learning for Precision Irrigation",
                "authors": "M. Gonzalez et al.",
                "year": 2023,
                "abstract": "Uses reinforcement learning to optimize irrigation schedules."
            }
        ]


class SummarizationTool:
    def summarize(self, paper):
        return (
            f"The paper '{paper['title']}' focuses on applying artificial intelligence "
            f"techniques to agricultural problems. It proposes innovative methods to "
            f"improve efficiency, decision-making, and sustainability in farming systems."
        )

class StorageTool:
    def store(self, data, filename="output.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)