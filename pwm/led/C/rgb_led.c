#include<wiringPi.h>
#include<softPwm.h>
#include<stdio.h>

#define uchar unsigned char
#define LedPinRed 0
#define LedPinGreen 1
#define LedPinBlue 2

void ledInit(void)
{
    softPwmCreate(LedPinRed, 0, 100);
    softPwmCreate(LedPinGreen, 0, 100);
    softPwmCreate(LedPinBlue, 0, 100);
}

void ledColorSet(uchar r_val, uchar g_val, uchar b_val)
{
    softPwmWrite(LedPinRed, r_val);
    softPwmWrite(LedPinGreen, g_val);
    softPwmWrite(LedPinBlue, b_val);
}

int main()
{
    // int i;
    if (wiringPiSetup() ==  -1){
        printf("setup wiringPi failed!\n");
    }

    ledInit();

    while (1){
        ledColorSet(0xff, 0x00, 0x00);
        delay(500);
        ledColorSet(0x00, 0xff, 0x00);
        delay(500);
        ledColorSet(0x00, 0x00, 0xff);
        delay(500);
    }


    return 0;
}