# Gyro Cube

This repo should contain all code to get a "Gyro Cube" running.
This is a product inspired by the Timeular tracker: <https://timeular.com/product/tracker/>

In the end the Gyro Cube should work similarly.

## Development

### Server

Use `make start` to start a local development server.

## Workflow

The cube has an On/Off-Switch.
When turned on the cube performs a reading roughly every 15 minutes and sends it to the server.
On the server it is stored in a database to be later used for reports.
