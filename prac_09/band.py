class Band:
    """Represent a Band object."""

    def __init__(self, name=""):
        """Initialise a Band object."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)}) "

    def add(self, musician):
        """Add a Musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Call play() on each musician in the band."""
        output = []
        for musician in self.musicians:
            output.append(musician.play())
        return "\n".join(output)