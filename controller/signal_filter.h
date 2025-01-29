#ifndef SIGNAL_FILTER_H
#define SIGNAL_FILTER_H
#define NUMBER_OF_SAMPLES 5

class SignalFilter {
  double samples[NUMBER_OF_SAMPLES]{};
  int index = 0;
public:
  void newSample(const double sample);
  double samplesAverage();
};

#endif