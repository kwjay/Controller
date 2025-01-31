#ifndef PID_REGULATOR_H
#define PID_REGULATOR_H

class PIDRegulator {
  float kp{}, ki{}, kd{};
  double integral{};
  double previousError{};
public:
  double pid(double measuredValue, double expectedValue);
};

#endif