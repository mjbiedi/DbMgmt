#!/usr/bin/python3

import os
import sqlite3

###########################################################
def db_open(database):
    return sqlite3.connect(database)

###########################################################
def db_close(connection):
    with connection:
        connection.commit()

###########################################################
def db_get_record(connection, db, element, value):
    select = f'SELECT * FROM {db} where {element} = ?';
    with connection:
        return connection.execute(select, (value,)).fetchall()

###########################################################
def get_all_dvd(connection):

    GET_ALL_DVD = "SELECT * FROM dvds"
    with connection:
        return connection.execute(GET_ALL_DVD).fetchall()

