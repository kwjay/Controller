#include "signal_filter.h"

void SignalFilter::newSample(const double sample) {
  samples[index] = sample;
  index = (index + 1) % NUMBER_OF_SAMPLES;
}

double SignalFilter::samplesAverage() {
  double averageValue = 0;
  for (int i = 0; i < NUMBER_OF_SAMPLES; i++) averageValue += samples[i];
  averageValue /= NUMBER_OF_SAMPLES;
  return averageValue;
}