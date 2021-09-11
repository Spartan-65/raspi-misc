#include<wiringPi.h>
#include<stdio.h>

#define RelayPin 0

int main()
{
    if(wiringPiSetup() == -1){
        printf("setup wiringPi failed !\n");
        return 1;
    }
    printf("linker RelayPin: GPIO %d(wiringPi pin)\n", RelayPin);
    pinMode(RelayPin, OUTPUT);
    while (1)
    {
        digitalWrite(RelayPin, LOW);
        printf("low\n");
        delay(1000);
        digitalWrite(RelayPin, HIGH);
        printf("high\n");
        delay(1000);
    }
    return 0;
}