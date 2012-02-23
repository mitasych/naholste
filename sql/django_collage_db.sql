-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Хост: localhost
-- Время создания: Фев 23 2012 г., 11:27
-- Версия сервера: 5.5.8
-- Версия PHP: 5.3.5

SET FOREIGN_KEY_CHECKS=0;
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

CREATE TABLE `account_userprofile` (
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

CREATE TABLE `auth_group` (
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

CREATE TABLE `auth_group_permissions` (
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

CREATE TABLE `auth_message` (
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

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_1bb8f392` (`content_type_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=100 ;

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
(99, 'Can delete mosaic', 33, 'delete_mosaic');

-- --------------------------------------------------------

--
-- Структура таблицы `auth_user`
--

CREATE TABLE `auth_user` (
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
(1, 'aries.ua@gmail.com', '', '', 'aries.ua@gmail.com', 'sha1$d0bcd$9bbf973b02708ff46813b005f6f00ad505c19ad8', 1, 1, 1, '2012-02-19 18:35:34', '2011-12-09 10:00:59'),
(2, 'aries.forum@gmail.com', '', '', 'aries.forum@gmail.com', 'sha1$72e79$fc2e36ea86668febe872ca776ae4504b33359300', 0, 1, 0, '2012-02-22 11:39:35', '2011-12-09 10:02:30');

-- --------------------------------------------------------

--
-- Структура таблицы `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
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

CREATE TABLE `auth_user_user_permissions` (
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
-- Структура таблицы `cart_order`
--

CREATE TABLE `cart_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `nouser` varchar(32) NOT NULL,
  `price` double NOT NULL,
  `shiping_price` double NOT NULL,
  `address` varchar(255) NOT NULL,
  `email` varchar(100) NOT NULL,
  `name` varchar(255) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `created` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cart_order_403f60f` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

--
-- Дамп данных таблицы `cart_order`
--


-- --------------------------------------------------------

--
-- Структура таблицы `cart_orderoption`
--

CREATE TABLE `cart_orderoption` (
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
-- Структура таблицы `common_frames`
--

CREATE TABLE `common_frames` (
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

CREATE TABLE `common_packaging` (
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

CREATE TABLE `common_stretch` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `descr` varchar(255) NOT NULL,
  `koef` double NOT NULL,
  `defrow` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=4 ;

--
-- Дамп данных таблицы `common_stretch`
--

INSERT INTO `common_stretch` (`id`, `name`, `descr`, `koef`, `defrow`) VALUES
(1, 'Стандартная натяжка', '', 1, 1),
(2, 'Галерейная натяжка', 'Обратите внимание! Часть изображения под светлой рамкой, будет завернута на торец подрамника.', 1, 0),
(3, 'Холст без подрамника', '', 1, 0);

-- --------------------------------------------------------

--
-- Структура таблицы `crop_crop`
--

CREATE TABLE `crop_crop` (
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
  `created` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `crop_crop_403f60f` (`user_id`),
  KEY `crop_crop_470d0678` (`img_stretch_id`),
  KEY `crop_crop_5f519445` (`img_size_id`),
  KEY `crop_crop_7b89a14a` (`frame_id`),
  KEY `crop_crop_412518f8` (`packaging_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

--
-- Дамп данных таблицы `crop_crop`
--


-- --------------------------------------------------------

--
-- Структура таблицы `crop_cropsize`
--

CREATE TABLE `crop_cropsize` (
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

CREATE TABLE `django_admin_log` (
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
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=119 ;

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
(118, '2012-02-19 19:11:08', 1, 32, '12', '28x35 см', 1, '');

-- --------------------------------------------------------

--
-- Структура таблицы `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=34 ;

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
(33, 'mosaic', 'mosaic', 'mosaic');

-- --------------------------------------------------------

--
-- Структура таблицы `django_flatpage`
--

CREATE TABLE `django_flatpage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(100) NOT NULL,
  `title` varchar(200) NOT NULL,
  `content` longtext NOT NULL,
  `enable_comments` tinyint(1) NOT NULL,
  `template_name` varchar(70) NOT NULL,
  `registration_required` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_flatpage_a4b49ab` (`url`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

--
-- Дамп данных таблицы `django_flatpage`
--

INSERT INTO `django_flatpage` (`id`, `url`, `title`, `content`, `enable_comments`, `template_name`, `registration_required`) VALUES
(1, '/about/', 'О сайте', 'COMING SOON...', 0, '', 0);

-- --------------------------------------------------------

--
-- Структура таблицы `django_flatpage_sites`
--

CREATE TABLE `django_flatpage_sites` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `flatpage_id` int(11) NOT NULL,
  `site_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `flatpage_id` (`flatpage_id`,`site_id`),
  KEY `django_flatpage_sites_21210108` (`flatpage_id`),
  KEY `django_flatpage_sites_6223029` (`site_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

--
-- Дамп данных таблицы `django_flatpage_sites`
--

INSERT INTO `django_flatpage_sites` (`id`, `flatpage_id`, `site_id`) VALUES
(1, 1, 1);

-- --------------------------------------------------------

--
-- Структура таблицы `django_session`
--

CREATE TABLE `django_session` (
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
('43794e334b27d0e457007bfaecce8e07', 'OGM1NjExOWU0NjQxOWVlZmU3NmYwMzMyNDVkMTc2NjM0MmZkNjQzMDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n', '2012-01-17 13:31:55'),
('5863793c76fc020da2356b718a5d8d8b', 'YjQwYjUzMzc4MWE0OGU2ZmY3YTM2YTVhNTRmNWVlY2FjNjdmY2I5MTqAAn1xAShVBGNhcnRxAl1x\nA1UNX2F1dGhfdXNlcl9pZHEEigECVRJfYXV0aF91c2VyX2JhY2tlbmRxBVUpZGphbmdvLmNvbnRy\naWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmRxBnUu\n', '2012-03-08 12:22:42'),
('5a44398dda47abe879294fe1abd862bc', 'NjIwMGVjOTgwMmQxMmNiYTNiNTk3ZjJjYzhmNzE2YmVlN2MwZTQ5YTqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n', '2012-02-07 22:39:15'),
('6f89bf7bb050c67fdc272d1e2d45da3b', 'OGM1NjExOWU0NjQxOWVlZmU3NmYwMzMyNDVkMTc2NjM0MmZkNjQzMDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n', '2012-02-05 14:25:25'),
('a466c1eae6d26889928b4d362c5e50e0', 'Nzg1NGZhZjI2YzFlMjU2YjUyNjM2YWE1YTM5MTA4NzBkMDEzNmM0MTqAAn1xAVUEY2FydHECXXED\ncy4=\n', '2012-02-28 10:19:43'),
('c4b7315883161ef1eaa9c45f582b8d0c', 'MDFkZjE0ZDQ2MzhmY2YwYmU2M2ZjNTY4MjA5NGI4ZDU5NzhiZGVkOTqAAn1xAVUEY2FydHECXXED\nKH1xBChVBm9wdF9pZHEFWCAAAAA5MThkNzJjM2FkMDQzODM1OGQ1MjUyYmM5NGFkNDI5OXEGVQNy\nZWdxB4hVB3R5cGVfaWRxCEsBdX1xCShVBm9wdF9pZHEKWCAAAAA3MTEzYzRhNDgyMGIzZmIyNjZm\nMGQwNjExNzAzYjc3M3ELVQNyZWdxDIhVB3R5cGVfaWRxDUsCdX1xDihVBm9wdF9pZHEPSwFVA3Jl\nZ3EQiFUHdHlwZV9pZHERSwN1fXESKFUGb3B0X2lkcRNYIAAAADYwZjViYTVmODE3YWY2NmE5YWNm\nYWJkNDE1NzhmNTU0cRRVA3JlZ3EViFUHdHlwZV9pZHEWSwF1fXEXKFUGb3B0X2lkcRhYIAAAADEy\nMjNjNTM3YjdkYzI1MmQ3YzAyM2JlODQzMGJhODUzcRlVA3JlZ3EaiFUHdHlwZV9pZHEbSwF1fXEc\nKFUGb3B0X2lkcR1YIAAAADE3ZTdmMjY2OTUzYmQ3MTlmOTQyZDFjMThjNjRlOTlkcR5VA3JlZ3Ef\niFUHdHlwZV9pZHEgSwF1fXEhKFUGb3B0X2lkcSJLAVUDcmVncSOJVQd0eXBlX2lkcSRLA3V9cSUo\nVQZvcHRfaWRxJlggAAAANmE1MDdjMGVlODI1ZTZmZTU3ZTJmNTE5YmU4ZDMyYWFxJ1UDcmVncSiJ\nVQd0eXBlX2lkcSlLAXV9cSooVQZvcHRfaWRxK1ggAAAAY2IzOGEzZWY1NzdiYzljZTc4MTFiN2Zm\nYThiMjc0NTlxLFUDcmVncS2JVQd0eXBlX2lkcS5LAnVlcy4=\n', '2012-02-19 09:38:05'),
('f61b0696ac60492fe5b028ad5f185d73', 'NWQ4ZjViMTZmMjA5MmI2ZTVmOWM4ZjMyZWRiMjlkZjEwZWQ2N2FkMTqAAn1xAShVCnRlc3Rjb29r\naWVxAlUGd29ya2VkcQNVEl9hdXRoX3VzZXJfYmFja2VuZHEEVSlkamFuZ28uY29udHJpYi5hdXRo\nLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEFVQ1fYXV0aF91c2VyX2lkcQaKAQJ1Lg==\n', '2011-12-24 12:51:31'),
('fd47239d8b5d82e2b576c43f3c9fcc01', 'OGM1NjExOWU0NjQxOWVlZmU3NmYwMzMyNDVkMTc2NjM0MmZkNjQzMDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n', '2012-01-11 17:45:49');

-- --------------------------------------------------------

--
-- Структура таблицы `django_site`
--

CREATE TABLE `django_site` (
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
-- Структура таблицы `mosaic_mosaic`
--

CREATE TABLE `mosaic_mosaic` (
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

CREATE TABLE `mosaic_mosaicsize` (
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

CREATE TABLE `puzzle_puzzle` (
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

CREATE TABLE `puzzle_puzzlesize` (
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
SET FOREIGN_KEY_CHECKS=1;
