import string
import random
from tkinter import Button,Label,Entry,Tk,messagebox
import re


class GUI():



    def __init__(self,master):


        
        master.title('Password Generator')
        master.geometry('840x500')
        
        master.resizable(False, False)

        self.label=Label(text="Password Generator",fg='red',font='elephant 35 underline bold')
        self.label.grid(row=0,column=0,columnspan=3)

        self.blank_label1=Label(text="")
        self.blank_label1.grid(row=1,column=0,columnspan=2)

        self.blank_label2=Label(text="")
        self.blank_label2.grid(row=2,column=0,columnspan=2)
        
        self.blank_label3=Label(text="")
        self.blank_label3.grid(row=3,column=0)

        self.blank_label4=Label(text="")
        self.blank_label4.grid(row=4,column=0)

        self.blank_label3=Label(text="")
        self.blank_label3.grid(row=6,column=0)

        self.length=Label(text="Enter the length:",font='times 25 bold italic')
        self.length.grid(row=7,column=0)

        self.length_textfield=Entry(font='times 20',bd=6,relief='groove')
        self.length_textfield.grid(row=7,column=1)

        self.blank_label4=Label(text="")
        self.blank_label4.grid(row=8,column=0)

        self.generated_password=Label(text="Generated Password:",font='times 25 bold italic')
        self.generated_password.grid(row=9,column=0)

        self.generated_password_textfield=Entry(font='times 20',bd=6,relief='groove',fg='darkgreen')
        self.generated_password_textfield.grid(row=9,column=1)
        
        self.blank_label5=Label(text="")
        self.blank_label5.grid(row=10,column=0)

        self.blank_label6=Label(text="")
        self.blank_label6.grid(row=11,column=0)

        self.generate=Button(text="Generate Password",bd=4,relief='solid',padx=1,pady=1,font='forte 25 bold',fg='maroon',bg='limegreen',command=self.generate_pass)
        self.generate.grid(row=12,column=0)

        self.reset=Button(text="Reset",bd=4,relief='solid',padx=1,pady=1,font='forte 25 bold',fg='darkblue',bg='red',command=self.reset_fields)
        self.reset.grid(row=12,column=2)


  
    

    def generate_pass(self):
         upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
         lower = "abcdefghijklmnopqrstuvwxyz"
         chars = "@#%&()\"?!"
         numbers = "1234567890"
         upper = list(upper)
         lower = list(lower)
         chars = list(chars)
         numbers = list(numbers)
       
         leng=self.length_textfield.get()
        
       
         if leng.isalpha()==True:
            messagebox.showwarning("Attention", "La longueur doit être un nombre étant égal à 8 !")
            self.length_textfield.delete(0,25)
            return
             
         if leng=='':
             self.blank_label2.configure(text="Le champ ne peut pas être vide !",font='times 20 bold',fg='blue')
             self.blank_label1.configure(text="")
             return
         else:
             self.blank_label2.configure(text="")
         length=int(leng)  
         
         if length<8:
              self.blank_label1.configure(text="Le mot de passe doit comporter au moins 8 caractères !",font='times 20 italic',fg='green')
              self.blank_label2.configure(text="")
              return
         else:
              self.blank_label1.configure(text="")

         if length>8:
              self.blank_label1.configure(text="Le mot de passe doit comporter pas plus de 8 caractères !",font='times 20 italic',fg='green')
              self.blank_label2.configure(text="")
              return
         else:
              self.blank_label1.configure(text="")

         
         self.generated_password_textfield.delete(0,length)
    
         u = random.randint(1, length-3)
         l = random.randint(1, length-2-u)
         c = random.randint(1, length-1-u-l)
         n = length-u-l-c
         password = random.sample(upper,u)+random.sample(lower,l)+random.sample(chars,c)+random.sample(numbers,n)
         random.shuffle(password)
         gen_passwd="".join(password)
         self.generated_password_textfield.insert(0,gen_passwd)
         

     
    def reset_fields(self):
        self.length_textfield.delete(0,25)
        self.generated_password_textfield.delete(0,25)
        


if __name__=='__main__':
     root=Tk()
     pass_gen=GUI(root)
     root.mainloop()