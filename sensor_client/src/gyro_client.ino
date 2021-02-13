#include <Wire.h>

// https://github.com/adafruit/Adafruit_ADXL345
#include <Adafruit_Sensor.h>
#include <Adafruit_ADXL345_U.h>

// sleep duration in micro seconds
unsigned long SLEEP_DURATION = 5 * 1000000;

Adafruit_ADXL345_Unified accel = Adafruit_ADXL345_Unified(12345);
 
void setup(void) {
    Serial.begin(9600);
    while (!Serial);

    // print the empty line to cut off any startup serial garbadge
    Serial.println("");

   /* Initialise the sensor */
   if(!accel.begin()) {
        /* There was a problem detecting the ADXL345 */
        Serial.println("Error: no ADXL345 detected ... Check wiring ...");
        Serial.println("Going into deep sleep mode");
        delay(500);
        ESP.deepSleep(0);
   }

   accel.setRange(ADXL345_RANGE_4_G);
   Serial.println("Setup finished");
   delay(500);
}
 
void loop(void) {
    measure();

    Serial.println("Going to deep sleep...");
    ESP.deepSleep(SLEEP_DURATION);
}
