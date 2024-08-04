CREATE Database mini_project;

USE mini_project;

DROP TABLE IF EXISTS `couriers`;
CREATE TABLE `couriers` (
  `courier_id` int NOT NULL AUTO_INCREMENT,
  `courier_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `phone_number` varchar(20) NOT NULL,
  PRIMARY KEY (`courier_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `couriers` (`courier_id`, `courier_name`, `phone_number`) VALUES
(1,	'Xavier',	'07253526514'),
(2,	'Johnny',	'07255322111'),
(3,	'tony',	'07462762710'),
(4,	'wesley',	'07253526512');

DROP TABLE IF EXISTS `orders`;
CREATE TABLE `orders` (
  `order_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(20) NOT NULL,
  `last_name` varchar(20) NOT NULL,
  `phone_number` varchar(100) DEFAULT NULL,
  `courier_id` int NOT NULL,
  `product_id` int NOT NULL,
  `order_status` enum('''preparing''','''ready to collect''') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`order_id`),
  KEY `courier_id` (`courier_id`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`courier_id`) REFERENCES `couriers` (`courier_id`),
  CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `orders` (`order_id`, `first_name`, `last_name`, `phone_number`, `courier_id`, `product_id`, `order_status`) VALUES
(1,	'John',	'Doe',	'07462653613',	1,	4,	'\'preparing\''),
(2,	'Sam',	'Smith',	'07473828483',	2,	4,	'\'preparing\''),
(3,	'Sam',	'Smith',	'07473828483',	2,	3,	'\'preparing\''),
(4,	'Roger',	'Fedderer',	'0746626472',	1,	4,	'\'preparing\''),
(5,	'Roger',	'Fedderer',	'0746626472',	1,	3,	'\'preparing\''),
(6,	'Roger',	'Fedderer',	'0746626472',	1,	2,	'\'preparing\''),
(7,	'Dolly',	'Parton',	'073882938211',	1,	6,	'\'preparing\''),
(8,	'Wesley',	'Snipes',	'073882938211',	1,	3,	'\'ready to collect\''),
(9,	'Romeo',	'Juliet',	'07654534123',	3,	7,	'\'preparing\''),
(10,	'Wesley',	'Snipes',	'073525361532',	1,	7,	'\'ready to collect\'');

DROP TABLE IF EXISTS `products`;
CREATE TABLE `products` (
  `product_id` int NOT NULL AUTO_INCREMENT,
  `product_name` varchar(20) NOT NULL,
  `product_price` float NOT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `products` (`product_id`, `product_name`, `product_price`) VALUES
(1,	'coffee',	3.25),
(2,	'wine',	10),
(3,	'redbull',	1.5),
(4,	'fanta',	1.6),
(5,	'beef burger',	5.59),
(6,	'coke',	1.4),
(7,	'chips',	3.3);
