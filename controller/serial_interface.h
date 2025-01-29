#ifndef SERIAL_INTERFACE_H
#define SERIAL_INTERFACE_H

#include <Arduino.h>

class SerialInterface {
public:
  void init();
  int readData();
  void printData(String &&data);
  void waitForData();
};
#endif