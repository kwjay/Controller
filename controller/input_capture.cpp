#include "input_capture.h"

void InputCapture::init() {
  pinMode(8, INPUT);
  TCCR1A = 0;
  TCCR1B = 0;
  TCCR1B = _BV(ICES1) | _BV(ICNC1) | _BV(CS11); // On rising edge and noise canceller enabled with prescaler set to 8
  TIMSK1 = _BV(ICIE1) | _BV(TOIE1); // Input capture and interrupt on timer overflow
}

void InputCapture::handleInputCapture() {
  if (cycleStart) {
    capturedTimestamp = ((uint32_t)overflowCount*TCNT_MAX_VALUE) + ICR1;
    cycleStart = false;
  } else {
    uint32_t previousTimestamp = capturedTimestamp;
    capturedTimestamp = ((uint32_t)overflowCount*TCNT_MAX_VALUE) + ICR1;
    period = (capturedTimestamp > previousTimestamp) ? capturedTimestamp - previousTimestamp : 0;
    frequency = CLOCK_SPEED / (PRESCALER * double(period));
    cycleStart = true;
    overflowCount = 0;
  }
  TIFR1 |= _BV(ICF1);
}

void InputCapture::handleTimerOverflow() {
  overflowCount++;
  TIFR1 |= _BV(TOV1);
}

uint32_t InputCapture::getCapturedTimestamp() {
  return capturedTimestamp;
}

double InputCapture::getSignalFrequency() {
  return frequency;
}

