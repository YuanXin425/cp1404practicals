"""
Programming Language
Estimate: 1 hour
Actual:   30 minutes
"""

from prac_06.programming_language import ProgrammingLanguage

def main():
    """Create ProgrammingLanguage objects, and show dynamically typed programming languages."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

    languages = [python, ruby, visual_basic]
    dynamic_languages = [language for language in languages if language.is_dynamic()]

    print("The dynamically typed languages are:")
    for language in dynamic_languages:
        print(f"{language.name}")

main()