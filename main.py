from tkinter import *
from tkinter import messagebox
from rsa import generate_keypair , encrypt, decrypt

#Create windoe object
app = Tk()

app.title('RSA')
app.geometry('855x750')

hidden = StringVar()

def add_item():
    global hidden
    if message.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    
    public, private  , (p,q)= generate_keypair(15)
    # print("Your public key is ", public ," and your private key is ", private)
    pValue.set(p)
    qValue.set(q)
    encrypted_msg = encrypt(public, message.get())

    publicKeyValue.set('(' + str(public[0])  + ','  + str(public[1]) + ')')
    privateKeyValue.set('(' + str(private[0])  + ',' + str(private[1]) + ')')

    # print("Your encrypted message is: ")
    encryptValue.set(''.join(map(lambda x: str(x), encrypted_msg)))
    # print("Decrypting message with public key ", public ,"...")
    # print("Your message is:")    
    hidden = decrypt(private, encrypted_msg)
    
def showDecrypt():
    decryptValue.set(hidden)
#ask for input message to be encrypted
message = StringVar()
messageLabel = Label(app, text = 'Enter the message to be encrypted' , font = ('bold' , 24) , pady = 20)

messageLabel.pack()
messageEntry = Entry(app , textvariable = message, font = (25), justify = CENTER)
messageEntry.focus_force()
messageEntry.pack(ipady = 4)

#button to start rsa
startBtn = Button(app, text='Start RSA', font = ('', 16), width=12, command=add_item)
startBtn.pack(pady = 25)

frame1 = LabelFrame(app ,bd=-2 ,  padx = 5, pady = 5)
frame1.pack()

frame2 = LabelFrame(app ,bd=-2, padx = 5, pady = 5)
frame2.pack()

#Show p,q primes
pValue = StringVar()
pLabel = Label(frame1 , text = 'Value of p is : ' ,font = ('' ,18), pady = 10)
pLabel.grid(row = 4, column =0 , padx = 10)
pEntry = Entry(frame1 , textvariable = pValue, font = (20),justify = CENTER)
pEntry.grid(ipady = 4,row = 4, column =1, padx = 5 )

qValue = StringVar()
qLabel = Label(frame1 , text = 'Value of q is : ' ,font = ('' ,18), pady = 10)
qLabel.grid(row = 4, column =2 , padx = 10)
qEntry = Entry(frame1 , textvariable = qValue, font = (20) , justify = CENTER)
qEntry.grid(ipady = 4,row = 4, column =3, padx = 5 )

#Show publickey , privatekey

publicKeyValue = StringVar()
publicLabel = Label(frame2, text = 'Public Key (e,n) ' , font = ('bold' , 19) , pady = 20)

publicLabel.grid(row = 5, column =1 , padx = 20)
publicEntry = Entry(frame2 , textvariable = publicKeyValue,font = (20), justify = CENTER)
publicEntry.grid(ipady = 4,row = 6, column =1, padx = 10 )

privateKeyValue = StringVar()
privateLabel = Label(frame2, text = 'Private Key (d,n) ' , font = ('bold' , 19) , pady = 20)

privateLabel .grid(row = 7, column =1 , padx = 20)
privateEntry  = Entry(frame2 , textvariable = privateKeyValue,font = (20), justify = CENTER)
privateEntry.grid(ipady = 4,row = 8, column =1, padx = 10 )

#Encrypted Message

encryptValue = StringVar()
encryptLabel = Label(frame2, text = 'Encrypted Message is ' , font = ('bold' , 19) , pady = 20)

encryptLabel .grid(row = 9, column =1 , padx = 20)
encryptEntry  = Entry(frame2 , textvariable = encryptValue,  width = 50,font = (24) , justify = CENTER)
encryptEntry.grid(ipady = 4,row = 10, column =1, padx = 10 )

#Decrypt Button
decBtn = Button(frame2, text='Decrypt',font = ('', 16), width=12, command=showDecrypt)
decBtn.grid(row = 11, column = 1, pady = 10)


#Show decrypted message
decryptValue = StringVar()
decryptLabel = Label(frame2, text = 'Decrypted Message is ' , font = ('bold' , 19) , pady = 20)

decryptLabel.grid(row = 12, column =1 , padx = 20)
decryptEntry = Entry(frame2 , textvariable = decryptValue, font = (24), justify = CENTER)
decryptEntry.grid(ipady = 4,row = 13, column =1, padx = 10 )
#Start Program
app.mainloop()