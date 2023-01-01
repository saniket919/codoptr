# Save the data in an Excel file
data = response.json()
df = pd.DataFrame(data)
df.to_excel("data.xlsx", index=False)
print("task done")