#/home/kali/.config/bin/target.sh

def change_file(target):
    f = open("/home/kali/.config/bin/target.sh", "w")
    f.write(target)
    f.close()

options = int(input('New Target\n\t(0) No Target\n\t(1) New Target\nWould like to change tha Target?:  '))

if options == 0:
    target = '#!/bin/sh\necho "%{u-} No Target' + '"'
    change_file(target)
elif options == 1:
    ip = str(input('Wich is the new address? '))
    target = '#!/bin/sh\necho "%{u-} ' + ip + '"'
    change_file(target)
else:
    print('Invalid Option')
