from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk

class Payment_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("University of Adamson")
        self.root.geometry("1285x563+260+233")

        #-------------- TITLE --------------
        lbl_title = Label(self.root, text="ONLINE PAYMENT", font = ("Arial", 18, "bold"), bg = "sky blue", fg = "navy blue", bd = 4, relief = RIDGE)
        lbl_title.place(x = 0, y = 0, width = 1295, height = 50)

        #-------------- LABEL FRAME --------------
        label_frame_up = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "Assessment of Fees", font = ("Arial", 12, "bold"), padx =1 )
        label_frame_up.place(x = 5, y = 50, width  = 440, height = 280)

        #tuition fee lec
        label_tuition_fee = Label(label_frame_up, text = "Tuition Fee Lecture", font = ("Arial", 12), padx = 2, pady = 4)
        label_tuition_fee.grid (row = 0, column = 0, sticky = W)

        tuition_fee = Label(label_frame_up, text = "30,000 PESOS", font = ("Arial", 12, "bold"), padx = 2, pady = 4)
        tuition_fee.grid (row = 0, column = 1, sticky = W)

        #tuition fee lab
        label_tuition_lab = Label(label_frame_up, text = "Tuition Fee Laboratory", font = ("Arial", 12), padx = 2, pady = 4)
        label_tuition_lab.grid (row = 1, column = 0, sticky = W)

        tuition_lab = Label(label_frame_up, text = "10,500 PESOS", font = ("Arial", 12, "bold"), padx = 2, pady = 4)
        tuition_lab.grid (row = 1, column = 1, sticky = W)

        #lab fee
        label_lab_fee = Label(label_frame_up, text = "Laboratory Usage Fee", font = ("Arial", 12), padx = 2, pady = 4)
        label_lab_fee.grid (row = 2, column = 0, sticky = W)

        lab_fee = Label(label_frame_up, text = "10,000 PESOS", font = ("Arial", 12, "bold"), padx = 2, pady = 4)
        lab_fee.grid (row = 2, column = 1, sticky = W)

        #development
        label_dev = Label(label_frame_up, text = "Development Fee", font = ("Arial", 12), padx = 2, pady = 4)
        label_dev.grid (row = 3, column = 0, sticky = W)

        dev = Label(label_frame_up, text = "  1,000 PESOS", font = ("Arial", 12, "bold"), padx = 2, pady = 4)
        dev.grid (row = 3, column = 1, sticky = W)

        #ausg
        label_ausg = Label(label_frame_up, text = "AUSG", font = ("Arial", 12), padx = 2, pady = 4)
        label_ausg.grid (row = 4, column = 0, sticky = W)

        ausg = Label(label_frame_up, text = "     500 PESOS", font = ("Arial", 12, "bold"), padx = 2, pady = 4)
        ausg.grid (row = 4, column = 1, sticky = W)

        #energy
        label_energy = Label(label_frame_up, text = "Energy Cost (Aircon)", font = ("Arial", 12), padx = 2, pady = 4)
        label_energy.grid (row = 5, column = 0, sticky = W)

        energy = Label(label_frame_up, text = "  2,280 PESOS", font = ("Arial", 12, "bold"), padx = 2, pady = 4)
        energy.grid (row = 5, column = 1, sticky = W)

        #activity
        label_activity = Label(label_frame_up, text = "Student Activity Fee", font = ("Arial", 12), padx = 2, pady = 4)
        label_activity.grid (row = 6, column = 0, sticky = W)

        activity = Label(label_frame_up, text = "     250 PESOS", font = ("Arial", 12, "bold"), padx = 2, pady = 4)
        activity.grid (row = 6, column = 1, sticky = W)

        #total
        label_total = Label(label_frame_up, text = "TOTAL", font = ("Arial", 12, "bold"), padx = 2, pady = 4)
        label_total.grid (row = 7, column = 0, sticky = W)

        total = Label(label_frame_up, text = "54,530 PESOS", font = ("Arial", 12, "bold"), padx = 2, pady = 4)
        total.grid (row = 7, column = 1, sticky = W)

        







        #-------------- LABEL FRAME --------------
        label_frame_left = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "Payment Information", font = ("Arial", 12, "bold"), padx =2 )
        label_frame_left.place(x = 5, y = 340, width  = 440, height = 210)

        #-------------- LABEL AND ENTRY --------------
        #payment method
        label_method = Label(label_frame_left, text = "Payment Method", font = ("Arial", 12, "bold"), padx = 2, pady = 6)
        label_method.grid (row = 0, column = 0, sticky = W)

        combo_method = ttk.Combobox(label_frame_left, font = ("Arial", 12, "bold"), width = 27, state = "readonly")
        combo_method["value"]= ("Gcash", "PayMaya", "Banco de Oro", "Philippine National Bank (PNB)", "Bank of the Philippine Islands (BPI)", "Union Bank of the Philippines", "Metrobank", "Security Bank")
        combo_method.current(0)
        combo_method.grid(row = 0, column = 1)

        #acc name
        label_acc_name = Label(label_frame_left, text = "Account Name", font = ("Arial", 12, "bold"), padx = 2, pady = 6)
        label_acc_name.grid (row = 1, column = 0, sticky = W)

        acc_name = ttk.Entry(label_frame_left, font = ("Arial", 13, "bold"), width = 29)
        acc_name.grid(row = 1, column = 1)

        #acc number
        label_acc_num = Label(label_frame_left, text = "Account Number", font = ("Arial", 12, "bold"), padx = 2, pady = 6)
        label_acc_num.grid (row = 2, column = 0, sticky = W)

        acc_num = ttk.Entry(label_frame_left, font = ("Arial", 13, "bold"), width = 29)
        acc_num.grid(row = 2, column = 1)

        #payment amount 
        label_amount = Label(label_frame_left, text = "Payment Amount", font = ("Arial", 12, "bold"), padx = 2, pady = 6)
        label_amount.grid (row = 3, column = 0, sticky = W)

        amount = ttk.Entry(label_frame_left, font = ("Arial", 13, "bold"), width = 29)
        amount.grid(row = 3, column = 1)


        #-------------- BUTTON FRAME --------------
        btn_frame = Label(label_frame_left, bd = 2, relief = RIDGE)
        btn_frame.place (x = 10, y = 145, width = 411, height = 36)

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
        combo_search["value"]= ("Payment Method", "Account Name", "Account Number", "Payment Amount")
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

        self.Student_Details_Table = ttk.Treeview(details_table, column =("payment_method", "acc_name", "acc_num", "payment_amount"), xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)
        
        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)

        scroll_x.config(command = self.Student_Details_Table.xview)
        scroll_y.config(command = self.Student_Details_Table.yview)

        #-------------- CONTENTS OF DATA TABLE --------------
        self.Student_Details_Table.heading("payment_method", text = "Payment Method")
        self.Student_Details_Table.heading("acc_name", text = "Account Name")
        self.Student_Details_Table.heading("acc_num", text = "Account Number")
        self.Student_Details_Table.heading("payment_amount", text = "Payment Amount")


        self.Student_Details_Table["show"] = "headings"
        self.Student_Details_Table.pack(fill = BOTH, expand = 1)










if __name__ == "__main__":
    root = Tk()
    obj = Payment_Win(root)
    root.mainloop()