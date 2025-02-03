#ifndef PID_REGULATOR_H
#define PID_REGULATOR_H

class PIDRegulator {
  float kp{0.7}, ki{0.005}, kd{0.1};
  double integral{};
  double previousError{};
public:
  double pid(double measuredValue, double expectedValue);
};

#endif