#--handle error at runtime
try:
    a=4
    c=a/b
except:
    print('Error ')
finally:
    print('Resource Closed')