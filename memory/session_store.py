# memory/session_store.py

class SessionMemory:
    """
    Stores conversation state across multiple turns.
    Detects contradictions and checks completeness.
    """

    def __init__(self):
        self.data = {
            "age": None,
            "income": None,
            "occupation": None,
            "state": None
        }

    def update(self, key: str, value: str):
        """
        Update a memory field.
        """
        if key not in self.data:
            raise KeyError(f"Invalid memory key: {key}")

        self.data[key] = value

    def get(self, key: str):
        """
        Get value from memory.
        """
        return self.data.get(key)

    def is_complete(self) -> bool:
        """
        Check if all required fields are filled.
        """
        return all(value is not None for value in self.data.values())

    def detect_contradiction(self, key: str, new_value: str):
        """
        Detect contradiction with previously stored value.
        Returns (True, old_value) if contradiction exists.
        """
        old_value = self.data.get(key)

        if old_value is not None and old_value != new_value:
            return True, old_value

        return False, None

    def reset(self):
        """
        Reset all stored memory.
        """
        for key in self.data:
            self.data[key] = None

    def __repr__(self):
        return f"SessionMemory({self.data})"
