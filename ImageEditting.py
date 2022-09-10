#///////////////////////////////////////////////////////Imports///////////////////////////////////////////////////////////
import tkinter
import filedialogfrom tkinter.filedialog 
import askopenfilefrom tkinter
import *from PIL
import Image, ImageTk

#////////////////////////////////////////////////////Setting up the GUI///////////////////////////////////////////////////
root = tk.Tk()
root.state('zoomed')
root.title("image")
root.geometry("1920x1080")
canvas = tk.Canvas(root, width = 1920, height = 1080, bg = "white")
canvas.grid(columnspan = 10, rowspan = 9)

#/////////////////////////////////////////////////Extra Helping Methods///////////////////////////////////////////////////
def close_win(top):
    top.destroy()
def store_Width_Height(inputWidth, inputHeight):
    global currentWidth
    currentWidth = int(inputWidth)
    global currentHeight
    currentHeight = int(inputHeight)
    #print(str(currentWidth) + ' X ' + str(currentHeight))

#///////////////////////////////////////////////////////Open File////////////////////////////////////////////////////////
def open_File():
    global filePath, openedImage1, openedImage2
    file = askopenfile(parent = root, mode = 'rb', title = 'Choose a file', filetype = [('Image', '*.jpg', '*.png')])
    filePath = str(file)[26:-2]
    #print(filePath)
    openedImage1 = Image.open(filePath)
    openedImage1 = openedImage1.convert('CMYK')
    print(openedImage1.mode)
    if Image.open(filePath):
        store_Width_Height(openedImage1.width, openedImage1.height)
        openedImage2 = ImageTk.PhotoImage(openedImage1)
        canvas.delete('all')
        canvas.create_image(canvas.winfo_width()/2, canvas.winfo_height()/2, image = openedImage2)
        canvas.image = openedImage2
        outputImage = tk.Label(image = inputImage)
        #outputImage.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        """
        else:
            top = Toplevel(root)
            label = Label(top, text = "Not a suppported file", font = ("Times", "12"))
            top.geometry = ('1000x1000')
            label.pack()
            button = Button(top, text="Return", font = ("Times", "12"), command = lambda:close_win(top))
            button.pack(pady=5, side= TOP)
        """
        openFile = tk.Button(root, text = "Open File", font = ("Times", "12", "bold"), command = lambda:open_File(), padx = 10, pady = 5, fg = "firebrick1", bg = "navy")
        openFile.grid(column = 0, row = 8)

#///////////////////////////////////////////////////////////////////Save////////////////////////////////////////////////////////////////////openedImage2 = NonesomeFunctionImage2 = NonerotatedImage2 = NoneflippedHorizontalImage2 = NoneflippedVerticalImage2 = NonecroppedImage2 = NoneresizedImage2 = NonefilteredImage2 = None
def save_File():
    global filePath, openedImage1 ,openedImage2, someFunctionImage1, someFunctionImage2, rotatedImage1, rotatedImage2, flippedHorizontalImage1, flippedHorizontalImage2, flippedVerticalImage1, flippedVerticalImage2, croppedImage1, croppedImage2, resizedImage1, resizedImage2, filteredImage1, filteredImage2
    ext = filePath.split(".")[-1]
    file = filedialog.asksaveasfilename(defaultextension = f".{ext}", filetypes = [("PNG file","*.png"), ("TIFF file","*.tiff")])
    if file:
        if canvas.image == openedImage2:
            openedImage1.save(file)
        elif canvas.image == someFunctionImage2:
            someFunctionImage1.save(file)
        elif canvas.image == rotatedImage2:
            rotatedImage1.save(file)
        elif canvas.image == flippedHorizontalImage2:
            flippedHorizontalImage1.save(file)
        elif canvas.image == flippedVerticalImage2:
            flippedVerticalImage1.save(file)
        elif canvas.image == croppedImage2:
            croppedImage1.save(file)
        elif canvas.image == resizedImage2:
            resizedImage1.save(file)
        elif canvas.image == filteredImage2:
            filteredImage1.save(file)
        else:
            print("Failed to save")
            print("Image saved")
    save = tk.Button(root, text = "Save", font = ("Times", "12", "bold"), command = lambda:save_File(), padx = 10, pady = 5, fg = "firebrick1", bg = "navy")
    save.grid(column = 1, row = 8)

#/////////////////////////////////////////////////////////Brightness///////////////////////////////////////////////////////
def adjust_brightness():
    filePathbrightness = tk.Button(root, text = "Brightness", font = ("Times", "12", "bold"), command = lambda:adjust_brightness(), padx = 10, pady = 5, fg = "firebrick1", bg = "navy")
adjust_brightness.grid(column = 2, row = 8)

#/////////////////////////////////////////////////////////Contrast/////////////////////////////////////////////////////////
def adjust_contrast():
    filePathcontrast = tk.Button(root, text = "Contrast", font = ("Times", "12", "bold"), command = lambda:adjust_contrast(), padx = 10, pady = 5, fg = "firebrick1", bg = "navy")
adjust_contrast.grid(column = 3, row = 8)

#////////////////////////////////////////////////////////Rotate////////////////////////////////////////////////////////////
def rotate_File():
    global rotatedImage1, rotatedImage2, openedImage1
    rotatedImage1 = openedImage1.transpose(Image.ROTATE_270)
    openedImage1 = rotatedImage1
    store_Width_Height(openedImage1.width, openedImage1.height)
    rotatedImage2 = ImageTk.PhotoImage(rotatedImage1)
    canvas.delete('all')
    canvas.create_image(canvas.winfo_width()/2, canvas.winfo_height()/2, image = rotatedImage2)
    canvas.image = rotatedImage2
rotate = tk.Button(root, text = "Rotate", font = ("Times", "12", "bold"), command = lambda:rotate_File(), padx = 10, pady = 5, fg = "firebrick1", bg = "navy")
rotate.grid(column = 4, row = 8)

#////////////////////////////////////////////////////////////////Flip///////////////////////////////////////////////////////////////////////////
def flippedHorizontal():
    print("fh")
flipHorizontal = tk.Button(root, text = "Flip Horizontal", font = ("Times", "12", "bold"), command = lambda:flippedHorizontal(), padx = 10, pady = 5, fg = "firebrick1", bg = "navy")
flipHorizontal.grid(column = 5, row = 8)
def flippedVertical():
    print("fv")
flipVertical = tk.Button(root, text = "Flip Vertical", font = ("Times", "12", "bold"), command = lambda:flippedVertical(), padx = 10, pady = 5, fg = "firebrick1", bg = "navy")
flipVertical.grid(column = 6, row = 8)

#////////////////////////////////////////////////////////////////////Crop///////////////////////////////////////////////////////////////////////
def crop_File():
    print("crop")
crop = tk.Button(root, text = "Crop", font = ("Times", "12", "bold"), command = lambda:crop_File(), padx = 10, pady = 5, fg = "firebrick1", bg = "navy")
crop.grid(column = 7, row = 8)

#///////////////////////////////////////////////////////////////////Resize///////////////////////////////////////////////////////////////////////
def dimensions():
    #print('Current dimensions: ', currentWidth, 'x', currentHeight)
    top = Toplevel(root)
    top.geometry = ('1000x1000')
    labelText = "What dimensions do you want your file to be?\nCurrent dimensions: " + str(currentWidth) + " X " + str(currentHeight)
    label = Label(top, text = labelText, font = ("Times", "12"))
    label.pack()
    entryWidth = Entry(top, font = ("Times", "12"), width = 4)
    labelX = Label(top, text = "X", font = ("Times", "12"))
    entryHeight = Entry(top, font = ("Times", "12"), width = 4)
    entryWidth.pack()
    labelX.pack()
    entryHeight.pack()
    #buttonApply = Button(top, text = "Apply", font = ("Times", "12"), command = lambda:[store_Width_Height(entryWidth.get(), entryHeight.get()), resize_File(), close_win(top)])    buttonCancel = Button(top, text = "Cancel", font = ("Times", "12"), command = lambda:close_win(top))    buttonApply.pack()    buttonCancel.pack()    def resize_File():    global resizedImage1, resizedImage2, openedImage1    resizedImage1 = openedImage1.resize((currentWidth, currentHeight))    openedImage1 = resizedImage1    resizedImage2 = ImageTk.PhotoImage(resizedImage1)    canvas.delete('all')    canvas.create_image(canvas.winfo_width()/2, canvas.winfo_height()/2, image = resizedImage2)
    canvas.image = resizedImage2
    #outputImage = tk.Label(image = tempImage)
    #outputImage.place(relx = 0.5, rely = 0.5, anchor = CENTER)
resize = tk.Button(root, text = "Resize", font = ("Times", "12", "bold"), command = lambda:dimensions(), padx = 10, pady = 5, fg = "firebrick1", bg = "navy")
resize.grid(column = 8, row = 8)
#////////////////////////////////////////////////////////////////Filter////////////////////////////////////////////////////////////////
def filter_File():
    print("filtered")
filter = tk.Button(root, text = "Filter", font = ("Times", "12", "bold"), command = lambda:filter_File(), padx = 10, pady = 5, fg = "firebrick1", bg = "navy")
filter.grid(column = 9, row = 8)
#////////////////////////////////////////////////////////////////Mainloop////////////////////////////////////////////////////////////////root.mainloop()