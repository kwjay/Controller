#include "input_capture.h"
#include "pwm_generator.h"
#include "serial_interface.h"
#include "signal_filter.h"
#include "pid_regulator.h"

SerialInterface serialInterface;
InputCapture inputCapture;
PWMGenerator pwmGenerator;
SignalFilter signalFilter;
PIDRegulator pidRegulator;
volatile bool regulateSignal{false};

ISR(TIMER1_OVF_vect) {
  inputCapture.handleTimerOverflow();
}

ISR(TIMER1_CAPT_vect) {
  inputCapture.handleInputCapture();
  signalFilter.newSample(inputCapture.getSignalFrequency());
  if (regulateSignal) {
      double measured = signalFilter.samplesAverage();
      int expected = expectedValue(pwmGenerator.getCompareValue());
      double pid = pidRegulator.pid(measured, expected);
      double newFrequency = measured + pid;
      int compareRegisterValue = compareValueFromFrequency(newFrequency);
      if (abs(compareRegisterValue - pwmGenerator.getCompareValue() > 1))
      pwmGenerator.updateRegister(compareRegisterValue);
      // Serial.println(String(signalFilter.samplesAverage()) + " " + String(millis()));
  }
  // Serial.println(String(signalFilter.samplesAverage()) + " " + String(millis()));
}

double expectedValue(int compareValue) {
  return 4.718 * compareValue - 624.9;
}

int compareValueFromFrequency(double frequency) {
  int compareValue = (frequency + 624.9) / 4.718;
  return compareValue;
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
      pwmGenerator.updateRegister(pwmGenerator.getCompareValue());
      Serial.read();
      // Serial.println(readData);
    } break;
    case 2: {
      regulateSignal = !regulateSignal;
    }
  }
}

void loop() {
  if (Serial.available() <= 0) {
    // Serial.println(String(signalFilter.samplesAverage()) + " " + String(millis()));
    return;
  }
  int readData = serialInterface.readData();
  Serial.read();
  client(readData);

}
