# assembler0

**Description of the Challenge:**
What does asm0(0xde, 0xex) return? Flag is in the following format:
`THICTF{<return value in hex}`

## Setup
--

## Solution
The XOR is important since it zeros the ebx value. As a result the return value is 0x00.

## Flag
THICTF{0x00}
