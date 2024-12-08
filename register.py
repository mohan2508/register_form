import streamlit as st 
import sqlite3

conn=sqlite3.connect('register.db',check_same_thread=False)
cursor=conn.cursor()

def formCreation():
    st.write(':rainbow[Please Fill This Form]')
    with st.form(key='Registration Form'):
        name = st.text_input('Enter your Name :')
        standard =st.text_input('Enter your Class :')
        board =st.text_input('Enter CBSE/State :')
        place =st.text_input('Enter yor Location :')
        online=st.text_input('Enter time of your class :')
        contact =st.text_input('Enter your Mobile:')
        submit =st.form_submit_button(label='Register')
        
        if submit == True:
            st.success('Your registration has been successful')
            addInfo(name,standard,board,place,online,contact)       
    
    
def addInfo(a,b,c,x,y,z):
    
    cursor.execute(
         """
    CREATE TABLE IF NOT EXISTS registration(Name Text(50),Standard Text(10),Board Text(10),
    Place Text(25),Online_Time Text(10),Contact Text(10))
    """
    )
    cursor.execute("INSERT INTO registration values (?,?,?,?,?,?)",(a,b,c,x,y,z))
    conn.commit()
    conn.close()
    st.success('User has been added to the SQLITE database')
    

            
    
formCreation()    
    
    
           
    
    

    
