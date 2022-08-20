# Python code to demonstrate table creation and  
# insertions with SQL 
  
# importing module 
import sqlite3 
from tkinter import * 
# Part 1 Creating a simple Database

# connecting to the database  

# SQL command to insert the data in the table 

  
# another SQL command to insert the data in the table 

  
# To save the changes in the files. Never skip this.  
# If we skip this, nothing will be saved in the database. 

  
# close the connection 


# Part 2 Creating a interface for entering values to our database.
# Create a submit function
def Submit():
    # connecting to the database  
    connection = sqlite3.connect("myTable.db") 
    # cursor  
    crsr = connection.cursor() 
    # Insert Into Table
    
def Query():
    # connecting to the database  
    connection = sqlite3.connect("myTable.db") 
    # cursor  
    crsr = connection.cursor() 
    # Insert Into Table
     
    # store all the fetched data in the ans variable 
   
    # Since we have already selected all the data entries  
    # using the "SELECT *" SQL command and stored them in  
    # the ans variable, all we need to do now is to print  
    # out the ans variable 
    # As we want to display the dataframe in our GUI we can use label widget
    # ans is a list and for example we want to find the names of all the 
    # People in datatable we can use the following command
    records =""
    for record in ans:
        records += record[1] +" " +record[2] + '\n'
    Label(root , text = records).grid(row = 7 ,column = 0 , columnspan = 2)
root = Tk()
# Create Text Boxes
Staffno = Entry(root , width = 30)
Staffno.grid(row = 0 ,column = 1, padx = 20)

f_name = Entry(root , width = 30)
f_name.grid(row = 1 ,column = 1, padx = 20)

l_name = Entry(root , width = 30)
l_name.grid(row = 2 ,column = 1, padx = 20)

Gender = Entry(root , width = 30)
Gender.grid(row = 3 ,column = 1, padx = 20)

DOJi = Entry(root , width = 30)
DOJi.grid(row = 4 ,column = 1, padx = 20)

# Create text box labels
Staffno_label = Label(root, text = "Staff Number") 
Staffno_label.grid(row = 0 , column =0)

f_name_label = Label(root, text = "First Name") 
f_name_label.grid(row = 1 , column =0)

l_name_label = Label(root, text = "Last Name") 
l_name_label.grid(row = 2 , column =0)

Gender_label = Label(root, text = "Gender") 
Gender_label.grid(row = 3 , column =0)

DOJi_label = Label(root, text = "Date of Joining") 
DOJi_label.grid(row = 4 , column =0)

# Create a submit button
Button(root , text = "Add record to data base" , command= Submit).grid(row = 5 , columnspan = 2 , pady=10 , padx = 20 , ipadx = 100 )
Button(root , text = "Query the database" , command= Query).grid(row = 6 , columnspan = 2 , pady=10 , padx = 20 , ipadx = 100 )
root.mainloop()
