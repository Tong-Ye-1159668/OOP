import tkinter as tk
from Controller import Controller
from GUI import LOSApp

if __name__ == "__main__":
    root = tk.Tk()

    # Initialize the controller
    controller = Controller()

    # Load customers and products into the controller
    controller.load_data()  # This method should read the data from the files and populate the Controller's customers and products lists

    # Start the Tkinter application with the controller
    app = LOSApp(root, controller)
    
    # Run the main loop
    root.mainloop()

