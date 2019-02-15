#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[])
{

	if (argc != 3)
	{
		printf("usage: ./byteswap \"input\" \"output\"\n");
		return -1;
	}

	FILE* fileptr = NULL;
	FILE* output = NULL;
	long i = 0;

	fileptr = fopen(argv[1], "rb");
	fseek(fileptr, 0, SEEK_END);
	const long filelen = ftell(fileptr);
	rewind(fileptr);

	char bytes[filelen];
	
	for (i = (filelen - 1); i >= 0; i--)
	{
		fread(&(bytes[i]), 1, 1, fileptr);
	}

	fclose(fileptr);

	output = fopen(argv[2], "wb");

	for (i = 0; i < filelen; i++)
	{
		fwrite(&(bytes[i]), 1, 1, output);
	}

	fclose(output);

	return 0;
}
