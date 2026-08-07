# Cryptography
Cryptography practical (Python)

# Image Steganography using Python (LSB Technique)

## Aim
To implement Image Steganography using the Least Significant Bit (LSB) technique in Python for securely hiding and retrieving secret messages inside an image.

---

## Objective
- To hide a secret text message inside an image.
- To retrieve the hidden message without affecting the visible quality of the image.
- To understand the concept of image steganography and LSB encoding.

---

## Software Requirements
- Python 3.x
- Pillow Library (PIL)

Install Pillow using:

```bash
pip install pillow
```

---

## Files Required

```
Project Folder
│── prg15.py
│── original_image.png
│── encoded_image.png (generated after execution)
```

---

## Theory

### What is Steganography?

Steganography is the practice of hiding secret information inside another file so that no one suspects the existence of the hidden data.

Unlike encryption, which makes data unreadable, steganography hides the presence of the data itself.

Images are commonly used because small changes in pixel values are almost impossible for the human eye to notice.

---

### Least Significant Bit (LSB)

Every pixel in an RGB image has three color values:

- Red (R)
- Green (G)
- Blue (B)

Each value is stored using 8 bits.

Example:

```
Red = 10110110
```

The last bit is called the Least Significant Bit (LSB).

Changing

```
10110110
```

to

```
10110111
```

changes the value by only 1, which is visually unnoticeable.

The secret message is hidden by replacing these least significant bits with the bits of the message.

---

## Algorithm

### Encoding

1. Open the original image.
2. Convert the image into RGB format.
3. Convert the secret message into binary.
4. Add an end marker (00000000).
5. Replace the least significant bit of each RGB value with the message bits.
6. Save the modified image as **encoded_image.png**.

---

### Decoding

1. Open the encoded image.
2. Read the least significant bit of every RGB component.
3. Combine the bits into bytes.
4. Stop when the end marker is found.
5. Convert binary back into text.
6. Display the hidden message.

---

## Working

### Encoding Process

Original Message

```
This is a hidden message!
```

↓

Convert to Binary

↓

Replace LSB of image pixels

↓

Save as

```
encoded_image.png
```

---

### Decoding Process

Read LSB Bits

↓

Convert Binary to Characters

↓

Stop at Terminator

↓

Display Secret Message

---

## Program Features

- Hides any text message inside an image.
- Retrieves the hidden message accurately.
- Uses UTF-8 encoding.
- Supports RGB images.
- Very small visual difference between original and encoded image.
- Easy to understand and implement.

---

## Advantages

- Simple implementation.
- Easy to use.
- High hiding capacity.
- No visible distortion.
- Fast encoding and decoding.
- Suitable for educational purposes.

---

## Limitations

- Anyone aware of LSB steganography can extract hidden data.
- Image compression may destroy hidden information.
- Not suitable for highly secure communication without encryption.
- Limited by image size.

---

## Applications

- Secure communication
- Digital watermarking
- Copyright protection
- Military communication
- Medical image security
- Confidential document sharing
- Data authentication

---

## Functions Used

### encode_image()

- Opens the image.
- Converts text into binary.
- Embeds data into image pixels.
- Saves encoded image.

---

### decode_image()

- Reads image pixels.
- Extracts LSB bits.
- Converts bits into characters.
- Returns the original hidden message.

---

## Input

```
Image:
original_image.png

Secret Message:
This is a hidden message!
```

---

## Output

```
Data encoded successfully.

Decoded Data:
This is a hidden message!
```

---

## Complexity

### Time Complexity

Encoding:

```
O(n)
```

Decoding:

```
O(n)
```

where **n** is the number of pixels.

---

### Space Complexity

```
O(m)
```

where **m** is the length of the hidden message.

---

## Conclusion

The program successfully implements Image Steganography using the Least Significant Bit (LSB) method. The secret message is embedded inside an image without producing noticeable visual changes. The hidden message can later be extracted accurately from the encoded image. This demonstrates a simple and effective technique for secure data hiding using Python and the Pillow library.

---

## Future Enhancements

- Password-protected message extraction.
- AES encryption before embedding.
- Hide files instead of only text.
- Support audio and video steganography.
- GUI application using Tkinter.
- Hide larger amounts of data.
- Support multiple image formats.

---

## References

1. Python Documentation
2. Pillow (PIL) Documentation
3. Digital Image Processing Concepts
4. Cryptography and Network Security by William Stallings
5. Research papers on Image Steganography
