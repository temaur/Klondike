from utils import parse_command
import functions

if __name__ == "__main__":
    cmd_name = ''
    while cmd_name != "exit":
        cmd_name = input("Enter command: ")
        command_name, command_param = parse_command(cmd_name)
        if command_name == "list":
            print(functions.show_storage(cmd_name))
        elif command_name == "add":
            print(functions.add_contact(cmd_name))
        elif command_name == "find":
            print(functions.find_number(cmd_name))
        elif command_name == "delete":
            try:
                print(functions.remove_number(cmd_name))
            except KeyError as e:
                print(str(e).replace("'",""))
        elif command_name == "exit":
            break            
        else:
            print("Unknown command")