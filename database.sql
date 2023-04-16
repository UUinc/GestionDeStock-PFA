-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 16, 2023 at 04:45 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gestion_stock`
--

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `product_id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `description` varchar(20) DEFAULT NULL,
  `unit_price` float NOT NULL,
  `quantity` int(11) NOT NULL,
  `alert_threshold` int(11) NOT NULL,
  `last_entry_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `last_release_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `stock_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `stock`
--

CREATE TABLE `stock` (
  `stock_id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `description` varchar(20) DEFAULT NULL,
  `last_edit` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `creation_date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `stock`
--

INSERT INTO `stock` (`stock_id`, `name`, `description`, `last_edit`, `creation_date`) VALUES
(1, 'IT shop', 'it accessories', '2023-04-16 14:37:59', '2023-04-16 14:37:59'),
(2, 'Fruits', 'fih l9oo9a wl br9o9a', '2023-04-16 14:37:59', '2023-04-16 14:37:59');

-- --------------------------------------------------------

--
-- Table structure for table `stockownership`
--

CREATE TABLE `stockownership` (
  `username` varchar(20) NOT NULL,
  `stock_id` int(11) NOT NULL,
  `ownership_start_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `role` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `stockownership`
--

INSERT INTO `stockownership` (`username`, `stock_id`, `ownership_start_date`, `role`) VALUES
('ouassima12', 2, '2023-04-15 21:50:25', 'view'),
('yahya.lz', 1, '2023-04-15 20:20:35', 'edit'),
('yousra.eb', 2, '2023-04-14 22:10:30', 'edit');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `username` varchar(20) NOT NULL,
  `first_name` varchar(20) NOT NULL,
  `last_name` varchar(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`username`, `first_name`, `last_name`, `email`, `password`) VALUES
('ouassima12', 'ouassima', 'ab', 'ouassima@gmail.com', 'ouassima1-'),
('yahya.lz', 'Yahya', 'Lazrek', 'duo.lz.yahya@gmail.com', '123456'),
('yousra.eb', 'Yousra', 'Elbarreq', 'yousra@gmail.com', '123456');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`product_id`),
  ADD KEY `stock_id` (`stock_id`);

--
-- Indexes for table `stock`
--
ALTER TABLE `stock`
  ADD PRIMARY KEY (`stock_id`);

--
-- Indexes for table `stockownership`
--
ALTER TABLE `stockownership`
  ADD PRIMARY KEY (`username`,`stock_id`),
  ADD KEY `stock_id` (`stock_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`username`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `UC_email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `stock`
--
ALTER TABLE `stock`
  MODIFY `stock_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `product`
--
ALTER TABLE `product`
  ADD CONSTRAINT `product_ibfk_1` FOREIGN KEY (`stock_id`) REFERENCES `stock` (`stock_id`);

--
-- Constraints for table `stockownership`
--
ALTER TABLE `stockownership`
  ADD CONSTRAINT `stockownership_ibfk_1` FOREIGN KEY (`username`) REFERENCES `user` (`username`),
  ADD CONSTRAINT `stockownership_ibfk_2` FOREIGN KEY (`stock_id`) REFERENCES `stock` (`stock_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
