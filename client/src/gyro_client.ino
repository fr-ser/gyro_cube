#include <Wire.h>

// https://github.com/adafruit/Adafruit_ADXL345
#include <Adafruit_Sensor.h>
#include <Adafruit_ADXL345_U.h>

// sleep duration in micro seconds
unsigned long SLEEP_DURATION = 15 * 60 * 1000000;

Adafruit_ADXL345_Unified accel = Adafruit_ADXL345_Unified(12345);
 
void setup(void) {
    Serial.begin(9600);

    if (!connect_to_wifi()) {
        Serial.println("Error: Connecting to Wifi ...");
        Serial.println("Going into deep sleep mode");
        delay(500);
        ESP.deepSleep(0);
    } else {
        Serial.println("Connected to Wifi");
    }

    /* Initialise the sensor */
    if (!accel.begin()) {
        Serial.println("Error: no ADXL345 detected ... Check wiring ...");
        Serial.println("Going into deep sleep mode");
        delay(500);
        ESP.deepSleep(SLEEP_DURATION);
    }
    accel.setRange(ADXL345_RANGE_2_G);

    // initialize digital pin LED_BUILTIN as an output.
    pinMode(LED_BUILTIN, OUTPUT);
    digitalWrite(LED_BUILTIN, HIGH); // logic is inverted: HIGH -> off

   Serial.println("Setup finished");
   delay(500);
}
 
void loop(void) {
    digitalWrite(LED_BUILTIN, LOW); // logic is inverted: LOW -> on
    measure();
    digitalWrite(LED_BUILTIN, HIGH);  // logic is inverted: HIGH -> off

    Serial.println("Finished. Going into sleep for (seconds): " + String(SLEEP_DURATION / 1000000));

    // the first value resets the register. The second turns it to sleep mode 
    accel.writeRegister(ADXL345_REG_POWER_CTL, 0x00);
    accel.writeRegister(ADXL345_REG_POWER_CTL, 0x04);
    ESP.deepSleep(SLEEP_DURATION);
}
