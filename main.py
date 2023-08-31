import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def list_and_select(items, prompt):
    for index, item in enumerate(items, start=1):
        print(f"{index}. {item}")
    
    while True:
        choice = input(prompt)
        try:
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(items):
                return choice_index
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    path = "./exercises"
    directories = os.listdir(path)

    folders = [
        d for d in directories if os.path.isdir(os.path.join(path, d))
    ]
    
    print("Select from exercises folders:")
    folder_choice_index = list_and_select(folders, "Enter folder number: ")
    selected_folder = folders[folder_choice_index]

    exercise_files = sorted([
        file_name for file_name in os.listdir(os.path.join(path, selected_folder))
        if file_name.endswith('.py')
    ])
    
    print("Select an exercise to run:")
    exercise_choice_index = list_and_select(exercise_files, "Enter the number of the exercise: ")
    selected_file = exercise_files[exercise_choice_index]
    
    print(f"Running {selected_file}")
    clear_screen()
    
    exercise_path = os.path.join(path, selected_folder, selected_file)
    exit_code = os.system(f"python {exercise_path}")
    
    if exit_code != 0:
        print(f"Exercise {selected_file} encountered an error.")
    
if __name__ == "__main__":
    main()