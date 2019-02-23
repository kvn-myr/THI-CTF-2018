# Certificate
This challenge introduces X509 certificates to the player.

**Description of the Challenge:**
Something seems to be wrong with this certificate...

## Setup
Edit certificate with a fake extension.

## Solution
This certificate has an extension by the name "Capture Identifier" which is made up. It holds the base64 encoded flag, with a ":" every two letters. As a result, `VE:hJ:Q1:RG:e2:V4:dG:Vu:c2:lv:bn:Nf:YX:Jl:X2:Z1:bn:0=` becomes `VEhJQ1RGe2V4dGVuc2lvbnNfYXJlX2Z1bn0==` which can be fed to something like (base64decode)[www.base64decode.org] to get the flag.

Note: Decoders might ignore the ":"'s already, so deleting them is not always necessary

## Flag
THICTF{extensions_are_fun}
