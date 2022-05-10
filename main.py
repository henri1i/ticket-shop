from store import Store
from interface import Displayer
from handler import Handler

class Main:
    def __init__(self):
        self.store = Store()
        self.handler = Handler()

        self.keepRunning = True

        self.handler.login()
        self.run()

    def run(self):
        selectedOption = Displayer.getUserOption()
        
        self.keepRunning = self.handler.shouldKeepRunning(selectedOption)

        if (not self.keepRunning):
            Displayer.renderExitMessage()
            return

        self.handler.handleInput(selectedOption)

        self.run()

Main()