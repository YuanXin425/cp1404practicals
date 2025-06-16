# Colour names with their colour codes.
COLOUR_HEX = {"ACIDGREEN": "#b0bf1a", "BABYPINK": "#f4c2c2",
                "BRIGHTNAVYBLUE": "#1974d2", "CANDYAPPLERED": "#ff0800",
                "DARKLAVENDER": "#734f96", "ELECTRICLIME": "#ccff00",
                "GOLDENPOPPY": "#fcc200", "CARROCTORANGE": "#ed9121",
                "COOLGREY": "#8c92ac", "EGGSHELL": "#f0ead6"}
print(COLOUR_HEX)

# Get user's colour name
colour_name = input("Enter colour name: ").upper()

# Check the color name and print the colour code.
while colour_name != "":
    if colour_name in COLOUR_HEX:
        print(COLOUR_HEX[colour_name])
    else:
        print("Invalid colour name.")
    colour_name = input("Enter colour name: ").upper()

print()


