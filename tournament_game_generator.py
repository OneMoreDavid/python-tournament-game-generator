"""    
- need to take number of teams as an input
-- need to handle errors
"""

def get_number_of_teams():
       
    while True:
        num_teams = int(input('Enter the number of teams: '))

        if num_teams >= 2:
            break

        print('It is a competition, the minimum number is clearly 2')

    return num_teams


"""
- need to take the name of each of the teams (store them somehow)
-- need to handle errors
"""

def get_team_names(num_teams):

    teams = []

    for num in num_teams:
        while True:
            team_name = input(f"What is the name of team {num + 1}: ")

            if team_name < 2:
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
    pass


num_teams = get_number_of_teams()
team_names = get_team_names(num_teams)
games_played = get_number_of_games_played(num_teams)
team_wins = get_team_wins(team_names, games_played)

'''
the team with the fewer wins needs to play at home

the team with fewer wins plays team with most wins
-- team with second fewest wins plays team with second most wins and so on
''' 

print("Generating the games to be played in the first round of the tournament...")
