#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int xorencrypt(char * input, char * key)
{
    size_t inputlen = strlen(input);
    size_t keylen = strlen(key);

    int flag = 0;

    char * encrypted = malloc(inputlen+1);

    int i = 0;
    for(i = 0; i < inputlen; i++)
    {
        encrypted[i] = input[i] ^ key[i % keylen];

        if(encrypted[i] == 0)
        {
        	flag = flag + 1;
        }
        else
        {
        	flag = 0;
        }
    }

    return flag;
}

int main(int argc, char * argv[])
{
    char * not_the_flag = "this_is_not_the_flag";

    int encrypted = xorencrypt(argv[1], not_the_flag);

    if(encrypted == strlen(not_the_flag))
    {
    	printf("You got it!!\nThe flag is THICTF{<password>} where <password> is your provied password.\n");
    }
    else
    {
    	printf("Hmm not correct. Try again!\n");
    }
    
    return 0;
}
