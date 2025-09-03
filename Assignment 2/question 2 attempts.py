# station_max_rows = combined_data.loc[combined_data.groupby("STATION_NAME")["Temp Range"].idxmax()] #get the rows with the maximum temperature range for each station
# range_large = station_max_rows.sort_values(by="Temp Range", ascending = False).head(5) #get the top 5 largest ranges
# station_min_rows = combined_data.loc[combined_data.groupby("STATION_NAME")["Temp Range"].idxmin()] #get the rows with the minimum temperature range for each station
# range_small = station_min_rows.sort_values(by="Temp Range", ascending = True).head(5)



# station_ranges_max = combined_data.groupby("STATION_NAME")["Temp Range"].max().reset_index() #avoid duplicate stations from data sets
# sorted_data = station_ranges_max.sort_values(by = "Temp Range", ascending = True) #sort the dataframe by the temperature range
# range_large = sorted_data.tail(5) #get the bottom 5 largest ranges

# station_ranges_min = combined_data.groupby("STATION_NAME")["Temp Range"].min().reset_index() #avoid duplicate stations from data sets
# sorted_data = station_ranges_min.sort_values(by = "Temp Range", ascending = True) #sort the dataframe by the temperature range
# range_small = sorted_data.head(5) #get the top 5 smallest ranges

# row_max = extremes_data.max(axis=1) #find the maximum value temperature in each row
# row_min = extremes_data.min(axis=1) #find the minimum value temperature in each row
# temp_range = row_max - row_min #range calculation

# sorted_data = combined_data.sort_values(by="Temp Range", ascending = True)
# range_large = sorted_data.tail(5) #get the bottom 5 largest ranges
# range_small = sorted_data.head(5) #get the top 5 smallest ranges

# with open(r"C:\Users\Gabriel\Desktop\Assignment 2\temperature_ranges.txt", "w") as f:
#   print("5 largest range/s:", file=f)
#   print(range_large[["STATION_NAME", "Temp Range"]].to_string(index = False), file=f) #largest ranges
#   print("\n5 smallest range/s:", file=f)
#   print(range_small[["STATION_NAME", "Temp Range"]].to_string(index = False), file=f) #smallest ranges

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# dev_list = extremes_data.std(axis=1) #deviate each station's temperature data
# combined_data["Deviation"] = dev_list #create the list
# station_devs = combined_data.groupby("STATION NAME")["Deviation"]
# sorted_data2 = combined_data.sort_values(by="Deviation")