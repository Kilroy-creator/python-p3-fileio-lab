def write_file(file_name, file_content):
    """
    Write content to a .txt file.
    
    Args:
        file_name: The name/path of the file (without .txt extension)
        file_content: The content to write to the file
    """
    with open(f"{file_name}.txt", "w") as file:
        file.write(file_content)


def append_file(file_name, append_content):
    """
    Append content to an existing .txt file.
    
    Args:
        file_name: The name/path of the file (without .txt extension)
        append_content: The content to append to the file
    """
    with open(f"{file_name}.txt", "a") as file:
        file.write(append_content)


def read_file(file_name):
    """
    Read and return the content of a .txt file.
    
    Args:
        file_name: The name/path of the file (without .txt extension)
    
    Returns:
        The content of the file as a string
    """
    with open(f"{file_name}.txt", "r") as file:
        return file.read()