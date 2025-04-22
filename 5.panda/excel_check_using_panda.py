
import pandas as pd

sheet = pd.read_excel("users.xlsx")


filtered_users = sheet[(sheet["Ηλικία"] > 30) & (sheet["Ενεργός"] == True)]
print("Users over 30 and active:")
print(filtered_users)

average_age = sheet["Ηλικία"].mean()
print("\nAverage age of all users:", round(average_age, 2))

active_users = df[df["Ενεργός"] == True]
average_salary = active_users["Μισθός (€)"].mean()
print("Average salary of active users: €", round(average_salary, 2))

top_30 = filtered_users.head(30)
top_30.to_excel("active_users_over30.xlsx", index=False)
print("\nSaved first 30 active users over 30 to 'active_users_over30.xlsx'")