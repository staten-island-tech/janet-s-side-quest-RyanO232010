## This function opens the CSV for You!
def csv_to_list(file_path):
    data_list = []
    
    with open(file_path, 'r') as file:
        for line in file:
            row = line.strip().split(',')
            row = [int(value) if value.isdigit() else value for value in row]
            data_list.append(row)

    return data_list


file_path = "SalesData.csv"  
data = csv_to_list(file_path)
row_totals = {}
def average(data):
    for row in data[1:]:  # Skip the first row
        store_name = row[0]  # First column is the store name
        sales = map(int, row[1:])  # Convert sales to numbers
        row_totals[store_name] = sum(sales)  # Sum up sales for the store
        sum(sales)%30

    return row_totals
totals = average(data)
print(totals)

    

