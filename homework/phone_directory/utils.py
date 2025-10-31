def parse_command(cmd_name: str) -> tuple[str, str]:
    parts = cmd_name.strip().split(" ", 1)
    command_name = parts[0]
    command_param = parts[1] if len(parts) > 1 else ""
    return command_name, command_param
          