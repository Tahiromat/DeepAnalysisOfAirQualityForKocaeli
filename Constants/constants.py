class ConstantsClass:
    
    def create_list_for_stations(os):
        station_name_list = []
        for file in os.listdir("/home/tahir/Documents/DataScience/DeepAnalysis/Dataset/"):
            file_name, file_ext = file.split(".")
            station_name_list.append(file_name)
        return station_name_list


