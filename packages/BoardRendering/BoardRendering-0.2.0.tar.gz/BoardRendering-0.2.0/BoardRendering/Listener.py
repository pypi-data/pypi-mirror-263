from ConsoleBoard import Board
from Exceptions import Exceptions



class Listener:
    def __init__(self, board=Board, title="", header=""):
            if board == Board:
                 raise Exceptions.InvalidBoard("Invalid Board Value")
            self.title = title
            self.header = header
            self.board = board

    def StartDisplay(self, update):
        """Starts the listener which constantly updates the board by you updating it
        
            Use the Update param to set a Update function and end the listener by returning True"""
        board = self.board
        pastboard = ""
        while True:
            s = update()
            if s is True:
                break
            if pastboard != board.display:
                pastboard = board.display
                import subprocess
                subprocess.run('cls', shell=True)
                print(
f"""{self.title}
{board.display}
{self.header}""")