-- phpMyAdmin SQL Dump
-- version 4.1.12
-- http://www.phpmyadmin.net
--
-- Host: localhost:8889
-- Generation Time: Jun 14, 2018 at 04:50 AM
-- Server version: 5.5.34
-- PHP Version: 5.5.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `w1801`
--

-- --------------------------------------------------------

--
-- Table structure for table `demo`
--

CREATE TABLE `demo` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `age` varchar(30) DEFAULT NULL,
  `sex` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=44 ;

--
-- Dumping data for table `demo`
--

INSERT INTO `demo` (`id`, `name`, `age`, `sex`) VALUES
(15, '李四', '17', '10'),
(16, '张三', 'dsa', 'dsa'),
(18, '1', '2', '3'),
(19, '1', '2', '3'),
(20, '2', '3', '4'),
(21, '王五', '4', '5'),
(37, '', '', ''),
(40, '', '', ''),
(43, '王五', '17', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `todo`
--

CREATE TABLE `todo` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `val` varchar(255) NOT NULL,
  `state` int(2) NOT NULL,
  `edit` int(2) NOT NULL,
  `uid` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=48 ;

--
-- Dumping data for table `todo`
--

INSERT INTO `todo` (`id`, `val`, `state`, `edit`, `uid`) VALUES
(10, '1111', 1, 0, 0),
(27, '66666', 0, 0, 6),
(28, 'admin1', 0, 0, 6),
(33, 'admin1', 0, 0, 6),
(34, 'admin22222', 0, 0, 6),
(35, 'zhangsan', 0, 0, 7),
(36, '张三的内容', 0, 0, 7),
(37, '11111111', 0, 0, 8),
(38, '历史历史', 0, 0, 8),
(39, 'sadshajh ', 0, 0, 8),
(40, 'dsakjdjash', 0, 0, 8),
(41, 'sadjhas', 0, 0, 8),
(42, 'djsahdas', 0, 0, 8),
(43, 'dhjsahdas', 0, 0, 8),
(44, 'jhdasjd', 0, 0, 8),
(45, '111', 0, 0, 1),
(46, 'sss', 0, 0, 1),
(47, '', 0, 0, 1);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `uname` varchar(50) DEFAULT NULL,
  `pass` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`uid`, `uname`, `pass`) VALUES
(1, 'admin', 'e10adc3949ba59abbe56e057f20f883e'),
(6, 'admin1', 'c4ca4238a0b923820dcc509a6f75849b'),
(7, 'zhangsan', 'e10adc3949ba59abbe56e057f20f883e'),
(8, 'lisi', 'e10adc3949ba59abbe56e057f20f883e');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
