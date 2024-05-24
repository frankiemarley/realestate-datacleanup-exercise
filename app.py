import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# this CSV file contains semicolons instead of comas as separator
ds = pd.read_csv('assets/real_estate.csv', sep=';')

# print(ds)

# ---------------------------------------------------------------------
# max_price = ds['price'].max()

# max_price_index = ds['price'].idxmax()

# max_price_address = ds['address'].loc[max_price_index]
# print(max_price)
# print(max_price_index)
# print(max_price_address)

# print('The house with address '+ str(max_price_address) +' is the most expensive and its price is '+ str(max_price))

# ---------------------------------------------------------------------

# min_price = ds['price'][ds['price']!=0].min() 

# min_price_index = ds['price'].idxmin()

# min_price_address = ds['address'].loc[min_price_index]

# print(min_price)
# print(min_price_index)
# print(min_price_address)

# print('The house with address '+ str(min_price_address) +' is the cheapest and its price is '+ str(min_price))

# ---------------------------------------------------------------------

# min_surface = ds['surface'].min()
# max_surface = ds['surface'].max()

# min_surface_index = ds['surface'].idxmin()
# max_surface_index = ds['surface'].idxmax()

# min_surface_address = ds['address'].loc[min_surface_index]
# max_surface_address = ds['address'].loc[max_surface_index]

# print('The house with address '+ str(min_surface_address) +' is the cheapest and its surface is '+ str(min_surface))
# print('The house with address '+ str(max_surface_address) +' is the cheapest and its surface is '+ str(max_surface))

# ---------------------------------------------------------------------

# populations = ds['level5']
# populations_as_string = ', '.join(str(population) for population in populations)
# print(populations_as_string)

# ---------------------------------------------------------------------

# print(ds.isna().any(axis=0))
# print(ds.isna().any(axis=1))

#----------------------------------------------------------------------
# print(ds)
# newDataframe= ds.dropna(axis=1)
# newDataframe1= newDataframe.dropna(axis=0)
# print(newDataframe1)

# only coulmns were deleted
#[15335 rows x 37 columns]
#[15335 rows x 25 columns]

#----------------------------------------------------------------------
# arroyoprices = ds[ds['level5'] == 'Arroyomolinos (Madrid)']['price']

# mean_arroyoprices = arroyoprices.mean()

# print(mean_arroyoprices)

#----------------------------------------------------------------------
# import matplotlib.pyplot as plt

# arroyomolinos_prices = ds[ds['level5'] == 'Arroyomolinos (Madrid)']['price']

# plt.figure(figsize=(10, 6))
# plt.hist(arroyomolinos_prices.dropna(), bins=20, edgecolor='black')
# plt.title('Histogram of Prices in Arroyomolinos (Madrid)')
# plt.xlabel('Price')
# plt.ylabel('Frequency')
# plt.show()
#----------------------------------------------------------------------

# valdemorillo_prices= ds[ds['level5'] == 'Valdemorillo']['price'].mean()
# galapagar_prices= ds[ds['level5'] == 'Galapagar']['price'].mean()

# print("Average price in Valdemorillo:", str(valdemorillo_prices))
# print("Average price in Galapagar:", str(galapagar_prices))

# if valdemorillo_prices == galapagar_prices:
#     print("The averages of Valdemorillo and Galapagar prices are the same.")
# else:
#     print("The averages of Valdemorillo and Galapagar prices are different.")

#----------------------------------------------------------------------
# ds['pps'] = ds['price'] / ds['surface']

# # valdemorillo_prices= ds[ds['level5'] == 'Valdemorillo']['price'].mean()
# # galapagar_prices= ds[ds['level5'] == 'Galapagar']['price'].mean()

# # valdemorillo_m2= ds[ds['level5'] == 'Valdemorillo']['surface'].mean()
# # galapagar_m2= ds[ds['level5'] == 'Galapagar']['surface'].mean()

# valdemorillo_price_m2 = ds[ds['level5'] == 'Valdemorillo']['pps'].mean()
# galapagar_price_m2 = ds[ds['level5'] == 'Galapagar']['pps'].mean()


# print("Average price/m2 in Valdemorillo:", str(valdemorillo_price_m2))
# print("Average price/m2 in Galapagar:", str(galapagar_price_m2))

# if valdemorillo_price_m2 == galapagar_price_m2:
#     print("The averages of Valdemorillo and Galapagar prices/m2 are the same.")
# else:
#     print("The averages of Valdemorillo and Galapagar prices are different.")

#----------------------------------------------------------------------

# print(len(ds['realEstate_name'].unique()))
# print(len(ds['id_realEstates'].unique()))

#----------------------------------------------------------------------
# population_count = ds['level5'].value_counts()

# print(population_count)


#----------------------------------------------------------------------

# south_belt =['Fuenlabrada','Leganés','Getafe','Alcorcón']
# print(ds[ds['level5'].isin(south_belt)])

#----------------------------------------------------------------------



#----------------------------------------------------------------------
# south_belt = ['Fuenlabrada','Leganés','Getafe','Alcorcón']
# variables = ['price', 'rooms', 'surface', 'bathrooms']

# ds_mean_and_var = ds[ds['level5'].isin(south_belt)]

# mean_price_south_1 = ds_mean_and_var['price'].mean()
# var_price_south_2 = ds_mean_and_var['price'].var()
# mean_rooms_south_3 = ds_mean_and_var['rooms'].mean()
# var_rooms_south_4 = ds_mean_and_var['rooms'].var()
# mean_surface_south_5 = ds_mean_and_var['surface'].mean()
# var_surface_south_6 = ds_mean_and_var['surface'].var()
# mean_bathrooms_south_7 = ds_mean_and_var['bathrooms'].mean()
# var_bathrooms_south_8 = ds_mean_and_var['bathrooms'].var()

# print(f"Mean price value: {mean_price_south_1}")
# print(f"Variance price value: {var_price_south_2}")
# print(f"Mean rooms value: {mean_rooms_south_3}")
# print(f"Variance rooms value: {var_rooms_south_4}")
# print(f"Mean surface value: {mean_surface_south_5}")
# print(f"Variance surface value: {var_surface_south_6}")
# print(f"Mean bathrooms value: {mean_bathrooms_south_7}")
# print(f"Variance bathrooms value: {var_bathrooms_south_8}")

#----------------------------------------------------------------------
# south_belt = ['Fuenlabrada','Leganés','Getafe','Alcorcón']

# ds_south_belt = ds[ds['level5'].isin(south_belt)]

# max_price_south_1 = ds_south_belt[ds_south_belt['level5'] == 'Fuenlabrada'].loc[ds_south_belt[ds_south_belt['level5'] == 'Fuenlabrada']['price'].idxmax()]
# max_price_south_2 = ds_south_belt[ds_south_belt['level5'] == 'Leganés'].loc[ds_south_belt[ds_south_belt['level5'] == 'Leganés']['price'].idxmax()]
# max_price_south_3 = ds_south_belt[ds_south_belt['level5'] == 'Getafe'].loc[ds_south_belt[ds_south_belt['level5'] == 'Getafe']['price'].idxmax()]
# max_price_south_4 = ds_south_belt[ds_south_belt['level5'] == 'Alcorcón'].loc[ds_south_belt[ds_south_belt['level5'] == 'Alcorcón']['price'].idxmax()]

# max1= max_price_south_1['price']
# max2= max_price_south_2['price']
# max3= max_price_south_3['price']
# max4= max_price_south_4['price']

# address1= max_price_south_1['address']
# address2= max_price_south_2['address']
# address3= max_price_south_3['address']
# address4= max_price_south_4['address']

# print(f"Most expensive house in Fuenlabrada: {address1}, {max1}")
# print(f"Most expensive house in Leganés: {address2}, {max2}")
# print(f"Most expensive house in Getafe: {address3}, {max3}")
# print(f"Most expensive house in Alcorcón: {address4}, {max4}")

#----------------------------------------------------------------------

# ds['pps'] = ds['price'] / ds['surface']

# south_belt = ['Fuenlabrada','Leganés','Getafe','Alcorcón']
# ds_mean_and_var = ds[ds['level5'].isin(south_belt)]
# max_price_south = ds_mean_and_var['pps'].max()

# getafe_price_m2 = ds[ds['level5'] == 'Getafe']['pps'].mean()
# alcorcon_price_m2 = ds[ds['level5'] == 'Alcorcón']['pps'].mean()


# print(getafe_price_m2)
# print(alcorcon_price_m2)

#----------------------------------------------------------------------
# south_belt = ['Fuenlabrada','Leganés','Getafe','Alcorcón']

# ds_south_belt = ds[ds['level5'].isin(south_belt)].copy()

# # normalized_df=(df-df.min())/(df.max()-df.min())
# ds_south_belt['normalized_price'] = ds_south_belt.groupby('level5')['price'].transform(lambda x: (x - x.min()) / (x.max() - x.min()))

# df_norm_prices = ds_south_belt[['level5', 'normalized_price']]

# ax = ds_south_belt.groupby('level5')['normalized_price'].plot(kind='hist', bins=20, alpha=0.5, figsize=(10, 6))

# plt.xlabel('Normalized Price')
# plt.ylabel('Frequency')
# plt.title('Normalized Price Distribution for South Belt Populations')
# plt.legend(title='Population')

# plt.show()


#----------------------------------------------------------------------
# south_belt = ['Fuenlabrada', 'Leganés', 'Getafe', 'Alcorcón']
# ds_south_belt = ds[ds['level5'].isin(south_belt)]

# fig, axs = plt.subplots(2,2, figsize=(10, 6))

# ds_1 = ds_south_belt[ds_south_belt['level5'] == 'Fuenlabrada'], label='Fuenlabrada'
# ds_2 = ds_south_belt[ds_south_belt['level5'] == 'Leganés'], label='Leganés'
# ds_3 = ds_south_belt[ds_south_belt['level5'] == 'Getafe'],label='Getafe'
# ds_4 = ds_south_belt[ds_south_belt['level5'] == 'Alcorcón'], label='Alcorcón'

# axs[0, 0].scatter(ds_1['surface'], ds_1['pps'], label='Fuenlabrada')
# axs[0, 0].set_title('Fuenlabrada')
# axs[0, 0].set_xlabel('Surface')
# axs[0, 0].set_ylabel('Price per square')
# axs[0, 0].legend()

# axs[0, 1].scatter(ds_2['surface'], ds_2['pps'], label='Leganés')
# axs[0, 1].set_title('Leganés')
# axs[0, 1].set_xlabel('Surface')
# axs[0, 1].set_ylabel('Price per square')
# axs[0, 1].legend()

# axs[1, 0].scatter(ds_3['surface'], ds_3['pps'], label='Getafe')
# axs[1, 0].set_title('Getafe')
# axs[1, 0].set_xlabel('Surface')
# axs[1, 0].set_ylabel('Price per square')
# axs[1, 0].legend()

# axs[1, 1].scatter(ds_4['surface'], ds_4['pps'], label='Alcorcón')
# axs[1, 1].set_title('Alcorcón')
# axs[1, 1].set_xlabel('Surface')
# axs[1, 1].set_ylabel('Price per square')
# axs[1, 1].legend()

# plt.show()

#----------------------------------------------------------------------

# south_belt = ['Fuenlabrada', 'Leganés', 'Getafe', 'Alcorcón']
# south_belt_df = ds[ds['level5'].isin(south_belt)]

# coordinates_df = south_belt_df[['latitude', 'longitude']]

# coordinates_dict = coordinates_df.to_dict()

# print(coordinates_df)
#------------------------------------------------

# import folium

# # Dictionary creation
# south_belt = ['Fuenlabrada', 'Leganés', 'Getafe', 'Alcorcón']
# south_belt_ds = ds[ds['level5'].isin(south_belt)]

# # Create a copy of the DataFrame to avoid SettingWithCopyWarning
# coordinates_ds = south_belt_ds[['latitude', 'longitude', 'address', 'level5']].copy()

# # Convert latitude and longitude columns to strings if they are not already
# if coordinates_ds['latitude'].dtype != 'object':
#     coordinates_ds['latitude'] = coordinates_ds['latitude'].astype(str)
# if coordinates_ds['longitude'].dtype != 'object':
#     coordinates_ds['longitude'] = coordinates_ds['longitude'].astype(str)

# # replace commas with periods and convert to floats
# coordinates_ds['latitude'] = coordinates_ds['latitude'].str.replace(',', '.').astype(float)
# coordinates_ds['longitude'] = coordinates_ds['longitude'].str.replace(',', '.').astype(float)

# # Madrid 
# center_lat, center_lon = 40.4168, -3.7038

# m = folium.Map(location=[center_lat, center_lon], zoom_start=10)
# colors = {
#     'Fuenlabrada': 'red',
#     'Leganés': 'blue',
#     'Getafe': 'green',
#     'Alcorcón': 'purple'
# }

# for index, row in coordinates_ds.iterrows():
#     lat, lon = row['latitude'], row['longitude']
#     location_name = row['address']
#     level5 = row['level5']
#     color = colors.get(level5, colors.get(location_name, 'gray')) 
#     folium.CircleMarker(
#         location=[lat, lon],
#         radius=3,
#         color=color,
#         fill=True,
#         fill_opacity=0.5,
#         popup=location_name
#     ).add_to(m)

# m
