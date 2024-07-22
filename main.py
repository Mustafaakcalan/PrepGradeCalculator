import tkinter as tk
from tkinter import messagebox

"""
Bu fonksiyon, verilen değerin geçerli bir sayı olup olmadığını ve 0 ile 100 arasında olup olmadığını kontrol eder.
float(value) ile float'a dönüştürür. Dönüştürme başarısız olursa, ValueError hatası verir ve bu durumda False döner.
Değer başarılı bir şekilde float'a dönüştürülür ise 0 ile 100 arasındaysa True döner.
"""

def check_value(value):
    try:
        value = float(value)
    except ValueError:
        return False
    return 0 <= value <= 100

""""
get() metodu her girilen sınav notu değerini stringe döndürür
ve bunları "values'in" içinde toplar. 
"""
def calculate_grades():

    values = [entry_y1.get(), entry_y2.get(), entry_y3.get(), entry_y4.get(), entry_y5.get(),
              entry_y6.get(), entry_y7.get(), entry_y8.get(), entry_y9.get(), entry_y10.get(),
              entry_y11.get()]

    """"    
    check_value(value) fonksiyonu, değerin sayı olup olmadığını ve 0 ile 100 arasında olup olmadığını kontrol eder.
    all() fonksiyonu, check_value fonksiyonunun tüm değerler için True döndürdüğünden emin olur.
    """
    if all(check_value(value) for value in values):
        y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11 = map(float, values)

        autumn_term = (y1 * 0.15 + y2 * 0.30 + y3 * 0.15 + y4 * 0.30 + y5 * 0.10)
        spring_term = (y6 * 0.15 + y7 * 0.30 + y8 * 0.15 + y9 * 0.30 + y10 * 0.10)
        genel_başarı_notu = (autumn_term * 0.30 + spring_term * 0.30 + y11 * 0.40)

        result_message = (
            f"Güz dönemi puan ortalamanız: {autumn_term:.2f}\n"
            f"Bahar dönemi puan ortalamanız: {spring_term:.2f}\n"
            f"Genel başarı notunuz: {genel_başarı_notu:.2f}\n"
            f"{'Tebrikler, hazırlık programını geçtiniz!' if genel_başarı_notu >= 65 else 'Hazırlık programını geçemediniz.'}"
        )
        messagebox.showinfo("Sonuç", result_message)
    else:
        messagebox.showerror("Hata", "Lütfen tüm alanlara geçerli bir not giriniz (0-100 arası).")


# root.title() metodu, pencerenin başlık çubuğunda görünen metni "Sınav Notları Hesaplama" olarak belirler.
root = tk.Tk()
root.title("Sınav Notları Hesaplama")


labels = [
    "1. Quiz notunuz:", "1. Vize notunuz:", "2. Quiz notunuz:", "2. Vize notunuz:", "1. Sunum notunuz:",
    "3. Quiz notunuz:", "3. Vize notunuz:", "4. Quiz notunuz:", "4. Vize notunuz:", "2. Sunum notunuz:",
    "Final sınavı notunuz:"
]

entries = []
for i, label in enumerate(labels):
    tk.Label(root, text=label).grid(row=i, column=0, padx=10, pady=5, sticky='e')
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)


(entry_y1, entry_y2, entry_y3, entry_y4, entry_y5,
 entry_y6, entry_y7, entry_y8, entry_y9, entry_y10,
 entry_y11) = entries


calculate_button = tk.Button(root, text="Hesapla", command=calculate_grades)
calculate_button.grid(row=len(labels), columnspan=2, pady=10)


root.mainloop()