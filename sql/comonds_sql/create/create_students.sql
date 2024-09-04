create table students (
	id int primary key auto_increment,
    user_name char(30) not null UNIQUE,
    course char(30),
    direction char(30),
    parity_week char(30),
    `group` char(30),
    local_group int,
    local_group_english int
)
