import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming 'df' is your DataFrame
df = pd.read_csv("C:\\Users\\ADMIN\\SRM\\PDS\\Product.csv")

# Title of the App
st.title('Interactive Data Visualization with Streamlit')

# Display the DataFrame
st.write('## Product.csv:')
st.write(df)

# Histogram
selected_column_hist = st.selectbox('Select a column for Histogram:', df.columns)
plt.figure(figsize=(8, 6))
sns.histplot(df[selected_column_hist], kde=True)
st.pyplot()

# Box Plot
selected_column_box = st.selectbox('Select a column for Box Plot:', df.columns)
plt.figure(figsize=(8, 6))
sns.boxplot(x=df[selected_column_box])
st.pyplot()

# Scatter Plot
selected_x = st.selectbox('Select X-axis:', df.columns)
selected_y = st.selectbox('Select Y-axis:', df.columns)
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df[selected_x], y=df[selected_y])
st.pyplot()

# Pair Plot
st.write('## Pair Plot:')
sns.pairplot(df)
st.pyplot()

# Heatmap
st.write('## Correlation Heatmap:')
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
st.pyplot()

# 3D Scatter Plot
st.write('## 3D Scatter Plot:')
selected_x_3d = st.selectbox('Select X-axis:', df.columns, key='x_axis')
selected_y_3d = st.selectbox('Select Y-axis:', df.columns, key='y_axis')
selected_z_3d = st.selectbox('Select Z-axis:', df.columns, key='z_axis')

fig_3d = plt.figure(figsize=(8, 6))
ax_3d = fig_3d.add_subplot(111, projection='3d')
ax_3d.scatter(df[selected_x_3d], df[selected_y_3d], df[selected_z_3d])
st.pyplot()
