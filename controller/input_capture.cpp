#include "input_capture.h"

void InputCapture::init() {
  pinMode(8, INPUT);
  TCCR1A = 0;
  TCCR1B = 0;
  TCCR1B = _BV(ICES1) | _BV(ICNC1) | _BV(CS10); // On rising edge and noise canceller enabled with prescaler set to 8
  TIMSK1 = _BV(ICIE1) | _BV(TOIE1); // Input capture and interrupt on timer overflow
}

void InputCapture::handleInputCapture() {
  uint32_t previousTimestamp = capturedTimestamp;
  capturedTimestamp = ((uint32_t)(overflowCount*TCNT_MAX_VALUE)) + ICR1;
  if (capturedTimestamp > previousTimestamp) {
    uptime = capturedTimestamp - previousTimestamp;
  } 
  overflowCount = 0;
  ICR1 = 0;
  TIFR1 |= _BV(ICF1);
}

void InputCapture::handleTimerOverflow() {
  overflowCount++;
  TIFR1 |= _BV(TOV1);
}

uint16_t InputCapture::getCapturedTimestamp() {
  return capturedTimestamp;
}

uint32_t InputCapture::getUptime() {
  return uptime;
}
