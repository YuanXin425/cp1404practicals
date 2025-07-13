"""
Project Management Program
Estimate: 3 hours
Actual:   5 hours 30 minutes
"""

import datetime

from operator import attrgetter

from prac_07.project import Project

FILENAME = "projects.txt"

def main():
    """Create a program to manage and display projects."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects_before_menu(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    menu()
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            # Allow user to input filename to load projects from
            filename = input("Enter filename to load projects from: ")
            projects = load_projects_before_menu(filename)

        elif choice == "S":
            # Allow user to input filename to save projects to
            filename = input("Enter filename to save projects to: ")
            save_projects_to_file(filename, projects)

        elif choice == "D":
            display_projects(projects)

        elif choice == "F":
            filter_projects_by_date(projects)

        elif choice == "A":
            add_projects(projects)

        elif choice == "U":
            update_projects(projects)

        else:
            print("Invalid menu choice.")

        menu()
        choice = input(">>> ").upper()

    save_choice = input(f"Would you like to save to {FILENAME}? ").lower()
    if save_choice == "yes" or save_choice == "y":
        save_projects_to_file(FILENAME, projects)
    else:
        print(f"{save_choice}, I think not.")
    print("Thank you for using custom-built project management software.")


def menu():
    """Display menu options."""
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")


def load_projects_before_menu(filename):
    """Read and load project details from given file."""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
    return projects


def save_projects_to_file(filename, projects):
    """Save the projects to file."""
    with open(filename, "w") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t"
                  f"{project.cost_estimate}\t{project.completion_percentage}", file=out_file)


def display_projects(projects):
    """Display projects into two categories: completed and incomplete."""
    # Check which projects are incomplete and completed
    incomplete_projects = [project for project in projects if not project.is_complete()]
    complete_projects = [project for project in projects if project.is_complete()]

    # Sort the projects by priority in ascending order from the lowest priority to the highest priority
    incomplete_projects.sort()
    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f" {project}")

    complete_projects.sort()
    print("Completed projects:")
    for project in complete_projects:
        print(f" {project}")


def filter_projects_by_date(projects):
    """Prompt user for a date and display only projects after that date."""
    start_date_input = input("Show projects that start after date (dd/mm/yy): ")
    filter_date = datetime.datetime.strptime(start_date_input, "%d/%m/%Y").date()
    # Check if the projects are after the start date the user input
    filtered_projects = [project for project in projects if project.start_date >= filter_date]
    # Sort the projects by dates in ascending order
    filtered_projects.sort(key=attrgetter("start_date"))
    for project in filtered_projects:
            print(project)


def add_projects(projects):
    """Allow user to add new project with new details."""
    print("Let's add a new project")
    new_name = input("Name: ").strip()
    date_string = input("Start Date (dd/mm/yyyy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    new_start_date = date.strftime("%d/%m/%Y")
    new_priority = int(input("Priority: "))
    new_cost_estimate = float(input("Cost estimate: $"))
    new_complete_percent = int(input("Percent complete: "))

    new_project = Project(new_name, new_start_date, new_priority, new_cost_estimate, new_complete_percent)
    projects.append(new_project)


def update_projects(projects):
    """Display the projects neatly with index and allow user to update project details."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_choice = input("Project choice: ")
    # Check if the user input choice is a digit
    if project_choice.isdigit():
        index = int(project_choice)
        # Check if the user input choice is within the indexes displayed
        if 0 <= index < len(projects):
            project = projects[index]
            print(project)
            # Update completion percentage
            new_percentage = input("New percentage: ")
            if new_percentage.isdigit():
                project.completion_percentage = int(new_percentage)
            # Update priority
            new_priority = input("New priority: ")
            if new_priority.isdigit():
                project.priority = int(new_priority)
        else:
            print("Invalid index.")
    else:
        print("Invalid choice.")


main()
