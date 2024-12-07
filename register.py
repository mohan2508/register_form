import streamlit as st 
import mysql.connector

st.header(':orange[MohanClasses]')
st.image('https://th.bing.com/th/id/OIP.rhl1XV7nIE3sJymInBApNQHaEK?w=500&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7')

mydb=mysql.connector.connect(
    host="localhost",
    #port='3306',
    user="root",
    #password="aparnaa12",
    database="mohanclasses",
    #auth_plugin='mysql_native_password'
)
mycursor=mydb.cursor()


def main():
    st.title(':rainbow[Please Fill This Form]')
  
    name = st.text_input('Enter your Name :')
    email =st.text_input('Enter your Email-Id :')
    phone =st.text_input('Enter your Phone :')
    Class =st.text_input('Enter yor Standard :')
    school=st.text_input('Enter your School Name :')
    
    if st.button(":green[Register]"):
        sql="insert into register_form (name,email,phone,Class,school) values(%s,%s,%s,%s,%s)"
        val=(name,email,phone,Class,school)
        mycursor.execute(sql,val)
        mydb.commit()
        st.success('Registration has been completed successfully')
        st.balloons()
    
    
    
       
        
              
    
    
if __name__=="__main__":
    main()
    
            
    
  
    
           
    
    
