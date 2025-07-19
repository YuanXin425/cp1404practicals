from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window

MILE = 1.60934

class ConvertMilesKm(App):
    """ConvertMilesKm is a Kivy App for converting miles to kilometres."""
    message = StringProperty()

    def build(self):
        """Build the Kivy App from the kv file."""
        Window.size = (800, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = "Convert miles to km"
        return self.root

    def handle_conversion(self):
        """Handle conversion calculation from the button."""
        try:
            miles = int(self.root.ids.input_miles.text)
            km = miles * MILE
            self.root.ids.output_km.text = str(km)
        except ValueError:
            self.root.ids.output_km.text = f"{0:.1f}"

    def handle_increment(self, value):
        """Handle increment from the button."""
        try:
            miles = int(self.root.ids.input_miles.text)
        except ValueError:
            miles = 0
        miles += value
        self.root.ids.input_miles.text = str(miles)

ConvertMilesKm().run()
