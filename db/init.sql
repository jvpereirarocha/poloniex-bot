DROP DATABASE IF EXISTS api_poloniex;

CREATE DATABASE IF NOT EXISTS api_poloniex;

CREATE USER IF NOT EXISTS 'jv'@'db' IDENTIFIED BY 'sci@2017';

GRANT ALL PRIVILEGES ON *.* TO 'jv'@'%';

USE api_poloniex;


CREATE TABLE IF NOT EXISTS candles (
    id int(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    currency varchar(50) NOT NULL,
    period int(4) NOT NULL,
    date_initial datetime NOT NULL,
    open_candle varchar(30) NOT NULL,
    close_candle varchar(30) NOT NULL,
    high varchar(30) NOT NULL,
    low varchar(30) NOT NULL
);
