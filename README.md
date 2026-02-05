# Quizzler – Python Quiz Application (GUI)

Quizzler is a simple Python based quiz application built using **Tkinter** for the graphical user interface and the **Open Trivia Database (OpenTDB)** API for fetching quiz questions.

The application presents True/False questions, tracks the user’s score, and provides instant visual feedback.

---

## Features

- Graphical User Interface using Tkinter
- Fetches real time questions from OpenTDB API
- True/False type quiz
- Score tracking
- Instant feedback for correct and wrong answers
- Clean separation of logic and UI

---

## Project Structure

| File | Description                                                |
|-----|------------------------------------------------------------|
| `main.py` | Entry point of the application, fetches questions from API |
| `quiz_brain.py` | Handles quiz logic, questions, and scoring                 |
| `ui.py` | Manages the Tkinter based user interface                   |
| `images/` | Contains button images (`true.png`, `false.png`)           |

---

## Requirements

- Python 3.7+
- `requests` library
- Tkinter (comes pre-installed with most Python distributions)

---

## Installation & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/quizzler-python-gui.git
   cd quizzler-python-gui
   
2. **Install dependencies**
   ```bash
    pip install -r requirements.txt
   
3. **Run the application**
   ```bash
    python main.py
   
## API Used

- **Open Trivia Database**
  - URL: https://opentdb.com/
  - Used to fetch True/False quiz questions dynamically