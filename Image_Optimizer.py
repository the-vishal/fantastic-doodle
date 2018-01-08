from tkinter import *
from PIL import ImageFilter,Image
from tkinter import filedialog, messagebox
import os
import psutil
import time
import subprocess

main_win = Tk()
main_win.iconbitmap('C:/Users/Vishal/Desktop/PYTHON BEST/Image Optimizer/favicon.ico')


main_win.config(background = "#ffffff")
#main_win.geometry("550x240")
main_win.wm_title("Image optimizer")


frame1 = Frame(main_win,height = 70,background="#ffffff")
frame1.grid(row=0,column=0,pady=10)

ban = PhotoImage(file='banner.gif')
banner = Label(frame1,image=ban)
banner.grid(row=0,column=1)

frame2 = Frame(main_win,height = 70,background="#ffffff")
frame2.grid(row=1,column=0,padx=10,pady=10)


frame3 = Frame(main_win,height = 30,background="#708090")
frame3.grid(row=2,column=0,padx=10,pady=10)

#load file
def open_file():
    file_ = filedialog.askopenfile()
    global file_name,name_,ext
    file_name = file_.name
    #print(file_name)
    name_, ext = os.path.splitext(file_name)
    global orgFile_name
    orgFile_name = os.path.basename(file_name)
    file_loaded['text'] = "File loaded : "+orgFile_name
    file_loaded['bg']="YELLOW"
    global image
    image = Image.open(str(file_name))
    image.show()
    time.sleep(3)
    kill_imageWindow()


#show image
def show_image():
    image.show()


#kill image windows
def kill_imageWindow():
    for process in psutil.process_iter():
        #print(process)
        if process.name() == "Microsoft.Photos.exe":
            process.kill()
            break



#save as image
def save_as():
    image.save(name_+ '.'+new_ext.get() )


#black and white
def bnw():
    bnw_img = image.convert(mode='L')
    kill_imageWindow()

    if apply.get()==1:
        bnw_img.save('temp.jpg')
        image.close()
        change_file()

    else:
        bnw_img.show()

#change file to temp and closes prev
def change_file():
    global image
    new_file = os.getcwd().replace("'\'", '/')
    image = Image.open(new_file+'/temp.jpg')
    file_loaded['text'] = "File : temp.jpg"
    file_loaded['bg']="WHITE"
    kill_imageWindow()
    show_image()


#crop image
#All the coordinates of box (x, y, w, h) are measured from the top left corner
# of the image. so the coordinates of the box should be (x, y, w+x, h+y).
def crop_image():
    parameter =tuple(map(int,crop_dim.get().strip().split(',')))
    crop_img = image.crop(box=parameter)
    kill_imageWindow()

    if apply.get()==1:
        crop_img.save('temp.jpg')
        image.close()
        change_file()

    else:
        crop_img.show()

#rotate
def rotate_image():
    rot_imag = image.rotate(int(angle.get()))
    kill_imageWindow()

    if apply.get()==1:
        rot_imag.save('temp.jpg')
        image.close()
        change_file()

    else:
        rot_imag.show()


#resize thumbnail
def resize_image():
    pixels_tup = tuple(map(int,pixels.get().strip().split(',')))
    #print(pixels_tup)
    image.thumbnail(pixels_tup)
    if apply.get()==1:
        image.save('temp.jpg')
        image.close()
        change_file()



#blur image
def blur_image():
    rad = int(blur_radius.get())
    blur_imag = image.filter(ImageFilter.GaussianBlur(radius= rad))
    kill_imageWindow()

    if apply.get()==1:
        blur_imag.save('temp.jpg')
        image.close()
        change_file()

    else:
        blur_imag.show()


#unsharp image
# def unsharp_image():
#     rad = int(unsharp_radius.get())
#     blur_imag = image.filter(ImageFilter.GaussianBlur(radius= rad))
#     kill_imageWindow()

    if apply.get()==1:
        blur_imag.save('temp.jpg')
        image.close()
        change_file()

    else:
        blur_imag.show()


def save_image():
   result = messagebox.askyesno(title="SAVE IMAGE", message="save image?")
   if result == True:
     image.save(orgFile_name)
     os.remove('temp.jpg')
   else:
       pass


# ----------------------tkinter GUI--------------------------------


#load image
load_img= PhotoImage(file='load.png')
load = Button(frame2,image=load_img, command = open_file)
load.grid(row=0,column=0,padx=4)


file_loaded = Label(frame1,text= 'No file loaded')
file_loaded.grid(row=1,column=1,padx=10,pady=10)

#show image
show_img= PhotoImage(file='show.png')
show = Button(frame2,image=show_img,command = show_image)
show.grid(row=0,column=1,padx=4)

#save as
new_ext = Entry(frame2,width=9)
new_ext.grid(row=1,column=2,pady=4)
new_ext.insert(0,'extension')

saveas_img= PhotoImage(file='saveas.png')
saveas = Button(frame2, command = save_as,image=saveas_img)
saveas.grid(row=0,column=2,padx=4)


#black and white
bw_img= PhotoImage(file='bw.png')
bw = Button(frame2,image=bw_img,command = bnw)
bw.grid(row=0,column=3,padx=4)
apply = IntVar()


# Apply
apply_effect = Checkbutton(frame3,text='APPLY',variable=apply)
apply_effect.grid(row=0,column=0)


#crop
crop_dim = Entry(frame2,width=12)
crop_dim.grid(row=1,column=4)
crop_dim.insert(0,"x,y,x+h,y+w")

crop_img= PhotoImage(file='crop.png')
crop = Button(frame2, command = crop_image,image=crop_img)
crop.grid(row=0,column=4)


# Blur
blur_radius = Entry(frame2,width=7)
blur_radius.grid(row=1,column=5)
blur_radius.insert(0,'Radius')

blur_img= PhotoImage(file='blur.png')
blur = Button(frame2,image=blur_img,command = blur_image)
blur.grid(row=0,column=5,padx=4)


#rotate
angle = Entry(frame2,width=7)
angle.grid(row=1,column=6)
angle.insert(0,'Angle')

rotate_img= PhotoImage(file='rotate.png')
rotate = Button(frame2, command = rotate_image,image=rotate_img)
rotate.grid(row=0,column=6,padx=4)



#resize
pixels = Entry(frame2,width=7)
pixels.grid(row=1,column=7)
pixels.insert(0,'H,W')

resize_img= PhotoImage(file='resize.png')
resize = Button(frame2,image=resize_img,command = resize_image)
resize.grid(row=0,column=7,padx=4)


#save
save_img= PhotoImage(file='save.png')
save = Button(frame2, command = save_image,image=save_img)
save.grid(row=0,column=8,padx=4)


#apply button : if clicked save it as temp file then close last opened file
# and load that temp file


main_win.mainloop()

