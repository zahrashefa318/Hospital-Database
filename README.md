# Hospital‑Database

A standalone Python application for managing hospital data with a Tkinter-based GUI and object-oriented design. It uses `.txt` files for data storage and features auto-updating tables, custom scrollbar controls, and class-based widgets.

---

## Features

- **Object-Oriented Programming (OOP):** Utilizes classes to encapsulate functionality:
  - `TableCreator`: Builds and manages table-like views in Tkinter.
  - `ScrollbarCreator`: Generates scrollbars for navigating data-rich interfaces.
- **Persistent Storage:** Reads and writes patient data to `.txt` files for simple, lightweight persistence.
- **Auto-updating Interface:** Table views refresh automatically when users add new patient data.

---

## Technologies & Tools

- **Programming Language:** Python
- **GUI Toolkit:** Tkinter
- **Data Storage:** Plain text files (`.txt`)
- **Design Approach:** Object-Oriented Programming (OOP)

---

## Project Structure

- **`Hospital-Database/`**  
  *(Root directory of the project)*

- **`Hospital.py`**  
  *Entry point: initializes the GUI*

- **`TableMaker.py`**  
  *Contains `TableCreator` class*

- **`scrollMaker.py`**  
  *Contains `ScrollbarCreator` class*

- **`PatientClass.py`**  
  *Handles `.txt` storage: read/write operations*

- **`hospital-icons-design-in-blue-circle-png.png`**  
  *GUI asset*

- **`patients.txt`**  
  *Default data storage file*

- **`secondwindow.py`**  
  *Additional GUI window*

- **`README.md`**  
  *Project documentation*

---

## Installation & Setup

### Prerequisites

- Python 3.x
- No external libraries required (standard library only)

### Setup

```bash
git clone https://github.com/yourusername/Hospital-Database.git
cd Hospital-Database
python Hospital.py
