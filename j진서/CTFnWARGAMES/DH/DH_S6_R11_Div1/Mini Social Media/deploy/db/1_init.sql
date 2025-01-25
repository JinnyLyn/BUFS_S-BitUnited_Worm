
CREATE USER 'dbuser'@'%' IDENTIFIED BY 'dbpass';

CREATE DATABASE social_media;

GRANT ALL PRIVILEGES ON social_media.* TO 'dbuser'@'%';

USE `social_media`;

CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    role_id INT NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Posts (
    post_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE Likes (
    like_id INT AUTO_INCREMENT PRIMARY KEY,
    post_id INT NOT NULL,
    user_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (post_id) REFERENCES Posts(post_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    UNIQUE (post_id, user_id)
);

CREATE TABLE Reports (
    report_id INT AUTO_INCREMENT PRIMARY KEY,
    post_id INT NOT NULL,
    reported_by_user_id INT NOT NULL,
    reported_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (post_id) REFERENCES Posts(post_id),
    FOREIGN KEY (reported_by_user_id) REFERENCES Users(user_id)
);

INSERT INTO Users (username, role_id, password, created_at) VALUES ('john_doe', 1, 'c2713b62c903791bdefc5a6a99df04d4330de491bbc7a0ca6a5007337e4a6028', NOW());
INSERT INTO Users (username, role_id, password, created_at) VALUES ('admin', 2, 'c2713b62c903791bdefc5a6a99df04d4330de491bbc7a0ca6a5007337e4a602', NOW()); -- Not only different from remote, but also reset on startup!
