import pandas as pd

Make = pd.Series(['toyato', 'honda', 'toyata', 'bmw', 'nissan',
                  'toyato', 'honda', 'honda', 'toyato', 'nissan'])
Color = pd.Series(['white', 'Red', 'Blue', 'Black', 'White',
                   'Green', 'Blue', 'Blue', 'White', 'White'])
Odometer = pd.Series([15200, 87420, 36920, 154630, 125633,
                      78990, 256491, 369871, 365891, 36222])
Doors = pd.Series([4, 4, 4, 4, 4, 4, 4, 4, 4, 4])
price = pd.Series([400000, 5000000, 60000000, 455000, 3600000,
                   560000, 980000, 4690000, 780000, 963000])

cars_data = pd.DataFrame(
    {'Make': Make, 'Color': Color, 'Odometer': Odometer, 'Doors': Doors, 'Price': price})
# print(cars_data)


# Making Columns  using list
fuel_economy = [7.5, 5.6, 6.2, 9.3, 7.5, 6.5, 7.2, 7.4, 3.1, 4.3]
cars_data['Fuel Per 100KM'] = fuel_economy

print(cars_data)

cars_data['Total Fuel Used'] = cars_data['Odometer'] / \
    100 * cars_data['Fuel Per 100KM']
print(cars_data)

# create column uisng single value

cars_data['Number of Wheels'] = 4
print(cars_data)

cars_data['Passed Road Safty'] = True
print(cars_data)

cars_data_shuffle = cars_data.sample(frac=0.2)
print(cars_data_shuffle)

cars_data['Odometer'] = cars_data['Odometer'].apply(lambda x: x / 1.6)
print(cars_data)
cars_data.to_csv("../data/Cars_data.csv", index=False)