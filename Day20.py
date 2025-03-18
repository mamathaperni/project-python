#matplotlib which is used for visualization.
# visualization is done using matplotlib library.
# it is used in story telling or when we are prsenting something to a manger etc..

import matplotlib.pyplot as plt

# if we need to plot simple graph
# eg:Hours vs Marks
 # Hours:2,4,6,8,10
 # Marks:90,85,95,80,92


# hours=[2,4,6,8,10]
# marks=[90,85,95,80,92]

# plt.scatter(hours,marks)
# plt.xlabel("Hours studied")
# plt.ylabel("Marks obtained")
# plt.title("Hours vs Marks")
# plt.show()

# if we have 2 sets of data
hours=[2,4,6,8,10]
M_marks=[90,85,95,80,92]
E_marks=[10,30,45,69,45]


# plt.scatter(hours,M_marks) #FOR SCATTER
# plt.scatter(hours,E_marks)

# plt.bar(hours,M_marks) # FOR BAR CHART
# plt.bar(hours,E_marks)

plt.plot(hours,M_marks) # FOR LINE CHART
plt.plot(hours,E_marks)

plt.xlabel("Hours studied")
plt.ylabel("Marks obtained")
plt.title("Hours vs Marks")
plt.legend(["Maths","English"])
plt.show()



# we can also make different graphs like bar graph, pie chart etc..