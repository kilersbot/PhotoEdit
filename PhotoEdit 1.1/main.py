from tkinter import filedialog as fd
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
root.title("Photoedit")
root.minsize( width = 1600, height = 900 )
root.maxsize( width = 2560, height = 1440 )
root.geometry("1600x900+70+10")
root.iconbitmap('BYclT2IXMGpi8TaJJY3Gyw.ico')

#переменная кнопки которая лежит в функции
open_file = ""
lic = None
information = None
contvert_b = None
Resize_image_b = None
#функция главного меню
def menu():
	global open_file, lic, information, contvert_b, Resize_image_b

	open_file = Button(text = "📷 Edit photo", bd = 3, relief = "solid", font = "arial 30")

	open_file.place(relx = 0.4, rely = 0.6)

	contvert_b = Label(text = " 📁 Сonvention photo ", bd = 3, relief = "solid", font = "arial 30")

	contvert_b.place(relx = 0.4, rely = 0.4, height = 75)

	Resize_image_b = Label(text = " 🛠 Resize photo ", bd = 3, relief = "solid", font = "arial 30")

	Resize_image_b.place(relx = 0.4, rely = 0.5, height = 75)


	information = Label(text = "❗", bd = 2, relief = "solid", font = "arial 30", width = 2, height = 2)

	

	lic = Label(text = "Photoedit 1.1 BETA")
	lic.pack(side = RIGHT, anchor = S)
	information.pack(side = BOTTOM, anchor = W)

	def info(b):
		window = Toplevel(root)
		window.title("Information")
		window.resizable(width = False, height = False)
		window.geometry("300x150")
		window.iconbitmap('BYclT2IXMGpi8TaJJY3Gyw.ico')

		info_text = Label(window, text = "Photoedit 1.1 BETA", font = "Arial 25")
		Creator = Label(window, text = "Creator: Raikage", font = "Arial 25")
		license = Label(window, text = "license GPL", font = "Arial 25")


		info_text.pack()
		Creator.pack()
		license.pack()

	information.bind("<Button-1>", info)

write_e_w = None
write_e_h = None
img55 = None
image_name1 = None
def Resize_image_d(da):
	global write_e_w, write_e_h, img55, image_name1
	image_name1 = fd.askopenfilename(filetypes=(("Image Files", "*.png *.jpg *.jpeg *.TIFF *.bmp *.dib"),
	("All files", "*.*") ))


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


image_name = None
def convert(d):

	global open_file, lic, information, contvert_b, image_name


	image_name = fd.askopenfilename(filetypes=(("Image Files", "*.png *.jpg *.jpeg *.TIFF *.bmp *.dib"),
	("All files", "*.*") ))

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




#функция редактировки изображения
img = ""
Image_main = ""
file_name = ""
save_kak = 0
Name_file_entry = ""
img2 = ""
width1 = None
height1 = None
def edit(bind):
	global img, Image_main, root, file_name, save_kak, Name_file_entry, img2, lic, width1, height1, Resize_image_b


	#функция save
	def save_():
		global img2, save_kak,Name_file_entry, img, information, contvert_b
		window = Toplevel(root)
		window.title("Save")
		window.resizable(width = False, height = False)
		window.geometry("400x200")
		window.iconbitmap('w256h2561339195982Save256x256.ico')

		Name_file = Label(window,text = "Name file:", font = "arial 20")
		Name_file_entry = Entry(window,font = "arial 20", width = 15)
		def dire(nb):
			cd = fd.askdirectory()
			os.chdir(cd)
			print(os.getcwd())

		def save_ima(nb):
			global img, Name_file_entry

			img1 = img

			if save_kak == 0:
				img1.save(Name_file_entry.get()+".png", 'png')
			elif save_kak == 1:
				img1 = img1.filter(GaussianBlur(radius=10))
				img1.save(Name_file_entry.get()+".png", 'png')
			elif save_kak == 2:
				img1 = img1.filter(ModeFilter(size=9))
				img1.save(Name_file_entry.get()+".png", 'png')
			elif save_kak == 3:
				img1 = img1.filter(CONTOUR())
				img1.save(Name_file_entry.get()+".png", 'png')
			elif save_kak == 4:
				img1 = img1.filter(FIND_EDGES())
				img1.save(Name_file_entry.get()+".png", 'png')
			elif save_kak == 5:
				img1 = img1.convert('L')
				img1.save(Name_file_entry.get()+".png", 'png')
			elif save_kak == 6:
				img1 = img1.convert('RGB')

				img1 = ImageOps.invert(img1)

				img1.save(Name_file_entry.get()+".png", 'png')

				img1 = ImageOps.invert(img1)
			elif save_kak == 7:
				img1 = img1.filter(DETAIL())
				img1.save(Name_file_entry.get()+".png", 'png')
			elif save_kak == 8:
				img1 = img1.filter(SHARPEN())
				img1.save(Name_file_entry.get()+".png", 'png')
			elif save_kak == 9:
				img1 = img1.filter(EMBOSS())
				img1.save(Name_file_entry.get()+".png", 'png')
			elif save_kak == 10:
				img1 = img1.filter(SMOOTH_MORE())
				img1.save(Name_file_entry.get()+".png", 'png')


			blur_button["bg"] = "gray"
			Drawn_button['bg'] = "gray"
			Contour_button['bg'] = "gray"
			FIND_EDGES_button['bg'] = "gray"
			GrayScale_button['bg'] = "gray"
			negative_button['bg'] = "gray"
			SHARPEN_button['bg'] = "gray"
			DETAIL_button['bg'] = "gray"
			EMBOSS_button['bg'] = "gray"

			window.withdraw()

		Directoriy = Button(window, font = "arial 15", width = 15, text = "Directory", bd = 3, relief = "solid")

		Button_save = Button(window, font = "arial 15", width = 15, text = "Save", bd = 3, relief = "solid")

		Button_save.pack(side = BOTTOM)
		Directoriy.place(x = 110, y = 60)
		Name_file.place(x = 0, y = 0)
		Name_file_entry.place(y = 0, x = 130)

		Directoriy.bind("<Button-1>", dire)
		Button_save.bind("<Button-1>", save_ima)


	#добавляем виджет menu
	mainmenu = Menu(root) 
	
	filemenu = Menu(mainmenu, tearoff=0)

	filemenu.add_command(label="Save", command = save_)

	mainmenu.add_cascade(label="File", menu=filemenu)

	root.config(menu=mainmenu)


	#уничтожаем кнопку 
	open_file.place_forget()
	lic.pack_forget()
	information.pack_forget()
	contvert_b.place_forget()
	Resize_image_b.place_forget()
	#открываем изображение
	file_name = fd.askopenfilename(filetypes=(("Image Files", "*.png *.jpg"),
	("All files", "*.*") ))




	img = Image.open(file_name)
	img2 = img

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
	width_height = Label(text = f"X = {width}; Y = {height}")

	#делаем label с изображением
	Image_main = Label(image = imgTK, bd = 1, relief = "solid", width = 700, height = 700)

	Image_main.image = imgTK

	Image_main.place(relx = 0.3, rely = 0.2)
	width_height.place(relx = 0.3, rely = 0.18)

	#blur
	blur_button = Button(text = "BLUR", font = "Arial 12", bd = 1, relief = "solid", width = 12, bg = "gray", fg = "white")
	blur_button.pack(anchor=NW)

	def blur_im(blur):
		global img2, Image_main, save_kak
		img_blur = img2

		dimg = img_blur.filter(GaussianBlur(radius=10))


		blur_button["bg"] = "black"
		Drawn_button['bg'] = "gray"
		Contour_button['bg'] = "gray"
		FIND_EDGES_button['bg'] = "gray"
		GrayScale_button['bg'] = "gray"
		negative_button['bg'] = "gray"
		SHARPEN_button['bg'] = "gray"
		DETAIL_button['bg'] = "gray"
		EMBOSS_button['bg'] = "gray"
		SMOOTH_MORE_button["bg"] = "gray"

		imgTK1 = ImageTk.PhotoImage(dimg)

		Image_main["image"] = imgTK1
		Image_main.image = imgTK1
		save_kak = 1
	blur_button.bind("<Button-1>", blur_im)

	#Рисованный
	Drawn_button = Button(text = "Drawn", font = "Arial 12", bd = 1, relief = "solid", width = 12, bg = "gray", fg = "white")
	Drawn_button.pack(anchor=NW)

	def ModeFilter_im(blur):
		global img2, Image_main, save_kak
		img_ModeFilter = img2

		dimg = img_ModeFilter.filter(ModeFilter(size=9))

		imgTK2 = ImageTk.PhotoImage(dimg)

		blur_button["bg"] = "gray"
		Drawn_button['bg'] = "black"
		Contour_button['bg'] = "gray"
		FIND_EDGES_button['bg'] = "gray"
		GrayScale_button['bg'] = "gray"
		negative_button['bg'] = "gray"
		SHARPEN_button['bg'] = "gray"
		DETAIL_button['bg'] = "gray"
		EMBOSS_button['bg'] = "gray"
		SMOOTH_MORE_button["bg"] = "gray"


		Image_main["image"] = imgTK2
		Image_main.image = imgTK2
		save_kak = 2
	Drawn_button.bind("<Button-1>", ModeFilter_im)

	#Контурный
	Contour_button = Button(text = "Contour", font = "Arial 12", bd = 1, relief = "solid", width = 12, bg = "gray", fg = "white")
	Contour_button.pack(anchor=NW)

	def Contour_im(blur):
		global img2, Image_main, save_kak
		img_Contour = img2

		dimg = img_Contour.filter(CONTOUR())


		blur_button["bg"] = "gray"
		Drawn_button['bg'] = "gray"
		Contour_button['bg'] = "black"
		FIND_EDGES_button['bg'] = "gray"
		GrayScale_button['bg'] = "gray"
		negative_button['bg'] = "gray"
		SHARPEN_button['bg'] = "gray"
		DETAIL_button['bg'] = "gray"
		EMBOSS_button['bg'] = "gray"
		SMOOTH_MORE_button["bg"] = "gray"


		imgTK3 = ImageTk.PhotoImage(dimg)

		Image_main["image"] = imgTK3
		Image_main.image = imgTK3
		save_kak = 3
	Contour_button.bind("<Button-1>", Contour_im)

	#Темный
	FIND_EDGES_button = Button(text = "Find Edges", font = "Arial 12", bd = 1, relief = "solid", width = 12, bg = "gray", fg = "white")
	FIND_EDGES_button.pack(anchor=NW)

	def FIND_EDGES_im(blur):
		global img2, Image_main, save_kak
		img_FIND_EDGES = img2

		dimg = img_FIND_EDGES.filter(FIND_EDGES())

		imgTK4 = ImageTk.PhotoImage(dimg)

		blur_button["bg"] = "gray"
		Drawn_button['bg'] = "gray"
		Contour_button['bg'] = "gray"
		FIND_EDGES_button['bg'] = "black"
		GrayScale_button['bg'] = "gray"
		negative_button['bg'] = "gray"
		SHARPEN_button['bg'] = "gray"
		DETAIL_button['bg'] = "gray"
		EMBOSS_button['bg'] = "gray"
		SMOOTH_MORE_button["bg"] = "gray"

		Image_main["image"] = imgTK4
		Image_main.image = imgTK4
		save_kak = 4
	FIND_EDGES_button.bind("<Button-1>", FIND_EDGES_im)

	GrayScale_button = Button(text = "Gray", font = "Arial 12", bd = 1, relief = "solid", width = 12, bg = "gray", fg = "white")
	GrayScale_button.pack(anchor=NW)

	def GrayScale_(blur):
		global img2, Image_main, save_kak
		img_FIND_EDGES = img2

		img_FIND_EDGES = img_FIND_EDGES.convert('L')

		imgTK4 = ImageTk.PhotoImage(img_FIND_EDGES)

		blur_button["bg"] = "gray"
		Drawn_button['bg'] = "gray"
		Contour_button['bg'] = "gray"
		FIND_EDGES_button['bg'] = "gray"
		GrayScale_button['bg'] = "black"
		negative_button['bg'] = "gray"
		SHARPEN_button['bg'] = "gray"
		DETAIL_button['bg'] = "gray"
		EMBOSS_button['bg'] = "gray"
		SMOOTH_MORE_button["bg"] = "gray"


		Image_main["image"] = imgTK4
		Image_main.image = imgTK4
		save_kak = 5
	GrayScale_button.bind("<Button-1>", GrayScale_)


	negative_button = Button(text = "Negative", font = "Arial 12", bd = 1, relief = "solid", width = 12, bg = "gray", fg = "white")
	negative_button.pack(anchor=NW)
	def negative_(blur):
		global img2, Image_main, save_kak
		img_FIND_EDGES = img2

		img_FIND_EDGES = img_FIND_EDGES.convert('RGB')

		img_FIND_EDGES = ImageOps.invert(img_FIND_EDGES)

		blur_button["bg"] = "gray"
		Drawn_button['bg'] = "gray"
		Contour_button['bg'] = "gray"
		FIND_EDGES_button['bg'] = "gray"
		GrayScale_button['bg'] = "gray"
		negative_button['bg'] = "black"
		SHARPEN_button['bg'] = "gray"
		DETAIL_button['bg'] = "gray"
		EMBOSS_button['bg'] = "gray"
		SMOOTH_MORE_button["bg"] = "gray"

		imgTK4 = ImageTk.PhotoImage(img_FIND_EDGES)

		Image_main["image"] = imgTK4
		Image_main.image = imgTK4
		save_kak = 6
	negative_button.bind("<Button-1>", negative_)

	DETAIL_button = Button(text = "Detail", font = "Arial 12", bd = 1, relief = "solid", width = 12, bg = "gray", fg = "white")
	DETAIL_button.pack(anchor=NW)
	def DETAIL_(blur):
		global img2, Image_main, save_kak
		img_FIND_EDGES = img2

		dimg = img_FIND_EDGES.filter(DETAIL())

		blur_button["bg"] = "gray"
		Drawn_button['bg'] = "gray"
		Contour_button['bg'] = "gray"
		FIND_EDGES_button['bg'] = "gray"
		GrayScale_button['bg'] = "gray"
		negative_button['bg'] = "gray"
		SHARPEN_button['bg'] = "gray"
		DETAIL_button['bg'] = "black"
		EMBOSS_button['bg'] = "gray"
		SMOOTH_MORE_button["bg"] = "gray"
		imgTK4 = ImageTk.PhotoImage(dimg)

		Image_main["image"] = imgTK4
		Image_main.image = imgTK4
		save_kak = 7
	DETAIL_button.bind("<Button-1>", DETAIL_)


	SHARPEN_button = Button(text = "Sharpen", font = "Arial 12", bd = 1, relief = "solid", width = 12, bg = "gray", fg = "white")
	SHARPEN_button.pack(anchor=NW)

	def SHARPEN_(blur):
		global img2, Image_main, save_kak
		img_FIND_EDGES = img2

		dimg = img_FIND_EDGES.filter(SHARPEN())

		blur_button["bg"] = "gray"
		Drawn_button['bg'] = "gray"
		Contour_button['bg'] = "gray"
		FIND_EDGES_button['bg'] = "gray"
		GrayScale_button['bg'] = "gray"
		negative_button['bg'] = "gray"
		SHARPEN_button['bg'] = "black"
		DETAIL_button['bg'] = "gray"
		EMBOSS_button['bg'] = "gray"
		SMOOTH_MORE_button["bg"] = "gray"


		imgTK4 = ImageTk.PhotoImage(dimg)

		Image_main["image"] = imgTK4
		Image_main.image = imgTK4
		save_kak = 8
	SHARPEN_button.bind("<Button-1>", SHARPEN_)

	EMBOSS_button = Button(text = "Emboss", font = "Arial 12", bd = 1, relief = "solid", width = 12, bg = "gray", fg = "white")
	EMBOSS_button.pack(anchor=NW)

	def EMBOSS_(blur):
		global img2, Image_main, save_kak
		img_FIND_EDGES = img2

		dimg = img_FIND_EDGES.filter(EMBOSS())

		blur_button["bg"] = "gray"
		Drawn_button['bg'] = "gray"
		Contour_button['bg'] = "gray"
		FIND_EDGES_button['bg'] = "gray"
		GrayScale_button['bg'] = "gray"
		negative_button['bg'] = "gray"
		SHARPEN_button['bg'] = "gray"
		DETAIL_button['bg'] = "gray"
		EMBOSS_button['bg'] = "black"
		SMOOTH_MORE_button["bg"] = "gray"

		imgTK4 = ImageTk.PhotoImage(dimg)

		Image_main["image"] = imgTK4
		Image_main.image = imgTK4
		save_kak = 9
	EMBOSS_button.bind("<Button-1>", EMBOSS_)

	SMOOTH_MORE_button = Button(text = "Smooth", font = "Arial 12", bd = 1, relief = "solid", width = 12, bg = "gray", fg = "white")
	SMOOTH_MORE_button.pack(anchor=NW)

	def SMOOTH_MORE_(blur):
		global img2, Image_main, save_kak
		img_FIND_EDGES = img2

		dimg = img_FIND_EDGES.filter(SMOOTH_MORE())

		blur_button["bg"] = "gray"
		Drawn_button['bg'] = "gray"
		Contour_button['bg'] = "gray"
		FIND_EDGES_button['bg'] = "gray"
		GrayScale_button['bg'] = "gray"
		negative_button['bg'] = "gray"
		SHARPEN_button['bg'] = "gray"
		DETAIL_button['bg'] = "gray"
		EMBOSS_button['bg'] = "gray"
		SMOOTH_MORE_button["bg"] = "black"

		imgTK4 = ImageTk.PhotoImage(dimg)

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
	size_m.bind("<Button-1>", minus_im)

menu()




open_file.bind("<Button-1>", edit)
contvert_b.bind("<Button-1>", convert)
Resize_image_b.bind("<Button-1>", Resize_image_d)


#за то работает

root.mainloop()
