# Copy line 3 and 4 into Python Interpreter (TERMINAL)

devices = ['r1', 'r2', 'r3']
print (devices[4])

# To see the error messages
# Then copy the remaining code into Python Interpreter, 
# (TERMINAL) then exit back you should see the Insert custom code... messages

try:
    print(devices[4])
except (IndexError) as err_msg:
    print ('Insert custom code...')
    print ('Error from Python:', err_msg)


