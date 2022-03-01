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

            if len(team_name) < 2:                                           # error, so I will try to makethis a length argument
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
Dry run - before generator was added: 

Enter the number of teams: 2
What is the name of team 1: AA
What is the name of team 2: BB
Enter the number of games each team plays: 2
How many time did team AA win: 2
How many time did team BB win: 0
Generating the games to be played in the first round of the tournament...
"""

print("Generating the games to be played in the first round of the tournament...")

