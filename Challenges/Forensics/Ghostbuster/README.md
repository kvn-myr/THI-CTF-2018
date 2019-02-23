# Ghostbuster
This task introduces forensic tools and challenge to the player.

**Description of the Challenge:**
"If there's somethin' strange in your neighborhood / Who ya gonna call? / (Ghostbusters!)" 
Do you know the Ghostbuster?
Not only ghosts are invisible!
Go and hunt them. :)

## Setup
Hide the files in a image file. Implemented in `createFolder.java` and `folder_structure`.

## Solution
1. Find the hidden file -> find-command or ls -a
2. Hidden file in: ```E: oMyJQ8jUik\uuaOEw7yNY\cKAnaa8390\Px5HLtGkMD\fW6X0JOX0c\ZxBYWHHKkQ\oDn1jNAnUS\3oSfnnhp89\fDfdDzZwnU\Y9grWFj2Nr```
3. Read the hint -> Recover the deleted file
4. Use a recovery tool (scalpel, sleuthkit)
5. Recover the PDF file
6. Hexdump the file and find the flag

## Flag
THICTF{LatexIsBetterThanWord}
