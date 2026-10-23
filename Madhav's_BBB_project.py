import tkinter as tk
from tkinter import messagebox, ttk


class SurveyApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.root.geometry("580x560")
        self.root.configure(bg="#F7FAFC")  # Soft off-white background

        # Performance and index trackers
        self.current_question_index = 0
        self.active_quiz_questions = []
        self.score = 0
        self.selected_level = tk.StringVar(master=self.root, value="S1")
        self.selected_subject = tk.StringVar(master=self.root, value="Maths")
        self.selected_answer = tk.StringVar(master=self.root, value="")

        self.question_bank = {
               "S1": {
                   "Maths": [
                       {
                           "question": "What is 8 squared?",
                           "options": ["16", "32", "64", "72"],
                           "answer": "64",
                           "hint": "What does squared mean?",
                       },
                       {
                           "question": "What is x, if x+14=29?",
                           "options": ["15", "13", "43", "14"],
                           "answer": "15",
                           "hint": "How can we isolate x from the equation?",
                       },
       {
                           "question": "What is 10 times 12",
                           "options": ["1200", "240", "60", "120"],
                           "answer": "120",
                           "hint": "Use the multiplication strategy",
                       },
       {
                           "question": "What is the value of x if  is an angle in an equilateral triangle",
                           "options": ["180", "100", "120", "60"],
                           "answer": "60",
                           "hint": "the sum of angles in a triangle adds up to 180 degrees",
                       },
       {
                           "question": "1728/h is  a perfect cube. Find the lowest possible value for h",
                           "options": ["1728", "7", "2", "1"],
                           "answer": "1",
                           "hint": "Use prime factorisation",
                       },
                   ],
                   "Biology": [
                       {
                       "question": "Which organelle is known as the powerhouse of the cell?",
                       "options": ["Nucleus", "Mitochondria", "Ribosome", "Cell Wall"],
                       "answer": "Mitochondria",
                       "hint": "It produces cellular energy (ATP).",
                       },
                       {
                       "question": "What is it that all plant cells have that animal cells do not?",
                       "options": ["Nucleus", "Mitochondria", "Ribosome", "Cell Wall"],
                       "answer": "Cell Wall",
                       "hint": "It provides structural support.",
                       },
                       {
                         "question": "What does a red blood cell not have tht other cells do?",
                        "options": ["Nucleus", "Mitochondria", "Ribosome", "Cell Wall"],
                        "answer": "Nucleus",
                         "hint": "It is something that is crucial in other cells).",
                       },
                       {
                       "question": "What is the primary function of red blood cells?",
                       "options": ["Fight infections", "Clot blood", "Transport oxygen", "Store fat"],
                       "answer": "Transport oxygen",
                       "hint": "They contain hemoglobin.",
                       },
                       {
                       "question": "What does the vacuole do?",
                       "options": ["Fight infections", "Contain energy", "Contain oxygen", "Isolate cell waste"],
                       "answer": "Isolate cell waste",
                       "hint": "It acts as a storage compartment.",
                       },
                     ],
       
                   "Chemistry": [
                       {
                       "question": "Which of the following is a physical change?",
                       "options": ["Burning wood","Melting ice","Rusting iron","Cooking an egg"], 
                       "answer": "Melting ice",
                       "hint": "A chemical change cannot be reversed.",
                       },
                       {
                       "question": "Which of the following is a non-metal element?",
                       "options": ["Sodium","Oxygen","Fluorine","Carbon"], 
                       "answer": "Sodium",
                       "hint": "Non-metals are typically situated to the right of the periodic table.",
                       },
                       {
                       "question": "which element has 39 protons",
                       "options": ["Yttrium","Oxygen","Vanadium","Chromium"], 
                       "answer": "Yttrium",
                       "hint": "Check the periodic table for the element with atomic number 39.",
                       },
                       {
                       "question": "Which element has the symbol Pb ",
                       "options": ["Potassium","Lead","Arsenic","Plutonium"], 
                       "answer": "Lead",
                       "hint": "Check the periodic table for the element with the symbol Pb.",
                       },
                       {
                       "question": "What is the chemical formula for salt?",
                       "options": ["NaCl", "H2SO4", "H2O", "MgCl2"],
                       "answer": "NaCl",
                       "hint": "It's a combination of sodium and chlorine.",
                       },
                   ],
                   "Physics": [
                       {
                       "question": "What is the speed of light",
                       "options": ["300,000 km/s","300,000 m/s","300,000,000 km/s","300km/s"],
                       "answer": "300,000 km/s",
                       "hint": "Light is really,really fast",
                       },
                       {
                       "question": "What is the SI unit of force?",
                       "options": ["Newton", "Joule", "Watt", "Pascal"],
                       "answer": "Newton",
                       "hint": "It's named after the dude who discovered gravity .",
                       },
                       {
                       "question": "Which type of mirror is curved outward?",
                       "options": ["Convex", "Concave", "Plane", "Parabolic"],
                       "answer": "Convex",
                       "hint": "It diverges light rays.",
                       },
                       {
                       "question": "What is the SI unit of electric current?",
                       "options": ["Ampere", "Volt", "Ohm", "Watt"],
                       "answer": "Ampere",
                       "hint": "It's named after the French physicist André-Marie ___.",
                       },
                       {
                       "question": "What is the SI unit of mass?",
                       "options": ["Kilogram", "Gram", "Pound", "Ounce"],
                       "answer": "Kilogram",
                       "hint": "It's the base unit of mass in the metric systemd.",
                       },
           
                      
                   ],
               
                },
               "S2": {
                   "Maths": [
                     {
                       "question": "Simplify the expression: 3x + 5x - 2x",
                       "options": ["6x", "8x", "10x", "4x"],
                       "answer": "6x",
                       "hint": "Combine the coefficients directly.",
                   },
                    {
                     "question": "Solve the linear equation: 4(x-2)-2(3x+1)=10",
                     "options": ["10", "8", "-10", "-8"],
                     "answer": "-10",
                     "hint": "Expand and simplify the equation.",
                    },
                    {
                     "question": "Find x from these 2 simultaneous equations:2x+y=7 and x-y=2",
                     "options": ["5", "2", "10", "3"],
                     "answer": "3",
                     "hint": "Use the equations wisely.",
                    },
                    {
                     "question": "Find x from these 2 simultaneous equations:2x+y=7 and x-y=2",
                     "options": ["5", "2", "10", "3"],
                     "answer": "3",
                     "hint": "Use the equations wisely.",
                    }, 
                    {
                     "question": "A right angled triangle has a base of 6 cm and a height of 8 cm. Find the length of the hypotenuse.",
                     "options": ["10", "8", "5", "3"],
                     "answer": "10",
                     "hint": "Use the Pythagorean theorem.",
                    }, 
                    
                   ],
                   "Biology": [
                     {
                       "question": "What is the primary function of red blood cells?",
                       "options": ["Fight infections","Clot blood","Transport oxygen","Store fat"],
                       "answer": "Transport oxygen",
                       "hint": "They contain hemoglobin.",
                   },
                   {
                     "question": "What is the primary function of white blood cells?",
                     "options": ["Fight infections","Clot blood","Transport oxygen","Store fat"],
                     "answer": "Fight infections",
                     "hint": "They are part of the immune system.",
                   },
                   {
                     "question": "What is the chemical reagent used to test for the presence of starch?",
                     "options": ["Iodine solution","Benedict's solution","Biuret reagent","Litmus paper"],
                     "answer": "Iodine solution",
                     "hint": "It turns blue-black in the presence of starch.",
                   },
                   {
                     "question": "Which element is found in proteins but not carbohydrates?",
                     "options": ["Oxygen","Carbon","Nitrogen","Hydrogen"],
                     "answer": "Nitrogen",
                     "hint": "It's a key component of amino acids.",
                   },
                   {
                     "question": "Which part of the human digestive system absorbs the most nutrients?",
                     "options": ["Stomach","Small intestine","Large intestine","Liver"],
                     "answer": "Small intestine",
                     "hint": "It has a large surface area for absorption.",
                   },
                   ],
                   "Chemistry": [
                     {
                       "question": "What is the chemical symbol for Gold?",
                       "options": ["Gd", "Go", "Ag", "Au"],
                       "answer": "Au",
                       "hint": "It comes from the Latin word 'Aurum'.",
                       },
                       {
                         "question": "What is the chemical symbol for Sodium?",
                         "options": ["Na", "So", "Sm", "S"],
                         "answer": "Na",
                         "hint": "It's a soft, silvery-white, highly reactive metal.",
                         },
                         {
                           "question": "A solution with a ph level of 2 is classified as:",
                           "options": ["Strong Acid", "Strong Alkali", "Weak acid", "Neutral"],
                           "answer": "Strong Acid",
                           "hint": "It has a low pH value.",
                           },
                           {
                             "question": "In the periodic table, horizontal rows are called:",
                             "options": ["Groups", "Periods", "Blocks", "Families"],
                             "answer": "Periods",
                             "hint": "These are the rows that go from up to down.",
                             },
                             {
                               "question": "What is the pH value of a neutral solution at room temperature?",
                               "options": ["7", "0", "14", "5"],
                               "answer": "7",
                               "hint": "It's the midpoint on the pH scale.",
                               },
                   ],
                   "Physics":[
                    {
                     "question":"What is the gravitational acceleration on earth",
                     "options": ["9.8 m per s", "98 m per s", "200 m per s", "225 m per s"],
                     "answer":"9.8 m per s",  
                     "hint":"It's not that high",
                   },
                   {
                     "question":"Which of the following is a contact force?",
                     "options": ["Gravity", "Magnetism", "Friction", "Electromagnetic force"],
                     "answer":"Friction",
                     "hint":"It occurs when two surfaces are in contact.",
                   },
                   {
                     "question":"A block of wood weighs 20N and has a base area of 2 m². What is the pressure it exerts?",
                     "options": ["10 Pa", "20 Pa", "40 Pa", "80 Pa"],
                     "answer":"10 Pa",
                     "hint":"Pressure = Force / Area.",
                   },
                   {
                     "question":"What is the SI unit of electric current?",
                     "options": ["Ampere", "Volt", "Ohm", "Watt"],
                     "answer":"Ampere",
                     "hint":"It's named after the French physicist André-Marie ___.",
                   },
                   {
                     "question":"What is the SI unit of mass?",
                     "options": ["Kilogram", "Gram", "Pound", "Ounce"],
                     "answer":"Kilogram",
                     "hint":"It's the base unit of mass in the metric system.",
                   },
                   ], 
               }
           }
        self.setup_styles()
        self.show_welcome_screen()

    def setup_styles(self):
        """Configures modern TTK styles and widget themes."""
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure(".", background="#F7FAFC", foreground="#2D3748")

        # Card container style
        self.style.configure("Card.TFrame", background="#FFFFFF", relief="flat")

        self.style.configure(
            "Header.TLabel",
            background="#FFFFFF",
            foreground="#2A4365",
            font=("Segoe UI", 18, "bold"),
        )
        self.style.configure(
            "Question.TLabel",
            background="#FFFFFF",
            foreground="#1A202C",
            font=("Segoe UI", 13, "bold"),
            wraplength=480,
        )
        self.style.configure(
            "Standard.TLabel",
            background="#FFFFFF",
            foreground="#4A5568",
            font=("Segoe UI", 11),
        )
        self.style.configure(
            "Progress.TLabel",
            background="#F7FAFC",
            foreground="#718096",
            font=("Segoe UI", 10, "italic"),
        )

        self.style.configure(
            "TCombobox",
            arrowsize=12,
            font=("Segoe UI", 11),
            background="#FFFFFF",
        )

        self.style.configure(
            "TRadiobutton",
            background="#FFFFFF",
            foreground="#2D3748",
            font=("Segoe UI", 11),
            padding=6,
        )

        self.style.configure(
            "Primary.TButton",
            background="#2A4365",
            foreground="#FFFFFF",
            font=("Segoe UI", 11, "bold"),
            padding=8,
            borderwidth=0,
        )
        self.style.map(
            "Primary.TButton", background=[("active", "#1A365D"), ("pressed", "#2A4365")]
        )

        self.style.configure(
            "Secondary.TButton",
            background="#E2E8F0",
            foreground="#4A5568",
            font=("Segoe UI", 10),
            padding=6,
            borderwidth=0,
        )
        self.style.map(
            "Secondary.TButton", background=[("active", "#CBD5E0"), ("pressed", "#E2E8F0")]
        )

    def clear_screen(self):
        """Helper to remove all widgets from the root window."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_welcome_screen(self):
        """Renders the attractive selection/setup dashboard screen."""
        self.clear_screen()

        card = ttk.Frame(self.root, style="Card.TFrame", padding=30)
        card.place(relx=0.5, rely=0.5, anchor="center", width=480, height=420)

        shadow = tk.Frame(self.root, bg="#E2E8F0", height=2)
        shadow.place(relx=0.5, rely=0.5, y=210, anchor="center", width=480)

        title = ttk.Label(
            card, text="Quiz Settings", style="Header.TLabel", anchor="center"
        )
        title.pack(pady=(0, 25))

        ttk.Label(card, text="Select Academic Level:", style="Standard.TLabel").pack(
            anchor="w", pady=(10, 5)
        )
        level_combo = ttk.Combobox(
            card,
            textvariable=self.selected_level,
            values=list(self.question_bank.keys()),
            state="readonly",
        )
        level_combo.pack(fill="x", pady=(0, 15))

        ttk.Label(card, text="Select Subject:", style="Standard.TLabel").pack(
            anchor="w", pady=(10, 5)
        )
        subject_combo = ttk.Combobox(
            card,
            textvariable=self.selected_subject,
            values=["Maths", "Biology", "Chemistry", "Physics"],
            state="readonly",
        )
        subject_combo.pack(fill="x", pady=(0, 30))

        start_btn = ttk.Button(
            card, text="Start Quiz", style="Primary.TButton", command=self.start_quiz
        )
        start_btn.pack(fill="x", ipady=4)

    def start_quiz(self):
        """Loads questions based on selection and initiates the interface."""
        level = self.selected_level.get()
        subject = self.selected_subject.get()

        if (
            level in self.question_bank
            and subject in self.question_bank[level]
        ):
            self.active_quiz_questions = self.question_bank[level][subject]
            self.current_question_index = 0
            self.score = 0
            self.display_question()
        else:
            messagebox.showerror(
                "Error", "No questions found for the selected configuration."
            )

    def display_question(self):
        """Renders the current active quiz question inside a beautiful UI card."""
        self.clear_screen()
        self.selected_answer.set("") 

        q_data = self.active_quiz_questions[self.current_question_index]

        progress_text = f"Question {self.current_question_index + 1} of {len(self.active_quiz_questions)}"
        progress_lbl = ttk.Label(
            self.root, text=progress_text, style="Progress.TLabel"
        )
        progress_lbl.pack(pady=(20, 5))

        card = ttk.Frame(self.root, style="Card.TFrame", padding=25)
        card.pack(fill="both", expand=True, padx=30, pady=(5, 30))

        q_label = ttk.Label(
            card, text=q_data["question"], style="Question.TLabel", justify="left"
        )
        q_label.pack(anchor="w", pady=(10, 20))

        options_frame = ttk.Frame(card, style="Card.TFrame")
        options_frame.pack(fill="x", pady=10)

        for option in q_data["options"]:
            r_btn = ttk.Radiobutton(
                options_frame,
                text=option,
                value=option,
                variable=self.selected_answer,
                style="TRadiobutton",
            )
            r_btn.pack(anchor="w", pady=6, fill="x")

        # Bottom Utilities Bar inside the card
        actions_frame = ttk.Frame(card, style="Card.TFrame")
        actions_frame.pack(fill="x", side="bottom", pady=(20, 0))

        hint_btn = ttk.Button(
            actions_frame,
            text="💡 View Hint",
            style="Secondary.TButton",
            command=lambda: messagebox.showinfo("Hint", q_data["hint"]),
        )
        hint_btn.pack(side="left")

        next_btn = ttk.Button(
            actions_frame,
            text="Submit & Next ➔",
            style="Primary.TButton",
            command=self.handle_next,
        )
        next_btn.pack(side="right", ipady=2)

    def handle_next(self):
        """Validates responses, scores user, and guides page state progression."""
        chosen = self.selected_answer.get()
        if not chosen:
            messagebox.showwarning(
                "Selection Required", "Please choose an answer before moving on!"
            )
            return

        correct_ans = self.active_quiz_questions[self.current_question_index][
            "answer"
        ]
        if chosen == correct_ans:
            self.score += 1

        self.current_question_index += 1
        if self.current_question_index < len(self.active_quiz_questions):
            self.display_question()
        else:
            self.show_results_screen()

    def show_results_screen(self):
        """Displays user score neatly with functional navigation loops."""
        self.clear_screen()
        card = ttk.Frame(self.root, style="Card.TFrame", padding=35)
        card.place(relx=0.5, rely=0.5, anchor="center", width=460, height=360)
        title = ttk.Label(
            card, text="Quiz Completed!", style="Header.TLabel", anchor="center"
        )
        title.pack(pady=(10, 20))

        total_qs = len(self.active_quiz_questions)
        score_percentage = int((self.score / total_qs) * 100)
        score_text = f"Your Score: {self.score} / {total_qs}"
        score_lbl = ttk.Label(
            card,
            text=score_text,
            font=("Segoe UI", 16, "bold"),
            background="#FFFFFF",
            foreground="#2B6CB0",
        )
        score_lbl.pack(pady=10)
        perc_lbl = ttk.Label(
            card,
            text=f"{score_percentage}% Correct",
            font=("Segoe UI", 12),
            background="#FFFFFF",
            foreground="#4A5568",
        )
        perc_lbl.pack(pady=(0, 30))

        # Restart app navigation trigger
        restart_btn = ttk.Button(
            card,
            text="Return to Main Menu",
            style="Primary.TButton",
            command=self.show_welcome_screen,
        )
        restart_btn.pack(fill="x", ipady=4)


if __name__ == "__main__":
    root = tk.Tk()
    app = SurveyApp(root)
    root.mainloop()
