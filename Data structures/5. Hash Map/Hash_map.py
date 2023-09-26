# Basic hash map implementation in Python 3

class HashTable:
    
    # Create the table with a particular size
    def __init__(self,size):
        self.size = size
        self.hash_table = self.create_buckets()
        
    def create_buckets(self):
        return [[] for _ in range(self.size)]
    
    # Inserts values into the hash map
    def set_val(self, key, val):
        
        hashed_key = hash(key)
        
        bucket = self.hash_table[hashed_key]
        found_key = False
        
        for index, record in enumerate(bucket):
            record_key, record_val = record
            if record_key == key:
                found_key = True
                break
            
        
        if found_key:
            bucket[index] = (key,val)
        else:
            bucket.append = ((key,val))
    
    def get_val(self,key):
        
        hashed_key = hash(key)
        
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
            
            if record_key == key:
                found_key = True
                break
        
        if found_key:
            return record_val
        else:
            return "No record found"
        
    def delete_val (self,key):
        
        hashed_key = hash(key)
        
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket.pop(index)
        return
        