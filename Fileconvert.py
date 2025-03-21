import os

def modify_and_save_file():
    """Reads a file, converts content to uppercase, and saves to a new file."""
    
    # Get input filename from user
    source_file = input("Enter the filename to process: ").strip()

    # Attempt to read and process the file
    try:
        with open(source_file, 'r') as f:
            original_content = f.read()
            
    except FileNotFoundError:
        print(f"✖ Error: The file '{source_file}' could not be found.")
        return
    except PermissionError:
        print(f"✖ Error: Permission denied to read '{source_file}'.")
        return
    except Exception as e:
        print(f"⚠ Unexpected error reading file: {str(e)}")
        return

    # Process the content (convert to uppercase)
    modified_content = original_content.upper()

    # Create new filename with _modified suffix
    base_name, file_extension = os.path.splitext(source_file)
    destination_file = f"{base_name}_modified{file_extension}"

    # Attempt to write the modified content
    try:
        with open(destination_file, 'w') as f:
            f.write(modified_content)
        print(f"✔ Successfully created modified file: {destination_file}")
        
    except PermissionError:
        print(f"✖ Error: Permission denied to write to '{destination_file}'.")
    except Exception as e:
        print(f"⚠ Unexpected error writing file: {str(e)}")

if __name__ == "__main__":
    modify_and_save_file()
