#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Sep 22, 2017 03:12:54 AM
import sys, programz, time

import threads # module gui threds
import threading #for threads module
import queue # to create the queue object
import concurrent.futures
import os
import re
import requests

try:
    from Tkinter import *
except ImportError:
    from tkinter import *
    from tkinter import filedialog

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import main_window_support

def main():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    main_window_support.set_Tk_var()
    top = New_Toplevel_1 (root)
    main_window_support.init(root, top)
    top.get_boards()
    root.mainloop()

w = None
def create_New_Toplevel_1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    main_window_support.set_Tk_var()
    top = New_Toplevel_1 (w)
    main_window_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None


class New_Toplevel_1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font9 = "-family {Segoe UI} -size 13 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("496x843+671+49")
        top.title("4Chan Downloader")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.board_frame = Frame(top)
        self.board_frame.place(relx=0.02, rely=0.01, relheight=0.52
                , relwidth=0.96)
        self.board_frame.configure(relief=GROOVE)
        self.board_frame.configure(borderwidth="2")
        self.board_frame.configure(relief=GROOVE)
        self.board_frame.configure(background="#d9d9d9")
        self.board_frame.configure(highlightbackground="#d9d9d9")
        self.board_frame.configure(highlightcolor="black")
        self.board_frame.configure(width=475)

        self.boards_list = ScrolledListBox(self.board_frame, exportselection=0)
        self.boards_list.place(relx=0.02, rely=0.02, relheight=0.95
                , relwidth=0.97)
        self.boards_list.configure(background="white")
        self.boards_list.configure(disabledforeground="#a3a3a3")
        self.boards_list.configure(font="TkFixedFont")
        self.boards_list.configure(foreground="black")
        self.boards_list.configure(highlightbackground="#d9d9d9")
        self.boards_list.configure(highlightcolor="#d9d9d9")
        self.boards_list.configure(selectbackground="#c4c4c4")
        self.boards_list.configure(selectforeground="black")
        self.boards_list.configure(width=10)
        self.boards_list.insert(END, "Getting Boards List....")


        self.start_run = Button(top, command = self.start_the_gattering)
        self.start_run.place(relx=0.12, rely=0.93, height=44, width=97)
        self.start_run.configure(activebackground="#d9d9d9")
        self.start_run.configure(activeforeground="#000000")
        self.start_run.configure(background="#d9d9d9")
        self.start_run.configure(disabledforeground="#a3a3a3")
        self.start_run.configure(foreground="#000000")
        self.start_run.configure(highlightbackground="#d9d9d9")
        self.start_run.configure(highlightcolor="#000000")
        self.start_run.configure(pady="0")
        self.start_run.configure(text='''START''')
        self.start_run.configure(width=97)


        self.Open_board = Button(top, command = self.get_threads)
        self.Open_board.place(relx=0.02, rely=0.53, height=44, width=77)
        self.Open_board.configure(activebackground="#d9d9d9")
        self.Open_board.configure(activeforeground="#000000")
        self.Open_board.configure(background="#d9d9d9")
        self.Open_board.configure(disabledforeground="#a3a3a3")
        self.Open_board.configure(foreground="#000000")
        self.Open_board.configure(highlightbackground="#d9d9d9")
        self.Open_board.configure(highlightcolor="black")
        self.Open_board.configure(pady="0")
        self.Open_board.configure(text='''Open Board''')
        self.Open_board.configure(width=77)


        self.status_label = Label(top)
        self.status_label.place(relx=0.03, rely=0.63, height=41, width=174)
        self.status_label.configure(activebackground="#f9f9f9")
        self.status_label.configure(activeforeground="black")
        self.status_label.configure(background="#d9d9d9")
        self.status_label.configure(disabledforeground="#a3a3a3")
        self.status_label.configure(font=font9)
        self.status_label.configure(foreground="#000000")
        self.status_label.configure(highlightbackground="#d9d9d9")
        self.status_label.configure(highlightcolor="black")
        self.status_label.configure(text='''STOP''')
        self.status_label.configure(width=174)

        self.status_frame = Frame(top)
        self.status_frame.place(relx=0.04, rely=0.69, relheight=0.22
                , relwidth=0.35)
        self.status_frame.configure(relief=GROOVE)
        self.status_frame.configure(borderwidth="2")
        self.status_frame.configure(relief=GROOVE)
        self.status_frame.configure(background="#d9d9d9")
        self.status_frame.configure(highlightbackground="#d9d9d9")
        self.status_frame.configure(highlightcolor="black")
        self.status_frame.configure(width=175)

        self.Label3 = Label(self.status_frame)
        self.Label3.place(relx=0.06, rely=0.27, height=41, width=64)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''SUCCESS''')

        self.Label4 = Label(self.status_frame)
        self.Label4.place(relx=0.03, rely=0.49, height=41, width=64)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''FAIL''')

        self.Label5 = Label(self.status_frame)
        self.Label5.place(relx=0.03, rely=0.7, height=41, width=74)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''TOTAL''')

        #The sucess
        self.success_label_var = StringVar()
        self.success_label_var.set("0")

        self.success_label = Label(self.status_frame, textvariable=self.success_label_var)
        self.success_label.place(relx=0.46, rely=0.32, height=21, width=34)
        self.success_label.configure(activebackground="#f9f9f9")
        self.success_label.configure(activeforeground="black")
        self.success_label.configure(background="#d9d9d9")
        self.success_label.configure(disabledforeground="#a3a3a3")
        self.success_label.configure(foreground="#000000")
        self.success_label.configure(highlightbackground="#d9d9d9")
        self.success_label.configure(highlightcolor="black")
        self.success_label.configure(text='''0''')

        #The total of the success
        self.total_fail_var = StringVar()
        self.total_fail_var.set("0")
        self.fail_label = Label(self.status_frame, textvariable=self.total_fail_var)
        self.fail_label.place(relx=0.49, rely=0.54, height=21, width=34)
        self.fail_label.configure(activebackground="#f9f9f9")
        self.fail_label.configure(activeforeground="black")
        self.fail_label.configure(background="#d9d9d9")
        self.fail_label.configure(disabledforeground="#a3a3a3")
        self.fail_label.configure(foreground="#000000")
        self.fail_label.configure(highlightbackground="#d9d9d9")
        self.fail_label.configure(highlightcolor="black")
        self.fail_label.configure(text='''0''')

        self.Label2 = Label(self.status_frame)
        self.Label2.place(relx=0.03, rely=0.09, height=31, width=64)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''FOUND''')

        #The total of the success
        self.total_result_var = StringVar()
        self.total_result_label = Label(self.status_frame, textvariable = self.total_result_var)
        self.total_result_var.set("0")
        self.total_result_label.place(relx=0.43, rely=0.72, height=31, width=44)
        self.total_result_label.configure(activebackground="#f9f9f9")
        self.total_result_label.configure(activeforeground="black")
        self.total_result_label.configure(background="#d9d9d9")
        self.total_result_label.configure(disabledforeground="#a3a3a3")
        self.total_result_label.configure(foreground="#000000")
        self.total_result_label.configure(highlightbackground="#d9d9d9")
        self.total_result_label.configure(highlightcolor="black")
        self.total_result_label.configure(text='''0''')

        #total found in all threads
        self.total_found_var = StringVar()
        self.total_found_label = Label(self.status_frame, textvariable=self.total_found_var)
        self.total_found_var.set("0")
        self.total_found_label.place(relx=0.46, rely=0.11, height=31, width=44)
        self.total_found_label.configure(activebackground="#f9f9f9")
        self.total_found_label.configure(activeforeground="black")
        self.total_found_label.configure(background="#d9d9d9")
        self.total_found_label.configure(disabledforeground="#a3a3a3")
        self.total_found_label.configure(foreground="#000000")
        self.total_found_label.configure(highlightbackground="#d9d9d9")
        self.total_found_label.configure(highlightcolor="black")
        self.total_found_label.configure(text='''0''')


        self.Frame3 = Frame(top)
        self.Frame3.place(relx=0.46, rely=0.7, relheight=0.29, relwidth=0.51)
        self.Frame3.configure(relief=GROOVE)
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief=GROOVE)
        self.Frame3.configure(background="#d9d9d9")
        self.Frame3.configure(highlightbackground="#d9d9d9")
        self.Frame3.configure(highlightcolor="black")
        self.Frame3.configure(width=255)

        self.Scrolledlistbox2 = ScrolledListBox(self.Frame3)
        self.Scrolledlistbox2.place(relx=0.04, rely=0.04, relheight=1.2
                , relwidth=0.91)
        self.Scrolledlistbox2.configure(background="white")
        self.Scrolledlistbox2.configure(disabledforeground="#a3a3a3")
        self.Scrolledlistbox2.configure(font="TkFixedFont")
        self.Scrolledlistbox2.configure(foreground="black")
        self.Scrolledlistbox2.configure(highlightbackground="#d9d9d9")
        self.Scrolledlistbox2.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox2.configure(selectbackground="#c4c4c4")
        self.Scrolledlistbox2.configure(selectforeground="black")
        self.Scrolledlistbox2.configure(width=10)

        self.Label12 = Label(top)
        self.Label12.place(relx=0.54, rely=0.66, height=31, width=164)
        self.Label12.configure(activebackground="#f9f9f9")
        self.Label12.configure(activeforeground="black")
        self.Label12.configure(background="#d9d9d9")
        self.Label12.configure(disabledforeground="#a3a3a3")
        self.Label12.configure(font=font9)
        self.Label12.configure(foreground="#000000")
        self.Label12.configure(highlightbackground="#d9d9d9")
        self.Label12.configure(highlightcolor="black")
        self.Label12.configure(text='''QUEUE LIST''')

        self.Button1 = Button(top, command = self.select_dir)
        self.Button1.place(relx=0.85, rely=0.53, height=24, width=70)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Select Dir''')
        self.Button1.configure(width=70)

        self.directory_folder = Entry(top)
        self.directory_folder.place(relx=0.34, rely=0.54, relheight=0.02
                , relwidth=0.49)
        self.directory_folder.configure(background="white")
        self.directory_folder.configure(disabledforeground="#a3a3a3")
        self.directory_folder.configure(font="TkFixedFont")
        self.directory_folder.configure(foreground="#000000")
        self.directory_folder.configure(insertbackground="black")
        self.localiza_var = StringVar()
        self.directory_folder.configure(textvariable=self.localiza_var)
        self.directory_folder.configure(width=244)

############################################################
        #EXTRA BINDINGS
        self.board_code = ""
        self.start_running = False
        self.boards_list.bind('<<ListboxSelect>>', self.get_board_code)

        #THESE LISTS WILL BE USED FOR THE QUEUE LISTS
        #self.threads_in_queue = [] # these will be the startup threads, one the user presses START, the other list will be used
        #self.threads_that_will_be_add_after_the_loop = [] # these threads will be added after a loop

        #number of pics that sucess , failed and total downloaded
        self.success_image = 0
        self.failed_image = 0
        self.total_image = 0

        #for the threads that you get
        self.threads_dict = {}
        #for all the images in those threads
        self.imgs_in_thread = {}

        #default localization
        self.localization = ""

        self.boards = []

        #SEMAPHORES
        self.semaphore = threading.Semaphore(50)

        #FUNCTIONSSS




    def select_dir(self):
        filename = filedialog.askdirectory()
        self.localiza_var.set(filename)
        self.localization = filename

    def get_boards(self):
        self.boards = programz.get_boards_json()
        self.boards_list.delete(0, END)

        for i in self.boards:
            self.boards_list.insert(END, i[0] + " - " + i[1])


    #get the index board
    def get_board_code(self, event):
        index = self.boards_list.curselection()[0]
        self.board_code = self.boards[index][0]
    #open the new thread window

    def get_threads(self):
        threads_gui = threads.create_threads(self.top)
        threads_gui[1].get_threads_to_gui(self.board_code)
        self.top.wait_window(threads_gui[0])
        if len(threads_gui[1].boards_selected) is not 0:
            if self.board_code in self.threads_dict:
                self.threads_dict[self.board_code] += threads_gui[1].boards_selected
            else:
                self.threads_dict[self.board_code] = threads_gui[1].boards_selected

            for keys, values in self.threads_dict.items():
                new_list = []
                for elements in values:
                    if elements not in new_list:
                        new_list.append(elements)
                self.threads_dict[keys] = new_list

            self.update_queue()
    #updates the queue list
    def update_queue(self):
        self.Scrolledlistbox2.delete(0, END)
        for k, v in self.threads_dict.items():
            self.Scrolledlistbox2.insert(END, k + ": " + str(len(v)))
    #start the downloads

    def start_the_gattering(self):
        #reset everything to 0
        self.reset_values()

        #this deletes the queue list
        self.Scrolledlistbox2.delete(0, END)

        #GET ALL PICS FROM THE THREADS
        self.status_label.configure(text='''GETTING ITEMS''')

        #threads to get all the pics
        self.new_thread = ""
        self.thread_queue = queue.Queue()
        self.new_thread = threading.Thread(
            target=self.runloop,
            kwargs={'thread_queue':self.new_thread})
        self.new_thread.start()

    def runloop(self, thread_queue=None):
        self.number_of_pics = 0

        for keys, values in self.threads_dict.items():
            list_add_images = []
            for thr in values:
                this_var_will_be_used_for_safe_keep = programz.get_files_from_thread(keys, thr)
                list_add_images.append(this_var_will_be_used_for_safe_keep[0])

                self.number_of_pics += this_var_will_be_used_for_safe_keep[1]

                self.total_found_var.set(str(self.number_of_pics))
            self.imgs_in_thread[keys] = list_add_images

        #this resets the original list
        self.threads_dict = {}
        for keys, values in self.imgs_in_thread.items():
            self.download_images_prepare(keys, values)

    def download_images_prepare(self, key, values):
        self.status_label.configure(text='''DOWNLOADING...''')
        for i in values:
            #same the folder name
            folder_name = re.sub(r'\W+', '_', i[0])
            directory = self.localization + "/" + key + "/" + folder_name + "/"
            #create the folders and the subfolders(webm gif jpg png)
            #name of the file, link to imagem, extention of the image, extention for the folders
            if not os.path.exists(os.path.abspath(directory)):
                os.makedirs(os.path.abspath(directory))
                for folders_name in ["webm", "png", "gif", "jpg"]:
                    os.makedirs(os.path.abspath(directory + folders_name + "/"))


            #download the actual images with threads
            for image in i[1]:
                self.semaphore.acquire()
                thread = threading.Thread(target=self.download_image, args=(image, directory))
                thread.start()
            self.status_label.configure(text='''DONE''')


    def download_image(self, image_array, directory_to_save):
        dir_to_save = directory_to_save + image_array[2] + "/"
        try:
            full_image_path = os.path.abspath(dir_to_save + image_array[0]+"."+image_array[2])
            if not os.path.isfile(full_image_path):
                r = requests.get(image_array[1])
                with open(full_image_path, "wb") as code:
                    code.write(r.content)
            self.success_image += 1
            self.success_label_var.set(str(self.success_image))
        except:
            os.remove(os.path.abspath(dir_to_save + image_array[0]+"."+image_array[2]))
            self.failed_image += 1
            self.total_fail_var.set(str(self.failed_image))

        finally:
            self.total_image += 1
            self.total_result_var.set(str(self.total_image))
            self.semaphore.release()

        #FINISH ROUNDS


    def reset_values(self):
        self.number_of_pics = 0
        self.success_image = 0
        self.total_image = 0
        self.failed_image = 0
        self.success_label_var.set(str(self.success_image))
        self.total_fail_var.set(str(self.failed_image))
        self.total_result_var.set(str(self.total_image))

############################################

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = Pack.__dict__.keys() | Grid.__dict__.keys() \
                  | Place.__dict__.keys()
        else:
            methods = Pack.__dict__.keys() + Grid.__dict__.keys() \
                  + Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, Listbox):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

if __name__ == '__main__':
    main()
