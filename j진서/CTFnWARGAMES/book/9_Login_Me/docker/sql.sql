CREATE DATABASE IF NOT EXISTS ctf;
USE ctf;
CREATE table IF NOT EXISTS users (id INT,loginid TEXT, password TEXT, auth_bit int, lasttime TIMESTAMP);

INSERT INTO `users` (`id`, `loginid`, `password` ,`auth_bit`, `lasttime`) VALUES
(1, 'adam', 'MROcsm3', 0, '2017-01-01 00:00:00'),
(2, 'eve', 'fewc3m4tC', 0, '2017-01-01 00:00:00'),
(3, 'seccon', 'SECCON_4b', 1023, '2017-01-01 00:00:00'),
(4, 'lee', 'sin', 0, '2017-01-01 00:00:00'),
(5, 'pat', 'goMFE', 0, '2017-01-01 00:00:00'),
(6, 'bob', 'bobobobob',0, '2017-01-01 00:00:00'),
(7, 'key', 'wordisSQLi',0, '2017-01-01 00:00:00');




