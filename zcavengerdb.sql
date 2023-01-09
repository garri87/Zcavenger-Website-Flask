-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 29-12-2022 a las 03:17:13
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `zcavengerdb`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `comments`
--

CREATE TABLE `comments` (
  `id` int(8) NOT NULL,
  `post_ID` int(8) NOT NULL,
  `user_ID` int(8) NOT NULL,
  `text` varchar(1000) NOT NULL,
  `media` varchar(255) DEFAULT NULL,
  `createdate` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `comments`
--

INSERT INTO `comments` (`id`, `post_ID`, `user_ID`, `text`, `media`, `createdate`) VALUES
(5, 1, 5, 'Hola este es un comentario\r\n        ', '2022104454Sin título-1.jpg', '2022-12-28 10:44:54'),
(6, 1, 5, 'Hola este es un comentario\r\n        ', '2022104640Sin título-1.jpg', '2022-12-28 10:46:40'),
(7, 1, 5, 'Hola este es un comentario\r\n        ', '2022104647Sin título-1.jpg', '2022-12-28 10:46:47'),
(8, 1, 5, 'otro comentario\r\n        ', '2022104846Imagen de WhatsApp 2022-12-22 a las 13.40.55.jpg', '2022-12-28 10:48:46'),
(9, 1, 5, 'Otro mas comentario jajsajdajdjwdjadksjdad\r\n        ', '2022104940WhatsApp Image 2022-12-22 at 12.55.17.jpeg', '2022-12-28 10:49:40'),
(10, 1, 5, 'dwadawdsfwafaw', '', '2022-12-28 10:52:30'),
(11, 1, 5, 'dwadawdsfwafaw', '', '2022-12-28 10:53:36'),
(12, 1, 5, 'dwadawdsfwafaw', '', '2022-12-28 10:54:42'),
(13, 1, 5, 'dawdagwfwad\r\n        ', '', '2022-12-28 10:55:26'),
(14, 1, 5, 'dawdagwfwad\r\n        ', '', '2022-12-28 10:56:02'),
(15, 1, 5, '\r\n        dwadadwda', '', '2022-12-28 10:57:10'),
(16, 1, 5, 'dasdwadasdwad', '', '2022-12-28 10:57:21'),
(17, 1, 5, 'dadasdwadawd\r\n        ', '', '2022-12-28 10:57:36'),
(18, 1, 5, 'dadasdwadawd\r\n        ', '', '2022-12-28 10:58:50'),
(19, 1, 5, 'ultimo comment\r\n        ', '2022105922WhatsApp Image 2022-12-22 at 12.55.17.jpeg', '2022-12-28 10:59:22'),
(20, 2, 5, 'otro comment\r\n        ', '', '2022-12-28 10:59:49'),
(21, 47, 5, '            Hola', '', '2022-12-28 13:34:15');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `posts`
--

CREATE TABLE `posts` (
  `id` int(8) NOT NULL,
  `title` varchar(100) NOT NULL,
  `user_ID` int(8) NOT NULL,
  `createdDate` datetime NOT NULL,
  `text` varchar(1000) DEFAULT NULL,
  `media` varchar(255) DEFAULT NULL,
  `topic` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `posts`
--

INSERT INTO `posts` (`id`, `title`, `user_ID`, `createdDate`, `text`, `media`, `topic`) VALUES
(1, 'Sample Title', 5, '2022-12-23 20:55:33', 'First Line\r\nSecond Line\r\nThird Line', '2022205533unnamed.jpg', 'announcements'),
(2, 'Sample Title', 5, '2022-12-23 20:56:09', 'First Line\r\nSecond Line\r\nThird Line', '2022205609unnamed.jpg', 'announcements'),
(3, 'Third Post', 5, '2022-12-24 12:37:50', 'Text\r\ntext \r\ntext', '2022123750_PBO2648.jpg', 'announcements'),
(4, 'Third Post', 5, '2022-12-24 12:39:36', 'Text\r\ntext \r\ntext', '2022123936_PBO2648.jpg', 'announcements'),
(5, 'Third Post', 5, '2022-12-24 12:41:16', 'Text\r\ntext \r\ntext', '2022124116_PBO2648.jpg', 'announcements'),
(6, 'Third Post', 5, '2022-12-24 12:42:17', 'Text\r\ntext \r\ntext', '2022124217_PBO2648.jpg', 'announcements'),
(7, 'Third Post', 5, '2022-12-24 12:42:46', 'Text\r\ntext \r\ntext', '2022124246_PBO2648.jpg', 'announcements'),
(8, 'Third Post', 5, '2022-12-24 12:43:35', 'Text\r\ntext \r\ntext', '2022124335_PBO2648.jpg', 'announcements'),
(9, 'Third Post', 5, '2022-12-24 12:44:27', 'Text\r\ntext \r\ntext', '2022124427_PBO2648.jpg', 'announcements'),
(10, 'Third Post', 5, '2022-12-24 12:44:38', 'Text\r\ntext \r\ntext', '2022124438_PBO2648.jpg', 'announcements'),
(11, 'Third Post', 5, '2022-12-24 12:44:46', 'Text\r\ntext \r\ntext', '2022124446_PBO2648.jpg', 'announcements'),
(12, 'Third Post', 5, '2022-12-24 12:46:47', 'Text\r\ntext \r\ntext', '2022124647_PBO2648.jpg', 'announcements'),
(13, 'Third Post', 5, '2022-12-24 12:47:03', 'Text\r\ntext \r\ntext', '2022124703_PBO2648.jpg', 'announcements'),
(14, 'Third Post', 5, '2022-12-24 12:48:42', 'Text\r\ntext \r\ntext', '2022124842_PBO2648.jpg', 'announcements'),
(15, 'Sample Title', 5, '2022-12-24 12:50:47', 'dafawgwgwgfa', NULL, 'announcements'),
(16, 'Sample Title', 5, '2022-12-24 12:51:02', 'dafawgwgwgfa', NULL, 'announcements'),
(17, 'Sample Title', 5, '2022-12-24 12:51:33', 'dafawgwgwgfa', NULL, 'announcements'),
(18, 'Sample Title', 5, '2022-12-24 12:51:42', 'dafawgwgwgfa', NULL, 'announcements'),
(19, 'Sample Title', 5, '2022-12-24 12:51:50', 'dafawgwgwgfa', NULL, 'announcements'),
(20, 'Sample Title', 5, '2022-12-24 12:52:03', 'dafawgwgwgfa', NULL, 'announcements'),
(21, 'Sample Title', 5, '2022-12-24 12:52:37', 'dafawgwgwgfa', NULL, 'announcements'),
(22, 'Sample Title', 5, '2022-12-24 12:52:53', 'dafawgwgwgfa', NULL, 'announcements'),
(23, 'Sample Title', 5, '2022-12-24 12:53:06', 'dafawgwgwgfa', NULL, 'announcements'),
(24, 'Sample Title', 5, '2022-12-24 12:53:18', 'dafawgwgwgfa', NULL, 'announcements'),
(25, 'Sample Title', 5, '2022-12-24 12:55:26', 'dafawgwgwgfa', NULL, 'announcements'),
(26, 'Sample Title', 5, '2022-12-24 12:55:39', 'dafawgwgwgfa', NULL, 'announcements'),
(27, 'Sample Title', 5, '2022-12-24 12:56:02', 'dafawgwgwgfa', NULL, 'announcements'),
(28, 'Sample Title', 5, '2022-12-24 12:56:22', 'dafawgwgwgfa', NULL, 'announcements'),
(29, 'Sample Title', 5, '2022-12-24 12:56:45', 'dafawgwgwgfa', NULL, 'announcements'),
(30, 'Sample Title', 5, '2022-12-24 13:41:40', 'dawdadwadwadaw', NULL, 'announcements'),
(31, 'Sample Title', 5, '2022-12-25 11:49:15', 'dwrwattwatwaawdaw', '2022114915Imagen de WhatsApp 2022-12-22 a las 12.55.18.jpg', 'bugreports'),
(32, 'Sample Title', 5, '2022-12-26 13:53:40', 'sdaafafwagfg', NULL, 'announcements'),
(33, 'Sample Title', 5, '2022-12-26 14:16:43', 'sdaafafwagfg', '2022141643_PBO2648.jpg', 'announcements'),
(34, 'Sample Title', 5, '2022-12-26 14:17:10', 'sdaafafwagfg', '2022141710_PBO2648.jpg', 'announcements'),
(35, 'Sample Title', 5, '2022-12-26 14:17:36', 'sdaafafwagfg', '2022141736_PBO2648.jpg', 'announcements'),
(36, 'Sample Title', 5, '2022-12-26 14:17:53', 'sdaafafwagfg', '2022141753_PBO2648.jpg', 'announcements'),
(37, 'Sample Title', 5, '2022-12-26 14:19:08', 'sdaafafwagfg', '2022141908_PBO2648.jpg', 'announcements'),
(38, 'Sample Title', 5, '2022-12-26 14:20:59', 'sdaafafwagfg', '2022142059_PBO2648.jpg', 'announcements'),
(39, 'dsadasd', 5, '2022-12-26 14:21:54', 'dsadsadsa', NULL, 'announcements'),
(40, 'dsadasd', 5, '2022-12-26 14:28:25', 'dsadsadsa', '202214282524114_n.jpg', 'announcements'),
(41, 'dasdwafwa', 6, '2022-12-26 17:18:45', 'gafwfwadwadwad', '2022171845WhatsApp Image 2022-12-22 at 12.55.17.jpeg', 'announcements'),
(42, 'Last Post', 5, '2022-12-28 00:14:06', 'text of the last Post\r\nof the user garri87', '2022001406Sin título-1.jpg', 'announcements'),
(43, 'Last LAst Post', 5, '2022-12-28 00:27:05', 'dwa dwdawd awfawgw fw ad', NULL, 'announcements'),
(44, 'Last LAst Post', 5, '2022-12-28 00:30:06', 'dwa dwdawd awfawgw fw ad', NULL, 'announcements'),
(45, 'Last LAst Post', 5, '2022-12-28 00:30:41', 'dwa dwdawd awfawgw fw ad', NULL, 'announcements'),
(46, 'dadsadsadsa', 5, '2022-12-28 13:32:50', 'sadasdsadsada', NULL, 'generaldiscussion'),
(47, 'dadsadsadsa', 5, '2022-12-28 13:33:59', 'sadasdsadsada', NULL, 'generaldiscussion');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id` int(8) NOT NULL,
  `username` varchar(40) NOT NULL,
  `contrasena` char(255) NOT NULL,
  `realname` varchar(100) NOT NULL,
  `mail` varchar(100) NOT NULL,
  `country` varchar(100) DEFAULT NULL,
  `createdate` datetime NOT NULL,
  `profileimg` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id`, `username`, `contrasena`, `realname`, `mail`, `country`, `createdate`, `profileimg`) VALUES
(5, 'garri87', 'pbkdf2:sha256:260000$ziLWI1Rb1sFXclRh$16367b5d8c2eea599347dea39a1a1d2633b2d5f2d53624969720501f96f9b975', 'Pablo Flores', 'garri87@hotmail.com', 'Argentina', '2022-12-23 19:28:14', '2022192814pablo.jpg'),
(6, 'chechupadilla', 'pbkdf2:sha256:260000$6WWhvrdNdohSvsBb$a11e809b4d01c298af4c4b3a897c6d12779688b2fc0c30e896d607d8eef7311f', 'Maria Cecilia Padilla', 'mariachechupadilla@gmail.com', 'Argentina', '2022-12-25 11:47:34', '2022114734Imagen de WhatsApp 2022-12-22 a las 13.40.54.jpg'),
(7, 'lalala', 'pbkdf2:sha256:260000$SaN7HzzX8Nro6a2X$cee011763a1a6cfdd0893f66c09619a5355dfca767a5bf379871c887ae8edfbd', 'Pablo Flores', 'garri87@hotmail.com', 'Afghanistan', '2022-12-28 21:57:04', '2022215704'),
(8, 'lolololo', 'pbkdf2:sha256:260000$B8bRJ9jciugNVStd$2d06d25e49aa3ae0f0b5700a6e708d4c93ba8839ccad7947d95485a7f714c631', 'Pablo Flores', 'garri87@hotmail.com', 'Bahrain', '2022-12-28 22:00:51', '2022220051'),
(9, 'juanperez', 'pbkdf2:sha256:260000$M4G2cNRcHg9Bo0Zb$9b81710c2b004090e0fc10ff85ce9219e9b38377f1c22378569c671234afa81b', 'Pablo Flores', 'garri87@hotmail.com', 'Bahrain', '2022-12-28 22:01:57', '2022220157');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `comments`
--
ALTER TABLE `comments`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `comments`
--
ALTER TABLE `comments`
  MODIFY `id` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT de la tabla `posts`
--
ALTER TABLE `posts`
  MODIFY `id` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=48;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
