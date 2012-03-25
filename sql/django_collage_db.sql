-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Хост: localhost
-- Время создания: Мар 25 2012 г., 19:53
-- Версия сервера: 5.5.8
-- Версия PHP: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- База данных: `django_collage_db`
--

-- --------------------------------------------------------

--
-- Структура таблицы `account_userprofile`
--

CREATE TABLE IF NOT EXISTS `account_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `auth_key` varchar(50) NOT NULL,
  `address` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `created` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- Дамп данных таблицы `account_userprofile`
--

INSERT INTO `account_userprofile` (`id`, `user_id`, `auth_key`, `address`, `name`, `phone`, `created`) VALUES
(1, 1, '', '', '', '', '2012-02-05 19:23:46'),
(2, 2, '-==KEY-CONFIRMED==-', 'Кирова 222, кв 56', 'Готовский Дмитрий', '56-83-23', '2012-02-12 16:26:48');

-- --------------------------------------------------------

--
-- Структура таблицы `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

--
-- Дамп данных таблицы `auth_group`
--


-- --------------------------------------------------------

--
-- Структура таблицы `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_425ae3c4` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

--
-- Дамп данных таблицы `auth_group_permissions`
--


-- --------------------------------------------------------

--
-- Структура таблицы `auth_message`
--

CREATE TABLE IF NOT EXISTS `auth_message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `auth_message_403f60f` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

--
-- Дамп данных таблицы `auth_message`
--


-- --------------------------------------------------------

--
-- Структура таблицы `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_1bb8f392` (`content_type_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=121 ;

--
-- Дамп данных таблицы `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add permission', 1, 'add_permission'),
(2, 'Can change permission', 1, 'change_permission'),
(3, 'Can delete permission', 1, 'delete_permission'),
(4, 'Can add group', 2, 'add_group'),
(5, 'Can change group', 2, 'change_group'),
(6, 'Can delete group', 2, 'delete_group'),
(7, 'Can add user', 3, 'add_user'),
(8, 'Can change user', 3, 'change_user'),
(9, 'Can delete user', 3, 'delete_user'),
(10, 'Can add message', 4, 'add_message'),
(11, 'Can change message', 4, 'change_message'),
(12, 'Can delete message', 4, 'delete_message'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session'),
(19, 'Can add site', 7, 'add_site'),
(20, 'Can change site', 7, 'change_site'),
(21, 'Can delete site', 7, 'delete_site'),
(22, 'Can add log entry', 8, 'add_logentry'),
(23, 'Can change log entry', 8, 'change_logentry'),
(24, 'Can delete log entry', 8, 'delete_logentry'),
(25, 'Can add flat page', 9, 'add_flatpage'),
(26, 'Can change flat page', 9, 'change_flatpage'),
(27, 'Can delete flat page', 9, 'delete_flatpage'),
(28, 'Can add user profile', 10, 'add_userprofile'),
(29, 'Can change user profile', 10, 'change_userprofile'),
(30, 'Can delete user profile', 10, 'delete_userprofile'),
(34, 'Can add captcha store', 12, 'add_captchastore'),
(35, 'Can change captcha store', 12, 'change_captchastore'),
(36, 'Can delete captcha store', 12, 'delete_captchastore'),
(43, 'Can add mosaic option', 15, 'add_mosaicoption'),
(44, 'Can change mosaic option', 15, 'change_mosaicoption'),
(45, 'Can delete mosaic option', 15, 'delete_mosaicoption'),
(61, 'Can add Размеры и цены', 21, 'add_mosaicprice'),
(62, 'Can change Размеры и цены', 21, 'change_mosaicprice'),
(63, 'Can delete Размеры и цены', 21, 'delete_mosaicprice'),
(67, 'Can add order', 23, 'add_order'),
(68, 'Can change order', 23, 'change_order'),
(69, 'Can delete order', 23, 'delete_order'),
(70, 'Can add Список заказов', 24, 'add_orderoption'),
(71, 'Can change Список заказов', 24, 'change_orderoption'),
(72, 'Can delete Список заказов', 24, 'delete_orderoption'),
(73, 'Can add puzzle size', 25, 'add_puzzlesize'),
(74, 'Can change puzzle size', 25, 'change_puzzlesize'),
(75, 'Can delete puzzle size', 25, 'delete_puzzlesize'),
(76, 'Can add Рамки', 26, 'add_frames'),
(77, 'Can change Рамки', 26, 'change_frames'),
(78, 'Can delete Рамки', 26, 'delete_frames'),
(79, 'Can add Упаковки', 27, 'add_packaging'),
(80, 'Can change Упаковки', 27, 'change_packaging'),
(81, 'Can delete Упаковки', 27, 'delete_packaging'),
(82, 'Can add puzzle', 28, 'add_puzzle'),
(83, 'Can change puzzle', 28, 'change_puzzle'),
(84, 'Can delete puzzle', 28, 'delete_puzzle'),
(85, 'Can add Натяжка', 29, 'add_stretch'),
(86, 'Can change Натяжка', 29, 'change_stretch'),
(87, 'Can delete Натяжка', 29, 'delete_stretch'),
(88, 'Can add Фото на холсте - Список размеров и цен', 30, 'add_cropsize'),
(89, 'Can change Фото на холсте - Список размеров и цен', 30, 'change_cropsize'),
(90, 'Can delete Фото на холсте - Список размеров и цен', 30, 'delete_cropsize'),
(91, 'Can add crop', 31, 'add_crop'),
(92, 'Can change crop', 31, 'change_crop'),
(93, 'Can delete crop', 31, 'delete_crop'),
(94, 'Can add Список размеров и цен', 32, 'add_mosaicsize'),
(95, 'Can change Список размеров и цен', 32, 'change_mosaicsize'),
(96, 'Can delete Список размеров и цен', 32, 'delete_mosaicsize'),
(97, 'Can add mosaic', 33, 'add_mosaic'),
(98, 'Can change mosaic', 33, 'change_mosaic'),
(99, 'Can delete mosaic', 33, 'delete_mosaic'),
(100, 'Can add Альбомы', 34, 'add_album'),
(101, 'Can change Альбомы', 34, 'change_album'),
(102, 'Can delete Альбомы', 34, 'delete_album'),
(103, 'Can add Изображение', 35, 'add_images'),
(104, 'Can change Изображение', 35, 'change_images'),
(105, 'Can delete Изображение', 35, 'delete_images'),
(106, 'Can add Доставка', 36, 'add_shiping'),
(107, 'Can change Доставка', 36, 'change_shiping'),
(108, 'Can delete Доставка', 36, 'delete_shiping'),
(109, 'Can add Валюта', 37, 'add_currency'),
(110, 'Can change Валюта', 37, 'change_currency'),
(111, 'Can delete Валюта', 37, 'delete_currency'),
(112, 'Can add shiping type', 38, 'add_shipingtype'),
(113, 'Can change shiping type', 38, 'change_shipingtype'),
(114, 'Can delete shiping type', 38, 'delete_shipingtype'),
(115, 'Can add Страны', 39, 'add_countries'),
(116, 'Can change Страны', 39, 'change_countries'),
(117, 'Can delete Страны', 39, 'delete_countries'),
(118, 'Can add Города', 40, 'add_cities'),
(119, 'Can change Города', 40, 'change_cities'),
(120, 'Can delete Города', 40, 'delete_cities');

-- --------------------------------------------------------

--
-- Структура таблицы `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- Дамп данных таблицы `auth_user`
--

INSERT INTO `auth_user` (`id`, `username`, `first_name`, `last_name`, `email`, `password`, `is_staff`, `is_active`, `is_superuser`, `last_login`, `date_joined`) VALUES
(1, 'aries.ua@gmail.com', '', '', 'aries.ua@gmail.com', 'sha1$d0bcd$9bbf973b02708ff46813b005f6f00ad505c19ad8', 1, 1, 1, '2012-03-22 13:23:24', '2011-12-09 10:00:59'),
(2, 'aries.forum@gmail.com', '', '', 'aries.forum@gmail.com', 'sha1$72e79$fc2e36ea86668febe872ca776ae4504b33359300', 0, 1, 0, '2012-03-21 08:33:21', '2011-12-09 10:02:30');

-- --------------------------------------------------------

--
-- Структура таблицы `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_403f60f` (`user_id`),
  KEY `auth_user_groups_425ae3c4` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

--
-- Дамп данных таблицы `auth_user_groups`
--


-- --------------------------------------------------------

--
-- Структура таблицы `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_403f60f` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

--
-- Дамп данных таблицы `auth_user_user_permissions`
--


-- --------------------------------------------------------

--
-- Структура таблицы `cart_cities`
--

CREATE TABLE IF NOT EXISTS `cart_cities` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `country_id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cart_cities_534dd89` (`country_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=11 ;

--
-- Дамп данных таблицы `cart_cities`
--

INSERT INTO `cart_cities` (`id`, `country_id`, `name`) VALUES
(1, 1, 'Москва'),
(2, 1, 'Санкт-Петербург'),
(3, 1, 'Орел'),
(4, 1, 'Екатеринбург'),
(5, 1, 'Нижний Новгород'),
(6, 1, 'Архангельск'),
(7, 2, 'Алматы'),
(8, 2, 'Астана'),
(9, 2, 'Караганда'),
(10, 2, 'Шымкент');

-- --------------------------------------------------------

--
-- Структура таблицы `cart_countries`
--

CREATE TABLE IF NOT EXISTS `cart_countries` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- Дамп данных таблицы `cart_countries`
--

INSERT INTO `cart_countries` (`id`, `name`) VALUES
(1, 'Россия'),
(2, 'Казахстан');

-- --------------------------------------------------------

--
-- Структура таблицы `cart_currency`
--

CREATE TABLE IF NOT EXISTS `cart_currency` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `code` varchar(100) NOT NULL,
  `factor` double NOT NULL,
  `defrow` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=6 ;

--
-- Дамп данных таблицы `cart_currency`
--

INSERT INTO `cart_currency` (`id`, `name`, `code`, `factor`, `defrow`) VALUES
(4, 'Тенге', 'KZ', 1, 0),
(5, 'Доллары', 'USD', 0.006802721, 1);

-- --------------------------------------------------------

--
-- Структура таблицы `cart_order`
--

CREATE TABLE IF NOT EXISTS `cart_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `nouser` varchar(32) NOT NULL,
  `price` double NOT NULL,
  `shiping_id` int(11) DEFAULT NULL,
  `shiping_price` double NOT NULL,
  `address` varchar(255) NOT NULL,
  `email` varchar(100) NOT NULL,
  `name` varchar(255) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `created` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cart_order_403f60f` (`user_id`),
  KEY `shiping_id` (`shiping_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

--
-- Дамп данных таблицы `cart_order`
--


-- --------------------------------------------------------

--
-- Структура таблицы `cart_orderoption`
--

CREATE TABLE IF NOT EXISTS `cart_orderoption` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_id` int(11) NOT NULL,
  `type_id` int(11) NOT NULL,
  `price` double NOT NULL,
  `img` varchar(32) NOT NULL,
  `f_0` varchar(32) NOT NULL,
  `f_1` varchar(32) NOT NULL,
  `f_2` varchar(32) NOT NULL,
  `f_3` varchar(32) NOT NULL,
  `f_4` varchar(32) NOT NULL,
  `f_5` varchar(32) NOT NULL,
  `f_6` varchar(32) NOT NULL,
  `f_7` varchar(32) NOT NULL,
  `f_8` varchar(32) NOT NULL,
  `options` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cart_orderoption_7cc8fcf5` (`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

--
-- Дамп данных таблицы `cart_orderoption`
--


-- --------------------------------------------------------

--
-- Структура таблицы `cart_shiping`
--

CREATE TABLE IF NOT EXISTS `cart_shiping` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `shiping_type_id` int(11) NOT NULL,
  `country_id` int(11) NOT NULL,
  `city_id` int(11) NOT NULL,
  `price` double NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cart_shiping_da38549` (`shiping_type_id`),
  KEY `cart_shiping_534dd89` (`country_id`),
  KEY `cart_shiping_586a73b5` (`city_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=14 ;

--
-- Дамп данных таблицы `cart_shiping`
--

INSERT INTO `cart_shiping` (`id`, `shiping_type_id`, `country_id`, `city_id`, `price`) VALUES
(1, 1, 2, 7, 150),
(2, 1, 2, 8, 155),
(3, 1, 2, 9, 160),
(4, 1, 2, 10, 165),
(5, 2, 2, 7, 200),
(6, 2, 2, 8, 210),
(7, 2, 2, 9, 205),
(8, 2, 2, 10, 201),
(9, 1, 1, 6, 300),
(10, 1, 1, 4, 305),
(11, 2, 1, 4, 300),
(12, 2, 1, 1, 299),
(13, 2, 1, 6, 350);

-- --------------------------------------------------------

--
-- Структура таблицы `cart_shipingtype`
--

CREATE TABLE IF NOT EXISTS `cart_shipingtype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- Дамп данных таблицы `cart_shipingtype`
--

INSERT INTO `cart_shipingtype` (`id`, `name`) VALUES
(1, 'EMS'),
(2, 'Казпочта');

-- --------------------------------------------------------

--
-- Структура таблицы `common_frames`
--

CREATE TABLE IF NOT EXISTS `common_frames` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `img` varchar(150) NOT NULL,
  `price` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=7 ;

--
-- Дамп данных таблицы `common_frames`
--

INSERT INTO `common_frames` (`id`, `name`, `img`, `price`) VALUES
(3, 'A052-1299', 'frames/A052-1299_2.jpg', 10),
(4, 'A052-1819', 'frames/A052-1819.jpg', 11),
(5, 'A052-2380', 'frames/A052-2380.jpg', 12),
(6, 'A052-2381', 'frames/A052-2381.jpg', 13);

-- --------------------------------------------------------

--
-- Структура таблицы `common_packaging`
--

CREATE TABLE IF NOT EXISTS `common_packaging` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `img` varchar(150) NOT NULL,
  `price` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=4 ;

--
-- Дамп данных таблицы `common_packaging`
--

INSERT INTO `common_packaging` (`id`, `name`, `img`, `price`) VALUES
(1, 'gold', 'packaging/gold.jpg', 20),
(2, 'noel', 'packaging/noel.jpg', 21),
(3, 'silver', 'packaging/silver.jpg', 22);

-- --------------------------------------------------------

--
-- Структура таблицы `common_stretch`
--

CREATE TABLE IF NOT EXISTS `common_stretch` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `descr` varchar(255) NOT NULL,
  `koef` double NOT NULL,
  `defrow` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- Дамп данных таблицы `common_stretch`
--

INSERT INTO `common_stretch` (`id`, `name`, `descr`, `koef`, `defrow`) VALUES
(1, 'Белые поля', '', 1, 1),
(2, 'Обернутые поля', 'Обратите внимание! Часть изображения под светлой рамкой, будет завернута на торец подрамника.', 1, 0);

-- --------------------------------------------------------

--
-- Структура таблицы `crop_crop`
--

CREATE TABLE IF NOT EXISTS `crop_crop` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `nouser` varchar(32) NOT NULL,
  `img` varchar(32) NOT NULL,
  `img_stretch_id` int(11) NOT NULL,
  `img_type` smallint(6) NOT NULL,
  `img_size_id` int(11) DEFAULT NULL,
  `img_effect` smallint(6) NOT NULL,
  `qty` int(11) NOT NULL,
  `frame_id` int(11) DEFAULT NULL,
  `packaging_id` int(11) DEFAULT NULL,
  `x1` int(11) NOT NULL,
  `y1` int(11) NOT NULL,
  `x2` int(11) NOT NULL,
  `y2` int(11) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `created` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `crop_crop_403f60f` (`user_id`),
  KEY `crop_crop_470d0678` (`img_stretch_id`),
  KEY `crop_crop_5f519445` (`img_size_id`),
  KEY `crop_crop_7b89a14a` (`frame_id`),
  KEY `crop_crop_412518f8` (`packaging_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- Дамп данных таблицы `crop_crop`
--


-- --------------------------------------------------------

--
-- Структура таблицы `crop_cropsize`
--

CREATE TABLE IF NOT EXISTS `crop_cropsize` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `price` double NOT NULL,
  `width` int(11) NOT NULL,
  `height` int(11) NOT NULL,
  `defsize` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=13 ;

--
-- Дамп данных таблицы `crop_cropsize`
--

INSERT INTO `crop_cropsize` (`id`, `name`, `price`, `width`, `height`, `defsize`) VALUES
(1, '30x20 см', 10, 30, 20, 1),
(2, '40x30 см', 11, 40, 30, 0),
(3, '50x40 см', 12, 50, 40, 0),
(4, '60x40 см', 13, 60, 40, 0),
(5, '70x50 см', 14, 70, 50, 0),
(6, '90x60 см', 15, 90, 60, 0),
(7, '30x30 см', 16, 30, 30, 0),
(8, '40x40 см', 17, 40, 40, 0),
(9, '50x50 см', 18, 50, 50, 0),
(10, '60x60 см', 19, 60, 60, 0),
(11, '70x70 см', 20, 70, 70, 0),
(12, '90x90 см', 21, 90, 90, 0);

-- --------------------------------------------------------

--
-- Структура таблицы `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_403f60f` (`user_id`),
  KEY `django_admin_log_1bb8f392` (`content_type_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=166 ;

--
-- Дамп данных таблицы `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `user_id`, `content_type_id`, `object_id`, `object_repr`, `action_flag`, `change_message`) VALUES
(1, '2011-12-09 10:10:46', 1, 9, '1', '/about/ -- О сайте', 1, ''),
(18, '2012-01-24 11:14:03', 1, 21, '1', '1 тенге', 1, ''),
(19, '2012-01-24 11:14:07', 1, 21, '2', '2 тенге', 1, ''),
(20, '2012-01-24 11:14:14', 1, 21, '3', '3 тенге', 1, ''),
(21, '2012-01-24 20:03:14', 1, 21, '4', '13 тенге', 1, ''),
(22, '2012-01-24 20:03:24', 1, 21, '5', '15 тенге', 1, ''),
(23, '2012-01-24 20:03:32', 1, 21, '6', '15 тенге', 1, ''),
(24, '2012-01-24 20:03:50', 1, 21, '7', '13 тенге', 1, ''),
(25, '2012-01-24 20:03:58', 1, 21, '8', '17 тенге', 1, ''),
(26, '2012-01-24 20:04:05', 1, 21, '9', '19 тенге', 1, ''),
(27, '2012-01-24 20:04:30', 1, 21, '10', '18 тенге', 1, ''),
(28, '2012-01-24 20:04:38', 1, 21, '11', '16 тенге', 1, ''),
(29, '2012-01-24 20:04:45', 1, 21, '12', '14 тенге', 1, ''),
(30, '2012-01-24 20:04:52', 1, 21, '13', '12 тенге', 1, ''),
(31, '2012-01-24 20:05:24', 1, 21, '10', '18 тенге', 3, ''),
(45, '2012-02-04 08:03:01', 1, 7, '1', '127.0.0.1:8000', 2, 'Изменен domain и name.'),
(46, '2012-02-14 11:31:08', 1, 25, '1', '4-45x45', 1, ''),
(47, '2012-02-14 11:32:02', 1, 25, '2', '3-25x100', 1, ''),
(48, '2012-02-14 11:32:17', 1, 25, '1', '4-45x45', 2, 'Изменен width и height.'),
(49, '2012-02-14 11:33:24', 1, 25, '3', '4-30x30', 1, ''),
(50, '2012-02-14 11:34:25', 1, 25, '4', '3-45x45', 1, ''),
(51, '2012-02-14 11:34:47', 1, 25, '3', '4-30x30', 2, 'Изменен width и height.'),
(52, '2012-02-14 11:35:01', 1, 25, '4', '3-45x45', 2, 'Изменен width и height.'),
(53, '2012-02-14 11:35:30', 1, 25, '2', '3-25x100', 2, 'Изменен width и height.'),
(54, '2012-02-14 11:35:46', 1, 25, '1', '4-45x45', 2, 'Изменен width и height.'),
(55, '2012-02-14 11:36:43', 1, 25, '5', '6-30x30', 1, ''),
(56, '2012-02-14 11:38:07', 1, 25, '6', '6-45x45', 1, ''),
(57, '2012-02-14 11:38:50', 1, 25, '7', '5-25x100', 1, ''),
(58, '2012-02-14 11:39:26', 1, 25, '8', '9-30x30', 1, ''),
(59, '2012-02-14 11:40:05', 1, 25, '9', '9-45x45', 1, ''),
(60, '2012-02-14 11:40:38', 1, 25, '10', '3-30x30', 1, ''),
(61, '2012-02-14 11:41:22', 1, 25, '11', '3-25x50', 1, ''),
(62, '2012-02-14 14:53:10', 1, 26, '1', 'A052-1299', 1, ''),
(63, '2012-02-14 14:58:04', 1, 26, '1', 'A052-1299', 3, ''),
(64, '2012-02-14 14:58:16', 1, 26, '2', 'hfjhgfjf', 1, ''),
(65, '2012-02-14 14:58:51', 1, 26, '2', 'hfjhgfjf', 3, ''),
(66, '2012-02-14 14:59:15', 1, 26, '3', 'A052-1299', 1, ''),
(67, '2012-02-14 14:59:36', 1, 26, '4', 'A052-1819', 1, ''),
(68, '2012-02-14 14:59:54', 1, 26, '5', 'A052-2380', 1, ''),
(69, '2012-02-14 15:01:40', 1, 26, '6', 'A052-2381', 1, ''),
(70, '2012-02-14 15:02:12', 1, 27, '1', 'gold', 1, ''),
(71, '2012-02-14 15:02:25', 1, 27, '2', 'noel', 1, ''),
(72, '2012-02-14 15:02:42', 1, 27, '3', 'silver', 1, ''),
(73, '2012-02-17 10:03:57', 1, 29, '1', 'Стандартная натяжка', 1, ''),
(74, '2012-02-17 10:05:03', 1, 29, '2', 'Галерейная натяжка', 1, ''),
(75, '2012-02-17 10:06:01', 1, 29, '3', 'Холст без подрамника', 1, ''),
(76, '2012-02-17 10:38:02', 1, 29, '2', 'Галерейная натяжка', 2, 'Изменен koef.'),
(77, '2012-02-17 10:38:08', 1, 29, '3', 'Холст без подрамника', 2, 'Изменен koef.'),
(78, '2012-02-17 10:54:17', 1, 29, '1', 'Стандартная натяжка', 2, 'Изменен name.'),
(79, '2012-02-17 10:54:37', 1, 29, '2', 'Галерейная натяжка', 1, ''),
(80, '2012-02-17 10:54:54', 1, 29, '3', 'Холст без подрамника', 1, ''),
(81, '2012-02-17 23:58:44', 1, 30, '1', '30x20 см', 1, ''),
(82, '2012-02-17 23:59:04', 1, 30, '2', '40x30 см', 1, ''),
(83, '2012-02-17 23:59:19', 1, 30, '3', '50x40 см', 1, ''),
(84, '2012-02-17 23:59:37', 1, 30, '4', '60x40 см', 1, ''),
(85, '2012-02-17 23:59:57', 1, 30, '5', '70x50 см', 1, ''),
(86, '2012-02-18 00:00:17', 1, 30, '6', '90x60 см', 1, ''),
(87, '2012-02-18 00:00:35', 1, 30, '7', '30x30 см', 1, ''),
(88, '2012-02-18 00:00:51', 1, 30, '8', '40x40 см', 1, ''),
(89, '2012-02-18 00:01:11', 1, 30, '9', '50x50 см', 1, ''),
(90, '2012-02-18 00:01:35', 1, 30, '10', '60x60 см', 1, ''),
(91, '2012-02-18 00:01:53', 1, 30, '11', '70x70 см', 1, ''),
(92, '2012-02-18 00:02:12', 1, 30, '12', '90x90 см', 1, ''),
(93, '2012-02-19 09:00:03', 1, 30, '1', '30x20 см', 2, 'Изменен width и height.'),
(94, '2012-02-19 09:00:12', 1, 30, '2', '40x30 см', 2, 'Изменен width и height.'),
(95, '2012-02-19 09:00:19', 1, 30, '3', '50x40 см', 2, 'Изменен width и height.'),
(96, '2012-02-19 09:00:27', 1, 30, '4', '60x40 см', 2, 'Изменен width и height.'),
(97, '2012-02-19 09:00:38', 1, 30, '5', '70x50 см', 2, 'Изменен width и height.'),
(98, '2012-02-19 09:00:47', 1, 30, '6', '90x60 см', 2, 'Изменен width и height.'),
(99, '2012-02-19 09:00:56', 1, 30, '7', '30x30 см', 2, 'Изменен width и height.'),
(100, '2012-02-19 09:03:50', 1, 30, '8', '40x40 см', 2, 'Изменен width и height.'),
(101, '2012-02-19 09:04:02', 1, 30, '9', '50x50 см', 2, 'Изменен width и height.'),
(102, '2012-02-19 09:04:10', 1, 30, '10', '60x60 см', 2, 'Изменен width и height.'),
(103, '2012-02-19 09:04:19', 1, 30, '11', '70x70 см', 2, 'Изменен width и height.'),
(104, '2012-02-19 09:04:28', 1, 30, '12', '90x90 см', 2, 'Изменен width и height.'),
(105, '2012-02-19 18:36:20', 1, 32, '1', '12x12см', 1, ''),
(106, '2012-02-19 18:36:41', 1, 32, '1', '12x12 см', 2, 'Изменен name.'),
(107, '2012-02-19 18:37:02', 1, 32, '2', '20x20 см', 1, ''),
(108, '2012-02-19 18:37:26', 1, 32, '3', '30x30 см', 1, ''),
(109, '2012-02-19 18:37:31', 1, 32, '1', '12x12 см', 2, 'Изменен defsize.'),
(110, '2012-02-19 18:37:56', 1, 32, '4', '36x36 см', 1, ''),
(111, '2012-02-19 18:38:26', 1, 32, '5', '16x12 см', 1, ''),
(112, '2012-02-19 18:39:22', 1, 32, '6', '20x16 см', 1, ''),
(113, '2012-02-19 19:09:01', 1, 32, '7', '30x24 см', 1, ''),
(114, '2012-02-19 19:09:29', 1, 32, '8', '35x28 см', 1, ''),
(115, '2012-02-19 19:09:53', 1, 32, '9', '12x16 см', 1, ''),
(116, '2012-02-19 19:10:17', 1, 32, '10', '16x20 см', 1, ''),
(117, '2012-02-19 19:10:46', 1, 32, '11', '24x30 см', 1, ''),
(118, '2012-02-19 19:11:08', 1, 32, '12', '28x35 см', 1, ''),
(119, '2012-03-12 17:19:01', 1, 9, '1', '/about/ -- О нас', 2, 'Изменен sites.'),
(120, '2012-03-12 17:19:08', 1, 9, '2', '/faq/ -- Вопросы и ответы', 2, 'Изменен sites.'),
(121, '2012-03-12 17:19:15', 1, 9, '3', '/faq/pay/ -- Доставка и оплата', 2, 'Изменен sites.'),
(122, '2012-03-13 12:01:19', 1, 36, '1', 'Алматы', 1, ''),
(123, '2012-03-13 12:02:04', 1, 36, '2', 'Астана', 1, ''),
(124, '2012-03-13 12:02:19', 1, 36, '3', 'Караганда', 1, ''),
(125, '2012-03-13 12:02:58', 1, 36, '4', 'Шымкент', 1, ''),
(126, '2012-03-13 17:14:14', 1, 36, '2', 'Астана - 12.00', 2, 'Изменен defrow.'),
(127, '2012-03-13 17:14:34', 1, 36, '1', 'Алматы - 10.00', 2, 'Изменен defrow.'),
(128, '2012-03-21 08:32:33', 1, 29, '1', 'Белые поля', 2, 'Изменен name.'),
(129, '2012-03-21 08:32:52', 1, 29, '2', 'Обернутые поля', 2, 'Изменен name.'),
(130, '2012-03-21 08:33:04', 1, 29, '3', 'Холст без подрамника', 3, ''),
(131, '2012-03-22 18:17:10', 1, 37, '4', '1.0000', 1, ''),
(132, '2012-03-22 18:17:18', 1, 37, '4', '1.0000', 2, 'Изменен defrow.'),
(133, '2012-03-22 18:20:20', 1, 37, '5', '0.0068', 1, ''),
(134, '2012-03-23 08:13:41', 1, 38, '1', 'Казах почта 1', 1, ''),
(135, '2012-03-23 08:13:55', 1, 38, '2', 'Казах почта 2', 1, ''),
(136, '2012-03-23 08:17:19', 1, 39, '1', 'Россия', 1, ''),
(137, '2012-03-23 08:17:29', 1, 39, '2', 'Казахстан', 1, ''),
(138, '2012-03-23 08:23:24', 1, 40, '1', 'Москва', 1, ''),
(139, '2012-03-23 08:24:18', 1, 40, '2', 'Санкт-Петербург', 1, ''),
(140, '2012-03-23 08:24:29', 1, 40, '3', 'Орел', 1, ''),
(141, '2012-03-23 08:24:43', 1, 40, '4', 'Екатеринбург', 1, ''),
(142, '2012-03-23 08:24:57', 1, 40, '5', 'Нижний Новгород', 1, ''),
(143, '2012-03-23 08:25:11', 1, 40, '6', 'Архангельск', 1, ''),
(144, '2012-03-23 08:25:50', 1, 40, '7', 'Алматы', 1, ''),
(145, '2012-03-23 08:26:00', 1, 40, '8', 'Астана', 1, ''),
(146, '2012-03-23 08:26:11', 1, 40, '9', 'Караганда', 1, ''),
(147, '2012-03-23 08:26:25', 1, 40, '10', 'Шымкент', 1, ''),
(148, '2012-03-23 08:50:30', 1, 40, '7', 'Алматы', 2, 'Ни одно поле не изменено.'),
(149, '2012-03-23 08:54:27', 1, 40, '7', 'Алматы', 2, 'Ни одно поле не изменено.'),
(150, '2012-03-23 11:48:21', 1, 38, '1', 'EMS', 2, 'Изменен name.'),
(151, '2012-03-23 11:48:30', 1, 38, '2', 'Казпочта', 2, 'Изменен name.'),
(152, '2012-03-23 14:06:55', 1, 36, '1', 'EMS - Алматы - 150.0', 1, ''),
(153, '2012-03-23 16:54:04', 1, 36, '1', 'EMS - Алматы - 150.0', 2, 'Ни одно поле не изменено.'),
(154, '2012-03-23 16:54:23', 1, 36, '2', 'EMS - Астана - 155.0', 1, ''),
(155, '2012-03-23 16:54:38', 1, 36, '3', 'EMS - Караганда - 160.0', 1, ''),
(156, '2012-03-23 16:55:00', 1, 36, '4', 'EMS - Шымкент - 165.0', 1, ''),
(157, '2012-03-23 16:55:22', 1, 36, '5', 'Казпочта - Алматы - 200.0', 1, ''),
(158, '2012-03-23 16:55:34', 1, 36, '6', 'Казпочта - Астана - 210.0', 1, ''),
(159, '2012-03-23 16:55:46', 1, 36, '7', 'Казпочта - Караганда - 205.0', 1, ''),
(160, '2012-03-23 16:56:00', 1, 36, '8', 'Казпочта - Шымкент - 201.0', 1, ''),
(161, '2012-03-23 16:56:26', 1, 36, '9', 'EMS - Архангельск - 300.0', 1, ''),
(162, '2012-03-23 16:56:48', 1, 36, '10', 'EMS - Екатеринбург - 305.0', 1, ''),
(163, '2012-03-23 17:04:51', 1, 36, '11', 'Казпочта - Екатеринбург - 300.0', 1, ''),
(164, '2012-03-23 17:05:25', 1, 36, '12', 'Казпочта - Москва - 299.0', 1, ''),
(165, '2012-03-23 17:05:43', 1, 36, '13', 'Казпочта - Архангельск - 350.0', 1, '');

-- --------------------------------------------------------

--
-- Структура таблицы `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=41 ;

--
-- Дамп данных таблицы `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `name`, `app_label`, `model`) VALUES
(1, 'permission', 'auth', 'permission'),
(2, 'group', 'auth', 'group'),
(3, 'user', 'auth', 'user'),
(4, 'message', 'auth', 'message'),
(5, 'content type', 'contenttypes', 'contenttype'),
(6, 'session', 'sessions', 'session'),
(7, 'site', 'sites', 'site'),
(8, 'log entry', 'admin', 'logentry'),
(9, 'flat page', 'flatpages', 'flatpage'),
(10, 'user profile', 'account', 'userprofile'),
(12, 'captcha store', 'captcha', 'captchastore'),
(15, 'mosaic option', 'mosaic', 'mosaicoption'),
(21, 'Размеры и цены', 'mosaic', 'mosaicprice'),
(23, 'order', 'cart', 'order'),
(24, 'Список заказов', 'cart', 'orderoption'),
(25, 'puzzle size', 'puzzle', 'puzzlesize'),
(26, 'Рамки', 'common', 'frames'),
(27, 'Упаковки', 'common', 'packaging'),
(28, 'puzzle', 'puzzle', 'puzzle'),
(29, 'Натяжка', 'common', 'stretch'),
(30, 'Фото на холсте - Список размеров и цен', 'crop', 'cropsize'),
(31, 'crop', 'crop', 'crop'),
(32, 'Список размеров и цен', 'mosaic', 'mosaicsize'),
(33, 'mosaic', 'mosaic', 'mosaic'),
(34, 'Альбомы', 'gallery', 'album'),
(35, 'Изображение', 'gallery', 'images'),
(36, 'Доставка', 'cart', 'shiping'),
(37, 'Валюта', 'cart', 'currency'),
(38, 'shiping type', 'cart', 'shipingtype'),
(39, 'Страны', 'cart', 'countries'),
(40, 'Города', 'cart', 'cities');

-- --------------------------------------------------------

--
-- Структура таблицы `django_flatpage`
--

CREATE TABLE IF NOT EXISTS `django_flatpage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(100) NOT NULL,
  `title` varchar(200) NOT NULL,
  `content` longtext NOT NULL,
  `enable_comments` tinyint(1) NOT NULL,
  `template_name` varchar(70) NOT NULL,
  `registration_required` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_flatpage_a4b49ab` (`url`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=4 ;

--
-- Дамп данных таблицы `django_flatpage`
--

INSERT INTO `django_flatpage` (`id`, `url`, `title`, `content`, `enable_comments`, `template_name`, `registration_required`) VALUES
(1, '/about/', 'О нас', '<p>\r\n	Интернет магазин &laquo;NaHolste.kz&raquo; работает на базе Центра Широкоформатной Печати &laquo;Мегапринт&raquo; - <a href="http://www.megaprint.kz" target="_blank">www.megaprint.kz&nbsp;</a></p>\r\n<div>\r\n	&laquo;Мегапринт&raquo; работает на рынке наружной рекламы с 2003 года.</div>\r\n<div>\r\n	&nbsp;</div>\r\n<div>\r\n	Мы имеем огромный опыт работы в сфере наружной рекламы и широкоформатной печати.</div>\r\n<div>\r\n	&nbsp;</div>\r\n<div>\r\n	Печать картин производится японскими высококачественными широкоформатными принтерами &laquo;Roland&raquo;.</div>\r\n<div>\r\n	&nbsp;</div>\r\n<div>\r\n	Наши дизайнеры проведут всю работу, связанную с цветовой коррекцией изображения.</div>\r\n', 0, '', 0),
(2, '/faq/', 'Вопросы и ответы', '<p>\r\n	Вопросы и ответы</p>\r\n', 0, '', 0),
(3, '/faq/pay/', 'Доставка и оплата', '<p>\r\n	Доставка и оплата</p>\r\n', 0, '', 0);

-- --------------------------------------------------------

--
-- Структура таблицы `django_flatpage_sites`
--

CREATE TABLE IF NOT EXISTS `django_flatpage_sites` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `flatpage_id` int(11) NOT NULL,
  `site_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `flatpage_id` (`flatpage_id`,`site_id`),
  KEY `django_flatpage_sites_21210108` (`flatpage_id`),
  KEY `django_flatpage_sites_6223029` (`site_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=5 ;

--
-- Дамп данных таблицы `django_flatpage_sites`
--

INSERT INTO `django_flatpage_sites` (`id`, `flatpage_id`, `site_id`) VALUES
(2, 1, 1),
(3, 2, 1),
(4, 3, 1);

-- --------------------------------------------------------

--
-- Структура таблицы `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_3da3d3d8` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('2421f59fbe417f724e4c0a576314b751', 'OGM1NjExOWU0NjQxOWVlZmU3NmYwMzMyNDVkMTc2NjM0MmZkNjQzMDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n', '2012-01-01 15:20:55'),
('30cda988e696cbed383c8629fcbb4e91', 'YzE3MmE3ZDJkYTcwY2NjMWIzMzE0MDY3MWFmMGI4YjI5M2YwODZjNjqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJVBGNhcnRxBV1xBnUu\n', '2012-02-28 09:22:23'),
('41c57cb22977c6ae86dc7aa288635962', 'Nzg1NGZhZjI2YzFlMjU2YjUyNjM2YWE1YTM5MTA4NzBkMDEzNmM0MTqAAn1xAVUEY2FydHECXXED\ncy4=\n', '2012-03-31 08:51:36'),
('43794e334b27d0e457007bfaecce8e07', 'OGM1NjExOWU0NjQxOWVlZmU3NmYwMzMyNDVkMTc2NjM0MmZkNjQzMDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n', '2012-01-17 13:31:55'),
('5863793c76fc020da2356b718a5d8d8b', 'YjQwYjUzMzc4MWE0OGU2ZmY3YTM2YTVhNTRmNWVlY2FjNjdmY2I5MTqAAn1xAShVBGNhcnRxAl1x\nA1UNX2F1dGhfdXNlcl9pZHEEigECVRJfYXV0aF91c2VyX2JhY2tlbmRxBVUpZGphbmdvLmNvbnRy\naWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmRxBnUu\n', '2012-03-08 12:22:42'),
('5a44398dda47abe879294fe1abd862bc', 'NjIwMGVjOTgwMmQxMmNiYTNiNTk3ZjJjYzhmNzE2YmVlN2MwZTQ5YTqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n', '2012-02-07 22:39:15'),
('6f89bf7bb050c67fdc272d1e2d45da3b', 'OGM1NjExOWU0NjQxOWVlZmU3NmYwMzMyNDVkMTc2NjM0MmZkNjQzMDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n', '2012-02-05 14:25:25'),
('70987a4e3ad332cff9d378e8a7d78677', 'Nzg1NGZhZjI2YzFlMjU2YjUyNjM2YWE1YTM5MTA4NzBkMDEzNmM0MTqAAn1xAVUEY2FydHECXXED\ncy4=\n', '2012-03-31 08:45:27'),
('7b46525650d3c56d798e18127a2c7b3d', 'N2E0NzRkMzI1MDAxZDRjOGVjODJkNDhlNGUxODA4N2Y2NDkxMWIxOTqAAn1xAShVB3NoaXBpbmdx\nAooBC1UNX2F1dGhfdXNlcl9pZHEDigEBVQRjYXJ0cQRdcQUofXEGKFUCaWRxB0sCVQRhdXRocQiI\nVQF0SwF1fXEJKFUCaWRxCksBVQRhdXRocQuIVQF0SwF1ZVULcHJvZ3Jlc3NiYXJxDH1xDShVCHVw\nbG9hZGVkcQ5LAFUGbGVuZ3RocQ9NHgVVBHN0b3BxEEsAdVUSX2F1dGhfdXNlcl9iYWNrZW5kcRFV\nKWRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kcRJVBW9yZGVycROKAQR1\nLg==\n', '2012-04-08 20:44:52'),
('918f4b7701a97240336649021549adb7', 'Nzg1NGZhZjI2YzFlMjU2YjUyNjM2YWE1YTM5MTA4NzBkMDEzNmM0MTqAAn1xAVUEY2FydHECXXED\ncy4=\n', '2012-03-31 08:43:22'),
('9689d9289d6fedd5154b7cac01d5b1c7', 'Nzg1NGZhZjI2YzFlMjU2YjUyNjM2YWE1YTM5MTA4NzBkMDEzNmM0MTqAAn1xAVUEY2FydHECXXED\ncy4=\n', '2012-03-31 08:51:21'),
('98d638b06a51afc6a36d6567df2a5059', 'MzI1OWRmMTM0ZjQyZTc5NTM1YTVkZTkwNjA4N2NmYjZiMDU1N2MxMDqAAn1xAS4=\n', '2012-03-27 12:38:08'),
('9e6d76ac93812e3821ab5ff3497adf6a', 'MmRlNTczMjQ5ZTkyMTllZjI3YTgxNGUyZDllZmYzOWFhMjA5N2EwZjqAAn1xAShVBGNhcnRxAl1x\nA1ULcHJvZ3Jlc3NiYXJxBE51Lg==\n', '2012-04-03 21:12:43'),
('a466c1eae6d26889928b4d362c5e50e0', 'Nzg1NGZhZjI2YzFlMjU2YjUyNjM2YWE1YTM5MTA4NzBkMDEzNmM0MTqAAn1xAVUEY2FydHECXXED\ncy4=\n', '2012-02-28 10:19:43'),
('acea9fc00081a76a18439b25ef190c34', 'Nzg1NGZhZjI2YzFlMjU2YjUyNjM2YWE1YTM5MTA4NzBkMDEzNmM0MTqAAn1xAVUEY2FydHECXXED\ncy4=\n', '2012-03-31 08:43:08'),
('c4b7315883161ef1eaa9c45f582b8d0c', 'MDFkZjE0ZDQ2MzhmY2YwYmU2M2ZjNTY4MjA5NGI4ZDU5NzhiZGVkOTqAAn1xAVUEY2FydHECXXED\nKH1xBChVBm9wdF9pZHEFWCAAAAA5MThkNzJjM2FkMDQzODM1OGQ1MjUyYmM5NGFkNDI5OXEGVQNy\nZWdxB4hVB3R5cGVfaWRxCEsBdX1xCShVBm9wdF9pZHEKWCAAAAA3MTEzYzRhNDgyMGIzZmIyNjZm\nMGQwNjExNzAzYjc3M3ELVQNyZWdxDIhVB3R5cGVfaWRxDUsCdX1xDihVBm9wdF9pZHEPSwFVA3Jl\nZ3EQiFUHdHlwZV9pZHERSwN1fXESKFUGb3B0X2lkcRNYIAAAADYwZjViYTVmODE3YWY2NmE5YWNm\nYWJkNDE1NzhmNTU0cRRVA3JlZ3EViFUHdHlwZV9pZHEWSwF1fXEXKFUGb3B0X2lkcRhYIAAAADEy\nMjNjNTM3YjdkYzI1MmQ3YzAyM2JlODQzMGJhODUzcRlVA3JlZ3EaiFUHdHlwZV9pZHEbSwF1fXEc\nKFUGb3B0X2lkcR1YIAAAADE3ZTdmMjY2OTUzYmQ3MTlmOTQyZDFjMThjNjRlOTlkcR5VA3JlZ3Ef\niFUHdHlwZV9pZHEgSwF1fXEhKFUGb3B0X2lkcSJLAVUDcmVncSOJVQd0eXBlX2lkcSRLA3V9cSUo\nVQZvcHRfaWRxJlggAAAANmE1MDdjMGVlODI1ZTZmZTU3ZTJmNTE5YmU4ZDMyYWFxJ1UDcmVncSiJ\nVQd0eXBlX2lkcSlLAXV9cSooVQZvcHRfaWRxK1ggAAAAY2IzOGEzZWY1NzdiYzljZTc4MTFiN2Zm\nYThiMjc0NTlxLFUDcmVncS2JVQd0eXBlX2lkcS5LAnVlcy4=\n', '2012-02-19 09:38:05'),
('f61b0696ac60492fe5b028ad5f185d73', 'NWQ4ZjViMTZmMjA5MmI2ZTVmOWM4ZjMyZWRiMjlkZjEwZWQ2N2FkMTqAAn1xAShVCnRlc3Rjb29r\naWVxAlUGd29ya2VkcQNVEl9hdXRoX3VzZXJfYmFja2VuZHEEVSlkamFuZ28uY29udHJpYi5hdXRo\nLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEFVQ1fYXV0aF91c2VyX2lkcQaKAQJ1Lg==\n', '2011-12-24 12:51:31'),
('fd47239d8b5d82e2b576c43f3c9fcc01', 'OGM1NjExOWU0NjQxOWVlZmU3NmYwMzMyNDVkMTc2NjM0MmZkNjQzMDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n', '2012-01-11 17:45:49'),
('fff1a7c42843a17756c84a4e552dd973', 'MDkyOGM3ODQwNmNkMzRmMzBmYjliYTNiMjAyOWQ5N2FjZDg1OTA1NjqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJVBGNhcnRxBV1xBlUFb3JkZXJxB4oBAnUu\n', '2012-03-13 10:17:59');

-- --------------------------------------------------------

--
-- Структура таблицы `django_site`
--

CREATE TABLE IF NOT EXISTS `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

--
-- Дамп данных таблицы `django_site`
--

INSERT INTO `django_site` (`id`, `domain`, `name`) VALUES
(1, '127.0.0.1:8000', '127.0.0.1:8000');

-- --------------------------------------------------------

--
-- Структура таблицы `gallery_album`
--

CREATE TABLE IF NOT EXISTS `gallery_album` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `img` varchar(150) NOT NULL,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=18 ;

--
-- Дамп данных таблицы `gallery_album`
--

INSERT INTO `gallery_album` (`id`, `img`, `name`) VALUES
(1, 'albums/Abstrakcii1.jpg', 'Абстракции1'),
(2, 'albums/vodnyi_mir.jpg', 'водный мир'),
(3, 'albums/gorodskie_panoramy.jpg', 'городские панорамы'),
(4, 'albums/zhivotnyi_mir.jpg', 'животный мир'),
(5, 'albums/zakat.jpg', 'закат'),
(6, 'albums/zima.jpg', 'зима'),
(7, 'albums/kapelka.jpg', 'капелька росы'),
(8, 'albums/krasota_prirody.jpg', 'красота природы'),
(9, 'albums/leto.jpg', 'лето'),
(10, 'albums/mir_romashek.jpg', 'мир ромашек'),
(11, 'albums/nochnoy_gorod.jpg', 'ночной город'),
(12, 'albums/osen.jpg', 'осень'),
(13, 'albums/prodykty.jpg', 'продукты'),
(14, 'albums/tekstury.jpg', 'текстура'),
(15, 'albums/tropicheskiy_ray.jpg', 'тропический рай'),
(16, 'albums/furnitura_interiera.jpg', 'фурнитура интерьера'),
(17, 'albums/cvetochnyi_ray.jpg', 'цветочный рай');

-- --------------------------------------------------------

--
-- Структура таблицы `gallery_images`
--

CREATE TABLE IF NOT EXISTS `gallery_images` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `album_id` int(11) NOT NULL,
  `img` varchar(150) NOT NULL,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `gallery_images_1293c648` (`album_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

--
-- Дамп данных таблицы `gallery_images`
--


-- --------------------------------------------------------

--
-- Структура таблицы `mosaic_mosaic`
--

CREATE TABLE IF NOT EXISTS `mosaic_mosaic` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `nouser` varchar(32) NOT NULL,
  `table_type` int(11) NOT NULL,
  `img_size_id` int(11) DEFAULT NULL,
  `img_effect` smallint(6) NOT NULL,
  `qty` int(11) NOT NULL,
  `frame_id` int(11) DEFAULT NULL,
  `packaging_id` int(11) DEFAULT NULL,
  `f_0` varchar(32) NOT NULL,
  `f_1` varchar(32) NOT NULL,
  `f_2` varchar(32) NOT NULL,
  `f_3` varchar(32) NOT NULL,
  `f_4` varchar(32) NOT NULL,
  `f_5` varchar(32) NOT NULL,
  `f_6` varchar(32) NOT NULL,
  `f_7` varchar(32) NOT NULL,
  `f_8` varchar(32) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `created` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `mosaic_mosaic_403f60f` (`user_id`),
  KEY `mosaic_mosaic_5f519445` (`img_size_id`),
  KEY `mosaic_mosaic_7b89a14a` (`frame_id`),
  KEY `mosaic_mosaic_412518f8` (`packaging_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

--
-- Дамп данных таблицы `mosaic_mosaic`
--


-- --------------------------------------------------------

--
-- Структура таблицы `mosaic_mosaicsize`
--

CREATE TABLE IF NOT EXISTS `mosaic_mosaicsize` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `price` double NOT NULL,
  `width` int(11) NOT NULL,
  `height` int(11) NOT NULL,
  `defsize` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=13 ;

--
-- Дамп данных таблицы `mosaic_mosaicsize`
--

INSERT INTO `mosaic_mosaicsize` (`id`, `name`, `price`, `width`, `height`, `defsize`) VALUES
(1, '12x12 см', 10, 12, 12, 1),
(2, '20x20 см', 11, 20, 20, 0),
(3, '30x30 см', 12, 30, 30, 0),
(4, '36x36 см', 13, 36, 36, 0),
(5, '16x12 см', 15, 16, 12, 0),
(6, '20x16 см', 16, 20, 16, 0),
(7, '30x24 см', 14, 30, 24, 0),
(8, '35x28 см', 17, 35, 28, 0),
(9, '12x16 см', 18, 12, 16, 0),
(10, '16x20 см', 19, 16, 20, 0),
(11, '24x30 см', 20, 24, 30, 0),
(12, '28x35 см', 21, 28, 35, 0);

-- --------------------------------------------------------

--
-- Структура таблицы `puzzle_puzzle`
--

CREATE TABLE IF NOT EXISTS `puzzle_puzzle` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `nouser` varchar(32) NOT NULL,
  `img` varchar(32) NOT NULL,
  `img_stretch_id` int(11) NOT NULL,
  `img_size_id` int(11) DEFAULT NULL,
  `img_effect` smallint(6) NOT NULL,
  `qty` int(11) NOT NULL,
  `frame_id` int(11) DEFAULT NULL,
  `packaging_id` int(11) DEFAULT NULL,
  `x1` int(11) NOT NULL,
  `y1` int(11) NOT NULL,
  `x2` int(11) NOT NULL,
  `y2` int(11) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `created` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `puzzle_puzzle_403f60f` (`user_id`),
  KEY `puzzle_puzzle_470d0678` (`img_stretch_id`),
  KEY `puzzle_puzzle_5f519445` (`img_size_id`),
  KEY `puzzle_puzzle_7b89a14a` (`frame_id`),
  KEY `puzzle_puzzle_412518f8` (`packaging_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

--
-- Дамп данных таблицы `puzzle_puzzle`
--


-- --------------------------------------------------------

--
-- Структура таблицы `puzzle_puzzlesize`
--

CREATE TABLE IF NOT EXISTS `puzzle_puzzlesize` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `img` varchar(150) NOT NULL,
  `price` double NOT NULL,
  `width` int(11) NOT NULL,
  `height` int(11) NOT NULL,
  `defsize` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=12 ;

--
-- Дамп данных таблицы `puzzle_puzzlesize`
--

INSERT INTO `puzzle_puzzlesize` (`id`, `name`, `img`, `price`, `width`, `height`, `defsize`) VALUES
(1, '4-45x45', 'puzzle_size/4-45x45.jpg', 10, 90, 90, 1),
(2, '3-25x100', 'puzzle_size/3-25x100.jpg', 11, 75, 100, 0),
(3, '4-30x30', 'puzzle_size/4-30x30.jpg', 12, 60, 60, 0),
(4, '3-45x45', 'puzzle_size/3-45x45.jpg', 13, 135, 45, 0),
(5, '6-30x30', 'puzzle_size/6-30x30.jpg', 14, 90, 60, 0),
(6, '6-45x45', 'puzzle_size/6-45x45.jpg', 15, 135, 90, 0),
(7, '5-25x100', 'puzzle_size/5-25x100.jpg', 16, 125, 100, 0),
(8, '9-30x30', 'puzzle_size/9-30x30.jpg', 17, 270, 270, 0),
(9, '9-45x45', 'puzzle_size/9-45x45.jpg', 18, 405, 405, 0),
(10, '3-30x30', 'puzzle_size/9-30x30_1.jpg', 19, 90, 90, 0),
(11, '3-25x50', 'puzzle_size/3-25x50.jpg', 20, 75, 50, 0);

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `account_userprofile`
--
ALTER TABLE `account_userprofile`
  ADD CONSTRAINT `user_id_refs_id_5ef8aa5f` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Ограничения внешнего ключа таблицы `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `group_id_refs_id_3cea63fe` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `permission_id_refs_id_5886d21f` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Ограничения внешнего ключа таблицы `auth_message`
--
ALTER TABLE `auth_message`
  ADD CONSTRAINT `user_id_refs_id_650f49a6` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Ограничения внешнего ключа таблицы `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `content_type_id_refs_id_728de91f` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Ограничения внешнего ключа таблицы `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `group_id_refs_id_f116770` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `user_id_refs_id_7ceef80f` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Ограничения внешнего ключа таблицы `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `permission_id_refs_id_67e79cb` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `user_id_refs_id_dfbab7d` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Ограничения внешнего ключа таблицы `cart_cities`
--
ALTER TABLE `cart_cities`
  ADD CONSTRAINT `country_id_refs_id_66c708c7` FOREIGN KEY (`country_id`) REFERENCES `cart_countries` (`id`);

--
-- Ограничения внешнего ключа таблицы `cart_order`
--
ALTER TABLE `cart_order`
  ADD CONSTRAINT `user_id_refs_id_52e4a147` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Ограничения внешнего ключа таблицы `cart_orderoption`
--
ALTER TABLE `cart_orderoption`
  ADD CONSTRAINT `order_id_refs_id_30b66738` FOREIGN KEY (`order_id`) REFERENCES `cart_order` (`id`);

--
-- Ограничения внешнего ключа таблицы `cart_shiping`
--
ALTER TABLE `cart_shiping`
  ADD CONSTRAINT `city_id_refs_id_4048a38d` FOREIGN KEY (`city_id`) REFERENCES `cart_cities` (`id`),
  ADD CONSTRAINT `country_id_refs_id_271d0b79` FOREIGN KEY (`country_id`) REFERENCES `cart_countries` (`id`),
  ADD CONSTRAINT `shiping_type_id_refs_id_495b5a51` FOREIGN KEY (`shiping_type_id`) REFERENCES `cart_shipingtype` (`id`);

--
-- Ограничения внешнего ключа таблицы `crop_crop`
--
ALTER TABLE `crop_crop`
  ADD CONSTRAINT `frame_id_refs_id_12ccab52` FOREIGN KEY (`frame_id`) REFERENCES `common_frames` (`id`),
  ADD CONSTRAINT `img_size_id_refs_id_217421de` FOREIGN KEY (`img_size_id`) REFERENCES `crop_cropsize` (`id`),
  ADD CONSTRAINT `img_stretch_id_refs_id_4ea590f4` FOREIGN KEY (`img_stretch_id`) REFERENCES `common_stretch` (`id`),
  ADD CONSTRAINT `packaging_id_refs_id_653158e8` FOREIGN KEY (`packaging_id`) REFERENCES `common_packaging` (`id`),
  ADD CONSTRAINT `user_id_refs_id_35e705a` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Ограничения внешнего ключа таблицы `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `content_type_id_refs_id_288599e6` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `user_id_refs_id_c8665aa` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Ограничения внешнего ключа таблицы `django_flatpage_sites`
--
ALTER TABLE `django_flatpage_sites`
  ADD CONSTRAINT `flatpage_id_refs_id_3f17b0a6` FOREIGN KEY (`flatpage_id`) REFERENCES `django_flatpage` (`id`),
  ADD CONSTRAINT `site_id_refs_id_4e3eeb57` FOREIGN KEY (`site_id`) REFERENCES `django_site` (`id`);

--
-- Ограничения внешнего ключа таблицы `gallery_images`
--
ALTER TABLE `gallery_images`
  ADD CONSTRAINT `album_id_refs_id_2e2e3bbf` FOREIGN KEY (`album_id`) REFERENCES `gallery_album` (`id`);

--
-- Ограничения внешнего ключа таблицы `mosaic_mosaic`
--
ALTER TABLE `mosaic_mosaic`
  ADD CONSTRAINT `frame_id_refs_id_539282de` FOREIGN KEY (`frame_id`) REFERENCES `common_frames` (`id`),
  ADD CONSTRAINT `img_size_id_refs_id_4bfc4cf6` FOREIGN KEY (`img_size_id`) REFERENCES `mosaic_mosaicsize` (`id`),
  ADD CONSTRAINT `packaging_id_refs_id_4727e15c` FOREIGN KEY (`packaging_id`) REFERENCES `common_packaging` (`id`),
  ADD CONSTRAINT `user_id_refs_id_46b8588a` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Ограничения внешнего ключа таблицы `puzzle_puzzle`
--
ALTER TABLE `puzzle_puzzle`
  ADD CONSTRAINT `frame_id_refs_id_440b29da` FOREIGN KEY (`frame_id`) REFERENCES `common_frames` (`id`),
  ADD CONSTRAINT `img_size_id_refs_id_1a5fc82a` FOREIGN KEY (`img_size_id`) REFERENCES `puzzle_puzzlesize` (`id`),
  ADD CONSTRAINT `img_stretch_id_refs_id_a88c608` FOREIGN KEY (`img_stretch_id`) REFERENCES `common_stretch` (`id`),
  ADD CONSTRAINT `packaging_id_refs_id_1d4661ec` FOREIGN KEY (`packaging_id`) REFERENCES `common_packaging` (`id`),
  ADD CONSTRAINT `user_id_refs_id_304c482e` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
