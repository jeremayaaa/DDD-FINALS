from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk

class Student_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("University of Adamson")
        self.root.geometry("1285x563+260+233")

        #-------------- TITLE --------------
        lbl_title = Label(self.root, text="ONLINE ENROLLMENT", font = ("Arial", 18, "bold"), bg = "sky blue", fg = "navy blue", bd = 4, relief = RIDGE)
        lbl_title.place(x = 0, y = 0, width = 1295, height = 50)

        #-------------- LABEL FRAME --------------
        label_frame_left = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "Student Information", font = ("Arial", 12, "bold"), padx =2 )
        label_frame_left.place(x = 5, y = 50, width  = 440, height = 500)

        #-------------- LABEL AND ENTRY --------------
        #fname
        label_fname = Label(label_frame_left, text = "First Name", font = ("Arial", 12, "bold"), padx = 2, pady = 6)
        label_fname.grid (row = 0, column = 0, sticky = W)

        fname = ttk.Entry(label_frame_left, font = ("Arial", 13, "bold"), width = 29)
        fname.grid(row = 0, column = 1)

        #mname
        label_mname = Label(label_frame_left, text = "Middle Name", font = ("Arial", 12, "bold"), padx = 2, pady = 6)
        label_mname.grid (row = 1, column = 0, sticky = W)

        mname = ttk.Entry(label_frame_left, font = ("Arial", 13, "bold"), width = 29)
        mname.grid(row = 1, column = 1)

        #lname
        label_lname = Label(label_frame_left, text = "Last Name", font = ("Arial", 12, "bold"), padx = 2, pady = 6)
        label_lname.grid (row = 2, column = 0, sticky = W)

        lname = ttk.Entry(label_frame_left, font = ("Arial", 13, "bold"), width = 29)
        lname.grid(row = 2, column = 1)

        #gender
        label_gender = Label(label_frame_left, text = "Gender", font = ("Arial", 12, "bold"), padx = 2, pady = 6)
        label_gender.grid (row = 3, column = 0, sticky = W)

        combo_gender = ttk.Combobox(label_frame_left, font = ("Arial", 12, "bold"), width = 27, state = "readonly")
        combo_gender["value"]= ("Male", "Female", "Rather Not Say")
        combo_gender.current(0)
        combo_gender.grid(row = 3, column = 1)

        #Citizenship
        label_citizenship = Label(label_frame_left, text = "Citizenship", font = ("Arial", 12, "bold"), padx = 2, pady = 6)
        label_citizenship.grid (row = 4, column = 0, sticky = W)

        combo_citizenship = ttk.Combobox(label_frame_left, font = ("Arial", 12, "bold"), width = 27, state = "readonly")
        combo_citizenship["value"]= ("American", "Chinese", "Egyptian", "Filipino", "French", "Indian", "Japanese")
        combo_citizenship.current(0)
        combo_citizenship.grid(row = 4, column = 1)

        #Mobile Number
        label_mobile = Label(label_frame_left, text = "Mobile Number", font = ("Arial", 12, "bold"), padx = 2, pady = 6)
        label_mobile.grid (row = 5, column = 0, sticky = W)

        mobile = ttk.Entry(label_frame_left, font = ("Arial", 13, "bold"), width = 29)
        mobile.grid(row = 5, column = 1)

        #Region
        label_region = Label(label_frame_left, text = "Region", font = ("Arial", 12, "bold"), padx = 2, pady = 6)
        label_region.grid (row = 6, column = 0, sticky = W)

        combo_region = ttk.Combobox(label_frame_left, font = ("Arial", 12, "bold"), width = 27, state = "readonly")
        combo_region["value"]= ("ARMM", "CAR", "NCR", "Region I", "Region II","Region III","Region IV-A","Region IV-B","Region V","Region VI","Region VII","Region VIII","Region IV","Region X","Region XI","Region XII", "Region XIII")
        combo_region.current(0)
        combo_region.grid(row = 6, column = 1)

        #Province
        label_province = Label(label_frame_left, text = "Province (if NCR)", font = ("Arial", 12, "bold"), padx = 2, pady = 6)
        label_province.grid (row = 7, column = 0, sticky = W)

        combo_province = ttk.Combobox(label_frame_left, font = ("Arial", 12, "bold"), width = 27, state = "readonly")
        combo_province["value"]= ("First District (City of Manila)", "Second District", "Third District", "Fourth District")
        combo_province.current(0)
        combo_province.grid(row = 7, column = 1)

        #Municipality
        label_municipality = Label(label_frame_left, text = "Municipality (Manila)", font = ("Arial", 12, "bold"), padx = 2, pady = 6)
        label_municipality.grid (row = 8, column = 0, sticky = W)

        combo_municipality = ttk.Combobox(label_frame_left, font = ("Arial", 12, "bold"), width = 27, state = "readonly")
        combo_municipality["value"]= ("Binondo", "Ermita", "Intramuros", "Malate", "Paco", "Port Area", "Quiapo", "Sampaloc", "San Miguel", "San Nicolas", "Santa Ana", "Santa Cruz", "Tondo I/II")
        combo_municipality.current(0)
        combo_municipality.grid(row = 8, column = 1)

        #Email
        label_email = Label(label_frame_left, text = "Email Address", font = ("Arial", 12, "bold"), padx = 2, pady = 6)
        label_email.grid (row = 9, column = 0, sticky = W)

        email = ttk.Entry(label_frame_left, font = ("Arial", 13, "bold"), width = 29)
        email.grid(row = 9, column = 1)
 
        #Bday
        label_bday = Label(label_frame_left, text = "Date of Birth", font = ("Arial", 12, "bold"), padx = 2, pady = 6)
        label_bday.grid (row = 10, column = 0, sticky = W)

        lbl_bday = Label(label_frame_left, bd = 0, relief = RIDGE)
        lbl_bday.grid(row = 10, column = 1, sticky = W)

        combo_month = ttk.Combobox(lbl_bday, font = ("Arial", 12, "bold"), width = 10, state = "readonly")
        combo_month["value"]= ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
        combo_month.current(0)
        combo_month.grid(row = 0, column = 0, padx = 1)

        combo_day = ttk.Combobox(lbl_bday, font = ("Arial", 12, "bold"), width = 4, state = "readonly")
        combo_day["value"]= ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31")
        combo_day.current(0)
        combo_day.grid(row = 0, column = 1, padx = 1)

        combo_year = ttk.Combobox(lbl_bday, font = ("Arial", 12, "bold"), width = 7, state = "readonly")
        combo_year["value"]= ("2022", "2021", "2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010", "2009", "2008", "2007", "2006", "2005", "2004", "2003","2002", "2001", "2000", "1999","1998", "1997", "1996", "1995", "1994", "1993", "1992", "1991", "1990")
        combo_year.current(0)
        combo_year.grid(row = 0, column = 2, padx = 1)

        #Course
        label_course = Label(label_frame_left, text = "Course", font = ("Arial", 12, "bold"), padx = 2, pady = 6)
        label_course.grid (row = 11, column = 0, sticky = W)

        combo_course = ttk.Combobox(label_frame_left, font = ("Arial", 12, "bold"), width = 27, state = "readonly")
        combo_course["value"] = ("BS in Architecture", "BS in Accountancy", "BS Major in Financial Management", "BSBA Major in Marketing Management", "BSBA Major in Operations Management", "BS Customs Administration", "BS Hospitality Management", "BS Chemical Engineering", "BS Civil Engineering", "BS Computer Engineering", "BS Electrical Engineering", "BS Electronics Engineering", "BS in Industrial Engineering", "BS in Mechanical Engineering", "BS in Mining Engineering", "BS in Geology", "BS in Petroleum Engineering", "BS in Nursing", "BS in Pharmacy", "BS in Juris Doctor");
        combo_course.current(0)
        combo_course.grid(row = 11, column = 1)

        

        #-------------- BUTTON FRAME --------------
        btn_frame = Label(label_frame_left, bd = 2, relief = RIDGE)
        btn_frame.place (x = 10, y = 428, width = 411, height = 36)

        btn_add = Button(btn_frame, text = "Add", font = ("Arial", 11, "bold"), bg = "dark blue", fg = "white", width = 10)
        btn_add.grid(row = 0, column = 0, padx = 1)

        btn_update = Button(btn_frame, text = "Update", font = ("Arial", 11, "bold"), bg = "dark blue", fg = "white", width = 10)
        btn_update.grid(row = 0, column = 1, padx = 1)

        btn_delete = Button(btn_frame, text = "Delete", font = ("Arial", 11, "bold"), bg = "dark blue", fg = "white", width = 10)
        btn_delete.grid(row = 0, column = 2, padx = 1)

        btn_reset = Button(btn_frame, text = "Reset", font = ("Arial", 11, "bold"), bg = "dark blue", fg = "white", width = 10)
        btn_reset.grid(row = 0, column = 3, padx = 1)

        #-------------- TABLE FRAME --------------
        table_frame = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "View Details and Search System", font = ("Arial", 12, "bold"), padx =2 )
        table_frame.place(x = 450, y = 50, width  = 830, height = 500)

        label_search = Label(table_frame, font = ("Arial", 12, "bold"), text = "Search By:", bg = "sky blue", fg = "white")
        label_search.grid(row = 0, column = 0, sticky = W, padx = 2)

        combo_search = ttk.Combobox(table_frame, font = ("Arial", 12, "bold"), width = 27, state = "readonly")
        combo_search["value"]= ("Last Name", "First Name", "Mobile Number")
        combo_search.current(0)
        combo_search.grid(row = 0, column = 1, padx = 2)

        search = ttk.Entry(table_frame, font = ("Arial", 13, "bold"), width = 24)
        search.grid(row = 0, column = 2, padx = 2)
        
        btn_search = Button(table_frame, text = "Search", font = ("Arial", 11, "bold"), bg = "white", fg = "navy blue", width = 10)
        btn_search.grid(row = 0, column = 3, padx = 1)

        btn_showall = Button(table_frame, text = "Show All", font = ("Arial", 11, "bold"), bg = "white", fg = "navy blue", width = 10)
        btn_showall.grid(row = 0, column = 4, padx = 1)

        #-------------- DATA TABLE --------------
        details_table = Label(table_frame, bd = 2, relief = RIDGE)
        details_table.place (x = 0, y = 50, width = 820, height = 350)

        scroll_x = ttk.Scrollbar(details_table, orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient = VERTICAL)

        self.Student_Details_Table = ttk.Treeview(details_table, column =("first_name", "middle_name", "last_name", "gender", "citizenship", "mobile_number", "region", "province", "municipality", "email_address", "religion", "date_of_birth"), xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)
        
        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)

        scroll_x.config(command = self.Student_Details_Table.xview)
        scroll_y.config(command = self.Student_Details_Table.yview)

        #-------------- CONTENTS OF DATA TABLE --------------
        self.Student_Details_Table.heading("first_name", text = "First Name")
        self.Student_Details_Table.heading("middle_name", text = "Middle Name")
        self.Student_Details_Table.heading("last_name", text = "Last Name")
        self.Student_Details_Table.heading("gender", text = "Gender")
        self.Student_Details_Table.heading("citizenship", text = "Citizenship")
        self.Student_Details_Table.heading("mobile_number", text = "Mobile Number")
        self.Student_Details_Table.heading("region", text = "Region")
        self.Student_Details_Table.heading("province", text = "Province (if NCR)")
        self.Student_Details_Table.heading("municipality", text = "Municipality (if Manila)")
        self.Student_Details_Table.heading("email_address", text = "Email Address")
        self.Student_Details_Table.heading("religion", text = "Religion")
        self.Student_Details_Table.heading("date_of_birth", text = "Date of Birth")

        self.Student_Details_Table["show"] = "headings"
        self.Student_Details_Table.pack(fill = BOTH, expand = 1)

    



if __name__ == "__main__":
    root = Tk()
    obj = Student_Win(root)
    root.mainloop()