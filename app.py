import streamlit as st
import pandas as pd
import openpyxl as xl
import shutil

st.title("Excel sheet spliter")

st.write("Choose our Template")
template = st.button("Template Excel file")

st.write("or")

uploaded_file = st.file_uploader("Choose a XLSX file", type="xlsx")


if template:
    uploaded_file = "pivot.xlsx"

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    # st.dataframe(df)
    st.table(df)
    # st.write(uploaded_file)


    workbook = xl.load_workbook(uploaded_file)
    # sheet_1 = workbook['Overview']
    # st.write(workbook.sheetnames)
    sheet = st.selectbox("Select tab", workbook.sheetnames)

    clicked = st.button("Save new Excel file")
    if clicked:
        filename = uploaded_file.name.replace('.xlsx','')+'_'+sheet+'.xlsx'
        shutil.copy(uploaded_file.name,filename)

        sn = workbook.sheetnames
        sn.remove(sheet)

        wb = xl.load_workbook(filename)
        for s in sn:
            std = wb.get_sheet_by_name(s)
            wb.remove_sheet(std)

        wb.save(filename)

        try:
            df2 = pd.read_excel(filename)
            st.table(df2)
        except:
            st.write("Cannot display table")