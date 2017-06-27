create table jn011test_session(
    id integer primary key autoincrement, 
    uuid varchar(32) unique,
    sn varchar(16),
    channel smallint,
    startTime timestamp not null default (datetime('now', 'localtime')), 
    endTime timestamp
);

create table jn011test_data(
    id integer primary key autoincrement,
    sid int,
    sn varchar(16),
    injectNo int,
    dataTime timestamp not null default (datetime('now', 'localtime')),
    leftTime int,
    rightTime int,
    battery float,
    capacitor float, 
    leftInsulin int,
    runTime int,
    alarm smallint,
    injectType smallint,
    pumpState smallint
);