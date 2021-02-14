# Gyro Cube

This repo should contain all code to get a "Gyro Cube" running.
This is a product inspired by the Timeular tracker: <https://timeular.com/product/tracker/>

In the end the Gyro Cube should work similarly.

## Workflow

The cube has an On/Off-Switch.
When turned on the cube performs a reading roughly every 15 minutes and sends it to the server.
On the server it is stored in a database to be later used for reports.

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
