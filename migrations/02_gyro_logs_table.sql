CREATE TABLE gyro_logs(
    timestamp INTEGER PRIMARY KEY
    , side INTEGER
    , side_timestamp INTEGER
    , FOREIGN KEY(side_timestamp) REFERENCES gyro_sides(timestamp)
);
