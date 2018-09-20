from tkinter import *
from tkinter import ttk
import json


root_window = Tk()


plan_name_label = Label(root_window, text = "Plan Name", padx = 10, pady= 10)
plan_name_label.grid(row = 1, column = 0,sticky="E")
plan_name_entry = Entry(root_window, bg="white",highlightthickness=2)
plan_name_entry.grid(row = 1 , column = 1)


monthly_rental_label = Label(root_window, text = "Monthly Rental",padx = 10, pady= 10)
monthly_rental_label.grid(row = 2 , column = 0,sticky="E")
monthly_rental_entry = Entry(root_window,highlightthickness=2)
monthly_rental_entry.grid(row = 2 , column = 1)


free_internet_label = Label(root_window, text = "Free Internet", padx = 10, pady= 10)
free_internet_label.grid(row = 3 , column = 0,sticky="E")
free_internet_entry = Entry(root_window,highlightthickness=2)
free_internet_entry.grid(row = 3 , column = 1)


free_calls_label = Label(root_window, text = "Free Calls", padx = 10, pady= 10)
free_calls_label.grid(row = 4 , column = 0,sticky="E")
free_calls_entry = Entry(root_window,highlightthickness=2)
free_calls_entry.grid(row = 4 , column = 1)

free_sms_label = Label(root_window, text = "Free SMSs", padx = 10, pady= 10)
free_sms_label.grid(row = 5 , column = 0,sticky="E")
free_sms_entry = Entry(root_window,highlightthickness=2)
free_sms_entry.grid(row = 5 , column = 1)


call_charges_label = Label(root_window, text = "Call Charges", padx = 10, pady= 10)
call_charges_label.grid(row = 6 , column = 0,sticky="E")
call_charges_entry = Entry(root_window,highlightthickness=2)
call_charges_entry.grid(row = 6 , column = 1)

sms_charge_label = Label(root_window, text = "SMS Charges", padx = 10, pady= 10)
sms_charge_label.grid(row = 7 , column = 0,sticky="E")
sms_charge_entry = Entry(root_window,highlightthickness=2)
sms_charge_entry.grid(row = 7 , column = 1)

internet_charge_label = Label(root_window, text = "Data Charges", padx = 10, pady= 10)
internet_charge_label.grid(row = 8 , column = 0,sticky="E")
internet_charge_entry = Entry(root_window,highlightthickness=2)
internet_charge_entry.grid(row = 8 , column = 1)

roaming_charge_label = Label(root_window, text = "Roaming Charges", padx = 10, pady= 10)
roaming_charge_label.grid(row = 9 , column = 0,sticky="E")
roaming_charge_entry = Entry(root_window,highlightthickness=2)
roaming_charge_entry.grid(row = 9 , column = 1)


submit_button = ttk.Button(root_window, text = "Submit", command = lambda : submit())
submit_button.grid(row = 10 , column = 0)

exit_button = ttk.Button(root_window, text = "Exit",command = lambda : sys.exit())
exit_button.grid(row = 10 , column = 1)

see_plans_button = ttk.Button(root_window, text = "See Plans",command = lambda : see_plans())
see_plans_button.grid(row = 10 , column = 2)


def submit():
	#when submit button is clicked, save all the entry made and write to the file named plans.json
	all_plans = []
	with open('plans.json', 'r') as f:
		all_plans = json.load(f)['plans']
		plans_dictionary = {
		"plan_name":plan_name_entry.get(),
		"monthly_rental":monthly_rental_entry.get(),
		"free_internet":free_internet_entry.get(),
		"free_calls":free_calls_entry.get(),
		"free_sms":free_sms_entry.get(),
		"call_charges":call_charges_entry.get(),
		"sms_charges":sms_charge_entry.get(),
		"internet_charge":internet_charge_entry.get(),
		"roaming_charge":roaming_charge_entry.get()
		}
		all_plans.append(plans_dictionary)
	save(all_plans)


def save(all_plans):
	with open('plans.json', 'w') as f:
		json.dump({'plans':all_plans}, f)





def see_plans():
	see_plans_window = Tk()
	see_plans_window.geometry("400x500+500+230")
	see_plans_window.title('Plans list')
	see_plans_window.mainloop()

root_window.geometry("400x500+500+230")
root_window.title("PostPaid plan User Interface")
root_window.mainloop()


