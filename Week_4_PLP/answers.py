try:
    # Reading the image
    with open("globe.png", "rb") as image:
        print("Reading the image:")
        for i in image:
            print(i)

    # Copying the image to a new file
    with open("globe.png", "rb") as image, open("My_Image.png", "wb") as copyImg:
        for i in image:
            copyImg.write(i)
    print("Image successfully copied to 'My_Image.png'.")
except FileNotFoundError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


# Error Handling for File Reading
filename = input("Enter the filename to open: ")

try:
    # Attempt to open the file
    with open(filename, "r") as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"Error: You do not have permission to read the file '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
