CREATE TABLE `wiki_articles` (  
    `article_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,  
    `title` VARCHAR(255) NOT NULL,  
    `summary` TEXT NOT NULL,  
    `image_url` TEXT DEFAULT NULL,  
    PRIMARY KEY (`article_id`)  
) ENGINE=InnoDB DEFAULT CHARSET=utf8; 


CREATE TABLE `trade_records` (
    `NO` INT NOT NULL,
    `ARRIVAL_DATE` DATETIME,
    `HS_CODE` INT,
    `HS_CODE_DESCRIPTION` VARCHAR(255),
    `IMPORTER_ADDRESS` TEXT,
    `IMPORTER_COUNTRY` VARCHAR(100),
    `TEL` VARCHAR(20),
    `EMAIL` VARCHAR(100),
    `WEB` TEXT,
    `EXPORTER_ADDRESS` TEXT,
    `COUNTRY_OF_ORIGIN` VARCHAR(100),
    `IMPORT_VALUE` DECIMAL(15, 2),
    `CURRENCY` VARCHAR(10),
    `NET_WEIGHT` DECIMAL(15, 2),
    `NET_WEIGHT_UNIT` TEXT,
    `GROSS_WEIGHT` DECIMAL(15, 2),
    `GROSS_WEIGHT_UNIT` VARCHAR(20),
    `QUANTITY` DECIMAL(15, 2),
    `QUANTITY_UNIT` VARCHAR(20),
    `PRODUCT_DETAILS` TEXT,
    `NUMBER_OF_PACKAGES` INT,
    `PACKAGES_UNIT` VARCHAR(20),
    `PLACE_OF_DELIVERY` TEXT,
    `MANUFACTURING_COMPANY` VARCHAR(100),
    `VOLUME` DECIMAL(15, 2),
    CONSTRAINT pk_trade_records PRIMARY KEY (`NO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



/*
An improvement idea for later...

CREATE TABLE `trade_records` (
    `no` INT NOT NULL PRIMARY KEY,
    `arrival_date` DATE NOT NULL,  
    `hs_code` INT NOT NULL,  
    `importer_id` INT NOT NULL,  
    `exporter_id` INT DEFAULT NULL,  
    `product_id` INT DEFAULT NULL,  
    `quantity` DECIMAL(10, 2) DEFAULT NULL,  
    `quantity_unit` VARCHAR(20) DEFAULT NULL,  
    `number_of_packages` INT NOT NULL,
    `packages_unit` VARCHAR(20) DEFAULT NULL,  
    `place_of_delivery` TEXT,
    `manufacturing_company` VARCHAR(100) DEFAULT NULL,  -- Optional, consider a separate manufacturers table
    `volume` DECIMAL(15, 2),
    FOREIGN KEY (`hs_code`) REFERENCES `hs_codes` (`hs_code`),  
    FOREIGN KEY (`importer_id`) REFERENCES `importers` (`importer_id`),  
    FOREIGN KEY (`exporter_id`) REFERENCES `exporters` (`exporter_id`),  
    FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `hs_codes` (  
  `hs_code` INT NOT NULL,  
  `description` TEXT NOT NULL,  
  PRIMARY KEY (`hs_code`)  
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `importers` (  
  `importer_id` INT AUTO_INCREMENT NOT NULL,  
  `address` TEXT NOT NULL,  
  `country` VARCHAR(255) NOT NULL,  
  `tel` VARCHAR(50) NOT NULL,  
  `email` VARCHAR(255) NOT NULL,  
  `web` TEXT DEFAULT NULL,  
  `import_value` DECIMAL(15, 2) NOT NULL,  
  `currency` VARCHAR(10) DEFAULT NULL,  
  PRIMARY KEY (`importer_id`)  
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `exporters` (  
  `exporter_id` INT AUTO_INCREMENT NOT NULL,  
  `address` TEXT DEFAULT NULL,  
  `country_of_origin` VARCHAR(255) DEFAULT NULL,  
  PRIMARY KEY (`exporter_id`)  
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `products` (  
  `product_id` INT AUTO_INCREMENT NOT NULL,  
  `trade_no` INT NOT NULL,  
  `net_weight` DECIMAL(10, 2) DEFAULT NULL,  
  `net_weight_unit` VARCHAR(20) DEFAULT NULL,  
  `gross_weight` DECIMAL(10, 2) DEFAULT NULL,  
  `gross_weight_unit` VARCHAR(20) DEFAULT NULL,  
  `details` TEXT DEFAULT NULL,  
  FOREIGN KEY (`trade_no`) REFERENCES `trade_records` (`no`),  
  PRIMARY KEY (`product_id`)  
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
*/