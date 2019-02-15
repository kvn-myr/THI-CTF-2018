#include<stdio.h>
#include<string.h>

typedef int bool;
#define true 1
#define false 0

bool fun_A(int a){
    bool b = true;
    for(int c = 2; c<a;c++){
        if(a%c == 0){
            b = false;
        }
    }
    return b;
}

int fun_B(int a){
    int b = 0;
    for(int c = 2;;c++){
        if(fun_A(c)){
            b++;
            if(b == a){
                return c;
            }
        }
    }
}

int fun_C(){
    int a = 0;
    for(int b = 1; a < 1000000000; b++){
        a += fun_B(b);
    }
    return a;
}



int main() {

    printf("THICTF{%i}", fun_C());
	return 0;
}
