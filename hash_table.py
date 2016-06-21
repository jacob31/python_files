# file name: hash_table.py 
# by: Ben Silbernagel
# date: 6/8/2016
# class: Intro to Computer Science, by Udacity
# purpose: functions to be used to create a hash table

def hash_string(keyword,buckets):
    bucket = 0
    for char in keyword:
        bucket += (bucket + ord(char)) % buckets
    return bucket

def make_hashtable(nbuckets):
    table = []

    for e in range(nbuckets):
        table.append([])
    return table

def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword, len(htable))]

def hashtable_update(htable,key,value):
    bucket = hashtable_get_bucket(htable,key)
    for entry in bucket:
        if entry[0] == key:
            entry[1] = value
            return
    bucket.append([key,value])

def hashtable_lookup(htable,key):
    bucket = hashtable_get_bucket(htable,key)
    for entry in bucket:
        if entry[0] == key:
            return entry[1]
    return None

def hashtable_add(htable,key,value):
    bucket = hashtable_get_bucket(htable,key)
    bucket.append([key,value])