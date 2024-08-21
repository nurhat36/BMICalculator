import tkinter as tk

# Pencere oluşturma
window = tk.Tk()
window.title("Python Tkinter")
window.minsize(width=450, height=300)

# Etiketler
my_label = tk.Label(text="BMI Calculator", font=("arial", 10, "italic"))
my_label.config(bg="black", fg="white")
my_label.place(x=0, y=0)

kg_label = tk.Label(text="Kilonuzu giriniz:", font=("arial", 10, "italic"))
kg_label.config(bg="black", fg="white")
kg_label.pack()

# Fonksiyon
def click_button():
    kg = kg_entry.get()
    boy = boy_entry.get()

    if kg == "" or boy == "":
        bos_label = tk.Label(text="Lütfen bilgilerinizi tam giriniz", font=("arial", 10, "italic"))
        bos_label.config(bg="black", fg="white")
        bos_label.pack()
    else:
        try:
            kg = float(kg)
            boy = float(boy)
            sonuc = kg / (boy ** 2)
            bos_label = tk.Label(text=f"BMI = {sonuc:.2f}", font=("arial", 10, "italic"))
            bos_label.config(bg="black", fg="white")
            bos_label.pack()
        except ValueError:
            bos_label = tk.Label(text="Lütfen geçerli bir sayı giriniz", font=("arial", 10, "italic"))
            bos_label.config(bg="black", fg="white")
            bos_label.pack()

# Giriş alanları
kg_entry = tk.Entry(width=20)
kg_entry.pack()

boy_label = tk.Label(text="Boyunuzu giriniz:", font=("arial", 10, "italic"))
boy_label.config(bg="black", fg="white")
boy_label.pack()

boy_entry = tk.Entry(width=20)
boy_entry.pack()

# Buton
my_button = tk.Button(text="Calculate", command=click_button)
my_button.pack()
bmi_label = tk.Label(text="18.5'in altı: Zayıf \n 18.5 - 24.9: Normal kilolu \n 25 - 29.9: Fazla kilolu\n 30 ve üstü: Obez", font=("arial", 10, "italic"))
bmi_label.config(bg="black", fg="white")
bmi_label.place(x=150,y=150)




# Pencere döngüsü
window.mainloop()
