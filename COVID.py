import os
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

os.chdir(r'C:\Users\DELL\Documents')
data = pd.read_csv('COVID19.csv',low_memory=False)
print(data.head())  #pRINT THE FIRST FEW ROWS OF DATA


#Print the shape of the data before and after cleaning
print("Before cleaning:", data.shape)

# Drop any rows with missing values
data.dropna(inplace=True)

# Print the shape of the data after cleaning
print("After cleaning:", data.shape)

#Check for any duplicate rows
print("Duplicate rows:", data.duplicated().sum())

print(data.describe())
print(data.columns)

plt.figure(figsize=(10,6))
plt.scatter(data['Peope Vaccinated(Cumulative)'], data['Cumulative excess deaths (central estimate)'])
plt.xlabel('People Vaccinated')
plt.ylabel('Cumulative Excess Deaths')
plt.title('Relationship between Vaccination and Excess Deaths')
plt.show()

for entity in data['Entity'].unique():
    entity_data = data[data['Entity'] == entity]
    plt.plot(entity_data['Day'], entity_data['Cumulative excess deaths (central estimate)'], label=entity)

plt.xlabel('Day')
plt.ylabel('Cumulative Excess Deaths')
plt.title('Cumulative Excess Deaths by Entity')
plt.legend()
plt.show()

for entity in data['Entity'].unique():
    entity_data = data[data['Entity'] == entity]
    plt.scatter(entity_data['Peope Vaccinated(Cumulative)'], entity_data['Cumulative excess deaths (central estimate)'], label=entity)

plt.xlabel('People Vaccinated')
plt.ylabel('Cumulative Excess Deaths')
plt.title('Relationship between Vaccination and Excess Deaths')
plt.legend()
plt.show()

# Create Streamlit app
st.title('COVID-19 Vaccination and Excess Deaths Analysis')

# Visualization options
st.sidebar.header('Visualization Options')
entity = st.sidebar.selectbox('Select Entity', data['Entity'].unique())

# Filter data by entity
entity_data = data[data['Entity'] == entity]

# Create visualizations
st.header('Cumulative Excess Deaths Over Time')
fig, ax = plt.subplots()
ax.plot(entity_data['Day'], entity_data['Cumulative excess deaths (central estimate)'])
st.pyplot(fig)

st.header('Relationship between Vaccination and Excess Deaths')
fig, ax = plt.subplots()
ax.scatter(entity_data['Peope Vaccinated(Cumulative)'], entity_data['Cumulative excess deaths (central estimate)'])
st.pyplot(fig)

           







