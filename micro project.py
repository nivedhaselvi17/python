import datetime
import time
class TreeNode:
    def __init__(self, scenario, choice_a=None, choice_b=None):
        self.scenario = scenario
        self.choice_a = choice_a
        self.choice_b = choice_b
        self.answer_a = ""
        self.answer_b = ""
def build_game_tree():
    # Leaves
    gold_mine = TreeNode("Victory! You discovered an ancient gold mine and became legendary.")
    dragon_cave = TreeNode("Game Over. You walked right into a sleeping dragon's lair.")
    safe_village = TreeNode("Victory! You safely navigated out of the forest into a cozy village.")
    lost_swamp = TreeNode("Game Over. You sank deep into the quicksand of the forgotten swamp.")

    # Intermediate Nodes
    left_path = TreeNode("The path narrows. Do you climb the rocky mountain ridge or enter the dark cavern?")
    left_path.choice_a = gold_mine; left_path.answer_a = "Climb mountain ridge"
    left_path.choice_b = dragon_cave; left_path.answer_b = "Enter dark cavern"

    right_path = TreeNode("You hear rushing water. Do you build a raft to cross or follow the river bank downstream?")
    right_path.choice_a = safe_village; right_path.answer_a = "Build a raft"
    right_path.choice_b = lost_swamp; right_path.answer_b = "Follow river bank"

    # Root
    root = TreeNode("You stand at the entrance of a mysterious forest. Do you go Left towards the mountains or Right towards the river?")
    root.choice_a = left_path; root.answer_a = "Go Left"
    root.choice_b = right_path; root.answer_b = "Go Right"
    return root

def play_game():
    root = build_game_tree()
    current = root
    log_file = open("game_log.txt", "a")
    log_file.write(f"\n--- Session Started at {datetime.datetime.now()} ---\n")

    print("\n=== INTERACTIVE DECISION TREE ADVENTURE GAME ===")
    while current.choice_a or current.choice_b:
        print(f"\n[Scenario]: {current.scenario}")
        print(f"1. {current.answer_a}")
        print(f"2. {current.answer_b}")
        choice = input("Enter choice (1 or 2): ").strip()
       
        if choice == '1':
            log_file.write(f"{datetime.datetime.now()}: Chose -> {current.answer_a}\n")
            current = current.choice_a
        elif choice == '2':
            log_file.write(f"{datetime.datetime.now()}: Chose -> {current.answer_b}\n")
            current = current.choice_b
        else:
            print("Invalid choice! Try again.")
           
    print(f"\n[Final Outcome]: {current.scenario}")
    log_file.write(f"{datetime.datetime.now()}: Outcome -> {current.scenario}\n")
    log_file.close()

if __name__ == '__main__':
    play_game()

