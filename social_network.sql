-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le :  lun. 18 mai 2020 à 17:33
-- Version du serveur :  5.7.26
-- Version de PHP :  7.3.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `social_network`
--

--
-- Déchargement des données de la table `comment`
--

INSERT INTO `comment` (`id`, `user_id`, `post_id`, `content`, `publication_date`) VALUES
(1, 4, 6, '\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin consectetur urna vitae lorem pulvinar hendrerit. Suspendisse ultricies venenatis tellus, ut mollis massa varius ac. Integer laoreet odio.', '2020-05-18 19:26:16'),
(2, 4, 4, '\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin consectetur urna vitae lorem pulvinar hendrerit. Suspendisse ultricies venenatis tellus, ut mollis massa varius ac. Integer laoreet odio.', '2020-05-18 19:27:07'),
(3, 4, 7, '\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin consectetur urna vitae lorem pulvinar hendrerit. Suspendisse ultricies venenatis tellus, ut mollis massa varius ac. Integer laoreet odio.', '2020-05-18 19:27:16'),
(4, 4, 5, '\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin consectetur urna vitae lorem pulvinar hendrerit. Suspendisse ultricies venenatis tellus, ut mollis massa varius ac. Integer laoreet odio.', '2020-05-18 19:27:23'),
(5, 4, 1, '\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin consectetur urna vitae lorem pulvinar hendrerit. Suspendisse ultricies venenatis tellus, ut mollis massa varius ac. Integer laoreet odio.', '2020-05-18 19:29:04'),
(6, 4, 1, '\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin consectetur urna vitae lorem pulvinar hendrerit. Suspendisse ultricies venenatis tellus, ut mollis massa varius ac. Integer laoreet odio.', '2020-05-18 19:29:10'),
(7, 4, 2, '\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin consectetur urna vitae lorem pulvinar hendrerit. Suspendisse ultricies venenatis tellus, ut mollis massa varius ac. Integer laoreet odio.', '2020-05-18 19:29:20'),
(8, 4, 2, '\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin consectetur urna vitae lorem pulvinar hendrerit. Suspendisse ultricies venenatis tellus, ut mollis massa varius ac. Integer laoreet odio.', '2020-05-18 19:29:21'),
(9, 1, 6, '\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin consectetur urna vitae lorem pulvinar hendrerit. Suspendisse ultricies venenatis tellus, ut mollis massa varius ac. Integer laoreet odio.', '2020-05-18 19:29:52'),
(10, 1, 8, '\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin consectetur urna vitae lorem pulvinar hendrerit. Suspendisse ultricies venenatis tellus, ut mollis massa varius ac. Integer laoreet odio.', '2020-05-18 19:30:03'),
(11, 1, 7, '\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin consectetur urna vitae lorem pulvinar hendrerit. Suspendisse ultricies venenatis tellus, ut mollis massa varius ac. Integer laoreet odio.', '2020-05-18 19:30:11'),
(12, 3, 1, '\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin consectetur urna vitae lorem pulvinar hendrerit. Suspendisse ultricies venenatis tellus, ut mollis massa varius ac. Integer laoreet odio.', '2020-05-18 19:30:47'),
(13, 3, 1, '\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin consectetur urna vitae lorem pulvinar hendrerit. Suspendisse ultricies venenatis tellus, ut mollis massa varius ac. Integer laoreet odio.', '2020-05-18 19:31:02'),
(14, 3, 2, '\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin consectetur urna vitae lorem pulvinar hendrerit. Suspendisse ultricies venenatis tellus, ut mollis massa varius ac. Integer laoreet odio.', '2020-05-18 19:31:10'),
(15, 3, 3, '\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin consectetur urna vitae lorem pulvinar hendrerit. Suspendisse ultricies venenatis tellus, ut mollis massa varius ac. Integer laoreet odio.', '2020-05-18 19:31:25'),
(16, 3, 3, '\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin consectetur urna vitae lorem pulvinar hendrerit. Suspendisse ultricies venenatis tellus, ut mollis massa varius ac. Integer laoreet odio.', '2020-05-18 19:31:31'),
(17, 3, 8, '\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin consectetur urna vitae lorem pulvinar hendrerit. Suspendisse ultricies venenatis tellus, ut mollis massa varius ac. Integer laoreet odio.', '2020-05-18 19:31:38'),
(18, 2, 1, '\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin consectetur urna vitae lorem pulvinar hendrerit. Suspendisse ultricies venenatis tellus, ut mollis massa varius ac. Integer laoreet odio.', '2020-05-18 19:32:22'),
(19, 2, 2, '\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin consectetur urna vitae lorem pulvinar hendrerit. Suspendisse ultricies venenatis tellus, ut mollis massa varius ac. Integer laoreet odio.', '2020-05-18 19:32:38'),
(20, 2, 3, '\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin consectetur urna vitae lorem pulvinar hendrerit. Suspendisse ultricies venenatis tellus, ut mollis massa varius ac. Integer laoreet odio.', '2020-05-18 19:32:56'),
(21, 2, 5, '\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin consectetur urna vitae lorem pulvinar hendrerit. Suspendisse ultricies venenatis tellus, ut mollis massa varius ac. Integer laoreet odio.', '2020-05-18 19:33:03');

--
-- Déchargement des données de la table `follow`
--

INSERT INTO `follow` (`follower_id`, `followby_id`) VALUES
(1, 2),
(1, 4),
(2, 1),
(2, 3),
(3, 1),
(3, 4),
(4, 1),
(4, 2),
(4, 3);

--
-- Déchargement des données de la table `like`
--

INSERT INTO `like` (`user_id`, `post_id`) VALUES
(2, 1),
(2, 2),
(2, 3),
(2, 5),
(3, 1),
(3, 2),
(3, 3),
(3, 8),
(4, 1),
(4, 6),
(4, 7);

--
-- Déchargement des données de la table `message`
--

INSERT INTO `message` (`id`, `content`, `set_date`, `send_by_id`, `receive_by_id`) VALUES
(1, 'Salut mon poto', '2020-05-18 19:07:36', 1, 3),
(2, 'Salut mon poto', '2020-05-18 19:08:02', 1, 2),
(3, 'Salut ça va ?', '2020-05-18 19:16:58', 3, 1),
(4, 'Couou', '2020-05-18 19:17:15', 3, 4),
(5, 'ça va mon pote', '2020-05-18 19:17:55', 2, 3),
(6, 'wesh bg', '2020-05-18 19:18:20', 2, 1),
(7, 'wesh bg', '2020-05-18 19:20:31', 2, 4),
(8, 'wesh loulou', '2020-05-18 19:28:17', 4, 2),
(9, 'hey bichette', '2020-05-18 19:28:34', 4, 3);

--
-- Déchargement des données de la table `post`
--

INSERT INTO `post` (`id`, `title`, `content`, `image`, `publication_date`, `modification_date`, `user_id`) VALUES
(1, 'Titre Post 1', '\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin consectetur urna vitae lorem pulvinar hendrerit. Suspendisse ultricies venenatis tellus, ut mollis massa varius ac. Integer laoreet odio.', '470a19a36904fe200610cc1f41eb00d9.jpg', '2020-05-18 19:04:20', '2020-05-18 19:04:20', 1),
(2, 'Titre Post 2', '\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin consectetur urna vitae lorem pulvinar hendrerit. Suspendisse ultricies venenatis tellus, ut mollis massa varius ac. Integer laoreet odio.', NULL, '2020-05-18 19:04:36', '2020-05-18 19:04:36', 1),
(3, 'Titre Post 3', '\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin consectetur urna vitae lorem pulvinar hendrerit. Suspendisse ultricies venenatis tellus, ut mollis massa varius ac. Integer laoreet odio.', '143271-astronomiya-rozovyj-kosmicheskoe_prostranstvo-astronomicheskij_obekt-tumannost-1920x1080_1.jpg', '2020-05-18 19:04:51', '2020-05-18 19:04:51', 1),
(4, 'Titre Post 4', '\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin consectetur urna vitae lorem pulvinar hendrerit. Suspendisse ultricies venenatis tellus, ut mollis massa varius ac. Integer laoreet odio.', NULL, '2020-05-18 19:09:31', '2020-05-18 19:09:31', 3),
(5, 'Titre Post 5', '\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin consectetur urna vitae lorem pulvinar hendrerit. Suspendisse ultricies venenatis tellus, ut mollis massa varius ac. Integer laoreet odio.', 'nebuleuse-166783.jpg', '2020-05-18 19:09:46', '2020-05-18 19:09:46', 3),
(6, 'Titre Post 6', '\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin consectetur urna vitae lorem pulvinar hendrerit. Suspendisse ultricies venenatis tellus, ut mollis massa varius ac. Integer laoreet odio.', '143271-astronomiya-rozovyj-kosmicheskoe_prostranstvo-astronomicheskij_obekt-tumannost-1920x1080_1.jpg', '2020-05-18 19:19:17', '2020-05-18 19:19:17', 2),
(7, 'Titre Post 7', '\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin consectetur urna vitae lorem pulvinar hendrerit. Suspendisse ultricies venenatis tellus, ut mollis massa varius ac. Integer laoreet odio.', 'stretched-1920-1080-936378.jpg', '2020-05-18 19:19:39', '2020-05-18 19:19:39', 2),
(8, 'Titre Post 8', '\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin consectetur urna vitae lorem pulvinar hendrerit. Suspendisse ultricies venenatis tellus, ut mollis massa varius ac. Integer laoreet odio.', '470a19a36904fe200610cc1f41eb00d9.jpg', '2020-05-18 19:28:06', '2020-05-18 19:28:06', 4);

--
-- Déchargement des données de la table `user`
--

INSERT INTO `user` (`id`, `username`, `age`, `mail`, `password`, `avatar`) VALUES
(1, 'David', 21, 'david.dasilvateixeira@ynov.com', 'pbkdf2:sha256:150000$awmMDYoM$0de7a83b42693f534ae362eeb2cffe05bb0bed8df8c43c6fe7a3188e06b6fc42', '1065736.jpg'),
(2, 'Louis', 22, 'louis.ardilly@ynov.com', 'pbkdf2:sha256:150000$Kvw9CcaQ$a601cc296fba6d9e065e0bde33fa487b8454c381fbeaf37e2c9c21829206ba55', NULL),
(3, 'Jeremy', 19, 'jeremy.richard@ynov.com', 'pbkdf2:sha256:150000$HmUW9HsT$e6ce565c1c3faefe49ec4295709fd1ca278dae4a6989988af0cb54f20a56ebe1', '936378.jpg'),
(4, 'Leo', 21, 'leo.peyre@ynov.com', 'pbkdf2:sha256:150000$sBETA1Js$73511559257c8f10fcaab1822fbe8633c97dc5e26fc230ac2381c3e6b5c71130', NULL);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
