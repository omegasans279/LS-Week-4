#include <SPI.h>
volatile boolean received;
volatile byte receivedData;

ISR(SPI_STC_vect) {
  received = true;
  receivedData = SPDR;
}

void setup() {
  pinMode(6,OUTPUT);
  SPCR |= _BV(SPE);
  received = false;
  SPI.attachInterrupt();
}

void loop() {
  if (received) digitalWrite(6,receivedData);
  received = false;
}