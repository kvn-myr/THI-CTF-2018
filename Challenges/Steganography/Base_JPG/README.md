# Base_JPG
This file displays how files can be hidden within a JPG.

**Description of the Challenge:**
This jpg <Link> looks really normal. Nothing special!

## Setup
Hide file within the JPG.

## Solution
The flag is at the end of the file, after the normal JPG end. The flag is also "base64" encoded.
```
tail -c 41 thi.jpg | base64 -d
(or copy the bytes manually after "hexdump -C" or something like this)
```

## Flag
Flag (base64): VEhJQ1RGe1RoZV9lbmRfaXNfbjB0X3RoZV9lbmR9Cg==
THICTF{The_end_is_n0t_the_end}
