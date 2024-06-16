import os
import matplotlib.pyplot as plt

# Function to count the number of questions in each folder
def count_questions_per_folder(root_dir):
    folder_counts = {}
    for folder in os.listdir(root_dir):
        folder_path = os.path.join(root_dir, folder)
        if os.path.isdir(folder_path):
            num_questions = len(os.listdir(folder_path))
            folder_counts[folder] = num_questions
    return folder_counts

# Function to visualize the number of questions per folder
def visualize_questions_per_folder(folder_counts):
    folders = list(folder_counts.keys())
    num_questions = list(folder_counts.values())

    plt.figure(figsize=(10, 6))
    plt.bar(folders, num_questions, color='skyblue')
    plt.xlabel('Folders')
    plt.ylabel('Number of Questions')
    plt.title('Number of Questions per Folder')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# Main function
def main():
    root_dir = 'stemQmain/data'  # Update with your root directory
    folder_counts = count_questions_per_folder(root_dir)
    visualize_questions_per_folder(folder_counts)

if __name__ == "__main__":
    main()
