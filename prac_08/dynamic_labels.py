from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.label import Label


class DynamicLabels(App):
    """DynamicLabels is a Kivy App for displaying a list of names."""
    message = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Steven", "Isabelle", "Kevin"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels and add them to the GUI."""
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)

DynamicLabels().run()
