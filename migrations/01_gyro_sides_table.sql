CREATE TABLE gyro_sides(
    timestamp INTEGER PRIMARY KEY
    , side INTEGER
    , name TEXT
);

INSERT INTO gyro_sides(timestamp, side, name) VALUES
(0, 0, 'unknown')
, (11, 1, 'PCB bottom up')
, (22, 2, 'gyroscope up')
, (33, 3, 'red-wide')
, (44, 4, 'grey-wide')
, (55, 5, 'red-short')
, (66, 6, 'grey-short')
;
