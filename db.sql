create table travelDestination (
    id integer primary key autoincrement,
    firstName char[25] not null,
    lastName char[25] not null,
    firstChoice char[25] not null,
    scndChoice char[25] not null,
    thirdChoice char[25] not null
);