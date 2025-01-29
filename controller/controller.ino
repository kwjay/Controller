#include "input_capture.h"
#include "pwm_generator.h"
#include "serial_interface.h"

SerialInterface serialInterface;
InputCapture inputCapture;
PWMGenerator pwmGenerator;

ISR(TIMER1_OVF_vect) {
  inputCapture.handleTimerOverflow();
}

ISR(TIMER1_CAPT_vect) {
  inputCapture.handleInputCapture();
}

void setup() {
  serialInterface.init();
  pwmGenerator.init();
  inputCapture.init();
  pwmGenerator.setCompareValue(0);
}

void client(int command) {
  switch(command) {
    case 1: {
      serialInterface.waitForData();
      int readData = serialInterface.readData();
      pwmGenerator.setCompareValue(readData);
    } break;
  }
}

void loop() {
  int readData = serialInterface.readData();
  if (readData >= 0) {
    client(readData);
  }
}
