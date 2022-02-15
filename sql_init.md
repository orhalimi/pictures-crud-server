
CREATE DATABASE prod;
use prod;

CREATE TABLE users(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY UNIQUE,
    username VARCHAR(21) NOT NULL, 
    password VARCHAR(64) NOT NULL,
    salt VARCHAR(8) NOT NULL
) ENGINE = InnoDB;

CREATE TABLE images(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY UNIQUE,
    owner_id int, 
    image_blob BLOB NOT NULL,
    create_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    FOREIGN KEY (owner_id) REFERENCES users (id)
		ON DELETE CASCADE
        ON UPDATE RESTRICT
) ENGINE = InnoDB;


CREATE TABLE images_tags(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY UNIQUE,
    image_id INT NOT NULL,
    tag VARCHAR(120) NOT NULL,
    FOREIGN KEY (image_id) REFERENCES images (id)
		ON DELETE CASCADE
        ON UPDATE RESTRICT
    
) ENGINE = InnoDB;


// there is also sql uuid data type 

//catching, etag
// read about context manager on python - the with statement
