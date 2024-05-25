import sys
import time
import smv_file_generator
import run_nuXmv
import extract_moves
import solve_iteratively
import os

def main(iterative_mode = False , engine = None , steps_num = None):
    #UPDATE BOARD FILE HERE
    board_path="boards/board.txt"
    if(iterative_mode):
        solve_iteratively.solve_sokoban_iteratively(board_path, engine, steps_num)
    else:
        #Generate smv file from board
        smv_file_name=smv_file_generator.generate_smv_file(board_path)
        print("The file has been created and the content has been written.")
        #Run Smv file using script
        output_file_name=run_nuXmv.run_nuxmv(smv_file_name,engine,steps_num)

        #Extract path to winning state
        winning_path=extract_moves.extract_moves_from_output_file(output_file_name)

        #Print results
        if len(winning_path) == 0 and engine == "SAT" and steps_num != None:
            print(f"No solution for this board in {steps_num} steps.")      
        elif len(winning_path) == 0:
            print("There is no solution for this board, Board unsolvable.")
        else:
            print(f"Path to win: {winning_path}.")

if __name__ == "__main__":
    # Ensure we have the correct number of command-line arguments
    if len(sys.argv) != 4:
        print("Usage: python Main.py <iterative_mode> <engine> <steps_num>")
        sys.exit(1)

    # Parse command-line arguments
    iterative_mode = sys.argv[1].lower() == 'true'
    engine = sys.argv[2]
    steps_num = int(sys.argv[3]) if sys.argv[3].isdigit() else None

    # Call the main function with parsed arguments
    main(iterative_mode, engine, steps_num)
