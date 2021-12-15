import streamlit as st
import pandas

data = {
  "test_1":[50,20,10,30,60] , 
  "test_2":[30,90,100,200,40]
}

df = pandas.DataFrame(data)


st.title('Frist streamlit app')
st.subheader('Bla bla bla')
st.write('''This is my frist web app
Enjoy it!
''')

st.write(df)
st.line_chart(df)
st.area_chart(df)