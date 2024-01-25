"""
Program: GUI_Template.py
Chapter 8 Example (Pg 281)
01/24/2024

**NOTE: The module breezypythongui.py MUST be in the same directory as this file for the app to run correctly!

GUI-based app demonstrating the use of the checkbutton (checkbox) graphic
"""

from breezypythongui import EasyFrame
from tkinter.font import Font
# Other imports go here

# Class header (class name will change project to project)
class CheckbuttonDemo(EasyFrame):

	# Definition of out classes' constructor method
	def __init__(self):
		# Call to the Easy Frame class constructor
		EasyFrame.__init__(self, title = 'Checkbutton Demo', width = 320, height = 200, resizable = False, background = 'paleturquoise')

		# add various components to the window
		self.addLabel(text = "Today's Menu", row = 0, column = 0, sticky = 'NSEW', columnspan = 2, background = 'paleturquoise', foreground = 'purple', font = Font(family = 'Arial', size = 28))

		# Add four checkbuttons
		self.chickCB = self.addCheckbutton(text = 'Chicken', row = 1, column = 0)
		self.taterCB = self.addCheckbutton(text = 'French Fries', row = 1, column = 1)
		self.beanCB = self.addCheckbutton(text = 'Green Beans', row = 2, column = 0)
		self.sauceCB = self.addCheckbutton(text = 'Apple Sauce', row = 2, column = 1)

		self.chickCB['background'] ='paleturquoise'
		self.taterCB['background'] ='paleturquoise'
		self.beanCB['background'] ='paleturquoise'
		self.sauceCB['background'] ='paleturquoise'

		# Add the command button
		self.order = self.addButton(text = 'Place Order', row = 3, column =0, columnspan = 2, command = self.placeOrder)
		self.order['background'] = 'cyan'
		self.order['foreground'] = 'purple'
		self.order['width'] = 24

	# Definition of the placeOrder() function which is the event handler
	def placeOrder(self):
		# Display a message box with order summary
		message = ''

		# Analyze each checkbutton to see if they have been checked
		if self.chickCB.isChecked():
			message += 'Chicken\n\n'
		if self.taterCB.isChecked():
			message += 'French Fries\n\n'
		if self.beanCB.isChecked():
			message += 'Green Beans\n\n'
		if self.sauceCB.isChecked():
			message += 'Apple Sauce\n\n'
		if message == '':
			message += 'Sorry, no food ordered!'

		# Now wthat we have looked at every checkbutton, let's push the message variable to our pop-up
		self.messageBox(title = 'Customer Order', message = message)


# Global definition of the main() method
def main():
	# instantiate an object from the class into mainloop()
	CheckbuttonDemo().mainloop()

if __name__ == '__main__':
	main()