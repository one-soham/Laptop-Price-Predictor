import streamlit as st
import pickle
import numpy as np


pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title("Laptop Price Predictor")

company = st.selectbox("Brand: ", df.Company.unique())
type = st.selectbox("Type: ", df.TypeName.unique())
ram = st.selectbox("RAM (in GB): ", [2,4,6,8,12,16,24,32,64])
weight = st.number_input("Weight (in KG)")
touchscreen = st.selectbox("Touchscreen: ", ["No","Yes"])
ips = st.selectbox("IPS Display: ", ["No","Yes"])
screensize = st.number_input("Screen Size (in Inches)")
resolution = st.selectbox("Screen Resolution", ["1920x1080","1366x768","1600x900","3840x2160","3200x1800",
                                                "2880x1800","2560x1600","2560x1440","2304x1440"])
cpu = st.selectbox("CPU: ", df.CpuBrand.unique())

chc1 = st.selectbox("HDD Present?: ", ["No", "Yes"])
hdd = 1 if chc1=="Yes" else 0
chc2 = st.selectbox("SSD Present?: ", ["No","Yes"])
ssd = 4 if chc2=="Yes" else 0

gpu = st.selectbox("GPU: ", df.GpuBrand.unique())
os = st.selectbox("OS: ", df.os.unique())

if st.button("Predict Price"):
    ppi = None
    if touchscreen == "Yes":
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == "Yes":
        ips = 1
    else:
        ips = 0

    X_res = int(resolution.split("x")[0])
    Y_res = int(resolution.split("x")[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5/screensize
    query = np.array([company,type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])

    query = query.reshape(1,12)
    st.title("The predicted price of this configuration is " + str(int(np.exp(pipe.predict(query)[0]))))