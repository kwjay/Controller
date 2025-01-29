#include "input_capture.h"
#include "pwm_generator.h"

InputCapture inputCapture;
PWMGenerator pwmGenerator;

ISR(TIMER1_OVF_vect) {
  inputCapture.handleTimerOverflow();
}

ISR(TIMER1_CAPT_vect) {
  inputCapture.handleInputCapture();
}

void setup() {
  Serial.begin(115200);
  pwmGenerator.init();
  inputCapture.init();
  pwmGenerator.setCompareValue(0);
}

void loop() {

}
