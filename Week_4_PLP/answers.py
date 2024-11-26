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
