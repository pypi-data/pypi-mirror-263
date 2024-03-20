from JSD_project.enums_consts import DIRECTIONS, display_help
from JSD_project.interpreter import parse_dsl

global game_world


def process_command(command):
    commands_mapping = {
        "move": game_world.player.move,
        "take": game_world.player.take,
        "drop": game_world.player.drop,
        "use": game_world.player.use,
        "open": game_world.player.open,
        "inc": game_world.player.inc_stat,
        "equip": game_world.player.equip,
        "unequip": game_world.player.unequip,
        "info": game_world.player.print_item_info
    }
    try:
        action, arg = command.split(" ", 1)
        if action in commands_mapping:
            text = ""
            if "move" in command:
                if game_world.current_enemy is not None:
                    print("You shall not pass")
                    return
                if command in DIRECTIONS:
                    text, moved = commands_mapping[action](arg, game_world)
                    if moved:
                        game_world.prev_direction = arg
            elif "inc" in command:
                text = commands_mapping[action](arg)
            else:
                text = commands_mapping[action](arg, game_world)
            print(text)
            print(game_world.player.print_self())
        else:
            print("Invalid command")
    except Exception as e:
        if command == "help":
            display_help()
        elif command == "inventory":
            print(game_world.player.print_inventory())
        elif command == "health":
            print(game_world.player.print_health())
        elif command == "attack" and game_world.current_enemy is not None:
            game_world.attack_enemy()
        elif command == "flee":
            game_world.flee()
        elif command == "stats":
            game_world.player.print_stats()
        else:
            print("Invalid command")


def initial_setup():
    global game_world
    game_world = parse_dsl()
    print("Enter 'help' for help")
    print(game_world.player.print_self())


def run_main():
    initial_setup()

    while game_world.player.position != game_world.final_position:
        user_input = input(">>").strip()
        process_command(user_input)


if __name__ == "__main__":
    run_main()