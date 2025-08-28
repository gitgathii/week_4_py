try:
    file=open('nonexistent.txt', 'r')
    data=file.read()
except FileNotFoundError:
    print('file not found .please check the filename')

