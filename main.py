import tkinter as tk
from tkinter import ttk
import sqlite3


class Main(tk.Frame):
	def __init__(self, root):
		super().__init__(root)
		self.init_main()
		self.db = db
		self.view_records()

	def init_main(self):	
		toolbar  = tk.Frame(bg='#d7d8e0', bd=2)
		toolbar.pack(side=tk.TOP, fill=tk.X)

		
		btn_open_dialog = tk.Button(toolbar, text='додати', command=self.open_dialog, bg='#d7d8e0', bd=0, 
			compound=tk.TOP)
		btn_open_dialog.pack(side=tk.LEFT)

		self.tree = ttk.Treeview(self, columns=('ID', 'description', 'costs', 'total'), height=15, show='headings')

		self.tree.column('ID', width=30, anchor=tk.CENTER)
		self.tree.column('description', width=360, anchor=tk.CENTER)
		self.tree.column('costs', width=150, anchor=tk.CENTER)
		self.tree.column('total', width=100, anchor=tk.CENTER)

		self.tree.heading('ID', text='№')
		self.tree.heading('description', text='микола')
		self.tree.heading('costs', text='котунович')
		self.tree.heading('total', text='567')

		self.tree.pack()
	


	def view_records(self):
	 	[self.tree.delete(i) for i in self.tree.get_children()]
	 	[self.tree.insert('', 'end', values=row) for row in self.db.get_records()]


	def open_dialog(self):
		Child()

class Child(tk.Toplevel):
	def __init__(self):
		super().__init__(root)
		self.init_child()
		#self.view = app

	def init_child(self):
		self.title('aasd llld')
		self.geometry('400x220+400+300')
		self.resizable(False, False)

		label_description = tk.Label(self, text='1name')
		label_description.place(x=50, y=50)
		label_select = tk.Label(self, text='1type')
		label_select.place(x=50, y=80)
		label_sum = tk.Label(self, text='1price')
		label_sum.place(x=50, y=110)

		self.entry_description = ttk.Entry(self)
		self.entry_description.place(x=200, y=50)

		self.entry_sparepart = ttk.Entry(self)
		self.entry_sparepart.place(x=200, y=110)

		self.Combobox = ttk.Combobox(self, values=[u'wheel', u'steel'])
		self.Combobox.current(0)
		self.Combobox.place(x=200, y=80)

		btn_cancel = ttk.Button(self, text='exit', command=self.destroy)
		btn_cancel.place(x=300, y= 170)
		btn_ok = ttk.Button(self, text='add')
		btn_ok.place(x=220, y=170)
		btn_ok.bind('<Button-1>', lambda event: self.view.records(
			self.entry_description.get(), self.entry_sparepart.get(), self.Combobox.get()))

		self.grab_set()
		self.focus_set()


class DataBase:
	def __init__(self):
		self.conn = sqlite3.connect('parts.db')
		self.c = self.conn.cursor()
		self.c.execute(
			'''CREATE TABLE IF NOT EXISTS parts (id integer primary key, description text, costs real, total integer)''')

		self.conn.commit()

	def insert_data(self, description, costs, total):
		self.c.execute('''INSERT INTO parts(description, costs, total) VALUES(?, ?, ?) ''', (description, costs, total)) 
	
		self.conn.commit()


	def get_records(self):
		self.c.execute('''SELECT * FROM parts''')
		return self.c.fetchall()

if __name__ == "__main__":
	root = tk.Tk()
	db = DataBase()
	app = Main(root)
	app.pack()
	root.title("abc cba")
	root.geometry("650x450+300+200")
	root.resizable(False, False)
	root.mainloop()
		