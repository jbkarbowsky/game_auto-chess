# main.py

from shop import buy_units
from game_logic import battle_round, check_victory, plot_damage_stats, display_unit_health
from utils import apply_initial_faction_buffs
import traceback

def play_game_round(max_rounds=5):
    """
    Main function to play the game.
    """
    try:
        budget = 20  # Starting budget for both players

        # Player 1 buys units
        print("Player 1, build your army!")
        player1_units = buy_units(budget, player_number=1)

        # Player 2 buys units
        print("\nPlayer 2, build your army!")
        player2_units = buy_units(budget, player_number=2)

        # Apply initial faction buffs
        apply_initial_faction_buffs(player1_units)
        apply_initial_faction_buffs(player2_units)

        round_number = 1
        while round_number <= max_rounds:
            print(f"\n--- Round {round_number} ---")
            battle_round(player1_units, player2_units)

            # Display health after each round
            display_unit_health(player1_units, player2_units, player1_name="Player 1", player2_name="Player 2")

            result = check_victory(player1_units, player2_units, player1_name="Player 1", player2_name="Player 2")
            if result:
                print(f"\n{result}")
                break

            round_number += 1

        # Check victory based on remaining health if max rounds reached
        if not result:
            player1_health = sum(unit.health for unit in player1_units if unit.is_alive())
            player2_health = sum(unit.health for unit in player2_units if unit.is_alive())
            if player1_health > player2_health:
                result = "Player 1 wins by remaining health!"
            elif player2_health > player1_health:
                result = "Player 2 wins by remaining health!"
            else:
                result = "Draw by equal remaining health!"

            print(f"\n{result}")

        # Display damage statistics
        plot_damage_stats(player1_units, player2_units, player1_name="Player 1", player2_name="Player 2")

    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    play_game_round(max_rounds=5)
