#include "pid_regulator.h"

double PIDRegulator::pid(double measured, double expected) {
  double error = expected - measured;
  integral += error;
  double derivative = error - previousError;
  previousError = error;
  return kp * error + ki * integral + kd * derivative;
}
