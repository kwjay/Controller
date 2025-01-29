#ifndef INPUT_CAPTURE_H
#define INPUT_CAPTURE_H
#define TCNT_MAX_VALUE 65536


#include <Arduino.h>

class InputCapture {
  volatile uint32_t capturedTimestamp{};
  volatile uint32_t overflowCount{};
  volatile uint32_t uptime{};
public:
  void init();
  void handleInputCapture();
  void handleTimerOverflow();
  uint16_t getCapturedTimestamp();
  uint32_t getUptime();
};
#endif