-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 29-09-2023 a las 04:59:20
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
-- Estructura de tabla para la tabla `comment`
--

CREATE TABLE `comment` (
  `id` int(11) NOT NULL,
  `post_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `text` text DEFAULT NULL,
  `media` varchar(255) DEFAULT NULL,
  `createdate` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `post`
--

CREATE TABLE `post` (
  `id` int(11) NOT NULL,
  `title` varchar(100) DEFAULT NULL,
  `user_ID` int(11) DEFAULT NULL,
  `createdate` datetime DEFAULT NULL,
  `text` text DEFAULT NULL,
  `media` varchar(255) DEFAULT NULL,
  `topic` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `post`
--

INSERT INTO `post` (`id`, `title`, `user_ID`, `createdate`, `text`, `media`, `topic`) VALUES
(6, 'FORUM RULES', 9, '2023-01-20 11:18:44', '<ul>\r\n	<li>Keep it friendly</li>\r\n	<li>Be courteous and respectful. Appreciate that others may have an opinion different from yours.</li>\r\n	<li>Stay on topic. When creating a new discussion thread, give a clear topic title and put your post in the appropriate category. When contributing to an existing discussion, try to stay &#39;on topic&#39;. If something new comes up within a topic that you would like to discuss, start a new thread.</li>\r\n	<li>Share your knowledge. Don&#39;t hold back in sharing your knowledge &ndash; it&#39;s likely someone will find it useful or interesting. When you give information, provide your sources.</li>\r\n	<li>Refrain from demeaning, discriminatory, or harassing behaviour and speech.</li>\r\n</ul>\r\n\r\n<p>We maintain the rights to remove posts and threads to ensure that material posted in the discussion forums is not potentially harmful. For this reason, we may edit or choose not to publish any post, that:</p>\r\n\r\n<ul>\r\n	<li>contains disrespectful or derogatory remarks about any person</li>\r\n	<li>contains advice or content that we believe is damaging, unhelpful or distressing to others</li>\r\n	<li>contains swearing or offensive language, is nonsensical and/or irrelevant</li>\r\n	<li>promotes personal beliefs in a way that is disrespectful of the choices of others</li>\r\n	<li>is racist, sexist, homophobic, sexually explicit or suggestive, abusive or otherwise discriminatory or objectionable</li>\r\n</ul>\r\n', '', 'announcements');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(40) NOT NULL,
  `contrasena` varchar(255) NOT NULL,
  `realname` varchar(100) DEFAULT NULL,
  `mail` varchar(100) NOT NULL,
  `country` varchar(100) DEFAULT NULL,
  `createdate` datetime DEFAULT NULL,
  `profileimg` varchar(255) DEFAULT NULL,
  `token` varchar(255) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`id`, `username`, `contrasena`, `realname`, `mail`, `country`, `createdate`, `profileimg`, `token`, `active`) VALUES
(9, 'garri87', 'pbkdf2:sha256:260000$Mm1wqmvcOOrjWaIs$04702f24f3446114dec725167762260d7d32f1efcc6a399728c99b50e0088884', 'Pablo Ezequiel Flores', 'garri87@hotmail.com', 'Argentina', '2023-01-20 10:43:50', '2023105759_pablo.jpg', 'ImdhcnJpODdAaG90bWFpbC5jb20i.Q_CjUDU4dQvNheF8Nf3qoo51CSg', 1),
(13, 'joseperez', 'pbkdf2:sha256:260000$83zJjszRFxlUeFx0$b6dac38982431fe4c593e979ca3dfc6b54a225efcf6cbc22bb76cf2f5171a040', 'jose perez', 'garri8783@gmail.com', 'Argentina', '2023-01-23 18:04:11', '2023180411_Ejercicio obligatorio_ MySQL II_ Revisión del intento.pdf', 'ImdhcnJpODc4M0BnbWFpbC5jb20i.2JACa5KrrKlxCh4kBgZUVSaqL3M', 0);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `comment`
--
ALTER TABLE `comment`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `post`
--
ALTER TABLE `post`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `mail` (`mail`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `comment`
--
ALTER TABLE `comment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `post`
--
ALTER TABLE `post`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
