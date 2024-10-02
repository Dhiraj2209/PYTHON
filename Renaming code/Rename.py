import os

def rename_files_in_folder(folder_path):
    try:
        # Remove any extra quotes around the folder path
        folder_path = folder_path.strip('"')

        # Get the folder name from the path
        folder_name = os.path.basename(folder_path)

        # Get all the files in the folder
        files = os.listdir(folder_path)

        if not files:
            print("The folder is empty!")
            return

        i = 1  # Start the counter for file numbering

        # Iterate over the files and rename them
        for filename in files:
            old_file_path = os.path.join(folder_path, filename)

            if os.path.isfile(old_file_path):  # Only rename files
                # Get the file extension
                file_extension = os.path.splitext(filename)[1]

                # Create the new filename
                new_filename = f"{folder_name}_{i}{file_extension}"
                new_file_path = os.path.join(folder_path, new_filename)

                # Check if the new filename already exists
                while os.path.exists(new_file_path):
                    i += 1  # Increment until we find a unique name
                    new_filename = f"{folder_name}_{i}{file_extension}"
                    new_file_path = os.path.join(folder_path, new_filename)

                # Rename the file
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: {filename} -> {new_filename}")

                i += 1  # Increment the counter for the next file
            else:
                print(f"Skipping directory: {filename}")

        print("All files renamed successfully!")
    except Exception as e:
        print(f"Error occurred: {e}")

# Get folder path from user input (without quotes)
folder_path = input("Enter the folder path: ").strip('"')
rename_files_in_folder(folder_path)
