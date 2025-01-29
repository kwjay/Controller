#include "serial_interface.h"

void SerialInterface::init() {
  Serial.begin(115200);
}

int SerialInterface::readData() {
  if (Serial.available() <= 0) return -1;
  return Serial.parseInt(SKIP_NONE);
}

void SerialInterface::printData(String &&data) {
  if (Serial.availableForWrite() > data.length()) {
    Serial.print(data);
  }
}

void SerialInterface::waitForData() {
  Serial.flush();
  while(Serial.available() == 0) {}
}