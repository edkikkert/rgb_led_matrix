/*
This is the most basic demonstration code of using HL1606-based digital LED strips. 
The HL1606 chips are not very 'smart' and do not have built in PWM control. (Although
there is a fading ability, its not that useful)

We have a few examples of using the setLEDcolor() and writeStrip() command that will 
allow changing the strip around

public domain
*/


// HL1606strip is an adaptation of LEDstrip from  http://code.google.com/p/ledstrip/
#include "HL1606strip.h"

// use -any- 3 pins!
#define STRIP_D 4
#define STRIP_C 3
#define STRIP_L 2

// Pin S is not really used in this demo since it doesnt use the built in PWM fade
// The last argument is the number of LEDs in the strip. Each chip has 2 LEDs, and the number
// of chips/LEDs per meter varies so make sure to count them! if you have the wrong number
// the strip will act a little strangely, with the end pixels not showing up the way you like
HL1606strip strip = HL1606strip(STRIP_D, STRIP_L, STRIP_C, 160);

void setup(void) {
  Serial.begin(57600);
   resetStrip();  

  // nothing to do!
}

void resetStrip(void) {
   for (int i = 0; i < 160; i++) {
     strip.setLEDcolor(i, BLACK);
   }
   strip.writeStrip();
}

int ledCount = 0;
int ledState = 0;
void loop(void) { 
   // first argument is the color, second is the delay in milliseconds between commands
  uint8_t i, j;
  int keyIn;
  while (Serial.available() > 0) {
    int keyIn = Serial.read();
    switch (keyIn) {
     case 'S':
       resetStrip();
       ledCount = 0;
       break;
     case 'R':
     case '+':
       strip.setLEDcolor(ledCount, RED);
       ledCount++;
       break;
     case 'G':
       case '*':
       strip.setLEDcolor(ledCount, GREEN);
       ledCount++;
       break;
     case 'B':
     case '-':
       strip.setLEDcolor(ledCount, BLUE);
       ledCount++;
       break;
        case 'Y':
       strip.setLEDcolor(ledCount, YELLOW);
       ledCount++;
       break;
       case 'V':
       strip.setLEDcolor(ledCount, VIOLET);
       ledCount++;
       break;
       case 'T':
       strip.setLEDcolor(ledCount, TEAL);
       ledCount++;
       break;
     case 'F':
       ledCount = 0;
       strip.writeStrip();
       break;
      case '.':
      case 'Z':
       strip.setLEDcolor(ledCount, BLACK);
       ledCount++;
       break;  
    }
  }
  delay(10);

//int color = RED;
//for (i=0; i < 78; i++) {
//  if (i % 20 < 5) {
//     color = WHITE;
//  } else {
//      color = BLUE;
//  }
//  for(j = 0; j < 156; j++) {
//    strip.setLEDcolor(j,color);
//  };
//   strip.setLEDcolor(i, RED);
//  strip.setLEDcolor(155-i, RED);
//strip.writeStrip(); 
//delay(50);
////  for(j = 0; j < 160; j++) {
////    strip.setLEDcolor(j,BLACK);
////  };
//strip.setLEDcolor(i, BLACK);
//strip.setLEDcolor(155-i, BLACK);
//strip.writeStrip(); 
////delay(10);
//}
}
