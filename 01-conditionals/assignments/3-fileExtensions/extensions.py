extensions = input('File name: ').strip()
a = extensions.lower().split('.')[-1]
if a == 'jpg' or a == 'jpeg':
    print('image/jpeg')

elif a == 'gif':
    print('image/gif')
elif a == "png":
    print("image/png")

elif a=='pdf':
    print('application/pdf')

elif a=='txt':
    print('text/plain')

elif a == 'zip':
    print('application/zip')

else:
    print('application/octet-stream')
