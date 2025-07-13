"""
Programming Language
Estimate: 1 hour
Actual:   30 minutes
"""

class ProgrammingLanguage:
    """Represent a Programming Language object."""

    def __init__(self, name="", typing="", reflection="",year=0):
        """Initialize a Language object."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if the language is dynamic."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return an f-string representation of the programming language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
