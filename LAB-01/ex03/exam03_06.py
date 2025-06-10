def xoa_phan_tu(index,key):
    if key in index:
        del index[key]
        return True
    else:
        return False
    
my_index = {'a:1', 'b:2', 'c:3', 'd:4'}
key_to_delete = 'b'
result = xoa_phan_tu(my_index,key_to_delete)
if result:
    print({my_index}, "deleted from index.")
else:
    print({key_to_delete}, "not found in index.")