#include "input_capture.h"
#include "pwm_generator.h"
#include "serial_interface.h"
#include "signal_filter.h"

SerialInterface serialInterface;
InputCapture inputCapture;
PWMGenerator pwmGenerator;
SignalFilter signalFilter;

ISR(TIMER1_OVF_vect) {
  inputCapture.handleTimerOverflow();
}

ISR(TIMER1_CAPT_vect) {
  inputCapture.handleInputCapture();
  signalFilter.newSample(inputCapture.getSignalFrequency());
}

void setup() {
  serialInterface.init();
  pwmGenerator.init();
  inputCapture.init();
}

void client(int command) {
  switch(command) {
    case 1: {
      serialInterface.waitForData();
      int readData = serialInterface.readData();
      pwmGenerator.setCompareValue(readData);
      // Serial.println(pwmGenerator.getCompareValue());
    } break;
  }
}

void loop() {
  int readData = serialInterface.readData();
  if (readData >= 0) {
    client(readData);
  }
}
