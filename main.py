from utils.functions import open_json, convert_to_datetime, sort_data, publish_operations

NUMBER_OF_LAST_OPERATIONS = 5  #set the number of last operations to display

def main():
    data = open_json("operations.json")
    convert_to_datetime(data)
    sorted_data = sort_data(data)
    publish_operations(sorted_data, NUMBER_OF_LAST_OPERATIONS)

if __name__ == '__main__':
    main()