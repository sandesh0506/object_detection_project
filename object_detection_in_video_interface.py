from tkinter import *
import os
from tkinter import filedialog
from object_detection_in_video import ObjectDetectionInVIdeo


class ObjectDetectionInVideoInterface:
    def object_detection_in_video_function(self):
        global panel
        panel_width = 400
        panel_height = 400
        panel = Tk()
        panel.geometry(str(panel_width)+"x"+str(panel_height))
        panel.title("Object Detection in Video Interface")
        Label(panel, text="Object Detection in Video Interface", bg="#4BC5DC", fg="white", width=panel_width, height=2, font=("Calibri", 14)).pack()

        Label(panel, text="").pack()
        Label(panel, text="Please Select the Input Video").pack()

        global video_name_entry
        video_name_entry = Entry(panel, width= 50)
        video_name_entry.pack()
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
        video_name_entry.insert(END, file_name)


    def button_command(self):
        # file_name = file_name_input.get()
        print(file_name)
        if file_name.endswith(".MP4") or file_name.endswith(".mp4"):
            obj = ObjectDetectionInVIdeo()
            obj.object_detection_in_video(file_name)
        else:
            self.video_validation_failed()

    def video_validation_failed(self):
        global root2
        root2 = Tk()
        root2.title("Video Format Error")
        root2.geometry("350x150")
        Label(root2, text="Video Format Error", bg="red", width=300, height=2, font=("Times New Roman", 14)).pack()
        Label(root2, text="").pack()
        Label(root2, text="Please Enter Correct Video Format (.mp4 Format)").pack()
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


