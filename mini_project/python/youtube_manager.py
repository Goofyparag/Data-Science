
import json

def load_data():
    try:
        with open("youtube.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)

def list_all_videos(videos):
    if not videos:
        print("No videos found!")
        return
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Name: {video['name']}, Time: {video['time']}")

def add_videos(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)
    print("Video added successfully!")

def update_videos(videos):
    if not videos:
        print("No videos to update!")
        return
    
    list_all_videos(videos)
    try:
        index = int(input("Enter the number of the video to update: ")) - 1
        if 0 <= index < len(videos):
            name = input("Enter new video name (or press enter to keep current): ")
            time = input("Enter new video time (or press enter to keep current): ")
            
            if name:
                videos[index]["name"] = name
            if time:
                videos[index]["time"] = time
                
            save_data_helper(videos)
            print("Video updated successfully!")
        else:
            print("Invalid video number!")
    except ValueError:
        print("Please enter a valid number!")

def delete_videos(videos):
    if not videos:
        print("No videos to delete!")
        return
    
    list_all_videos(videos)
    try:
        index = int(input("Enter the number of the video to delete: ")) - 1
        if 0 <= index < len(videos):
            deleted = videos.pop(index)
            save_data_helper(videos)
            print(f"Video '{deleted['name']}' deleted successfully!")
        else:
            print("Invalid video number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    videos = load_data()
    while True:
        print("\nYouTube Manager | Choose an option")
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video")
        print("4. Delete a YouTube video")
        print("5. Exit the app")
        
        choice = input("Enter your choice: ")
        
        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_videos(videos)
            case "3":
                update_videos(videos)
            case "4":
                delete_videos(videos)
            case "5":
                print("Thanks for using YouTube Manager!")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()