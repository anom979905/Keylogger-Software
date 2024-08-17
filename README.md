# Keylogger-Software

The keylogger-software is a demonstration of how to monitor and interact with keyboard and mouse events using Python. Keyloggers are software tools that record keystrokes on a device, capturing everything typed by the user. While keylogging has valid applications in debugging, user activity monitoring, and research, it also has ethical implications and risks associated with privacy and misuse.

This project explores the fundamental aspects of keylogging and input control through three main components: a keylogger script, a control script, and a mouse listener script. Together, these scripts showcase the power and flexibility of Python in automating and monitoring user inputs.

Project Components
Keylogger Script

Functionality: Captures every keystroke made by the user and logs it to a text file.
Key Features:
Converts key events into readable text.
Logs special keys like space, enter, and others appropriately.
Continuously writes keystrokes to log.txt, allowing for real-time monitoring.
Control Script

Functionality: Programmatically controls the mouse and keyboard, simulating user actions.
Key Features:
Moves the mouse pointer to a specified screen coordinate.
Types predefined text at the current cursor position.
Demonstrates how to automate tasks and simulate user inputs.
Mouse Listener Script

Functionality: Tracks and prints the position of the mouse cursor as it moves.
Key Features:
Monitors mouse movements in real-time.
Outputs the exact coordinates of the cursor to the console.
Useful for tracking user interactions and debugging GUI applications.

### Steps to Use the Full Keylogger Project

#### 1. **Install Required Dependencies:**
   - Open a terminal or command prompt and install the `pynput` library:
     ```bash
     pip install pynput
     ```

#### 2. **Run the Keylogger Script:**
   - Create a file (e.g., `keylogger.py`) and paste the keylogger code.
   - Execute the script:
     ```bash
     python keylogger.py
     ```
   - Keystrokes will be logged to a file named `log.txt`.

#### 3. **Run the Control Script:**
   - Create a file (e.g., `control.py`) and paste the control script code.
   - Execute the script:
     ```bash
     python control.py
     ```
   - The script will move the mouse and type the predefined text.

#### 4. **Run the Mouse Listener Script:**
   - Create a file (e.g., `mouse_listener.py`) and paste the mouse listener code.
   - Execute the script:
     ```bash
     python mouse_listener.py
     ```
   - The mouse position will be printed to the console as it moves.

#### 5. **(Optional) Integrate Scripts:**
   - Combine the scripts into a single file if you want to run all functionalities together.
   - Execute the combined script:
     ```bash
     python combined_script.py
     ```

This sequence allows you to fully utilize and test the keylogger project.
