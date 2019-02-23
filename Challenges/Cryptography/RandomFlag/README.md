# RandomFlag
This java program generates a pseudorandom flag with a fixed seed. The fixed seed causes the random number in the following value range to always have the same number. A random flag was calculated. This flag must be transformed back. The code changes the charachters to ASCII values.

**Description of the Challenge:**
On the server runs the java program „randomFlag.java“, which reads a text file and returns the flag.Hm! Something went wrong.
The output is *JVufbHUqVgnOvFSZwDOLnhSRQVZWds*.
Can you help?

## Setup
The directory *RandomFlag* contains the source code of the challenge.

## Solution
1. Find out that the constant ASCII values cancel out themsevles.
2. Also the random number is the same -> you must change the signs (- -> + | + -> -) 
	* Before: randomFlag += iTc(cTi(c) + 2*cTi('e') - (r.nextInt(5)*2-3) - cTi('b') - cTi('h'));
	* After: randomFlag += iTc(cTi(c) + 2*cTi('e') + (r.nextInt(5)*2-3) - cTi('b') - cTi('h'));   
	* The same applies to the others!!!
3. The flag will be printed in the right format.
 
## Flag
THICTF{OUrecKTpYdsLwGV]xIRIqgVOVWWTix}