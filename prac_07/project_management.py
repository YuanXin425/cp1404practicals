"""
Project Management Program
Estimate: 1 hour
Actual:   1 hour 15 minutes
"""

import datetime

from prac_07.project import Project

FILENAME = "projects.txt"

def main():
    """Create a program to manage and display projects."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    menu()
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            projects = load_projects(FILENAME)

        #elif choice == "S":

        elif choice == "D":
            display_projects(projects)

        #elif choice == "F":

        elif choice == "A":
            add_projects(projects)

        elif choice == "U":
            update_projects(projects)

        else:
            print("Invalid menu choice.")

        menu()
        choice = input(">>> ").upper()


    #print(f"Would you like to save to {FILENAME}?")
    #print("Thank you for using custom-built project management software.")


def menu():
    """Display menu options."""
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")


def load_projects(filename):
    """Read and load file of project details."""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)

    return projects


def display_projects(projects):
    """Display projects into two categories: completed and incomplete."""
    incomplete_projects = []
    complete_projects = []

    # Check if the project is completed
    for project in projects:
        if project.completion_percentage < 100:
            incomplete_projects.append(project)
        else:
            complete_projects.append(project)

    # Sort the projects by priority in ascending order from the lowest priority to the highest priority
    incomplete_projects.sort()
    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f" {project}")

    complete_projects.sort()
    print("Complete projects:")
    for project in complete_projects:
        print(f" {project}")

def add_projects(projects):
    """Allow user to add new project with new details."""
    print("Let's add a new project")
    new_name = input("Name: ").strip()
    date_string = input("Date (d/m/yyyy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    new_start_time = date.strftime("%d/%m/%Y")
    new_priority = int(input("Priority: "))
    new_cost_estimate = float(input("Cost estimate: $"))
    new_complete_percent = int(input("Percent complete: "))

    new_project = Project(new_name, new_start_time, new_priority, new_cost_estimate, new_complete_percent)
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
