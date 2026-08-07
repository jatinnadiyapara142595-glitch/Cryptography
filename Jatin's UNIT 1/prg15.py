from PIL import Image

def encode_image(image_path, data_to_hide):
    image = Image.open(image_path).convert("RGB")

    binary_data = ''.join(format(b, '08b') for b in data_to_hide.encode('utf-8')) + '00000000'

    capacity = image.width * image.height * 3
    if len(binary_data) > capacity:
        raise Exception("Data too large to hide in image.")

    data_index = 0

    for y in range(image.height):
        for x in range(image.width):
            r, g, b = image.getpixel((x, y))

            if data_index < len(binary_data):
                r = (r & ~1) | int(binary_data[data_index])
                data_index += 1

            if data_index < len(binary_data):
                g = (g & ~1) | int(binary_data[data_index])
                data_index += 1

            if data_index < len(binary_data):
                b = (b & ~1) | int(binary_data[data_index])
                data_index += 1

            image.putpixel((x, y), (r, g, b))

            if data_index >= len(binary_data):
                break

        if data_index >= len(binary_data):
            break

    image.save("encoded_image.png")
    print("Data encoded successfully.")


def decode_image(encoded_image_path):
    image = Image.open(encoded_image_path).convert("RGB")

    bit_buffer = ""
    output = bytearray()

    for y in range(image.height):
        for x in range(image.width):
            r, g, b = image.getpixel((x, y))

            for value in (r, g, b):
                bit_buffer += str(value & 1)

                if len(bit_buffer) >= 8:
                    byte = bit_buffer[:8]
                    bit_buffer = bit_buffer[8:]

                    if byte == "00000000":
                        return output.decode("utf-8")

                    output.append(int(byte, 2))

    return output.decode("utf-8")


data_to_hide = "This is a hidden message!"

encode_image("D:\jatin\images.jpg", data_to_hide)

decoded_data = decode_image("encoded_image.png")

print("Decoded Data:", decoded_data)