#!/bin/bash

set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER"  <<-EOSQL

    DROP DATABASE IF EXISTS amir_deals;

    CREATE DATABASE amir_deals;

	\c amir_deals ;
    
    DROP TABLE IF EXISTS amir_deals;

    CREATE TABLE IF NOT EXISTS amir_deals(
	    id		INTEGER PRIMARY KEY,
	    product     TEXT,
	    client      TEXT,
	    status      TEXT,
	    amount      DECIMAL(8,2),
	    num_users   INTEGER);

EOSQL
