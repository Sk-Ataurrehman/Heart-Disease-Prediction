from tkinter import *
from tkinter import ttk, messagebox
import pandas as pd
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from fpdf import FPDF

class Main:
    pdf = FPDF() 
    pdf.add_page()
    pdf.set_font("Arial", size = 15) 
        
    df = pd.read_csv('Dataset.csv')
    knn = KNeighborsClassifier(n_neighbors=5)
    target = df['Heart Disease']
    features = df.drop('Heart Disease', axis=1)
    knn.fit(features, target)

    def __init__(self,root):
        self.root = root
        self.root.geometry('930x550+0+0')
        self.root.title("Heart Disease Prediction")
        self.root.config(bg="white")
        
        Label(self.root, text="Heart Disease Prediction using Machine Learning Alogrithm",font=("Times New Roman",20, "bold"),bg="white",fg="black").place(x=20, y=10)
        Label(self.root, text="Note: Details should be filled by Medical Personel.",font=("Times New Roman",12, "bold"),bg="white",fg="red").place(x=20, y=50)

        Label(self.root, text="Full Name:",font=("Times New Roman",16, "bold"),bg="white",fg="gray").place(x=20, y=100)
        self.txt_fname = Entry(self.root,font=("Times New Roman",14))
        self.txt_fname.place(x=20, y=130, width=200)

        Label(self.root, text="Gender:",font=("Times New Roman",16, "bold"),bg="white",fg="gray").place(x=240, y=100)
        self.gender = ttk.Combobox(self.root,font=("Times New Roman",14),state="readonly",justify=CENTER)
        self.gender['values'] = ("Select","Male","Female") 
        self.gender.place(x=240, y=130,width=200)
        self.gender.current(0)

        Label(self.root, text="Age Group:",font=("Times New Roman",16, "bold"),bg="white",fg="gray").place(x=460, y=100)
        self.age = ttk.Combobox(self.root,font=("Times New Roman",14),state="readonly",justify=CENTER)
        self.age['values'] = ("Select","(20-34)","(35-50)","(51-60)","(61-79)","Greater than 79") 
        self.age.place(x=460, y=130,width=200)
        self.age.current(0)

        Label(self.root, text="Blood Cholestrol:",font=("Times New Roman",16, "bold"),bg="white",fg="gray").place(x=20, y=200)
        self.chol = ttk.Combobox(self.root,font=("Times New Roman",14),state="readonly",justify=CENTER)
        self.chol['values'] = ("Select","Below 200 mg/dL - Low","200-239 mg/dL - Normal", "240 mg/dL and above - High") 
        self.chol.place(x=20, y=230,width=200)
        self.chol.current(0)

        Label(self.root, text="Blood Pressure:",font=("Times New Roman",16, "bold"),bg="white",fg="gray").place(x=240, y=200)
        self.pressure = ttk.Combobox(self.root,font=("Times New Roman",14),state="readonly",justify=CENTER)
        self.pressure['values'] = ("Select","Below 120 mm Hg- Low","120 to 139 mm Hg- Normal", "Above 139 mm Hg- High") 
        self.pressure.place(x=240, y=230,width=200)
        self.pressure.current(0)

        Label(self.root, text="Hereditary (Family Member diagnosed with HD):",font=("Times New Roman",16, "bold"),bg="white",fg="gray").place(x=460, y=200)
        self.here = ttk.Combobox(self.root,font=("Times New Roman",14),state="readonly",justify=CENTER)
        self.here['values'] = ("Select","Yes", "No") 
        self.here.place(x=460, y=230,width=200)
        self.here.current(0)

        Label(self.root, text="Smoking:",font=("Times New Roman",16, "bold"),bg="white",fg="gray").place(x=20, y=300)
        self.smoke = ttk.Combobox(self.root,font=("Times New Roman",14),state="readonly",justify=CENTER)
        self.smoke['values'] = ("Select","Yes","No") 
        self.smoke.place(x=20, y=330,width=200)
        self.smoke.current(0)

        Label(self.root, text="Alcohol Intake:",font=("Times New Roman",16, "bold"),bg="white",fg="gray").place(x=240, y=300)
        self.alcohol = ttk.Combobox(self.root,font=("Times New Roman",14),state="readonly",justify=CENTER)
        self.alcohol['values'] = ("Select","Yes","No") 
        self.alcohol.place(x=240, y=330,width=200)
        self.alcohol.current(0)

        Label(self.root, text="Physical Activity:",font=("Times New Roman",16, "bold"),bg="white",fg="gray").place(x=460, y=300)
        self.phy = ttk.Combobox(self.root,font=("Times New Roman",14),state="readonly",justify=CENTER)
        self.phy['values'] = ("Select","Low", "Normal", "High") 
        self.phy.place(x=460, y=330,width=200)
        self.phy.current(0)

        Label(self.root, text="Diabetes:",font=("Times New Roman",16, "bold"),bg="white",fg="gray").place(x=20, y=400)
        self.diab = ttk.Combobox(self.root,font=("Times New Roman",14),state="readonly",justify=CENTER)
        self.diab['values'] = ("Select","Yes","No") 
        self.diab.place(x=20, y=430,width=200)
        self.diab.current(0)

        Label(self.root, text="Diet:",font=("Times New Roman",16, "bold"),bg="white",fg="gray").place(x=240, y=400)
        self.diet = ttk.Combobox(self.root,font=("Times New Roman",14),state="readonly",justify=CENTER)
        self.diet['values'] = ("Select","Poor", "Normal", "Good") 
        self.diet.place(x=240, y=430,width=200)
        self.diet.current(0)

        Label(self.root, text="Obesity:",font=("Times New Roman",16, "bold"),bg="white",fg="gray").place(x=460, y=400)
        self.obes = ttk.Combobox(self.root,font=("Times New Roman",14),state="readonly",justify=CENTER)
        self.obes['values'] = ("Select","Yes","No") 
        self.obes.place(x=460, y=430,width=200)
        self.obes.current(0)

        Label(self.root, text="Stress:",font=("Times New Roman",16, "bold"),bg="white",fg="gray").place(x=680, y=400)
        self.stress = ttk.Combobox(self.root,font=("Times New Roman",14),state="readonly",justify=CENTER)
        self.stress['values'] = ("Select","Yes","No") 
        self.stress.place(x=680, y=430,width=200)
        self.stress.current(0)

        self.predictBtn = Button(self.root,text="Predict", font=("Times New Roman",16, "bold"), bg="green",fg="white", bd=0,cursor="hand2", command=self.fun_predict).place(x=20,y=500, width=200)

    def fun_predict(self):
        if ((self.txt_fname.get() == "") or (self.gender.get() == "Select") or (self.age.get() == "Select") or (self.chol.get() == "Select") or (self.pressure.get() == "Select") or (self.here.get() == "Select") or (self.smoke.get() == "Select") or (self.alcohol.get() == "Select") or (self.diab.get() == "Select") or (self.phy.get() == "Select") or (self.diet.get() == "Select") or (self.obes.get() == "Select") or (self.stress.get() == "Select")):
            messagebox.showerror("Error!", "Please, Fill All the Details!")
        else:
            if(self.gender.get() == "Male"):
                gender = 1
            elif(self.gender.get() == "Female"):
                gender = 0
                
            if(self.age.get() == "(20-34)"):
                age = -2
            elif(self.age.get() == "(35-50)"):
                age = -1
            elif(self.age.get() == "(51-60)"):
                age = 0
            elif(self.age.get() == "(61-79)"):
                age = 1
            elif(self.age.get() == "Greater than 79"):
                age = 2
            
            if(self.chol.get() == "Below 200 mg/dL - Low"):
                chol = -1
            elif(self.chol.get() == "200-239 mg/dL - Normal"):
                chol = 0
            elif(self.chol.get() == "240 mg/dL and above - High"):
                chol = 1
            
            if(self.pressure.get() == "Below 120 mm Hg- Low"):
                pressure = -1
            elif(self.pressure.get() == "120 to 139 mm Hg- Normal"):
                pressure = 0
            elif(self.pressure.get() == "Above 139 mm Hg- High"):
                pressure = 1
            
            if(self.here.get() == "Yes"):
                here = 1
            elif(self.here.get() == "No"):
                here = 0
            
            if(self.smoke.get() == "Yes"):
                smoke = 1
            elif(self.smoke.get() == "No"):
                smoke = 0
                
            if(self.alcohol.get() == "Yes"):
                alcohol = 1
            elif(self.alcohol.get() == "No"):
                alcohol = 0
                
            if(self.phy.get() == "Low"):
                phy = -1
            elif(self.phy.get() == "Normal"):
                phy = 0
            elif(self.phy.get() == "High"):
                phy = 1
                
            if(self.diab.get() == "Yes"):
                diab = 1
            elif(self.diab.get() == "No"):
                diab = 0
            
            if(self.diet.get() == "Poor"):
                diet = -1
            elif(self.diet.get() == "Normal"):
                diet = 0
            elif(self.diet.get() == "Good"):
                diet = 1
                
            if(self.obes.get() == "Yes"):
                obes = 1
            elif(self.obes.get() == "No"):
                obes = 0
            
            if(self.stress.get() == "Yes"):
                stress = 1
            elif(self.stress.get() == "No"):
                stress = 0
        
            self.predict = Main.knn.predict([[gender, age, chol, pressure, here, smoke, alcohol, phy, diab, diet, obes, stress]])
            self.generate_report()
                
    def generate_report(self):
        self.pdf.cell(200, 10, txt = "Report - Heart Disease Prediction", ln = 1, align = 'C') 
        self.pdf.set_font("Arial", size = 13) 
        self.pdf.cell(50, 15, txt = "Full Name: "+self.txt_fname.get(), ln = 1) 
        self.pdf.cell(50, 15.2, txt = "Gender: "+self.gender.get(), ln = 1) 
        self.pdf.cell(50, 15.4, txt = "Age Group: "+self.age.get(), ln = 1) 
        self.pdf.cell(50, 15.6, txt = "Blood Cholestrol: "+self.chol.get(), ln = 1) 
        self.pdf.cell(50, 15.8, txt = "Blood Pressure: "+self.pressure.get(), ln = 1) 
        self.pdf.cell(50, 16, txt = "Hereditary: "+self.here.get(), ln = 1) 
        self.pdf.cell(50, 16.2, txt = "Smoking: "+self.smoke.get(), ln = 1) 
        self.pdf.cell(50, 16.4, txt = "Alcohol: "+self.alcohol.get(), ln = 1) 
        self.pdf.cell(50, 16.6, txt = "Physical Activity: "+self.phy.get(), ln = 1) 
        self.pdf.cell(50, 16.8, txt = "Diabetes: "+self.diab.get(), ln = 1) 
        self.pdf.cell(50, 17, txt = "Diet: "+self.diet.get(), ln = 1) 
        self.pdf.cell(50, 17.2, txt = "Obesity: "+self.obes.get(), ln = 1) 
        self.pdf.cell(50, 17.4, txt = "Stress: "+self.stress.get(), ln = 1)
        if (self.predict[0] == 1):
            self.pdf.cell(50, 18, txt = "Result: You can be affected by Heart Disease!", ln = 1)
        elif(self.predict[0] == 0):
            self.pdf.cell(50, 18, txt = "Result: You aren't affected by Heart Disease!", ln = 1)         
        self.pdf.output(self.txt_fname.get() + ".pdf")
        self.root.destroy()
        
root = Tk()
obj = Main(root)
root.mainloop() 



