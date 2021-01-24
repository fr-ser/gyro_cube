CREATE TABLE gyro_logs(
    timestamp INTEGER PRIMARY KEY
    , side INTEGER CHECK(side in (1, 2, 3, 4)) 
    , side_timestamp INTEGER
    , FOREIGN KEY(side_timestamp) REFERENCES gyro_sides(timestamp)
);

CREATE TABLE gyro_sides(
    timestamp INTEGER PRIMARY KEY
    , side INTEGER CHECK(side in (1, 2, 3, 4)) 
    , name TEXT
);
