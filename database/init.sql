CREATE TABLE `wiki_articles` (  
`article_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,  
`title` VARCHAR(255) NOT NULL,  
`summary` TEXT NOT NULL,  
`image_url` TEXT DEFAULT NULL,  
PRIMARY KEY (`article_id`)  
) ENGINE=InnoDB DEFAULT CHARSET=utf8; 
