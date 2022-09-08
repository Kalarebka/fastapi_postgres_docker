\c fastapi

CREATE TABLE user_account(
    id SERIAL, 
    username VARCHAR (32) UNIQUE NOT NULL, 
    password VARCHAR (255) NOT NULL, 
    email VARCHAR (128) UNIQUE NOT NULL, 
    PRIMARY KEY(id)
    );

CREATE TABLE event(
    id SERIAL,
    name VARCHAR (128) NOT NULL,
    time TIME,
    date DATE,
    place VARCHAR (128),
    PRIMARY KEY(id)
);


CREATE TABLE user_event(
    user_id INT NOT NULL,
    event_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user_account(id),
    FOREIGN KEY (event_id) REFERENCES event(id),
    PRIMARY KEY (user_id, event_id)
);

-- Sample data
insert into user_account (username, password, email) values ('Eryk', 'password', 'eryk@gmail.com');
insert into user_account (username, password, email) values ('Ika', 'password', 'ika@gmail.com');
insert into event (name, time, date, place) values ('event', '12:30', '01-01-2022', 'place');
insert into event (name, time, date, place) values ('event2', '12:35', '02-01-2022', 'place2');
insert into user_event (user_id, event_id) values (1, 1);
insert into user_event (user_id, event_id) values (1, 2);
insert into user_event (user_id, event_id) values (2, 1);
