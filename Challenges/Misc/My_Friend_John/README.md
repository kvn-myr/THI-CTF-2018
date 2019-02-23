# My_Friend_John
This challenge introduces the tool *John the Ripper* and ZIP file password cracking to the player.

**Description of the Challenge:**
That guy named "John" handed me this <Link>. Can you help?

## Setup
Create ZIP file with a very weak password.

## Solution
The flag.txt file is password protected in the zip file. The zip file has also a diffrent file extension ("ctf"). Use (John the Ripper)[https://www.openwall.com/john/] or a similar tool to crack the zip file.
```
$ mv secret.ctf secret.zip
$ zip2john secret.zip > hash.txt
$ john hash.txt
```
Password: thictf

## Flag
THICTF{use_n0t_a_crap_passw0rd_for_y0ur_secret_z1ps}
