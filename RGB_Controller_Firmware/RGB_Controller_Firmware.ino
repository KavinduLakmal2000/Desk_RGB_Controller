#include <FastLED.h>
#define NUM_LEDS 60
#define DATA_PIN 5

unsigned long previousMillis = 0;  
const long interval = 2000;  


unsigned char prefix[] = {'A', 'd', 'a'}, hi, lo, chk, i;


CRGB leds[NUM_LEDS];

void setup() {

  Serial.begin(500000);
  pinMode(13,OUTPUT);
  
  FastLED.addLeds<NEOPIXEL, DATA_PIN>(leds, NUM_LEDS);
  
  LEDS.showColor(CRGB(255, 0, 0));
  delay(500);
  LEDS.showColor(CRGB(0, 255, 0));
  delay(500);
  LEDS.showColor(CRGB(0, 0, 255));
  delay(500);
  LEDS.showColor(CRGB(0, 0, 0));
  
  Serial.print("Ada\n");
}

void loop() { 

   unsigned long currentMillis = millis();  

    if (currentMillis - previousMillis >= interval) {
        previousMillis = currentMillis;  
        digitalWrite(13, HIGH);
        delay(5);
    }

  for(i = 0; i < sizeof prefix; ++i) {
    waitLoop: while (!Serial.available()) ;;
    if(prefix[i] == Serial.read()) continue;
    i = 0;
    goto waitLoop;
  }
  
  while (!Serial.available()) ;;
  hi=Serial.read();
  while (!Serial.available()) ;;
  lo=Serial.read();
  while (!Serial.available()) ;;
  chk=Serial.read();
  
  if (chk != (hi ^ lo ^ 0x55)) {
    i=0;
    goto waitLoop;
  }
  
  memset(leds, 0, NUM_LEDS * sizeof(struct CRGB));
  for (uint8_t i = 0; i < NUM_LEDS; i++) {
    byte r, g, b;    
    while(!Serial.available());
    r = Serial.read();
    while(!Serial.available());
    g = Serial.read();
    while(!Serial.available());
    b = Serial.read();
    leds[i].r = r;
    leds[i].g = g;
    leds[i].b = b;
  }
  
  FastLED.show(); 

digitalWrite(13, LOW);

}
