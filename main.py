from agent import AgenticAI
import json

def main():
    goal = (
        "Find the top 3 recent AI research papers on agriculture, "
        "summarize them, and store the output in a structured format."
    )

    agent = AgenticAI()
    result = agent.execute(goal)

    print("\n✅ Final Output:\n")
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()