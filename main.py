import tkinter as tk
from tkcalendar import DateEntry  # Make sure to install tkcalendar using pip
from datetime import  datetime 
import numpy as np  # Make sure to install numpy
import pandas as pd  # Make sure to install pandas
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
def estimate_coef(x, y):
    #  عدد الملاحظات/النقاط
    n = np.size(x)

    # متوسط ​​المتجه x و y
    m_x = np.mean(x)
    m_y = np.mean(y)

    # حساب الانحراف العرضي والانحراف حول x
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x

    # حساب معاملات الانحدار
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x

    return (b_0, b_1)
def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color = "m",   marker = "o", s = 30)

    # predicted response vector
    y_pred = b[0] + b[1]*x

    # plotting the regression line
    plt.plot(x, y_pred, color = "g")

    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def get_days_between_two_dates(current_date_str : str):
    reference_date = datetime(2023, 1, 1)
    # print(type( current_date_str.replace('b','')),'-',current_date_str.replace('b',''),'-'*100)
    date_format='%m/%d/%y'


    dateStr=current_date_str
    
    if(current_date_str[0]=='b'):
        dateStr=current_date_str.replace('b','').replace("'","")


    current_date=datetime.strptime(dateStr,date_format)  
    difference = current_date - reference_date
    return difference.days + 1
def custom_round(number, decimal_places=2):
    return round(number, decimal_places)

def submit_form():
    date_value = date_picker.get()
    if len(date_value)==0:
        data_value="1/1/23"

    file_path = 'random_values.csv'  # يجب استبداله بالمسار الفعلي لملف CSV الخاص بك
    data = pd.read_csv(file_path)

    global x 
    x=data["x"] #np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    global y
    y = data["y"]#np.array([22.5, 22.6, 22.7, 22.5, 22.65, 22.5, 22.7, 22.67, 22.75, 22.8])
    
    # estimating coefficients
    global b
    b = estimate_coef(x, y)
    

    date_value = date_picker.get()

    dayes=get_days_between_two_dates(date_value)
    f=b[0]+dayes*b[1]


    balance_resalt=tk.Label(root, text=f"{custom_round(f)} TL",)
    print(f"dayes: {dayes}")

    balance_resalt.grid(row=0, column=1, padx=10, pady=10,)




# Create the main window
root = tk.Tk()
root.title("Balance Form")
root.geometry("450x250")

# Create and place the Balance Label and Entry
balance_label = tk.Label(root, text="Balance:")
balance_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

balance_resalt = tk.Label(root, text="",font=('Helvetica bold',20,))
balance_resalt.grid(row=0, column=1, padx=10, pady=10,)

# Create and place the Date Label and DatePicker
date_label = tk.Label(root, text="Date:")
date_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

date_picker = DateEntry(root, width=50, background='darkblue', foreground='white', borderwidth=2)
date_picker.grid(row=1, column=1, padx=10, pady=10)

# Create and place the Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=2, column=0, columnspan=2, pady=20)
submit_button = tk.Button(root, text="show diagram", command=lambda :plot_regression_line(x, y, b) )
submit_button.grid(row=6, column=0, columnspan=2, pady=20)
# Run the Tkinter event loop
root.mainloop()





 