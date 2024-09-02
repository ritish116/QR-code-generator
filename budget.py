import tkinter as tk
from tkinter import ttk, messagebox

class HostelBudgetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Hostel Budget Planner (INR)")

        
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))


        tk.Label(self.main_frame, text="Enter Monthly Allowance (INR):").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.salary_entry = tk.Entry(self.main_frame)
        self.salary_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)


        self.calculate_button = tk.Button(self.main_frame, text="Calculate", command=self.calculate_budget)
        self.calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

        
        self.result_text = tk.Text(self.main_frame, height=15, width=50, wrap=tk.WORD)
        self.result_text.grid(row=2, column=0, columnspan=2, pady=10)

    
        self.categories = {
            "Hostel Rent": 0.40,        
            "Utilities (Electricity, Water, etc.)": 0.10, 
            "Groceries": 0.20,           
            "Transportation": 0.10,      
            "Miscellaneous": 0.10,       
            "Savings": 0.10              
        }

    def calculate_budget(self):
        try:
            salary = float(self.salary_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for the allowance.")
            return

        total_percentage = sum(self.categories.values())
        
        if total_percentage != 1:
            messagebox.showerror("Error", "The total percentage for categories must equal 100%.")
            return

        expenditures = {category: salary * percentage for category, percentage in self.categories.items()}
        savings = expenditures.pop('Savings')  

        
        result_message = (
            f"Monthly Allowance: ₹{salary:.2f}\n\n"
            f"Recommended Allocation:\n"
        )
        for category, amount in expenditures.items():
            result_message += f"  {category}: ₹{amount:.2f}\n"
        result_message += f"\nTotal Expenditure: ₹{sum(amount for category, amount in expenditures.items() if category != 'Savings'):.2f}\n"
        result_message += f"Total Savings: ₹{savings:.2f}"

    
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result_message)

if __name__ == "__main__":
    root = tk.Tk()
    app = HostelBudgetApp(root)
    root.mainloop()
