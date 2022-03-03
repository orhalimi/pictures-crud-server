
CREATE DATABASE prod;
use prod;

CREATE TABLE images(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY UNIQUE,
    owner_id VARCHAR(60), 
    image_blob BLOB NOT NULL,
    create_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    name VARCHAR(44) 
) ENGINE = InnoDB;


CREATE TABLE images_tags(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY UNIQUE,
    image_id INT NOT NULL,
    tag VARCHAR(40) NOT NULL,
    FOREIGN KEY (image_id) REFERENCES images (id)
		ON DELETE CASCADE
        ON UPDATE RESTRICT
    
) ENGINE = InnoDB;


// there is also sql uuid data type 

//catching, etag
// read about context manager on python - the with statement
