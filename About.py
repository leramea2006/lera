class FlourishingTracker:
    def __init__(self):
        self.goals = []
        self.reflections = []

    def set_goal(self, goal):
        self.goals.append(goal)
        print(f"Goal '{goal}' has been set!")

    def reflect(self, reflection):
        self.reflections.append(reflection)
        print("Reflection noted!")

    def show_goals(self):
        print("\n--- Your Goals ---")
        for i, goal in enumerate(self.goals, 1):
            print(f"{i}. {goal}")
        if not self.goals:
            print("No goals set yet.")

    def show_reflections(self):
        print("\n--- Your Reflections ---")
        for i, reflection in enumerate(self.reflections, 1):
            print(f"{i}. {reflection}")
        if not self.reflections:
            print("No reflections noted yet.")

def main():
    tracker = FlourishingTracker()
    while True:
        print("\n--- Flourishing Tracker ---")
        print("1. Set a Goal")
        print("2. Reflect on your day")
        print("3. Show Goals")
        print("4. Show Reflections")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            goal = input("Enter your goal: ")
            tracker.set_goal(goal)
        elif choice == '2':
            reflection = input("Enter your reflection: ")
            tracker.reflect(reflection)
        elif choice == '3':
            tracker.show_goals()
        elif choice == '4':
            tracker.show_reflections()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
