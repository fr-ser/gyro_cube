# Gyro Cube

This repo should contain all code to get a "Gyro Cube" running.
This is a product inspired by the Timeular tracker: <https://timeular.com/product/tracker/>

In the end the Gyro Cube should work similarly.

## Workflow

The cube has an On/Off-Switch.
When turned on the cube performs a reading roughly every 15 minutes and sends it to the server.
On the server it is stored in a database to be later used for reports.

## Hardware

- As gyroscope an ADXL345 is used: <https://www.analog.com/media/en/technical-documentation/data-sheets/ADXL345.pdf>
- As micro controller an ESP8266 is used
- As server host a Raspberry Pi Zero is used

## Development

### Server

Use `make server-start` to start a local development server.

### Deployment

To enable (on a very specific Raspberry Pi Zero) use the command `make deploy-server`.
This will install dependencies and copy a *systemd* service.

Also a `.env` file should be located in the directory (indicated in the systemd-service file),
that looks like this:

```env
ENVIRONMENT=production
AUTH_USERS=user:pass,user2:pass2
SQLALCHEMY_DATABASE_URL=sqlite:///file_path.db
```

## Work Specifications

During deep sleep the setup has a power consumption of ~ 1.6mA. This is mostly due to the Power
LED of the ADXL345 board.
During a wake up the power consumption is ~75mA.
