class DigraphNode:
    def __init__(self, value = None, neighbors = None):
        if neighbors is None:
            neighbors = []
        self.value = value
        self.neighbors = neighbors