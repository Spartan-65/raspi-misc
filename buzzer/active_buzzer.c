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

    pinMode(BuzPin, OUTPUT);
    while(1){
        digitalWrite(BuzPin, HIGH);
        delay(1000);
        digitalWrite(BuzPin, LOW);
        delay(1000);
    }

    return 0;
}