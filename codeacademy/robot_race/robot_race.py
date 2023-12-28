from collections import deque, Counter, namedtuple
from time import time, sleep
import robot_race_functions as rr
import pdb


maze_file_name = './robot_race/maze_data_1.csv'
seconds_between_turns = 0.3
max_turns = 35

# Initialize the robot race
maze_data = rr.read_maze(maze_file_name)
rr.print_maze(maze_data)
walls, goal, bots = rr.process_maze_init(maze_data)
print(walls, goal, bots)
# print(bots)
# Populate a deque of all robot commands for the provided maze
# pdb.set_trace()
robot_moves = deque()
num_of_turns = 0

while not rr.is_race_over(bots) and num_of_turns < max_turns:
    # For every bot in the list of bots,
    # if the bot has not reached the end, add a new move to the robot_moves deque
    # Add your code below!
    unfinished_bots = filter(lambda x: not x.has_finished, bots)

    for bot in unfinished_bots:
        print(bot)
        name, move, hit_wall = rr.compute_robot_logic(walls, goal, bot)
        print(name, move, hit_wall)
        robot_moves.append((name, move, hit_wall))

    num_of_turns += 1
    print(num_of_turns)

print(robot_moves)
# Count the number of moves based on the robot names
# Add your code below!
move_counts = Counter(move[0] for move in robot_moves)
print(move_counts)

# Count the number of collisions by robot name
# Add your code below!
collision_counts = Counter(move[0] for move in robot_moves if move[-1])
print(collision_counts)

# Create a namedtuple to keep track of our robots' points
# Add your code below!
BotScoreData = namedtuple(
    "BotScoreData", field_names="name, num_moves, num_collisions, score")

# Calculate the scores (moves + collisions) for each robot and append it to bot_scores
bot_scores = []
# Add your code below!
for bot in bots:
    bot_scores.append(BotScoreData(
        bot.name, move_counts[bot.name], collision_counts[bot.name], move_counts[bot.name]+collision_counts[bot.name]))


# rr.print_results(bot_scores)
# Populate a dict to keep track of the robot movements

# Add your code below!
bot_data = {bot.name: bot for bot in bots}

# Move the robots and update the map based on the moves deque
while len(robot_moves) > 0:
    # Make sure to pop moves from the front of the deque
    # Add your code below!
    move = robot_moves.popleft()
    this_bot = move[0]
    this_move = move[1]
    # process the move
    bot_data[this_bot].process_move(this_move)
    # Update the maze characters based on the robot positions and print it to the console
    rr.update_maze_characters(maze_data, bots)
    rr.print_maze(maze_data)
    sleep(seconds_between_turns - time() % seconds_between_turns)

# Print out the results!
rr.print_results(bot_scores)
