create table lessons(
	id int primary key auto_increment,
    name char(200) not null,
    features char (200),
    `group` char (100) not NULL,
    local_group int,
    local_group_english int,
    course char(30),
    id_time_pair int not null,
    day_week char(30) not null,
    parity_week char(30),
    id_lecturer int,
	foreign key (id_time_pair) references time_pairs (id),
    foreign key (id_lecturer) references lecturers (id)
);
