import tkinter as tnk
#from PIL import Image, ImageTk

class App(tnk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.delayTime = 1;
        self.recordTime = 1;
        self.delayBox = self.createTextBox(0,0)
        self.recordBox = self.createTextBox(0,0)

    def run(self):
        button1 = self.createButton('Set', self.setDelay,7,1 )
        textBox1 = self.createTextBox(23,1)
        label1 = self.createLabel("Delay",5,1)

        button2 = self.createButton('Set', self.setRecord,7,1 )
        textBox2 = self.createTextBox(23,1)
        label2 = self.createLabel("Record Time",11,1)

        button3 = self.createButton('Confirm', self.closeWindow,7,1)
        self.delayBox = textBox1
        self.recordBox = textBox2

        label1.pack()
        textBox1.pack()
        button1.pack()
        self.placeItem(button1,225,30)
        self.placeItem(textBox1,30,30)
        self.placeItem(label1,30,12)
        self.placeItem(button2,225,70)
        self.placeItem(textBox2,30,70)
        self.placeItem(label2,30,52)
        self.placeItem(button3,225,110)
        self.mainloop()

    def placeItem(self, item, xcoord, ycoord):
        item.place(x=xcoord,y=ycoord)
    
    def createCanvas(self, canvas_width, canvas_height):
        canvas = tnk.Canvas(self.master, width=canvas_width, height=canvas_height)
        return canvas

    def createButton(self, txt, cmd, w, h):
        button = tnk.Button(self.master, text=txt, command = cmd, width=w, height=h,padx=0,pady=0)
        return button

    def createTextBox(self, w, h):
        textBox= tnk.Text(self.master,width=w,height=h,padx=0,pady=0)
        return textBox

    def createLabel(self,txt,w,h):
        label = tnk.Label(self.master,text=txt,padx=0,pady=0,width=w,height=h)
        return label

    def closeWindow(self):
        self.master.destroy()

    def setDelay(self):
        self.delayTime = int(self.delayBox.get(1.0,'end'))

    def setRecord(self):
        self.recordTime = int(self.recordBox.get(1.0,'end'))

