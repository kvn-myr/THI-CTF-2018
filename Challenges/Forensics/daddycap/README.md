# daddycap
This challenge introduces PCAPs to the player and the analysis of such files.

**Description of the Challenge:**
I am a CIA user agent and sometimes download certificates. You are not able to find me.
Flag: THICTF{<MD5 of your finding}

## Setup
Look within a PCAP file for unique messages.

## Solution
Look for traffic which contains certificates. One in particular (No. 7819) is a HTTP GET request on a *godaddy.com* repository.
The used useragent is com.apple.trustd/1.0
```md5 -s com.apple.trustd/1.0 --> MD5 ("com.apple.trustd/1.0") = 5275bb694516939d9414718bac9623c6```

## Flag
Flag: THICTF{5275bb694516939d9414718bac9623c6}
