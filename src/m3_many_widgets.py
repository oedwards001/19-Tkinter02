import tkinter as tk

###############################################################################
#
# In this module, all of the _todo_ items will be in one comment because you
# will be modifying the same block of code as you go.
#
# TODO: 1. (1 pt)
#
#   First, create a tkinter window called window.
#
#   Make sure you call window's mainloop() method so your window will show up
#   when you run this module.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# TODO: 2. (4 pts)
#
#   Now, we are going to practice all of our widgets.
#
#   First, create two different frames.
#
#   Next, place widgets in both frames. Your frames should have these widgets
#   in them:
#
#       - Frame 1
#           - Label
#           - Button
#           - Single Line Text Entry
#       - Frame 2
#           - Label
#           - Multi Line Text Entry
#
#   You choose what text to have in the labels and button.
#
#   Make sure you call the pack method on all your widgets and that each widget
#   is in the proper frame.
#   
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
window = tk.Tk()

frm_1 = tk.Frame()
frm_1.pack()

label_1 = tk.Label(master = frm_1, text = "Frame 1")
label_1.pack()

button_1 = tk.Button(window, text = "Click!")
button_1.pack()

entry_1 = tk.Entry(window)
entry_1.pack()

entry_1.insert(0, "What's your name?")

frm_2 = tk.Frame()
frm_2.pack()

label_2 = tk.Label(master = frm_2, text = "Frame 2")
label_2.pack()

text_box = tk.Text()
text_box.pack()

text_box.insert("1.0", "What is your date of birth?")
text_box.insert("2.0", "\nWhere do you live?")

window.mainloop()