# Coded_Message
This challenge introduces the AES_ECB algorithm to the player.

**Description of the Challenge:**
Hey you! Did you see that message that looks like an electronic codebook? I can't decrypt it because the key is not complete. I only know that the three question marks have something to do with one of those names:
* Thesaurus
* Schneier
* Security
* Reykjavik
* Safety
* Rjindael
* Feistel
* Ratchet

Key: 16-BYTE-???-KEY!

## Setup
Encrypt the clear-text (flag) using an online tool implementing the AES_ECB algorithm.

## Solution
The ciphertext is base64 encoded.
Decyrpt the content of the file *message.txt* (AES_ECB) with the key: "16-BYTE-AES-KEY!

## Flag
Flag: THICTF{be_careful_with_AES_ECB_mode}