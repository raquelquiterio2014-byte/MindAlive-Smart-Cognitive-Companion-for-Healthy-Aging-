import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
import os
import sys
import random

try:
    import google.generativeai as genai
except ImportError:
    genai = None


# =========================================================
# APP CONFIGURATION
# =========================================================

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

APP_NAME = "MindAlive"
APP_VERSION = "1.0"

API_KEY = ""  # Add your Gemini API key here

if genai and API_KEY:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-2.5-flash")
else:
    model = None


# =========================================================
# COLORS
# =========================================================

DARK_BLUE = "#0B1F3A"
BLUE = "#3B82F6"
LIGHT_BLUE = "#DCEBFF"
PURPLE = "#A78BFA"
LIGHT_PURPLE = "#EDE9FE"
WHITE = "#FFFFFF"
TEXT = "#1E293B"
DANGER = "#C0392B"


# =========================================================
# ASSETS
# =========================================================

def asset_path(filename):
    if getattr(sys, "frozen", False):
        base_dir = sys._MEIPASS
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_dir, "assets", filename)


def load_image(filename, size):
    try:
        image = Image.open(asset_path(filename))
        return ctk.CTkImage(light_image=image, dark_image=image, size=size)
    except Exception:
        return None


# =========================================================
# MAIN APP
# =========================================================

class VivaMenteApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Mind Alive - Smart Cognitive System")
        self.geometry("920x680")
        self.resizable(False, False)
        self.configure(fg_color=WHITE)

        self.current_frame = None

        self.show_home()

    def clear_screen(self):
        if self.current_frame:
            self.current_frame.destroy()

    def create_header(self, parent, title, subtitle):
        ctk.CTkLabel(
            parent,
            text=title,
            font=("Arial", 30, "bold"),
            text_color=DARK_BLUE
        ).pack(pady=(15, 5))

        ctk.CTkLabel(
            parent,
            text=subtitle,
            font=("Arial", 16),
            text_color=TEXT
        ).pack(pady=(0, 10))

    def create_back_button(self, parent):
        ctk.CTkButton(
            parent,
            text="⬅ Back to Menu",
            width=180,
            height=40,
            fg_color=PURPLE,
            hover_color=DARK_BLUE,
            font=("Arial", 15, "bold"),
            command=self.show_home
        ).pack(pady=10)

    # =====================================================
    # HOME SCREEN
    # =====================================================

    def show_home(self):
        self.clear_screen()

        frame = ctk.CTkFrame(self, fg_color=WHITE)
        frame.pack(fill="both", expand=True)
        self.current_frame = frame

        self.create_header(
            frame,
            "💜 Mind Alive",
            "Smart Cognitive System for Older Adults - Version 1.0"
        )

        menu_frame = ctk.CTkFrame(
            frame,
            fg_color=LIGHT_PURPLE,
            corner_radius=25
        )
        menu_frame.pack(padx=40, pady=20, fill="both", expand=True)

        ctk.CTkLabel(
            menu_frame,
            text="Choose an activity:",
            font=("Arial", 24, "bold"),
            text_color=DARK_BLUE
        ).pack(pady=20)

        buttons = [
            ("🤖 Virtual Assistant", self.show_assistant),
            ("🧠 Memory Quiz", self.show_memory_quiz),
            ("🔢 Logic Sequence", self.show_logic_sequence),
            ("🧩 Cognitive Association", self.show_association),
            ("✏️ Hangman Game", self.show_hangman),
            ("🔎 Word Search", self.show_word_search),
        ]

        for text, command in buttons:
            ctk.CTkButton(
                menu_frame,
                text=text,
                width=340,
                height=50,
                font=("Arial", 18, "bold"),
                fg_color=BLUE,
                hover_color=DARK_BLUE,
                command=command
            ).pack(pady=8)

        ctk.CTkButton(
            menu_frame,
            text="❌ Exit System",
            width=340,
            height=50,
            font=("Arial", 18, "bold"),
            fg_color=DANGER,
            hover_color="#922B21",
            command=self.destroy
        ).pack(pady=(20, 10))

        ctk.CTkLabel(
            frame,
            text="Technology for active, healthy and connected aging.",
            font=("Arial", 14),
            text_color=TEXT
        ).pack(pady=5)

    # =====================================================
    # VIRTUAL ASSISTANT
    # =====================================================

    def show_assistant(self):
        self.clear_screen()

        frame = ctk.CTkFrame(self, fg_color=WHITE)
        frame.pack(fill="both", expand=True)
        self.current_frame = frame

        self.assistant_name = "Ana"
        self.personality = """
        You are Ana, a kind, gentle, friendly virtual assistant
        designed to support older adults.
        """

        self.create_header(
            frame,
            "🤖 Virtual Assistant",
            "Talk with Ana or Sandro in a simple and welcoming way."
        )

        self.assistant_label = ctk.CTkLabel(
            frame,
            text="Talking with Ana 💜",
            font=("Arial", 18, "bold"),
            text_color=DARK_BLUE
        )
        self.assistant_label.pack(pady=5)

        avatar_frame = ctk.CTkFrame(frame, fg_color=LIGHT_BLUE, corner_radius=20)
        avatar_frame.pack(pady=8)

        ana_img = load_image("ana.png", (140, 140))
        sandro_img = load_image("sandro.png", (140, 140))

        ctk.CTkLabel(avatar_frame, image=ana_img, text="").grid(row=0, column=0, padx=25, pady=10)
        ctk.CTkLabel(avatar_frame, image=sandro_img, text="").grid(row=0, column=1, padx=25, pady=10)

        ctk.CTkButton(
            avatar_frame,
            text="Ana 💜",
            width=150,
            height=40,
            fg_color=PURPLE,
            hover_color=DARK_BLUE,
            font=("Arial", 16, "bold"),
            command=self.choose_ana
        ).grid(row=1, column=0, pady=10)

        ctk.CTkButton(
            avatar_frame,
            text="Sandro 💙",
            width=150,
            height=40,
            fg_color=BLUE,
            hover_color=DARK_BLUE,
            font=("Arial", 16, "bold"),
            command=self.choose_sandro
        ).grid(row=1, column=1, pady=10)

        self.chat = ctk.CTkTextbox(
            frame,
            width=760,
            height=180,
            font=("Arial", 16),
            corner_radius=20
        )
        self.chat.pack(pady=10)
        self.chat.insert("end", "🤖 Ana:\nHello! How can I help you today?\n")

        input_frame = ctk.CTkFrame(frame, fg_color=LIGHT_PURPLE, corner_radius=20)
        input_frame.pack(pady=8)

        self.user_input = ctk.CTkEntry(
            input_frame,
            width=520,
            height=45,
            font=("Arial", 17),
            placeholder_text="Type your message..."
        )
        self.user_input.grid(row=0, column=0, padx=10, pady=10)

        ctk.CTkButton(
            input_frame,
            text="Send",
            width=130,
            height=45,
            font=("Arial", 17, "bold"),
            fg_color=BLUE,
            hover_color=DARK_BLUE,
            command=self.send_message
        ).grid(row=0, column=1, padx=10)

        self.create_back_button(frame)

    def choose_ana(self):
        self.assistant_name = "Ana"
        self.personality = """
        You are Ana, a kind, gentle, friendly virtual assistant
        designed to support older adults.
        """
        self.assistant_label.configure(text="Talking with Ana 💜")

    def choose_sandro(self):
        self.assistant_name = "Sandro"
        self.personality = """
        You are Sandro, a positive, friendly, fun virtual assistant
        designed to support older adults.
        """
        self.assistant_label.configure(text="Talking with Sandro 💙")

    def send_message(self):
        message = self.user_input.get().strip()

        if not message:
            return

        self.chat.insert("end", f"\n🧑 You:\n{message}\n")
        self.user_input.delete(0, "end")

        if not model:
            answer = (
                "Gemini API is not configured yet. "
                "Please add your API key in the API_KEY variable."
            )
        else:
            try:
                prompt = f"""
                {self.personality}

                Answer in a simple, warm and friendly way for older adults.

                User said:
                {message}
                """
                response = model.generate_content(prompt)
                answer = response.text
            except Exception as error:
                answer = f"AI connection error: {error}"

        self.chat.insert("end", f"\n🤖 {self.assistant_name}:\n{answer}\n")
        self.chat.see("end")

    # =====================================================
    # MEMORY QUIZ
    # =====================================================

    def show_memory_quiz(self):
        self.clear_screen()

        self.quiz_questions = [
            ("What color is the sky on a clear day?", "Blue"),
            ("How many days are there in a week?", "7"),
            ("Which animal barks?", "Dog"),
            ("What do we use to read time?", "Clock"),
            ("What season comes after summer?", "Autumn"),
        ]

        self.quiz_index = 0
        self.quiz_score = 0

        frame = ctk.CTkFrame(self, fg_color=WHITE)
        frame.pack(fill="both", expand=True)
        self.current_frame = frame

        self.create_header(frame, "🧠 Memory Quiz", "Answer simple questions and train your memory.")

        self.quiz_label = ctk.CTkLabel(
            frame,
            text="",
            font=("Arial", 22, "bold"),
            text_color=DARK_BLUE,
            wraplength=700
        )
        self.quiz_label.pack(pady=30)

        self.quiz_entry = ctk.CTkEntry(
            frame,
            width=400,
            height=45,
            font=("Arial", 18),
            placeholder_text="Type your answer..."
        )
        self.quiz_entry.pack(pady=10)

        ctk.CTkButton(
            frame,
            text="Check Answer",
            width=220,
            height=45,
            fg_color=BLUE,
            hover_color=DARK_BLUE,
            font=("Arial", 17, "bold"),
            command=self.check_quiz_answer
        ).pack(pady=10)

        self.quiz_feedback = ctk.CTkLabel(
            frame,
            text="",
            font=("Arial", 17),
            text_color=TEXT
        )
        self.quiz_feedback.pack(pady=10)

        self.create_back_button(frame)

        self.load_quiz_question()

    def load_quiz_question(self):
        question, _ = self.quiz_questions[self.quiz_index]
        self.quiz_label.configure(text=f"Question {self.quiz_index + 1}: {question}")
        self.quiz_entry.delete(0, "end")
        self.quiz_feedback.configure(text="")

    def check_quiz_answer(self):
        _, correct = self.quiz_questions[self.quiz_index]
        answer = self.quiz_entry.get().strip()

        if answer.lower() == correct.lower():
            self.quiz_score += 1
            self.quiz_feedback.configure(text="✅ Correct!")
        else:
            self.quiz_feedback.configure(text=f"❌ Correct answer: {correct}")

        self.quiz_index += 1

        if self.quiz_index < len(self.quiz_questions):
            self.after(1200, self.load_quiz_question)
        else:
            messagebox.showinfo(
                "Quiz Finished",
                f"Your score: {self.quiz_score}/{len(self.quiz_questions)}"
            )
            self.show_home()

    # =====================================================
    # LOGIC SEQUENCE
    # =====================================================

    def show_logic_sequence(self):
        self.clear_screen()

        self.sequence_data = [
            ("2, 4, 6, 8, ?", "10"),
            ("1, 3, 5, 7, ?", "9"),
            ("5, 10, 15, 20, ?", "25"),
            ("10, 20, 30, 40, ?", "50"),
        ]

        self.sequence_index = 0
        self.sequence_score = 0

        frame = ctk.CTkFrame(self, fg_color=WHITE)
        frame.pack(fill="both", expand=True)
        self.current_frame = frame

        self.create_header(frame, "🔢 Logic Sequence", "Complete the number sequence.")

        self.sequence_label = ctk.CTkLabel(
            frame,
            text="",
            font=("Arial", 26, "bold"),
            text_color=DARK_BLUE
        )
        self.sequence_label.pack(pady=40)

        self.sequence_entry = ctk.CTkEntry(
            frame,
            width=300,
            height=45,
            font=("Arial", 18),
            placeholder_text="Next number..."
        )
        self.sequence_entry.pack(pady=10)

        ctk.CTkButton(
            frame,
            text="Check",
            width=200,
            height=45,
            fg_color=BLUE,
            hover_color=DARK_BLUE,
            font=("Arial", 17, "bold"),
            command=self.check_sequence
        ).pack(pady=10)

        self.sequence_feedback = ctk.CTkLabel(frame, text="", font=("Arial", 17))
        self.sequence_feedback.pack(pady=10)

        self.create_back_button(frame)

        self.load_sequence()

    def load_sequence(self):
        sequence, _ = self.sequence_data[self.sequence_index]
        self.sequence_label.configure(text=sequence)
        self.sequence_entry.delete(0, "end")
        self.sequence_feedback.configure(text="")

    def check_sequence(self):
        _, correct = self.sequence_data[self.sequence_index]
        answer = self.sequence_entry.get().strip()

        if answer == correct:
            self.sequence_score += 1
            self.sequence_feedback.configure(text="✅ Correct!")
        else:
            self.sequence_feedback.configure(text=f"❌ Correct answer: {correct}")

        self.sequence_index += 1

        if self.sequence_index < len(self.sequence_data):
            self.after(1200, self.load_sequence)
        else:
            messagebox.showinfo(
                "Finished",
                f"Your score: {self.sequence_score}/{len(self.sequence_data)}"
            )
            self.show_home()

    # =====================================================
    # COGNITIVE ASSOCIATION
    # =====================================================

    def show_association(self):
        self.clear_screen()

        self.association_data = [
            ("Sun", "Day"),
            ("Moon", "Night"),
            ("Book", "Reading"),
            ("Medicine", "Health"),
            ("Music", "Sound"),
        ]

        self.association_index = 0
        self.association_score = 0

        frame = ctk.CTkFrame(self, fg_color=WHITE)
        frame.pack(fill="both", expand=True)
        self.current_frame = frame

        self.create_header(frame, "🧩 Cognitive Association", "Type the word that best matches the clue.")

        self.association_label = ctk.CTkLabel(
            frame,
            text="",
            font=("Arial", 26, "bold"),
            text_color=DARK_BLUE
        )
        self.association_label.pack(pady=40)

        self.association_entry = ctk.CTkEntry(
            frame,
            width=350,
            height=45,
            font=("Arial", 18),
            placeholder_text="Associated word..."
        )
        self.association_entry.pack(pady=10)

        ctk.CTkButton(
            frame,
            text="Check",
            width=200,
            height=45,
            fg_color=BLUE,
            hover_color=DARK_BLUE,
            font=("Arial", 17, "bold"),
            command=self.check_association
        ).pack(pady=10)

        self.association_feedback = ctk.CTkLabel(frame, text="", font=("Arial", 17))
        self.association_feedback.pack(pady=10)

        self.create_back_button(frame)

        self.load_association()

    def load_association(self):
        clue, _ = self.association_data[self.association_index]
        self.association_label.configure(text=f"Clue: {clue}")
        self.association_entry.delete(0, "end")
        self.association_feedback.configure(text="")

    def check_association(self):
        _, correct = self.association_data[self.association_index]
        answer = self.association_entry.get().strip()

        if answer.lower() == correct.lower():
            self.association_score += 1
            self.association_feedback.configure(text="✅ Correct!")
        else:
            self.association_feedback.configure(text=f"❌ Correct answer: {correct}")

        self.association_index += 1

        if self.association_index < len(self.association_data):
            self.after(1200, self.load_association)
        else:
            messagebox.showinfo(
                "Finished",
                f"Your score: {self.association_score}/{len(self.association_data)}"
            )
            self.show_home()

    # =====================================================
    # HANGMAN
    # =====================================================

    def show_hangman(self):
        self.clear_screen()

        self.hangman_words = ["MEMORY", "HEALTH", "FAMILY", "MUSIC", "GARDEN"]
        self.hangman_word = random.choice(self.hangman_words)
        self.hangman_letters = []
        self.hangman_attempts = 6

        frame = ctk.CTkFrame(self, fg_color=WHITE)
        frame.pack(fill="both", expand=True)
        self.current_frame = frame

        self.create_header(frame, "✏️ Hangman Game", "Guess the hidden word letter by letter.")

        self.hangman_word_label = ctk.CTkLabel(
            frame,
            text="",
            font=("Arial", 34, "bold"),
            text_color=DARK_BLUE
        )
        self.hangman_word_label.pack(pady=40)

        self.hangman_info = ctk.CTkLabel(
            frame,
            text="",
            font=("Arial", 18),
            text_color=TEXT
        )
        self.hangman_info.pack(pady=5)

        self.hangman_entry = ctk.CTkEntry(
            frame,
            width=180,
            height=45,
            font=("Arial", 20),
            placeholder_text="Letter"
        )
        self.hangman_entry.pack(pady=10)

        ctk.CTkButton(
            frame,
            text="Try Letter",
            width=200,
            height=45,
            fg_color=BLUE,
            hover_color=DARK_BLUE,
            font=("Arial", 17, "bold"),
            command=self.try_hangman_letter
        ).pack(pady=10)

        self.create_back_button(frame)

        self.update_hangman_display()

    def update_hangman_display(self):
        display = " ".join(
            letter if letter in self.hangman_letters else "_"
            for letter in self.hangman_word
        )

        self.hangman_word_label.configure(text=display)
        self.hangman_info.configure(
            text=f"Attempts left: {self.hangman_attempts} | Used letters: {', '.join(self.hangman_letters)}"
        )

    def try_hangman_letter(self):
        letter = self.hangman_entry.get().strip().upper()
        self.hangman_entry.delete(0, "end")

        if len(letter) != 1 or not letter.isalpha():
            messagebox.showwarning("Invalid", "Please type only one letter.")
            return

        if letter in self.hangman_letters:
            messagebox.showinfo("Repeated", "You already tried this letter.")
            return

        self.hangman_letters.append(letter)

        if letter not in self.hangman_word:
            self.hangman_attempts -= 1

        self.update_hangman_display()

        if all(letter in self.hangman_letters for letter in self.hangman_word):
            messagebox.showinfo("Congratulations!", f"You guessed the word: {self.hangman_word}")
            self.show_home()

        elif self.hangman_attempts == 0:
            messagebox.showinfo("Game Over", f"The word was: {self.hangman_word}")
            self.show_home()

    # =====================================================
    # WORD SEARCH
    # =====================================================

    def show_word_search(self):
        self.clear_screen()

        frame = ctk.CTkFrame(self, fg_color=WHITE)
        frame.pack(fill="both", expand=True)
        self.current_frame = frame

        self.create_header(frame, "🔎 Word Search", "Find the hidden words in the grid.")

        words = ["HEALTH", "MUSIC", "MEMORY", "CARE", "BRAIN", "FAMILY"]

        grid_text = """
H  E  A  L  T  H
M  U  S  I  C  A
M  E  M  O  R  Y
C  A  R  E  S  T
B  R  A  I  N  S
F  A  M  I  L  Y
"""

        ctk.CTkLabel(
            frame,
            text=grid_text,
            font=("Courier New", 28, "bold"),
            text_color=DARK_BLUE,
            justify="center"
        ).pack(pady=25)

        ctk.CTkLabel(
            frame,
            text="Words to find:",
            font=("Arial", 20, "bold"),
            text_color=TEXT
        ).pack(pady=5)

        ctk.CTkLabel(
            frame,
            text=", ".join(words),
            font=("Arial", 20),
            text_color=BLUE
        ).pack(pady=5)

        ctk.CTkLabel(
            frame,
            text="This activity trains attention, focus and visual recognition.",
            font=("Arial", 16),
            text_color=TEXT
        ).pack(pady=20)

        self.create_back_button(frame)


# =========================================================
# RUN APP
# =========================================================

if __name__ == "__main__":
    app = VivaMenteApp()
    app.mainloop()