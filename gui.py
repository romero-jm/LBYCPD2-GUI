import tkinter as tk
from tkinter import ttk

class HRSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("HR System")
        self.root.geometry("1366x768")  # Optimized for 1366x768 resolution
        
        # Main Frame
        self.main_frame = tk.Frame(root, padx=20, pady=20)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Employee Picture (Using Tkinter's built-in PhotoImage, limited to PNG/GIF)
        self.photo = tk.PhotoImage(file="default.png")  # Replace with actual image
        self.img_label = tk.Label(self.main_frame, image=self.photo)
        self.img_label.grid(row=0, column=0, padx=20, pady=10, sticky="nw")
        
        # Employee Info Frame
        self.info_frame = tk.Frame(self.main_frame)
        self.info_frame.grid(row=0, column=1, padx=40, pady=10, sticky="nw")
        
        tk.Label(self.info_frame, text="Employee Name: John Doe", font=("Arial", 16)).grid(row=0, column=0, sticky="w")
        tk.Label(self.info_frame, text="Employee ID: 12345", font=("Arial", 16)).grid(row=1, column=0, sticky="w")
        tk.Label(self.info_frame, text="Department: IT", font=("Arial", 16)).grid(row=2, column=0, sticky="w")
        
        # Attendance Table Frame
        self.attendance_frame = tk.Frame(self.main_frame)
        self.attendance_frame.grid(row=1, column=0, columnspan=2, pady=20, sticky="w")
        
        tk.Label(self.attendance_frame, text="Attendance Record", font=("Arial", 16, "bold")).pack(anchor="w")
        
        self.tree = ttk.Treeview(self.attendance_frame, columns=("Date", "Status"), show="headings", height=15)
        self.tree.heading("Date", text="Date")
        self.tree.heading("Status", text="Status")
        self.tree.column("Date", width=200)
        self.tree.column("Status", width=150)
        self.tree.pack(expand=True, fill=tk.BOTH)
        
        # Sample Data
        sample_data = [("2025-03-25", "Present"), ("2025-03-24", "Absent"), ("2025-03-23", "Present"),
                       ("2025-03-22", "Present"), ("2025-03-21", "Present"), ("2025-03-20", "Absent"),
                       ("2025-03-19", "Present"), ("2025-03-18", "Present"), ("2025-03-17", "Absent")]
        for item in sample_data:
            self.tree.insert("", "end", values=item)

if __name__ == "__main__":
    root = tk.Tk()
    app = HRSystemGUI(root)
    root.mainloop()
