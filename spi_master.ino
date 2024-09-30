#include <SPI.h>
void setup() {
  pinMode(6,INPUT_PULLUP);
  pinMode(10,OUTPUT);
  SPI.begin();
  SPI.setClockDivider(SPI_CLOCK_DIV8);
}

void loop() {
  boolean state = (digitalRead(6))?0:1;
  digitalWrite(10,LOW);
  SPI.transfer(state);
  digitalWrite(10,HIGH);
}