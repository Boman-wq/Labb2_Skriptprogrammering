import csv, json, os
#######Globala Variablar#######
csv_file_path = "labb2-personer.csv"
json_file_path = "labb2_personer.json"
json_startup_file = "labb2_personer.json"


def read_csv_file():
    try:
        with open(csv_file_path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
        input()
    except FileNotFoundError:
        input("Det finns ingen csv fil att läsa ifrån")

def read_json_data():
    while True:
        try:
            with open(json_file_path, "r", encoding="utf-8") as file:
                obj = json.load(file)
                i = 0
                for list_obj in obj:
                    username = list_obj["Användarnamn"]
                    first_name = list_obj["Förnamn"]
                    last_name = list_obj["Efternamn"]
                    email = list_obj["epost"]
                    print(f"Index       : {i}")
                    print(f"Användarnamn: {username}")
                    print(f"Förnamn     : {first_name}")
                    print(f"Efternamn   : {last_name}")
                    print(f"E-mailadress: {email}")
                    print("\n")
                    i=i+1
            break
        except FileNotFoundError:
            try:
                with open(csv_file_path, "r", encoding="utf-8") as file:
                        reader = csv.reader(file, delimiter=";")
                        next(reader)
                        data = []
                        i = 0
                        for row in reader:
                            data.append({"Användarnamn": row[0], "Förnamn": row[1], "Efternamn": row[2], "epost": row[3]})

                with open(json_file_path, "w", encoding="utf-8") as file:
                    json.dump(data, file, indent=4, ensure_ascii=False)
            except FileNotFoundError:
                input("Det finns ingen csv fil att läsa ifrån")
                return


def add_person_to_list(time_stamp):
    while True:
        if os.path.isfile(json_file_path) == True:
            usernamn = input("Skriv in Användarnamn:\n")
            first_name = input("Skriv in Förnamn:\n")
            last_name = input("Skriv in efternamn:\n")
            email = input ("Skriv in e-posten:\n")
            
            with open(json_file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            with open("labb2_personer_{}.json".format(str(time_stamp)), "w", encoding="utf-8") as file:
                data.append({"Användarnamn": usernamn, "Förnamn": first_name, "Efternamn": last_name, "epost": email})
                json.dump(data, file, indent=4, ensure_ascii=False)
            save_json_file("labb2_personer_{}.json".format(str(time_stamp)))
            break
        else:
            input("Det finns ingen json fil, tryck på enter för att skapa upp en json fil.")
            read_json_data()

    

def remove_person_from_list(time_stamp):
    read_json_data()
    new_data = []
    with open(json_file_path, "r", encoding="utf-8") as file:
        obj = json.load(file)
        index_length = len(obj)-1
    print("Vilket indexnummer vill du ta bort?")
    print(f"välj ett nummer mellan 0-{index_length}\n")
    delete_data = int_check(index_length)
    i=0
    for list_obj in obj:
        if i == int(delete_data):
            pass
            i=i+1
        else:
            new_data.append(list_obj)
            i=i+1

    with open("labb2_personer_{}.json".format(str(time_stamp)), "w", encoding="utf-8") as file:
        json.dump(new_data, file, indent=4, ensure_ascii=False)
    
    
    save_json_file("labb2_personer_{}.json".format(str(time_stamp)))

def json_to_startup(time_stamp):
    if os.path.isfile("labb2_personer_{}.json".format(str(time_stamp))) == True:
        user_input = input("Är du säker på att du vill spara filen? y/n\n")
        if user_input.upper() == "Y":
            with open("labb2_personer_{}.json".format(str(time_stamp)), "r", encoding="utf-8") as file:
                data = json.load(file)
                input("Filen är sparad")
            delete_file(time_stamp)
            save_json_file(json_startup_file)

            with open(json_startup_file, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
        elif user_input.upper() == "N":
            return
    else:
        input("Finns ingen fil att spara :)")


def save_json_file(json_file):
    global json_file_path
    json_file_path = json_file

def delete_file(time_stamp):
    os.remove("labb2_personer_{}.json".format(str(time_stamp)))

def close_program(time_stamp):
        if os.path.isfile("labb2_personer_{}.json".format(str(time_stamp))) == True:
            user_input = input("Är du säker på att du vill avsluta programmet utan att spara? Vill du spara ändringarna? y/n\n")
            if user_input.upper() == "N":
                delete_file(time_stamp)
            elif user_input.upper() == "Y":
                json_to_startup(time_stamp)
        else:
            print("Stänger av programmet....")


def int_check(max_value):
    while True:
        try:
            user_input = int(input())
            if user_input >= 0 and user_input <= max_value:
                return user_input
            else:
                print(f"Välj ett index mellan 0 och {max_value}")
        except ValueError:
            print("Skriv ett heltal")