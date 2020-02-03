from tkinter import *

# # from gui_stuff import *
#
# # l1=['salt','eggs','bananas','milk']
# #
# # food_name=['']
#
# # l2=[]
# # for x in range(0,len(l1)):
# #     l2.append(0)
#
# # TESTING DATA df -------------------------------------------------------------------------------------
# df=pd.read_csv("train.csv")
#
# # print(df.head())
#
# X= df[l1]
#
# y = df[["ingredients__001"]]
# np.ravel(y)
# # print(y)
#
# # TRAINING DATA tr --------------------------------------------------------------------------------
# tr=pd.read_csv("test.csv")
#
# X_test= tr[l1]
# y_test = tr[["ingredients"]]
# np.ravel(y_test)
# # ------------------------------------------------------------------------------------------------------
#
# # def NaiveBayes():
# #     from sklearn.naive_bayes import GaussianNB
# #     gnb = GaussianNB()
# #     gnb=gnb.fit(X,np.ravel(y))
# #
# #     # calculating accuracy-------------------------------------------------------------------
# #     from sklearn.metrics import accuracy_score
# #     y_pred=gnb.predict(X_test)
# #     print(accuracy_score(y_test, y_pred))
# #     print(accuracy_score(y_test, y_pred,normalize=False))
# #     # -----------------------------------------------------
# #
# #     psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]
# #     for k in range(0,len(l1)):
# #         for z in psymptoms:
# #             if(z==l1[k]):
# #                 l2[k]=1
# #
# #     inputtest = [l2]
# #     predict = gnb.predict(inputtest)
# #     predicted=predict[0]
# #
# #     h='no'
# #     for a in range(0,len(disease)):
# #         if(predicted == a):
# #             h='yes'
# #             break
# #
# #     if (h=='yes'):
# #         t3.delete("1.0", END)
# #         t3.insert(END, disease[a])
# #     else:
# #         t3.delete("1.0", END)
# #         t3.insert(END, "Not Found")
# #
# # # gui_stuff------------------------------------------------------------------------------------
# #
# # root = Tk()
# # root.configure(background='white')
# #
# # # entry variables
# # Symptom1 = StringVar()
# # Symptom1.set(None)
# # Symptom2 = StringVar()
# # Symptom2.set(None)
# # Symptom3 = StringVar()
# # Symptom3.set(None)
# # Symptom4 = StringVar()
# # Symptom4.set(None)
# # Symptom5 = StringVar()
# # Symptom5.set(None)
# # Name = StringVar()

# Heading
w2 = Label(root, justify=LEFT, text="Recipe Generator with the currrent ingredient", fg="brown", bg="yellow")
w2.config(font=("Arial", 30))

w2.grid(row=1, column=0, columnspan=2, padx=100)

w2.grid(row=2, column=0, columnspan=2, padx=100)

# labels
NameLb = Label(root, text="Ingredient", fg="black", bg="white")
NameLb.grid(row=6, column=0, pady=15, sticky=W)

#
# S1Lb = Label(root, text="Symptom 1", fg="black", bg="white")
# S1Lb.grid(row=7, column=0, pady=2, sticky=W)
#
# S2Lb = Label(root, text="Symptom 2", fg="black", bg="white")
# S2Lb.grid(row=8, column=0, pady=2, sticky=W)
#
# S3Lb = Label(root, text="Symptom 3", fg="black", bg="white")
# S3Lb.grid(row=9, column=0, pady=2, sticky=W)
#
# S4Lb = Label(root, text="Symptom 4", fg="black", bg="white")
# S4Lb.grid(row=10, column=0, pady=2, sticky=W)
#
# S5Lb = Label(root, text="Symptom 5", fg="black", bg="white")
# S5Lb.grid(row=11, column=0, pady=2, sticky=W)
#
# ranfLb = Label(root, text="NaiveBayes", fg="white", bg="red")
# ranfLb.grid(row=19, column=0, pady=10, sticky=W)

# entries
OPTIONS = sorted(l1)

NameEn = Entry(root, textvariable=Name)
NameEn.grid(row=6, column=1)

S1En = OptionMenu(root, Symptom1,*OPTIONS)
S1En.grid(row=7, column=1)

S2En = OptionMenu(root, Symptom2,*OPTIONS)
S2En.grid(row=8, column=1)

S3En = OptionMenu(root, Symptom3,*OPTIONS)
S3En.grid(row=9, column=1)

S4En = OptionMenu(root, Symptom4,*OPTIONS)
S4En.grid(row=10, column=1)

S5En = OptionMenu(root, Symptom5,*OPTIONS)
S5En.grid(row=11, column=1)

lr = Button(root, text="NaiveBayes", command=NaiveBayes,bg="green",fg="yellow")
lr.grid(row=10, column=3,padx=10)

#textfileds
t1 = Text(root, height=1, width=40,bg="orange",fg="black")
t1.grid(row=15, column=1, padx=10)

t2 = Text(root, height=1, width=40,bg="orange",fg="black")
t2.grid(row=17, column=1 , padx=10)

t3 = Text(root, height=1, width=40,bg="orange",fg="black")
t3.grid(row=19, column=1 , padx=10)

root.mainloop()