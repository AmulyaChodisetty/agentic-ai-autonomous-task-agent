class AgentMemory:
    """
    Stores intermediate results and context
    """
    def __init__(self):
        self.data = []

    def store(self, item):
        self.data.append(item)

    def get_all(self):
        return self.data