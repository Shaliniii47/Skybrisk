# sample raw data from clients

Raw_data = [10, 20, 30, 10, 25, 67, 38, 92, 25, 10, 67, None, ""]

def cleaned_data(data):
    Cleaned=[]

    for item in data:
        if item is not None and item !="":
            Cleaned.append(item)
    
    # remove duplicates using sets
    Cleaned = list(set(Cleaned))
    return Cleaned

cleaned_data = cleaned_data(Raw_data)
print("Cleaned Data :", cleaned_data)


#using lambda(), filter(), map()

nums = [10,29,34,25,18,45]

# lambda() and filter()
even = list(filter(lambda n: n%2==0, nums))
print(even)

#map()
double =list(map(lambda n: n*2, even)) 
print(double)