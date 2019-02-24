# strings
Basic reverse engineering challenge.

**Description of the Challenge:**
Wow so many strings in one program. Which one is the correct one? The flag format is `THICTF{<clear-text>}` where `<clear-text>` is the decrypted string of the displayed hash.

Hint: You will not be able to brute force the hash.

## Setup
--

## Solution
Read the assembler and see the correct address which is passed to the printf. Or run `ltrace`/`strace`.

## Flag
THICTF{NwMGaxzgiQHyANdjvlWDkMv}
