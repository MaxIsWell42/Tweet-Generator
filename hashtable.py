#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]
        self.size = 0

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Running time: Always O(n), because it goes through everything no matter what"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Running time: Always O(n), because it goes through everything no matter what"""
        all_values = []

        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Running time: Always 0(n), because it goes through everything no matter what"""
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        # Running time: Always O(1), because we save the length of the hashtable"""
        return self.size

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Running time: Best case: O(1), Worst case: 0(the average of L), or 0(n/b) if it has to go through every last bucket and key"""
        specific_bucket = self.buckets[self._bucket_index(key)]

        for other_key, other_value in specific_bucket.items():
            if other_key == key:
                return True
        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Running time: Best case: O(1), Average case: 0(the average of L), or 0(n/b)"""
        # Define the bucket we're looking for
        specific_bucket = self.buckets[self._bucket_index(key)]

        # Go through all items, check if the item is the one we're looking for, and if item is not found in whole list raise Key Error
        for other_key, value in specific_bucket.items():
            if other_key == key:
                return value
        raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Running time: Best case: O(1), Average case: 0(the average of L), or 0(n/b)"""
        # Define the bucket we're looking for
        specific_bucket = self.buckets[self._bucket_index(key)]
        # Helped by @Youssef-Sawiris
        # iterate through all the buckets and find the one we want, and
        # replace it with the new value using replace from linkedlist
        for other_key, other_value in specific_bucket.items():
            if other_key == key:
                specific_bucket.replace((other_key, other_value), (key, value))
                return
        specific_bucket.append((key, value))
        self.size += 1
            
    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        Running time: Best case: O(1), Average case: 0(the average of L), or 0(n/b)"""
        specific_bucket = self.buckets[self._bucket_index(key)]
        # Using delete from linkedlist. Bless reusable code.
        for other_key, other_value in specific_bucket.items():
            if other_key == key:
                specific_bucket.delete((other_key, other_value))
                self.size -= 1
                return
        raise KeyError('Key not found: {}'.format(key))

    def iterate(self):
        """Iterates through all the nodes available."""
        for node in self.items():
            yield node

    def __setitem__(self, key, value):
        self.set(key, value)
    
    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return self.contains(key)
    
    def __len__(self):
        return self.size

def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))

if __name__ == '__main__':
    test_hash_table()
