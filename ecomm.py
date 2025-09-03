import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def main():
    st.title("This is my streamlit app for ecommerce that i have")
    st.sidebar.title("Upload your File")

    uploaded_file = st.sidebar.file_uploader("Upload your File", type=["csv","xlsx"])
    try :
        if uploaded_file  is not None:
            try:
                if uploaded_file.name.endswith(".csv"):
                    data = pd.read_csv(uploaded_file)
                else :
                    data = pd.read_excel(uploaded_file)

                st.sidebar.success("File Uploaded Successfully")

                st.subheader("data overview")
                st.dataframe(data.head())

                st.subheader("Basic information of the data")
                st.write("Shape of the data", data.shape)
                st.write("Columns in my data", data.columns)
                st.write("Missing value", data.isnull().sum())
                
                st.subheader("I will show you stats of the data")
                st.write(data.describe())

            except Exception as e:
                print("it will handle if thing gets wrong",e)
        else:
            pass
    except Exception as e :
        print("error is {e}")


if __name__ == "__main__":
    main()
