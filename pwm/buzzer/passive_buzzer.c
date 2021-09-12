#include<wiringPi.h>
#include<softTone.h>
#include<stdio.h>

#define BuzPin 0

#define CL1 131
#define CL2 147
#define CL3 165

int main()
{
    if(wiringPiSetup() == -1){
        printf("setup wiringPi failed !\n");
        return 1;
    }

    if(softToneCreate(BuzPin) == -1){
        printf("setup softTone failed!\n");
        return 1;
    }

    return 0;
}