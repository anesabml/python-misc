from PIL import Image

# ascii characters used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


# resize image according to a new width
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = float(height) / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image


# conver each pixel to grayscale
def grayify(image):
    return image.convert("L")


# convert pixels to a string of ASCII characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel / 25] for pixel in pixels])
    return characters


def main(new_width=50):
    path = raw_input("Enter a valid pathname to an image:\n")
    try:
        image = Image.open(path)

        new_image_data = pixels_to_ascii(grayify(resize_image(image, new_width)))
        
        pixel_count = len(new_image_data)
        ascii_image = "\n".join([new_image_data[i:(i + new_width)] for i in range(0, pixel_count, new_width)])

        print ascii_image

        with open("ascii_image.txt", "w") as f:
            f.write(ascii_image)

    except RuntimeError as err:
        print err


if __name__ == "__main__":
    main()
