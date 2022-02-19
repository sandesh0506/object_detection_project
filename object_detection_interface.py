from tkinter import *
import os
from tkinter import filedialog
from object_detection import ObjectDetection


class ObjectDetectionInterface:
    def object_detection_function(self):
        global panel
        panel_width = 400
        panel_height = 400
        panel = Tk()
        panel.geometry(str(panel_width)+"x"+str(panel_height))
        panel.title("Object Detection Interface")
        Label(panel, text="Object Detection Interface", bg="#4BC5DC", fg="white", width=panel_width, height=2, font=("Calibri", 14)).pack()

        Label(panel, text="").pack()
        Label(panel, text="Please Select the Input Image").pack()

        global image_name_entry
        image_name_entry = Entry(panel, width= 50)
        image_name_entry.pack()
        Button(panel, text="Browse", width=10, height=1, bg="#4BC5DC", fg="white", command=self.browse).pack()


        Label(panel, text="").pack()
        Button(panel, text="Object Detection", width=30, height=2, bg="#4BC5DC", fg="white", command=self.button_command).pack()
        Label(panel, text="").pack()
        Button(panel, text="Back", width=30, height=2, bg="#4BC5DC", fg="white", command=self.back).pack()
        Label(panel, text="").pack()
        Button(panel, text="Exit The System", width=30, height=2, bg="#4BC5DC", fg="white", command=self.exit).pack()
        panel.mainloop()

    def browse(self):
        global file_name
        currdir = os.getcwd()
        file_name = filedialog.askopenfilename(initialdir = currdir)
        print(file_name)
        image_name_entry.insert(END, file_name)


    def button_command(self):
        # file_name = file_name_input.get()
        print(file_name)
        if file_name.endswith(".jpg") or file_name.endswith(".JPG") or file_name.endswith(".png") or file_name.endswith(".PNG"):
            obj = ObjectDetection()
            obj.object_detection_function(file_name)
        else:
            self.image_validation_failed()

    def image_validation_failed(self):
        global root2
        root2 = Tk()
        root2.title("Image Format Error")
        root2.geometry("350x150")
        Label(root2, text="Image Format Error", bg="red", width=300, height=2, font=("Times New Roman", 14)).pack()
        Label(root2, text="").pack()
        Label(root2, text="Please Enter Correct Image Format (.JPG or .PNG Format)").pack()
        Label(root2, text="").pack()
        Button(root2, text="OK", command=self.ok).pack()
        root2.mainloop()

    def ok(self):
        root2.destroy()

    def exit(self):
        panel.destroy()

    def back(self):
        panel.withdraw()
        from main_menu import MainMenu
        obj = MainMenu()
        obj.main_menu_function()


