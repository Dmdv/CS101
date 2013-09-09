__author__ = 'dmitrijdackov'

def hash_string(keyword, buckets):
    """
    Calculates the bucket index for a string
    """
    summ = sum([ord(ch) for ch in keyword])
    return summ % buckets

def make_hashtable(nbuckets):
    return [[] for bucket in range(nbuckets)]

def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword, len(htable))]

def bucket_lookup(bucket, key):
    for entry in bucket:
        if entry[0] == key:
            return entry
    return None

# TODO: What if such a value already exists?
def hashtable_add(htable,key,value):
    bucket = hashtable_get_bucket(htable, key)
    bucket.append([key, value])
#    found = False
#    for pair in bucket:
#        if pair[0] == key:
#            pair[1].append(value)
#    if not found:
#        bucket.append([key, value])

def hashtable_lookup(htable, key):
    bucket = hashtable_get_bucket(htable, key)
    entry = bucket_lookup(bucket, key)
    if entry == None:
        return None
    return entry[1]

def hashtable_update(htable, key, value):
    bucket = hashtable_get_bucket(htable, key)
    entry = bucket_lookup(bucket, key)
    if entry == None:
        bucket.append([key, value])
    else:
        entry[1] = value

table = make_hashtable(3)
table[1].append(['test', ['rle']])

hashtable_lookup(table, 'test1')

#Whenever we have duplicate code like the loop that finds the entry in
#hashtable_update and hashtable_lookup, we should think if there is a better way
#to write this that would avoid the duplication.  We should be able to rewrite
#these procedures to be shorter by defining a new procedure and rewriting both
#hashtable_update and hashtable_lookup to use that procedure.

#Modify the code for both hashtable_update and hashtable_lookup to have the same
#behavior they have now, but using fewer lines of code in each procedure.  You
#should define a new procedure to help with this.  Your new version should have
#approximately the same running time as the original version, but neither
#hashtable_update or hashtable_lookup should include any for or while loop, and
#the block of each procedure should be no more than 6 lines long.

#Your procedures should have the same behavior as the originals.  For example,

table = make_hashtable(10)
hashtable_update(table, 'Python', 'Monty')
hashtable_update(table, 'CLU', 'Barbara Liskov')
hashtable_update(table, 'JavaScript', 'Brendan Eich')
hashtable_update(table, 'Python', 'Guido van Rossum')
print (hashtable_lookup(table, 'Python')) # => Guido van Rossum

