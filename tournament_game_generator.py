"""    
- need to take number of teams as an input
-- need to handle errors
"""

def get_number_of_teams():
       
    while True:
        num_of_teams = int(input('Enter the number of teams: '))

        if num_of_teams >= 2:
            break

        print('It is a competition, the minimum number is clearly 2')

    return num_of_teams


"""
- need to take the name of each of the teams (store them somehow)
-- need to handle errors
"""

def get_team_names(num_teams):

    teams = []

    for num in range(num_teams):                                        # I was getting an error here, so made this a range
        """
        line 28, in get_team_names 
            for num in num_teams:
        TypeError: 'int' object is not iterable
        """
        while True:
            team_name = input(f"What is the name of team {num + 1}: ")

            if len(team_name) < 2:                                     # error, so I will try to makethis a length argument
                """
                line 37, in get_team_names
                    if team_name < 2:
                TypeError: '<' not supported between instances of 'str' and 'int'
                """
                print("Team names need at least 2x char!")
            else:
                break

        teams.append(team_name)


    return teams


"""
- how many games did EACH team play? 
-- need to handle errors
"""

def get_number_of_games_played(num_teams):

    while True:
        played = int(input('Enter the number of games each team plays: '))

        if played >= num_teams - 1:
            break

        print(f'It is a competition, each team needs to play at least {num_teams - 1} times')

    return played

"""
- how many wins did [n] team have
-- need to handle errors
"""
def get_team_wins(team_names, games_played):
    
    teams_win = []
    
    for name in team_names:
        while True:
            wins = int(input(f"How many time did team {name} win: "))

            if wins > games_played:
                print(f"Erm, no, the maximum number of games played can be {games_played}")
            elif wins < 0:
                print("Nope, can't be less than 0")
            else:
                break

        teams_win.append((name, wins))

    return teams_win

'''
the team with the fewer wins needs to play at home

the team with fewer wins plays team with most wins
-- team with second fewest wins plays team with second most wins and so on
''' 

num_teams = get_number_of_teams()
team_names = get_team_names(num_teams)
games_played = get_number_of_games_played(num_teams)
team_wins = get_team_wins(team_names, games_played)

"""
>>> Dry run - before generator was added: 

Enter the number of teams: 2
What is the name of team 1: AA
What is the name of team 2: BB
Enter the number of games each team plays: 2
How many time did team AA win: 2
How many time did team BB win: 0
Generating the games to be played in the first round of the tournament...
"""


print(team_wins)                                                       # just to see >> [('AA', 2), ('BB', 0)]

def sort_the_teams(sort_by):                                          # I know this should be higher in program, but for now..... 
    return sort_by[1]

sorted_teams_by_wins = sorted(team_wins, key=sort_the_teams)

paired_games = []

how_many_games = len(sorted_teams_by_wins)//2

"""
now I need a [FOR] loop to basically do: 

for [each_game] of [how_many_games]:
    [home_team] = [LOWEST_score]
    [away_team] = [HIGHEST_score] 
    update my current empty list [paired_games] >>> paired_games.append([home_team, away_team])

and to output this to the screen using another [FOR] loop as unknown number of teams at this stage

for [gameX] in [paired_games]:       # my list
    home_team, away_team = gameX
    print(f"Home: {home_team} VS Away: {away_team}")

>>> where score = number of wins
"""

for each_game in range(how_many_games):
    home_team = sorted_teams_by_wins[each_game][0]
    away_team = sorted_teams_by_wins[num_teams - 1 - each_game][0]
    paired_games.append([home_team, away_team])

print(paired_games)
"""
>>> OUTPUT just to see >>> 

Enter the number of teams: 3
What is the name of team 1: aa
What is the name of team 2: bb
What is the name of team 3: cc
Enter the number of games each team plays: 2
How many time did team aa win: 1
How many time did team bb win: 2
How many time did team cc win: 1
Generating the games to be played in the first round of the tournament...
[('aa', 1), ('bb', 2), ('cc', 1)]
[['aa', 'bb']]

ONE THING I NOTICED IS THAT MY CODE IS ALLOWING UNEVEN NUMBER OF PLAYERS< THEREFORE THE FINAL TOURNAMENT MAY HAVE SOME TEAMS WITHOUT A CHALLENGER??
--- need to check notes to see if this was something I should error against?? 
"""
print("Generating the games to be played in the first round of the tournament...")
for gameX in paired_games:
    home_team, away_team = gameX
    print(f"HOME: {home_team} VS AWAY: {away_team}")

"""
>>> OUTPUT >>>

Enter the number of teams: 4
What is the name of team 1: team1
What is the name of team 2: team2
What is the name of team 3: team3
What is the name of team 4: team4
Enter the number of games each team plays: 3
How many time did team team1 win: 4
Erm, no, the maximum number of games played can be 3
How many time did team team1 win: 3
How many time did team team2 win: 2
How many time did team team3 win: 2
How many time did team team4 win: 1
[('team1', 3), ('team2', 2), ('team3', 2), ('team4', 1)]
[['team4', 'team1'], ['team2', 'team3']]
Generating the games to be played in the first round of the tournament...
HOME: team4 VS AWAY: team1
HOME: team2 VS AWAY: team3

-===-===-===-===-

I THINK THIS IS WORKING FINE - possibly need to check error handling
"""