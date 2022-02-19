from tkinter import *
from object_detection_interface import ObjectDetectionInterface
from person_detection_interface import PersonDetectionInterface
from object_detection_in_video_interface import ObjectDetectionInVideoInterface


class MainMenu:

    def main_menu_function(self):
        global panel
        panel = Tk()
        panel.geometry("300x350")
        panel.title("Object Detection System")
        Label(panel, text="Object Detection System", bg="#4BC5DC", fg="white", width=300, height=2, font=("Times New Roman", 14)).pack()

        Label(panel, text="").pack()
        Button(panel, text="Object Detection", height=2, width=30, bg="#4BC5DC", fg="white", command=self.object_detection).pack()

        Label(panel, text="").pack()
        Button(panel, text="Person Detection", height=2, width=30, bg="#4BC5DC", fg="white", command=self.person_detection).pack()

        Label(panel, text="").pack()
        Button(panel, text="Object Detection in Video", height=2, width=30, bg="#4BC5DC", fg="white", command=self.object_detection_in_video).pack()

        Label(panel, text="").pack()
        Button(panel, text="Exit the System", height=2, width=30, bg="#4BC5DC", fg="white", command=self.exit).pack()

        panel.mainloop()


    def object_detection(self):
        panel.withdraw()
        obj = ObjectDetectionInterface()
        obj.object_detection_function()


    def person_detection(self):
        panel.withdraw()
        obj = PersonDetectionInterface()
        obj.person_detection_function()

    def object_detection_in_video(self):
        panel.withdraw()
        obj = ObjectDetectionInVideoInterface()
        obj.object_detection_in_video_function()


    def exit(self):
        panel.destroy()


obj = MainMenu()
obj.main_menu_function()
