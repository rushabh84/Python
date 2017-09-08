# Author: Rushabh Shah
# Original Creation Date: 04/19/17
# Last modification date: 04/19/17
# This is a GUI program that takes a value and calculates the assessment and propery tax value for the actual property value enetered by the user

import tkinter

class TaxGUI:
    def __init__(self):
     
        self.main_window = tkinter.Tk()
        # Create three frames to group widgets.
        self.top_frame = tkinter.Frame()
        self.middle_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # Create the widgets for the top frame.
        self.prompt_label = tkinter.Label(self.top_frame, \
                                          text = "Enter the value of a property")
        #input will be entered by the user in prop_value
        self.prop_value = tkinter.Entry(self.top_frame, \
                                        width = 10)
        # Pack the top frame's widgets.
        self.prompt_label.pack(side = 'left')
        self.prop_value.pack(side = 'left')

        # Create the widgets for the middle frame.
        self.descr_label1 = tkinter.Label(self.middle_frame, \
                                          text = "Assessment value: ")
        self.value1 = tkinter.StringVar()
        self.assess_label = tkinter.Label(self.middle_frame, \
                                         textvariable = self.value1)
        # Pack the middle frame's widgets.
        self.descr_label1.pack(side='left')
        self.assess_label.pack(side = 'left')

        self.descr_label2 = tkinter.Label(self.middle_frame, \
                                          text = "Property tax: ")
        self.value2 = tkinter.StringVar()
        self.tax_label = tkinter.Label(self.middle_frame, \
                                         textvariable = self.value2)
        # Pack the middle frame's widgets.
        self.descr_label2.pack(side='left')
        self.tax_label.pack(side = 'left')

        # Create the widgets for the bottom frame.
        #quit the main window when button quit clicked, and if convert clicked call the convert method of the class
        self.convert_button = tkinter.Button(self.bottom_frame, \
                                             text = "Convert", \
                                             command = self.convert)
        #quit the main window when button quit clicked
        self.quit_button = tkinter.Button(self.bottom_frame, \
                                          text = "Quit", \
                                          command = self.main_window.destroy)
        # Pack the bottom frame's widgets.
        self.convert_button.pack(side='left')
        self.quit_button.pack()

        # Pack the frames.
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()
    def convert(self):
        # Get the value entered by the user into the
        # prop_value widget.

        value = float(self.prop_value.get())
        assessment = value*.6
        # Convert kvalue into the pproperty tax incurred on it.
        prop_tax = (assessment/100)*.75
        #sets the of widgets value1 and value2
        self.value1.set(assessment)
        self.value2.set(prop_tax)
#starting point of the program, and creates an object of TaxGUI, and so automatically calls the _init_ method and then the folloowing operations are performed    
def main():
   my_GUI = TaxGUI() 
main()
