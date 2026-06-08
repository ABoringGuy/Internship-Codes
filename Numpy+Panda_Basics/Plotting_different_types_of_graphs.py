import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(2,2)
sales_of_year_2020=int(input("Enter the sales of the year 2020: "))
sales_of_year_2021=int(input("Enter the sales of the year 2021: "))
sales_of_year_2022=int(input("Enter the sales of the year 2022: "))
sales_of_year_2023=int(input("Enter the sales of the year 2023: "))
sales_of_year_2024=int(input("Enter the sales of the year 2024: "))


years=[2020,2021,2022,2023,2024]

sales=np.array([sales_of_year_2020, sales_of_year_2021, sales_of_year_2022, sales_of_year_2023, sales_of_year_2024])

ax[0,0].plot(years, sales,label="sales")
ax[0,0].set_xticks(years)
ax[0,0].set_xlabel("Years")
ax[0,0].set_ylabel("Sales")

ax[1,0].scatter(years, sales,label="sales")
ax[1,0].set_xticks(years)
ax[1,0].set_xlabel("Years")
ax[1,0].set_ylabel("Sales")

ax[0,1].pie(sales, labels=years)

plt.show()