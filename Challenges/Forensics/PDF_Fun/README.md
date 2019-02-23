# PDF_Fun
PDF with hidden (embedded) attachment (JPG).

**Description of the Challenge:**
My friend gave me this *<Link>*. Maybe there is something hidden, figure it out!

## Setup
Create the file with:    
```pdftk <PDF filename> attach_files <attachment filename> output <output filename>```
Then we have changed the *PDF Reference Table* so, that the attachment shows up, but you can't extract it.

## Solution
1. Use something like `binwalk` to extract the content.
2. Read the file binary with "vi" or something else and search for "xref". Change the fourth entry from "f" to "n. Extraction with: 
```pdftk <PDF filename> unpack_files [output <output folder>]"```

## Flag
THICTF{FUN_W1TH_PDFs}
