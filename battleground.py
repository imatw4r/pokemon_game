from pokemon import Pokemon
from player import Player


def battle_arena(pretendent: Pokemon, champion: Pokemon) -> None:
    if not pretendent or not champion:
        return

    faster_pokemon, slower_pokemon = sorted([pretendent, champion], key=Pokemon.get_speed, reverse=True)

    while faster_pokemon.is_alive() and slower_pokemon.is_alive():
        faster_pokemon.attack(slower_pokemon)
        if slower_pokemon.is_alive():
            slower_pokemon.attack(faster_pokemon)


def battleground(player: Player, computer: Player):
    print("Choose one starting pokemon: ")
    player.show_pokedex()
    old_player_pokemon = player.choose_pokemon()

    old_pc_pokemon = computer.choose_pokemon()

    player_score = 0
    computer_score = 0
    while player_score != 3 and computer_score != 3:
        battle_arena(old_player_pokemon, old_pc_pokemon)
        if old_player_pokemon.is_alive():
            print(f"Your pokemon({old_player_pokemon.name}) wins")
            computer_score += 1
            if computer_score != 3:
                new_computer_pokemon = computer.choose_pokemon()
                print("Selected computer pokemon:", new_computer_pokemon)
                old_pc_pokemon = new_computer_pokemon
        else:
            print(f"Your pokemon({old_player_pokemon.name}) lost")
            player_score += 1
            if player_score != 3:
                new_player_pokemon = player.choose_pokemon()
                print("Selected player pokemon:", new_player_pokemon)
                old_player_pokemon = new_player_pokemon
    if player_score == 3:
        print(f"Your pokemons lose with trainer {computer.name}. KEKW")
    else:
        print(f"Your pokemons win with trainer {computer.name}. PogU")
