----------------------------
Sokoban Solver                                                          
----------------------------
by Daniel Hazan and Ori Glam

This program is designed for solving sokoban boards.
The main script ('Main.py) is designed to run nuXmv model checking using either the BDD engine or the SAT engine with BMC (Bounded Model Checking).
You can either run in iterative mode(solving for 1 box at a time) or non iterative mode (all boxes at a time).
The script can be executed from the command line or through Visual Studio Code (VS Code).


----------------------------
 Prerequisites

- Python 3.x installed on your system
- nuXmv installed and accessible from the command line
- Ensure the path to the `nuXmv` executable is correctly set in system environment variables and can be executable from any location

----------------------------
Downloading the files

Please download all files and folders:
1.Main.py
2.smv_file_generator.py
3.extract_moves.py
4.run_nuXmv.py
5.solve_iteratively.py
6. download boards folder

----------------------------
Running Modes

the main script recieves three variables:
<iterative_mode> - True if you want to run in iterative mode, else False(default).
<engine> - "BDD"/"SAT"/None (default)
<steps_num> - for SAT engine insert number of steps(int) for running in BMC (bounded model checking) if you want to bound number of steps (dedault - None)

----------------------------
Choosing Board

Defaultively the script will run for the file board.txt in boards folder.
else, please open the main script and update the board_path
make sure it is the same folder as the main file (or decendant folder)
Update this line in main.py
board_path="boards/board.txt"

----------------------------
Running the Script through Command Line

1. Open Command Line:
   Open Command Prompt, PowerShell, or a terminal emulator of your choice.

2. Navigate to the Script Directory:
   Use the `cd` command to navigate to the directory where `Main.py` is located. For example:
     ```sh
     cd path/to/directory
     ```

3. Run the Script:
   Execute the script with the necessary arguments by typing:
     ```sh
     python Main.py <iterative_mode> <engine> <steps_num>
     ```

   - Example:
     ```sh
     python Main.py False "SAT" 10 
     ```
	 
----------------------------
Running the Script through VS Code

1. Open VS Code:
	Launch Visual Studio Code on your computer.

2. Open the Script:
	Go to File > Open File... and navigate to the location of Main.py.
	Select Main.py and click Open.

3. Install Python Extension:
	If you haven't installed the Python extension for VS Code, open the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window or by pressing Ctrl+Shift+X.
	Search for "Python" and install the extension provided by Microsoft.

4. Configure the Python Interpreter:
	Click on the interpreter version displayed at the bottom-left corner of VS Code (or press Ctrl+Shift+P and type Python: Select Interpreter).
	Choose the correct Python interpreter from the list.

5. Run the Script:
	Open a terminal in VS Code by going to View > Terminal or pressing Ctrl+`.
	In the terminal, navigate to the directory where Main.py is located (if not already there):

	sh
	cd path/to/directory
6. Run the script with the necessary arguments by typing:

	sh
	python Main.py <iterative_mode> <engine> <steps_num>
	Example:

	sh
	python Main.py False "SAT" 10



