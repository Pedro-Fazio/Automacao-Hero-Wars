# 🤖 Hero Wars: Dominion Era - Automation Engine

A high-performance automation bot developed in Python for the game *Hero Wars* (Desktop/Web). 

Unlike traditional macro scripts (which rely on blind, static wait times), this project utilizes an **Asynchronous Greedy Scheduling Architecture** and **Dynamic Pixel Verification** to maximize efficiency, reducing machine idle time to zero.

## 🚀 Key Features & Architecture

* **⚡ Smart Cooldown Interleaving (Asynchronous):** The bot doesn't sit idle. During the mandatory 47-second cooldown between Arena fights, the engine enters a dynamic scheduling mode, executing smaller tasks (Astral Seer, Gifts, Tower, etc.) and surgically returning to the Arena at the exact moment combat is unlocked.
* **👁️ Dynamic Visual Verification (Pixel Matching):** Replaces rigid `time.sleep()` calls with real-time "Watchdog" screen monitoring functions. The bot detects UI transitions (e.g., "Attack" or "Collect" buttons turning green) to proceed milliseconds after the game allows, drastically slashing the total runtime of long routines like the Dungeon.
* **🧩 Intelligent Task Partitioning (State Management):** Lengthy tasks are logically partitioned by the main engine. The bot can enter the Dungeon, execute Auto mode, exit to the City to complete a pending Arena fight, and autonomously return to the Dungeon's Manual mode without losing the application state.
* **🖥️ Rich Command-Line Interface (CLI):** A terminal UI built with the `rich` library, providing real-time feedback, information panels, formatted timers, and professional progress bars for routine monitoring.
* **📍 Built-in Coordinate Manager:** A native tool that uses global mouse hooks (`pynput`) to map screen coordinates (X, Y) and calibrate timings. It automatically saves configurations to text files without requiring external mapping software.

## 🛠️ Tech Stack & Tools

* **Python 3.10+**
* **PyAutoGUI:** GUI automation (Mouse/Keyboard control) and Screen Capturing.
* **Pynput:** Global listening of physical mouse events for coordinate mapping.
* **Rich:** Advanced terminal component rendering.
* **Threading:** Management of timeouts, safe interrupt inputs, and asynchronous UI panels.

## 📁 Project Structure

```text
📦 Automacao-Hero-Wars
 ┣ 📂 Componentes_Hero_Wars/      # Isolated task modules (Component Architecture)
 ┃ ┣ 📂 Arena
 ┃ ┣ 📂 Masmorra
 ┃ ┣ 📂 Torre
 ┃ ┗ ...
 ┣ 📂 Configuracoes/
 ┃ ┣ 📂 Coordenadas/              # .txt files containing user-generated (X, Y, Delay) mappings
 ┃ ┣ 📜 interface.py              # Visual terminal engine (Rich)
 ┃ ┗ 📜 rotina.py                 # Task selection logic and queue management
 ┣ 📂 Util/
 ┃ ┗ 📜 funcoes_suporte.py        # Core Engine: Humanized clicks, Pixel Matching, Crop Tool
 ┣ 📜 menu.py                     # Entry Point (Main Loop and Task Scheduler)
 ┗ 📜 requirements.txt            # Dependency contract
