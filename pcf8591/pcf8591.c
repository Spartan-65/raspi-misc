#include<stdio.h>
#include<wiringPi.h>
#include<pcf8591.h>

#define PCF 120

int main()
{
    int value;
    if(wiringPiSetup() == -1){
        printf("setup wiringPi failed !\n");
        return 1;
    }

    pcf8591Setup(PCF, 0x48);
    while(1){
        value = analogRead(PCF + 1);
        printf("%d\n", value);
        analogWrite(PCF + 0, value);
        delay(10);
    }
}