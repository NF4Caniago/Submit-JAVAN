-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 22, 2021 at 05:52 PM
-- Server version: 10.1.36-MariaDB
-- PHP Version: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `silsilah`
--

-- --------------------------------------------------------

--
-- Table structure for table `silsilah`
--

CREATE TABLE `silsilah` (
  `nama` varchar(100) DEFAULT NULL,
  `jenis_kelamin` varchar(100) DEFAULT NULL,
  `anak_dari` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `silsilah`
--

INSERT INTO `silsilah` (`nama`, `jenis_kelamin`, `anak_dari`) VALUES
('Budi', 'pria', '-'),
('Dedi', 'pria', 'Budi'),
('Dodi', 'pria', 'Budi'),
('Dede', 'pria', 'Budi'),
('Dewi', 'wanita', 'Budi'),
('Feri', 'pria', 'Dedi'),
('Farah', 'wanita', 'Dedi'),
('Gugus', 'pria', 'Dodi'),
('Gandi', 'pria', 'Dodi'),
('Hani', 'wanita', 'Dede'),
('Hana', 'wanita', 'Dede');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
