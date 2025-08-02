import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError

title = input("Enter page title: ").strip()

while title != "":
    try:
        # Try getting the full page
        page = wikipedia.page(title, auto_suggest=False)
        print(f"{page.title}")
        print(page.summary)
        print(page.url)

    except DisambiguationError as e:
        print("We need a more specific title. Try one of the following, or a new search:")
        print(e.options)

    except PageError:
        print(f'Page id "{title}" does not match any pages. Try another id!')

    print()  # spacing
    title = input("Enter page title: ").strip()

print("Thank you.")


