body = open("itt-endsem-prep/l6codes/body.txt", "r+")
names = open("itt-endsem-prep/l6codes/names.txt", "r+")

bdy = body.read()

for nam in names:
    mail = "Hello " + nam.strip() + "\n" + bdy
    wri = open(nam.strip() + ".txt", "w")
    wri.write(mail)
