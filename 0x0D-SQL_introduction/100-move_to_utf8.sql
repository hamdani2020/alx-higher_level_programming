-- This script converts database to UTF8
USE `hbtn_0c_0`
ALTER TABLE `first_table`
CONVERT TO CHARACTER SET utf8mb COLLATE utf8mb_unicode_ci;
