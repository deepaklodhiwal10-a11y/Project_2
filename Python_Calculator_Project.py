import tkinter as tk
from tkinter import ttk, messagebox
import math

# =========================
# SmartCalc Pro
# =========================

class SmartCalcPro:

    def __init__(self, root):
        self.root = root
        self.root.title("SmartCalc Pro")
        self.root.geometry("1200x700")
        self.root.configure(bg="#2b2b2b")

        self.dark_mode = True

        self.main_bg = "#2b2b2b"
        self.sidebar_bg = "#252525"
        self.button_bg = "#3b4cca"
        self.active_bg = "#ff9800"
        self.text_color = "white"

        self.create_ui()

    # ---------------------
    # UI
    # ---------------------
    def create_ui(self):

        self.sidebar = tk.Frame(
            self.root,
            bg=self.sidebar_bg,
            width=250
        )
        self.sidebar.pack(side="left", fill="y")

        self.content = tk.Frame(
            self.root,
            bg=self.main_bg
        )
        self.content.pack(side="right", fill="both", expand=True)

        title = tk.Label(
            self.sidebar,
            text="🧮 SmartCalc Pro",
            bg=self.sidebar_bg,
            fg="white",
            font=("Segoe UI", 20, "bold")
        )
        title.pack(pady=20)

        menu_items = [
            ("Calculator", self.show_calculator),
            ("Scientific", self.show_scientific),
            ("Converter", self.show_converter),
            ("Statistics", self.show_statistics),
            ("Programmer", self.show_programmer),
            ("Finance", self.show_finance),
            ("Equation Solver", self.show_equation_solver)
        ]

        for text, cmd in menu_items:
            tk.Button(
                self.sidebar,
                text=text,
                command=cmd,
                bg=self.button_bg,
                fg="white",
                relief="flat",
                font=("Segoe UI", 11),
                height=2
            ).pack(fill="x", padx=10, pady=5)

        self.dark_var = tk.IntVar(value=1)

        tk.Checkbutton(
            self.sidebar,
            text="Dark Mode",
            variable=self.dark_var,
            command=self.toggle_theme,
            bg=self.sidebar_bg,
            fg="white",
            selectcolor=self.sidebar_bg
        ).pack(pady=20)

        self.show_calculator()

    # ---------------------
    # Helpers
    # ---------------------
    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    def create_title(self, text):
        tk.Label(
            self.content,
            text=text,
            bg=self.main_bg,
            fg="white",
            font=("Segoe UI", 24, "bold")
        ).pack(pady=15)

    # ---------------------
    # Standard Calculator
    # ---------------------
    def show_calculator(self):

        self.clear_content()
        self.create_title("Calculator")

        self.calc_entry = tk.Entry(
            self.content,
            font=("Segoe UI", 24),
            justify="right"
        )
        self.calc_entry.pack(fill="x", padx=30, pady=10)

        frame = tk.Frame(self.content, bg=self.main_bg)
        frame.pack()

        buttons = [
            ['7','8','9','/'],
            ['4','5','6','*'],
            ['1','2','3','-'],
            ['0','.','=','+']
        ]

        for r,row in enumerate(buttons):
            for c,val in enumerate(row):

                cmd = lambda x=val: self.calc_click(x)

                tk.Button(
                    frame,
                    text=val,
                    command=cmd,
                    width=8,
                    height=3,
                    font=("Segoe UI",16),
                    bg="#1f2f6d" if val not in "+-*/=" else "#ff9800",
                    fg="white"
                ).grid(row=r,column=c,padx=5,pady=5)

        tk.Button(
            self.content,
            text="AC",
            command=lambda:self.calc_entry.delete(0,"end"),
            bg="#2196f3",
            fg="white",
            font=("Segoe UI",14)
        ).pack(pady=10)

    def calc_click(self,value):

        if value == "=":
            try:
                result = eval(self.calc_entry.get())
                self.calc_entry.delete(0,"end")
                self.calc_entry.insert("end",str(result))
            except:
                messagebox.showerror("Error","Invalid Expression")
            return

        self.calc_entry.insert("end",value)

    # ---------------------
    # Scientific
    # ---------------------
    def show_scientific(self):

        self.clear_content()
        self.create_title("Scientific Calculator")

        self.sci_entry = tk.Entry(
            self.content,
            font=("Segoe UI",22),
            justify="right"
        )
        self.sci_entry.pack(fill="x", padx=20, pady=10)

        frame = tk.Frame(self.content,bg=self.main_bg)
        frame.pack()

        funcs = [
            ("sin",self.sin_func),
            ("cos",self.cos_func),
            ("tan",self.tan_func),
            ("log",self.log_func),
            ("√",self.sqrt_func),
            ("π",lambda:self.insert_sci(math.pi)),
            ("e",lambda:self.insert_sci(math.e))
        ]

        for i,(txt,cmd) in enumerate(funcs):
            tk.Button(
                frame,
                text=txt,
                command=cmd,
                width=10,
                height=2
            ).grid(row=i//4,column=i%4,padx=5,pady=5)

    def insert_sci(self,val):
        self.sci_entry.insert("end",str(val))

    def get_sci(self):
        return float(self.sci_entry.get())

    def sin_func(self):
        self.sci_result(math.sin(math.radians(self.get_sci())))

    def cos_func(self):
        self.sci_result(math.cos(math.radians(self.get_sci())))

    def tan_func(self):
        self.sci_result(math.tan(math.radians(self.get_sci())))

    def log_func(self):
        self.sci_result(math.log10(self.get_sci()))

    def sqrt_func(self):
        self.sci_result(math.sqrt(self.get_sci()))

    def sci_result(self,val):
        self.sci_entry.delete(0,"end")
        self.sci_entry.insert(0,str(val))

    # ---------------------
    # Converter
    # ---------------------
    def show_converter(self):

        self.clear_content()
        self.create_title("Unit Converter")

        tk.Label(
            self.content,
            text="Meters",
            bg=self.main_bg,
            fg="white"
        ).pack()

        self.meter_entry = tk.Entry(self.content)
        self.meter_entry.pack(pady=10)

        tk.Button(
            self.content,
            text="Convert To CM",
            command=self.convert_cm
        ).pack()

        self.conv_label = tk.Label(
            self.content,
            text="0",
            bg=self.main_bg,
            fg="white",
            font=("Segoe UI",18)
        )
        self.conv_label.pack(pady=20)

    def convert_cm(self):
        try:
            m = float(self.meter_entry.get())
            self.conv_label.config(text=f"{m*100} cm")
        except:
            pass

    # ---------------------
    # Statistics
    # ---------------------
    def show_statistics(self):

        self.clear_content()
        self.create_title("Statistics")

        tk.Label(
            self.content,
            text="Enter numbers separated by comma",
            bg=self.main_bg,
            fg="white"
        ).pack()

        self.stats_entry = tk.Entry(self.content,width=50)
        self.stats_entry.pack(pady=10)

        tk.Button(
            self.content,
            text="Calculate Mean",
            command=self.calc_mean
        ).pack()

        self.stats_label = tk.Label(
            self.content,
            text="",
            bg=self.main_bg,
            fg="white",
            font=("Segoe UI",18)
        )
        self.stats_label.pack(pady=20)

    def calc_mean(self):
        nums = list(map(float,self.stats_entry.get().split(",")))
        mean = sum(nums)/len(nums)
        self.stats_label.config(text=f"Mean = {mean}")

    # ---------------------
    # Programmer
    # ---------------------
    def show_programmer(self):

        self.clear_content()
        self.create_title("Programmer Calculator")

        self.prog_entry = tk.Entry(self.content)
        self.prog_entry.pack(pady=10)

        tk.Button(
            self.content,
            text="Decimal → Binary",
            command=self.dec_to_bin
        ).pack()

        self.prog_label = tk.Label(
            self.content,
            text="",
            bg=self.main_bg,
            fg="white",
            font=("Segoe UI",18)
        )
        self.prog_label.pack(pady=20)

    def dec_to_bin(self):
        n = int(self.prog_entry.get())
        self.prog_label.config(text=bin(n))

    # ---------------------
    # Finance
    # ---------------------
    def show_finance(self):

        self.clear_content()
        self.create_title("Finance Calculator")

        tk.Label(
            self.content,
            text="Principal",
            bg=self.main_bg,
            fg="white"
        ).pack()

        self.p = tk.Entry(self.content)
        self.p.pack()

        tk.Label(
            self.content,
            text="Rate %",
            bg=self.main_bg,
            fg="white"
        ).pack()

        self.r = tk.Entry(self.content)
        self.r.pack()

        tk.Label(
            self.content,
            text="Time",
            bg=self.main_bg,
            fg="white"
        ).pack()

        self.t = tk.Entry(self.content)
        self.t.pack()

        tk.Button(
            self.content,
            text="Simple Interest",
            command=self.simple_interest
        ).pack(pady=10)

        self.finance_label = tk.Label(
            self.content,
            text="",
            bg=self.main_bg,
            fg="white",
            font=("Segoe UI",18)
        )
        self.finance_label.pack()

    def simple_interest(self):
        p=float(self.p.get())
        r=float(self.r.get())
        t=float(self.t.get())

        si=(p*r*t)/100

        self.finance_label.config(
            text=f"Interest = {si}"
        )

    # ---------------------
    # Equation Solver
    # ---------------------
    def show_equation_solver(self):

        self.clear_content()
        self.create_title("Equation Solver")

        tk.Label(
            self.content,
            text="ax + b = 0",
            bg=self.main_bg,
            fg="white"
        ).pack()

        self.a = tk.Entry(self.content)
        self.a.pack()

        self.b = tk.Entry(self.content)
        self.b.pack()

        tk.Button(
            self.content,
            text="Solve",
            command=self.solve_eq
        ).pack(pady=10)

        self.eq_label = tk.Label(
            self.content,
            text="",
            bg=self.main_bg,
            fg="white",
            font=("Segoe UI",18)
        )
        self.eq_label.pack()

    def solve_eq(self):
        a=float(self.a.get())
        b=float(self.b.get())

        x=-b/a

        self.eq_label.config(text=f"x = {x}")

    # ---------------------
    # Theme
    # ---------------------
    def toggle_theme(self):

        if self.dark_var.get():

            self.main_bg="#2b2b2b"
            self.sidebar_bg="#252525"

        else:

            self.main_bg="#f2f2f2"
            self.sidebar_bg="#dddddd"

        self.root.configure(bg=self.main_bg)
        self.sidebar.configure(bg=self.sidebar_bg)
        self.content.configure(bg=self.main_bg)


# =========================
# RUN
# =========================

root = tk.Tk()
app = SmartCalcPro(root)
root.mainloop()