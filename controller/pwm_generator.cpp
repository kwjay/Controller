#include "pwm_generator.h"

void PWMGenerator::init() {
    /* Setting timer 2 to work in PWM mode at pin 3 */
  pinMode(3, OUTPUT);
  TCCR2A = _BV(COM2B1) | _BV(WGM20); // PWM 0 to OCR2A
  TCCR2B = _BV(WGM22) | _BV(CS20); // Prescaler set to 1
  OCR2A = 255;
  OCR2B = 0;
}

void PWMGenerator::setCompareValue(int value) {
  if (value > 255) value = 255;
  else if (value < 0) value = 0;
  OCR2B = value;
}

int PWMGenerator::getCompareValue() {
  return compareValue;
}