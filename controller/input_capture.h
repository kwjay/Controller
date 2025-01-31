#ifndef INPUT_CAPTURE_H
#define INPUT_CAPTURE_H
#define TCNT_MAX_VALUE 65536UL
#define CLOCK_SPEED 16000000.0
#define PRESCALER 64

#include <Arduino.h>

class InputCapture {
  volatile uint32_t capturedTimestamp{};
  volatile uint32_t overflowCount{};
  volatile uint32_t period{};
  volatile double frequency{};
  volatile bool cycleStart = true;
public:
  void init();
  void handleInputCapture();
  void handleTimerOverflow();
  double getSignalFrequency();
};
#endif