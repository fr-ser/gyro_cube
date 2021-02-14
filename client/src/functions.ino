#include <ESP8266HTTPClient.h>
#include <ESP8266WiFi.h>
#include "base64.h"

const char* ssid = "${WIFI_SSID}";
const char* password = "${WIFI_PASS}";
 
const String authUsername = "${GYRO_BASIC_AUTH_USER}";
const String authPassword = "${GYRO_BASIC_AUTH_PASS}";
const String baseURL = "${GYRO_BASE_URL}";

void measure(void) {
    sensors_event_t event; 
    accel.getEvent(&event);

    int side = get_side(event);

    if (side == 0) {
        Serial.println("Unknown side");
        Serial.print("X: "); Serial.print(event.acceleration.x); Serial.print(" ");
        Serial.print("Y: "); Serial.print(event.acceleration.y); Serial.print(" ");
        Serial.print("Z: "); Serial.print(event.acceleration.z); Serial.print(" ");
        Serial.println("m/s^2 ");
        return;
    }

    Serial.print("Side: "); Serial.println(side);
    
    send_side_to_server(side);
}

/*
  Determine the "side" based on the event/acceleration. Sides:
  1: "345 up": the gyroscope is on the side and the side with the number 345 is looking up
  2: "top": the top of the gyroscope is up
*/
int get_side(sensors_event_t event) {
    if (
        event.acceleration.z > 8 &&
        abs(event.acceleration.y) + abs(event.acceleration.x) < 7
    ) {
        return 1;
    }

    if (
        event.acceleration.y > 8 &&
        abs(event.acceleration.z) + abs(event.acceleration.x) < 7
    ) {
        return 2;
    }

    return 0;
}

bool connect_to_wifi(void) {
    WiFi.begin(ssid, password);

    if (WiFi.status() == WL_CONNECTED) return true;
    Serial.println("Waiting for Wifi connection (5 seconds)");
    delay(5000);
    if (WiFi.status() == WL_CONNECTED) return true;
    Serial.println("Waiting for Wifi connection (10 seconds)");
    delay(10000);
    if (WiFi.status() == WL_CONNECTED) return true;

    return false;
}

void send_side_to_server(int side) {
    String auth = base64::encode(authUsername + ":" + authPassword);
    String endpoint = "/gyro/logs?side=" + String(side);
    HTTPClient http;

    Serial.println(baseURL + endpoint);
    http.begin(baseURL + endpoint);
    http.addHeader("Authorization", "Basic " + auth);

    int httpCode = http.POST("");
    if (httpCode > 0) { 
        Serial.print("HTTP Response Code: "); Serial.println(httpCode);
    } else {
        Serial.println("Error on HTTP request");
    }
}