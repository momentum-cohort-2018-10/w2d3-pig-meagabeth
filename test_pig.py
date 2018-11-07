from pig import Die, Player

def test_create_die():
    die = Die(3, 6)
    assert die.side == 3

def test_what_is_value_of_side():
    die = Die(4, 6)
    assert die.value_of_side() == 4

def test_who_goes_first():
    player = Player()
    assert player.first_player() == "human will go first."