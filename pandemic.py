import random

roles_db = {
    'Researcher':
        "Can GIVE any card to a player in the same location. "
        "The card can be shared in either player's turn. "
        "Standard rules apply for RECEIVING cards.",
    'Scientist':
        "Needs only 4 City cards (normally 5) of the same color to Discover a Cure.",
    'Medic':
        "Removes all cubes of the chosen color when Treating Disease. "
        "Automatically removes all cubes of cured diseases from current location, even outside of his turn.",
    'Dispatcher':
        "For 1 action, can move any pawn to any city containing another pawn. "
        "With permission, can MOVE other players' pawns using his own action points and city cards. "
        "Does NOT use players' cards for direct/charter flights.",
    'Operations Expert':
        "Can build a research station in the current city without having/using a card. "
        "Once per turn, can move anywhere from a research station by discarding any city card.",
    'Contingency Planner':
        "For 1 action, recovers an Event card from the Discard Pile. "
        "The card is not counted as part of the hand. "
        "Only 1 Event card can be set aside at a time.",
    'Quarantine Specialist':
        "Prevents the placement of cubes in their current city and those connected to it.",
    'Field Operative':
        "Once per turn, for 1 action, can remove and store 1 cube from the city they are in. "
        "Can discover a Cure with three cards and three stored cubes of the same color.",
    'Generalist':
        "Can perform up to 5 actions per turn, instead of the usual 4.",
    'Containment Specialist':
        "When entering a city with 2+ cubes of the same color, removes 1 cube for that disease. "
        "If multiple diseases have 2+ cubes, removes 1 from each.",
    'Epidemiologist':
        "Once per turn, can take any City card from another player in the same city. "
        "The ability does not consume action points.",
    'Archivist':
        "Can hold up to 8 City cards (normal limit: 7). "
        "Once per turn, for 1 action, recovers the City card that matches their location from the Discard Pile.",
    'Troubleshooter':
        "Can look at the top N cards of the Infection deck, where N is the current Infection Rate. "
        "Keeps the card when flying TO a city in their hand (Direct Flight)."}


def print_role(role, player=None):
    print(role.upper() + (f' ({player})' if player else ''))
    print((roles_db[role] + '\n').replace(". ", ".\n"))


def print_all_roles():
    for role in roles_db:
        print_role(role)


def random_roles(players, randomize_order, base_roles_only, assign_roles):
    players = players.split()  
    if randomize_order:
        random.shuffle(players)

    roles = list(roles_db)
    roles = roles[:7] if base_roles_only else roles
    roles = random.sample(roles, len(players))

    for player, role in zip(players, roles):
        print_role(role, player if assign_roles else None)


if __name__ == '__main__':
    random_roles('Yuko Riccardo Audrey German',
                 randomize_order=True,  # randomize players' order
                 base_roles_only=False,  # don't use roles from the 'On the Brink' extension
                 assign_roles=True)  # assign roles to players, instead of letting them pick
