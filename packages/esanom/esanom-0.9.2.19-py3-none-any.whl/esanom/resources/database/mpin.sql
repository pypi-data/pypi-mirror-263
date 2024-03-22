
/*
#################################################################################
#
# {___     {__          {__       {__
# {_ {__   {__          {_ {__   {___
# {__ {__  {__   {__    {__ {__ { {__
# {__  {__ {__ {__  {__ {__  {__  {__
# {__   {_ {__{__    {__{__   {_  {__
# {__    {_ __ {__  {__ {__       {__
# {__      {__   {__    {__       {__
#
# (C) Copyright European Space Agency, 2024
# 
# This file is subject to the terms and conditions defined in file 'LICENCE.txt', 
# which is part of this source code package. No part of the package, including 
# this file, may be copied, modified, propagated, or distributed except 
# according to the terms contained in the file ‘LICENCE.txt’.“ 
#
#################################################################################
*/

CREATE TABLE `mpin` (

    `id` int UNSIGNED NOT NULL AUTO_INCREMENT,

    `mport_id` INT UNSIGNED DEFAULT NULL,
    `unit_id` INT UNSIGNED NOT NULL,

    `size_limit` INT UNSIGNED DEFAULT 0,

    `enable` BOOLEAN DEFAULT 1,
    `visible` BOOLEAN DEFAULT 1,
    `pipeline` BOOLEAN DEFAULT 1,
    `download` BOOLEAN DEFAULT 1,
    `read` BOOLEAN DEFAULT 1,
    `write` BOOLEAN DEFAULT 1,

    `qualifier` varchar(255) DEFAULT "",

    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
    `updated_at` DATETIME DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,

    PRIMARY KEY (`id`) ,
    
    KEY `mport_id` (`mport_id`),
    KEY `unit_id` (`unit_id`),
    KEY `enable` (`enable`),
    
    CONSTRAINT `mpin_mport_id` FOREIGN KEY (`mport_id`) REFERENCES `mport` (`id`) ON DELETE CASCADE ,
    CONSTRAINT `mpin_unit_id` FOREIGN KEY (`unit_id`) REFERENCES `unit` (`id`) ON DELETE CASCADE ,
    CONSTRAINT `mpin_unique_mportunit` UNIQUE (`mport_id`,`unit_id`)

) ENGINE=InnoDB,AUTO_INCREMENT=101;
 




