import streamlit as st
import pandas

data = {
  "Today Temperature":[30,27,31,32,28] , 
  "Yesterday Temperature":[28,29,31,32,33]
}

df = pandas.DataFrame(data)


st.title('Frist streamlit app')
st.subheader('Temperature')
st.write('''This is my frist web app
Enjoy it!
''')

st.write(df)
st.line_chart(df)
st.area_chart(df)

myslider = st.slider('celcius')
st.write(myslider, 'in Fahrenheit is' ,myslider * 9/5 +32)