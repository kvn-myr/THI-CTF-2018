# Crypted_Joke
The flag is in the image, but the text is encrypted with the vigenere cipher. You have to extract the text with an ocr (like tesseract or with MS OneNote) and then decrypt it.

**Description of the Challenge:**
Hey man, I can't read the text in the image <Link>. 
Maybe I need a key or something else? 
Can you help?

## Setup
1. Encrypt clear-text using an online tool which implements the vigenere cipher.
2. Paste ciphertext into an image. 

## Solution
Exctract the text using the OCR tool *tesseract*:
```tesseract eggs.jpg stdout|file.txt```
Copy the text into an online tool to decrypt the text (vigenere cipher). The necessary key for the vigenere cipher is *eggs* (image name).

## Flag
Flag: THICTF{BECAUSE_THEY_HAD_EGGS}
