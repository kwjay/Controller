#ifndef PWM_GENERATOR_H
#define PWM_GENERATOR_H

#include <Arduino.h>

class PWMGenerator {
  int compareValue{};
public:
  void init();
  void setCompareValue(int value);
  int getCompareValue();
};
#endif