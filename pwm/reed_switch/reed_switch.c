#include <wiringPi.h>
#include <stdio.h>
#include <signal.h>

#define ReedPin 0
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

void sig_int(int signo)
{
    printf("........catch you, SIGINT\n");
    digitalWrite(Rpin, HIGH);
    digitalWrite(Gpin, HIGH);
    pinMode(Rpin, INPUT);
    pinMode(Gpin, INPUT);
    signal(SIGINT, SIG_DFL);
    exit(0);
}

int main()
{
    if(wiringPiSetup() == -1){
        printf("fail\n");
        return 1;
    }
    signal(SIGINT, sig_int);
    pinMode(ReedPin, INPUT);
    LED("green");
    while (1)
    {
        if(!digitalRead(ReedPin)){
            delay(10);
            if(!digitalRead(ReedPin)){
                LED("red");
                printf("Detectec Magnetic material\n");
            }
        } else {
            delay(10);
            if (digitalRead(ReedPin))
            {
                while(!digitalRead(ReedPin));
                LED("green");
                printf("green\n");
            }

        }

    }

}