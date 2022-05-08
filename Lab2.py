def display_main_menu():
    print("display_main_menu")

def get_user_input():
    print("Enter some numbers separated by commas (e.g 5, 67, 32)")

    str_list=[]
    num_list=[]
    str = input()
    str_list = str.split(",")
    # convert string to int or float
    for item in str_list:
        num_list.append(float(item))

    return num_list

def calc_average_temperature(list):
    sumoflist = sum(list)
    countoflist = len(list)
    avg = sumoflist/countoflist
    return avg

def calc_min_max_temperature(list):
    minimum = int(min(list))
    maximum = int(max(list))
    maxmin = [minimum, maximum]
    return maxmin

def sort_temperature(list):
    sortedList=sorted(list)
    return sortedList


def calc_median_temperature(list):
    n = len(list)
    if n%2 ==0:
        median1=list[n//2]
        median2=list[n//2-1]
        median=(median1+median2)/2
    else:
        median=list[n//2]
    return median



def main():
    print("ET0735 (DevOps for AIoT - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_average_temperature(num_list)
    print("average value of all temperature readings: ", calc_average_temperature(num_list))
    calc_min_max_temperature(num_list)
    print('minimum and maximum temperature: ', calc_min_max_temperature(num_list))
    sort_temperature(num_list)
    print("the sorted list is: ", sort_temperature(num_list))
    calc_median_temperature(sort_temperature(num_list))
    print('the median temperature is: ',calc_median_temperature(sort_temperature(num_list)))

    #print(num_list)
    #print(str(type(num_list[0])))




if __name__ == "__main__":
    main()