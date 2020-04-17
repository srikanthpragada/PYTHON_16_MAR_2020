CREATE TABLE jobs (
    id        INTEGER      PRIMARY KEY AUTOINCREMENT,
    title     VARCHAR (20) NOT NULL,
    minsalary INTEGER
);

insert into jobs(title,minsalary) values('QA',20000)
