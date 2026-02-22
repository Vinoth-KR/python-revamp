# Tuples : immutable sequences of values
dimensions = (1920, 1080)
print('Original dimensions: ')
print(dimensions[0])
print(dimensions[1])

#editing the values will throw an error
#dimensions[0] = 720

# cannot modify the tuple but we can reassign it to a new value
dimensions = (720, 480)
print('Modified dimensions: ')
print(dimensions[0])
print(dimensions[1])