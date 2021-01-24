CREATE TABLE gyro_sides(
    timestamp INTEGER PRIMARY KEY
    , side INTEGER CHECK(side in (1, 2, 3, 4)) 
    , name TEXT
);
