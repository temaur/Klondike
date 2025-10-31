from storage import get_storage, get_contact, add_to_storage, load_storage, find_contact, remove_contact
from utils import parse_command
# Просмотр справочника/ Просмотр номера по имени
def show_storage(cmd_name)-> dict:
    command_name, command_param = parse_command(cmd_name)
    if command_param == "":
        return get_storage()
    else:
        return get_contact(command_param)
#if __name__ == "__main__":
#    print(show_storage('list Иван Иванов'))

# Добавление контакта
def add_contact(cmd_name):
    command_name, command_param = parse_command(cmd_name)
    parts_of_param = command_param.strip().split()
    if len(parts_of_param) >= 2:
        contact_name = ' '.join(parts_of_param[0:-1])
        contact_number = parts_of_param[-1]
        return add_to_storage(contact_name, contact_number)
if __name__ == "__main__":
    add_contact('add Темирлан 774823')
    print(show_storage('list'))

# Поиск контакта по номеру телефона
def find_number(cmd_name):
    command_name, command_param = parse_command(cmd_name)
    return find_contact(command_param)

# Удаление контакта    
def remove_number(cmd_name):
    command_name, command_param = parse_command(cmd_name)
    return remove_contact(command_param) 
    
        