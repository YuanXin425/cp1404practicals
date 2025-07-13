"""
Project Management Program
Estimate: 3 hours
Actual:   5 hours 30 minutes
"""

import datetime

class Project:
    """Represent details about a project."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialize a Project object from the given values."""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        """Return a string representation of a Project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority},"
                f" estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Compare Projects by priority to sort them by priority from low priority to high priority."""
        return self.priority < other.priority

    def is_complete(self):
        """Determine if the project is completed."""
        return self.completion_percentage >= 100
