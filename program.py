import module as run
import datetime , time

stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d-%H.%M")

def main():
    while True:
        print("1. Läs in orginalfil\n2. Visa json-data\n3. Lägg till personer\n4. Ta bort person\n5. Spara fil\n6. Avsluta")
        menu_input = input()
        if menu_input == "1":
            run.read_csv_file()
        elif menu_input == "2":
            run.read_json_data()
        elif menu_input == "3":
            run.add_person_to_list(stamp)
        elif menu_input == "4":
            run.remove_person_from_list(stamp)
        elif menu_input == "5":
            run.json_to_startup(stamp)
        elif menu_input == "6":
            run.close_program(stamp)
            break

if __name__ == "__main__":
    main()