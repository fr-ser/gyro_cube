CREATE TABLE gyro_sides(
    timestamp INTEGER PRIMARY KEY
    , side INTEGER
    , name TEXT
);

INSERT INTO gyro_sides(timestamp, side, name) VALUES (0, 0, "unknown");
