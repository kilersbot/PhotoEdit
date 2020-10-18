from tkinter import filedialog as fd, messagebox	
from tkinter import *
from PIL import Image, ImageTk, ImageFilter, ImageOps
from PIL.ImageFilter import (
	BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
	EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN, GaussianBlur, ModeFilter
	)
import os
import sys
#настройка окна
root = Tk()
root.title("PhotoEdit")
root.minsize( width = 1600, height = 900 )
root.maxsize( width = 2560, height = 1440 )
root.geometry("1600x900+70+10")
root.iconbitmap('BYclT2IXMGpi8TaJJY3Gyw.ico')

#переменная кнопки которая лежит в функции
open_file = ""
lic = None
contvert_b = None
Resize_image_b = None
#функция главного меню
def menu():
	global open_file, lic, contvert_b, Resize_image_b

	open_file = Label(text = "📷 Edit photo", bd = 3, relief = "solid", font = "arial 30", width = 20)

	open_file.place(relx = 0.38, rely = 0.6, height = 75)

	contvert_b = Label(text = " 📁 Сonvention photo ", bd = 3, relief = "solid", font = "arial 30", width = 20)

	contvert_b.place(relx = 0.38, rely = 0.4, height = 75)

	Resize_image_b = Label(text = " 🛠 Resize photo ", bd = 3, relief = "solid", font = "arial 30", width = 20)

	Resize_image_b.place(relx = 0.38, rely = 0.5, height = 75)



	

	lic = Label(text = "License: GPL\nPhotoEdit 1.2 BETA\nCreator: SayHelloRoman", justify = RIGHT)
	lic.pack(side = RIGHT, anchor = S)


write_e_w = None
write_e_h = None
img55 = None
image_name1 = None

def Resize_image_d(da):
	global write_e_w, write_e_h, img55, image_name1

	

	image_name1 = fd.askopenfilename(filetypes=(("Image Files", "*.png *.jpg *.jpeg *.TIFF *.bmp *.dib"),
	("All files", "*.*") ))

	if image_name1 != "":

		window = Toplevel(root)
		window.title("Resize photo")
		window.resizable(width = False, height = False)
		window.geometry("500x500")
		window.iconbitmap('BYclT2IXMGpi8TaJJY3Gyw.ico')

		img55 = Image.open(image_name1)

		width, height = img55.size

		Current_width = Label(window, text = f"Current width = {width}", font = "arial 30")
		Current_width.pack()
		Current_height = Label(window, text = f"Current height = {height}", font = "arial 30")
		Current_height.pack()

		write_l_w = Label(window, text = "New width  = ", font = "arial 30")
		write_l_h = Label(window, text = "New height = ", font = "arial 30")

		write_l_w.place(rely = 0.3, relx = 0.01)
		write_l_h.place(rely = 0.45, relx = 0.01)

		write_e_w = Entry(window,font = "arial 30", width = 8)
		write_e_h = Entry(window,font = "arial 30", width = 8)

		write_e_w.place(rely = 0.3, relx = 0.5)
		write_e_h.place(rely = 0.45, relx = 0.5)

		save_b = Button(window, text = "Save", bd = 1, relief = "solid", font = "arial 30")
		save_b.place(rely = 0.8, relx = 0.4)

		def save_rise(d):
			global write_e_w, write_e_h, img55, image_name1

			new_height = write_e_h.get()
			new_width = write_e_w.get()

			save_name= fd.asksaveasfilename()

			img = Image.open(image_name1)

			img = img.resize((int(new_width), int(new_height)), Image.ANTIALIAS)


			img.save(save_name+".png", "png")





			window.withdraw()
		save_b.bind("<Button-1>", save_rise)
	elif image_name1 == "":
		messagebox.showerror(title="Error", message="You have not selected a photo")


image_name = None
def convert(d):

	global open_file, lic, information, contvert_b, image_name


	image_name = fd.askopenfilename(filetypes=(("Image Files", "*.png *.jpg *.jpeg *.TIFF *.bmp *.dib"),
	("All files", "*.*") ))

	if image_name != "":

		window = Toplevel(root)
		window.title("Convert")
		window.resizable(width = False, height = False)
		window.geometry("500x500")
		window.iconbitmap('BYclT2IXMGpi8TaJJY3Gyw.ico')


		b_to_png = Button(window, text = "To PNG", font = "arial 30", bd = 2, relief = "solid", width = 20)
		b_to_jpeg = Button(window,text = "To JPG", font = "arial 30", bd = 2, relief = "solid", width = 20)
		b_to_TIFF = Button(window,text = "To TIFF", font = "arial 30", bd = 2, relief = "solid", width = 20)
		b_to_bmp = Button(window,text = "To BMP", font = "arial 30", bd = 2, relief = "solid", width = 20)
		b_to_pdf = Button(window,text = "To PDF", font = "arial 30", bd = 2, relief = "solid", width = 20)

		b_to_png.pack(pady = 8, padx = 8)
		b_to_jpeg.pack(pady = 8, padx = 8)
		b_to_TIFF.pack(pady = 8, padx = 8)
		b_to_bmp.pack(pady = 8, padx = 8)
		b_to_pdf.pack(pady = 8, padx = 8)

		def to_png(с):
			global image_name

			save_name= fd.asksaveasfilename()

			img = Image.open(image_name)



			img.save(save_name+".png", "png")

			window.withdraw()


		def to_jpeg(с):
			global image_name

			#f = Image.open(image_name, 'r')

			#b_to_png.save("Convert.png", 'png')
			save_name= fd.asksaveasfilename()

			img = Image.open(image_name)

			img = img.convert('RGB')


			img.save(save_name+".jpeg", "jpeg")

			window.withdraw()

		def to_TIFF(с):
			global image_name

			save_name= fd.asksaveasfilename()

			img = Image.open(image_name)

			img.save(save_name+".tiff", "tiff")

			window.withdraw()
			
		def to_bmp(с):
			global image_name

			save_name= fd.asksaveasfilename()

			img = Image.open(image_name)

			img.save(save_name+".bmp", "bmp")


			window.withdraw()

		def to_pdf(с):
			global image_name

			save_name= fd.asksaveasfilename()

			img = Image.open(image_name)

			img.save(save_name+".pdf", "pdf")

			window.withdraw()




		b_to_png.bind("<Button-1>", to_png)
		b_to_jpeg.bind("<Button-1>", to_jpeg)
		b_to_TIFF.bind("<Button-1>", to_TIFF)
		b_to_bmp.bind("<Button-1>", to_bmp)
		b_to_pdf.bind("<Button-1>", to_pdf)
	elif image_name == "":
		messagebox.showerror(title="Error", message="You have not selected a photo")



#функция редактировки изображения
img = ""
Image_main = ""
file_name = ""
save_kak = 0
Name_file_entry = ""
img2 = ""
width1 = None
height1 = None
img3 = None
def edit(bind):
	global img, Image_main, root, file_name, save_kak, Name_file_entry, img2, lic, width1, height1, Resize_image_b

	
	#открываем изображение

	file_name = fd.askopenfilename(filetypes=(("Image Files", "*.png *.jpeg *.tiff *.bmp*.jpef *.jpg"),
	("Your format", "*")))

	if file_name != "":
	
		#уничтожаем кнопку 
		open_file.place_forget()
		lic.pack_forget()
		contvert_b.place_forget()
		Resize_image_b.place_forget()
		#функция save
		def save_():
			global img2, save_kak,Name_file_entry, img, contvert_b, img3, Image_main


			

			save_name= fd.asksaveasfilename(initialfile = "File.png",filetypes=(("PNG", "*.png"),("JPEG", "*.jpeg"),("TIFF", "*.tiff"),("BMP", "*.bmp")), defaultextension='.png')

			width1, height1 = img.size
			
			img2 = img2.resize((int(width1), int(height1)), Image.ANTIALIAS)

			img2.save(save_name, "png")	


			img2 = img
			width1, height1 = img2.size
			if width1 >= 900:
				width1 = width1 / 2
				height1 = height1 / 2
				img2 = img2.resize((int(width1), int(height1)), Image.ANTIALIAS)

			if height1 >= 900:
				height1 = height1 / 2
				width1 = width1 / 2
				img2 = img2.resize((int(width1), int(height1)), Image.ANTIALIAS)
			imgTK = ImageTk.PhotoImage(img2)
			Image_main["image"] = imgTK

			blur_button["bg"] = "gray"
			Drawn_button['bg'] = "gray"
			Contour_button['bg'] = "gray"
			FIND_EDGES_button['bg'] = "gray"
			GrayScale_button['bg'] = "gray"
			negative_button['bg'] = "gray"
			SHARPEN_button['bg'] = "gray"
			DETAIL_button['bg'] = "gray"
			EMBOSS_button['bg'] = "gray"
			SMOOTH_MORE_button["bg"] = "gray"


			Image_main.image = imgTK

			

		


		#добавляем виджет menu
		mainmenu = Menu(root) 
		
		filemenu = Menu(mainmenu, tearoff=0)

		filemenu.add_command(label="Save", command = save_)

		mainmenu.add_cascade(label="File", menu=filemenu)

		root.config(menu=mainmenu)


		




		img = Image.open(file_name)
		img2 = img
		img3 = img

		img2 = img2.convert('RGB')

		width1, height1 = img2.size

		if width1 >= 900:
			width1 = width1 / 2
			height1 = height1 / 2

		if height1 >= 900:
			height1 = height1 / 2
			width1 = width1 / 2

		img2 = img2.resize((int(width1), int(height1)), Image.ANTIALIAS)

		imgTK = ImageTk.PhotoImage(img2)

		width, height = img.size
		width_height = Label(text = f"Size: {width}x{height}")

		#делаем label с изображением
		Image_main = Label(image = imgTK, bd = 1, relief = "solid", width = 900, height = 900)

		Image_main.image = imgTK

		Image_main.place(relx = 0.25, rely = 0.05)
		width_height.place(relx = 0.25, rely = 0.03)

		#blur
		blur_button = Button(text = "BLUR", font = "Arial 12", bd = 1, relief = "solid", width = 12, bg = "gray", fg = "white")
		blur_button.pack(anchor=NW)

		def blur_im(blur):
			global img2, Image_main, save_kak
			

			img2 = img2.filter(GaussianBlur(radius=10))


			blur_button["bg"] = "black"


			imgTK1 = ImageTk.PhotoImage(img2)

			Image_main["image"] = imgTK1
			Image_main.image = imgTK1
			save_kak = 1
		blur_button.bind("<Button-1>", blur_im)

		#Рисованный
		Drawn_button = Button(text = "Drawn", font = "Arial 12", bd = 1, relief = "solid", width = 12, bg = "gray", fg = "white")
		Drawn_button.pack(anchor=NW)

		def ModeFilter_im(blur):
			global img2, Image_main, save_kak


			img2 = img2.filter(ModeFilter(size=9))

			imgTK2 = ImageTk.PhotoImage(img2)


			Drawn_button['bg'] = "black"



			Image_main["image"] = imgTK2
			Image_main.image = imgTK2
			save_kak = 2
		Drawn_button.bind("<Button-1>", ModeFilter_im)

		#Контурный
		Contour_button = Button(text = "Contour", font = "Arial 12", bd = 1, relief = "solid", width = 12, bg = "gray", fg = "white")
		Contour_button.pack(anchor=NW)

		def Contour_im(blur):
			global img2, Image_main, save_kak
			

			img2 = img2.filter(CONTOUR())



			Contour_button['bg'] = "black"



			imgTK3 = ImageTk.PhotoImage(img2)

			Image_main["image"] = imgTK3
			Image_main.image = imgTK3
			save_kak = 3
		Contour_button.bind("<Button-1>", Contour_im)

		#Темный
		FIND_EDGES_button = Button(text = "Find Edges", font = "Arial 12", bd = 1, relief = "solid", width = 12, bg = "gray", fg = "white")
		FIND_EDGES_button.pack(anchor=NW)

		def FIND_EDGES_im(blur):
			global img2, Image_main, save_kak
			

			img2 = img2.filter(FIND_EDGES())

			imgTK4 = ImageTk.PhotoImage(img2)



			FIND_EDGES_button['bg'] = "black"


			Image_main["image"] = imgTK4
			Image_main.image = imgTK4
			save_kak = 4
		FIND_EDGES_button.bind("<Button-1>", FIND_EDGES_im)

		GrayScale_button = Button(text = "Gray", font = "Arial 12", bd = 1, relief = "solid", width = 12, bg = "gray", fg = "white")
		GrayScale_button.pack(anchor=NW)

		def GrayScale_(blur):
			global img2, Image_main, save_kak
			

			img2 = img2.convert('LA')

			imgTK4 = ImageTk.PhotoImage(img2)



			GrayScale_button['bg'] = "black"

			img2 = img2.convert('RGB')



			Image_main["image"] = imgTK4
			Image_main.image = imgTK4
			save_kak = 5
		GrayScale_button.bind("<Button-1>", GrayScale_)


		negative_button = Button(text = "Negative", font = "Arial 12", bd = 1, relief = "solid", width = 12, bg = "gray", fg = "white")
		negative_button.pack(anchor=NW)
		def negative_(blur):
			global img2, Image_main, save_kak
			


			img2 = ImageOps.invert(img2)


			negative_button['bg'] = "black"


			imgTK4 = ImageTk.PhotoImage(img2)

			Image_main["image"] = imgTK4
			Image_main.image = imgTK4
			save_kak = 6
		negative_button.bind("<Button-1>", negative_)

		DETAIL_button = Button(text = "Detail", font = "Arial 12", bd = 1, relief = "solid", width = 12, bg = "gray", fg = "white")
		DETAIL_button.pack(anchor=NW)
		def DETAIL_(blur):
			global img2, Image_main, save_kak
			

			img2 = img2.filter(DETAIL())

			
			DETAIL_button['bg'] = "black"
			
			imgTK4 = ImageTk.PhotoImage(img2)

			Image_main["image"] = imgTK4
			Image_main.image = imgTK4
			save_kak = 7
		DETAIL_button.bind("<Button-1>", DETAIL_)


		SHARPEN_button = Button(text = "Sharpen", font = "Arial 12", bd = 1, relief = "solid", width = 12, bg = "gray", fg = "white")
		SHARPEN_button.pack(anchor=NW)

		def SHARPEN_(blur):
			global img2, Image_main, save_kak
			 

			img2 = img2.filter(SHARPEN())

			
			SHARPEN_button['bg'] = "black"
			


			imgTK4 = ImageTk.PhotoImage(img2)

			Image_main["image"] = imgTK4
			Image_main.image = imgTK4
			save_kak = 8
		SHARPEN_button.bind("<Button-1>", SHARPEN_)

		EMBOSS_button = Button(text = "Emboss", font = "Arial 12", bd = 1, relief = "solid", width = 12, bg = "gray", fg = "white")
		EMBOSS_button.pack(anchor=NW)

		def EMBOSS_(blur):
			global img2, Image_main, save_kak
				 

			img2 = img2.filter(EMBOSS())

				
			EMBOSS_button['bg'] = "black"
				

			imgTK4 = ImageTk.PhotoImage(img2)

			Image_main["image"] = imgTK4
			Image_main.image = imgTK4
			save_kak = 9
		EMBOSS_button.bind("<Button-1>", EMBOSS_)

		SMOOTH_MORE_button = Button(text = "Smooth", font = "Arial 12", bd = 1, relief = "solid", width = 12, bg = "gray", fg = "white")
		SMOOTH_MORE_button.pack(anchor=NW)

		def SMOOTH_MORE_(blur):
			global img2, Image_main, save_kak
			 

			img2 = img2.filter(SMOOTH_MORE())

			
			SMOOTH_MORE_button["bg"] = "black"

			imgTK4 = ImageTk.PhotoImage(img2)

			Image_main["image"] = imgTK4
			Image_main.image = imgTK4
			save_kak = 10
		SMOOTH_MORE_button.bind("<Button-1>", SMOOTH_MORE_)



		reset_button = Button(text = "Reset", font = "Arial 12", bd = 1, relief = "solid", width = 12, bg = "gray", fg = "white")
		#reset_button.pack(anchor=W, side = BOTTOM)

		def reset(blur):
			global img, Image_main, save_kak, img2
			img2 = img
			width1, height1 = img2.size
			if width1 >= 900:
				width1 = width1 / 2
				height1 = height1 / 2
				img2 = img2.resize((int(width1), int(height1)), Image.ANTIALIAS)

			if height1 >= 900:
				height1 = height1 / 2
				width1 = width1 / 2
				img2 = img2.resize((int(width1), int(height1)), Image.ANTIALIAS)
			imgTK = ImageTk.PhotoImage(img2)
			Image_main["image"] = imgTK

			blur_button["bg"] = "gray"
			Drawn_button['bg'] = "gray"
			Contour_button['bg'] = "gray"
			FIND_EDGES_button['bg'] = "gray"
			GrayScale_button['bg'] = "gray"
			negative_button['bg'] = "gray"
			SHARPEN_button['bg'] = "gray"
			DETAIL_button['bg'] = "gray"
			EMBOSS_button['bg'] = "gray"
			SMOOTH_MORE_button["bg"] = "gray"


			Image_main.image = imgTK
			save_kak = 0
		reset_button.bind("<Button-1>", reset)

		size_p = Button(text = "+", font = "Arial 12", bd = 1, relief = "solid", width = 12, bg = "gray", fg = "white")
		#size_p.pack(anchor=W, side = BOTTOM)

		def plus_im(b):
			global img2
			width, height = img2.size
			img2 = img2.resize((width + 50 , height + 50), Image.ANTIALIAS)
			imgTK = ImageTk.PhotoImage(img2)
			Image_main["image"] = imgTK




			Image_main.image = imgTK
		size_p.bind("<Button-1>", plus_im)



		size_m = Button(text = "-", font = "Arial 12", bd = 1, relief = "solid", width = 12, bg = "gray", fg = "white")
		size_m.pack(anchor=W, side = BOTTOM)
		size_p.pack(anchor=W, side = BOTTOM)
		reset_button.pack(anchor=W, side = BOTTOM)

		def minus_im(b):
			global img2
			width, height = img2.size
			img2 = img2.resize((width - 50 , height - 50), Image.ANTIALIAS)
			imgTK = ImageTk.PhotoImage(img2)
			Image_main["image"] = imgTK




			Image_main.image = imgTK
		size_m.bind("<Button-1>", minus_im)
	elif file_name == "":
		messagebox.showerror(title="Error", message="You have not selected a photo")

menu()




open_file.bind("<Button-1>", edit)
contvert_b.bind("<Button-1>", convert)
Resize_image_b.bind("<Button-1>", Resize_image_d)


#за то работает

root.mainloop()