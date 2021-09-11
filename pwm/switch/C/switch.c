#include <wiringPi.h>
#include <stdio.h>

#define BtnPin 0
#define Gpin 1
#define Rpin 2

void LED(char *color)
{
    pinMode(Gpin, OUTPUT);
    pinMode(Rpin, OUTPUT);

    if(color == "red"){
        digitalWrite(Rpin, HIGH);
        digitalWrite(Gpin, LOW);
    } else if(color == "green"){
        digitalWrite(Gpin, HIGH);
        digitalWrite(Rpin, HIGH);
    }
}

int main()
{
    if(wiringPiSetup() == -1){
        printf("fail\n");
        return 1;
    }
    pinMode(BtnPin, INPUT);
    LED("green");
    while (1)
    {
        if(!digitalRead(BtnPin)){
            delay(10);
            if(!digitalRead(BtnPin)){
                LED("red");
                printf("Button is pressed\n");
            }
        } else {
            delay(10);
            if (digitalRead(BtnPin))
            {
                LED("green");
                printf("button is \n");
            }

        }

    }

}