import actions

story_one = {
        "intro_message": """
        ---- Pro. Oak Lab ---

        Prof. Oak: Congratulation Ash Ketchum, you have turned 18 years old today. Now your journey to become pokemon master begins. For that, you should start collecting badges.
        Ash: I have been waiting for this moment from the day I was born.
        Prof. Oak: But you need your first Pokemon. Here, Take this Pikachu. Your first pokemon.
        Prof. Oak: Your priority is to learn basic for now, lets start with viewing the pokemon you have.
        Ash: Okay.
        Prof. Oak: Select action 'v' to view your new Pikachu pokemon.

        """,
        "actions": [actions.ViewPokemons()]
    }

story_two = {
    "intro_message" : """
    ---- Pro. Oak Lab ---

   Prof. Oak: Now you viewed your pokemon, you have to remember its pokeball id. Pikachu's is no.1. You can always go back and view the id.
              Now, to select the pokemon.

              select action 'p' and you have to enter pokemon 'id'.

              DO IT!
   Ash: Okay, Prof.
    """,
    "actions": [actions.ViewPokemons(),actions.selectPokemon()]
}

story_three = {
    "intro_message" : """
       Prof. Oak: I see you leveling up quick. Go get hurry get your first badge.
       Ash: Okay, Prof.
    """,
    "actions": [actions.ViewPokemons(),actions.selectPokemon(),actions.ViewInventory() ]
}
#
story_four= {
    "intro_message" :  """
    ---- Pro. Oak Lab ---

       Prof. Oak: Why Are you here? Go get hurry get your first badge.
                    And remember to take care of your pokemon
       Ash: Okay, Prof.
    """,
    "actions": [actions.ViewPokemons(),actions.selectPokemon(),actions.ViewInventory() ]
}


player_level_map_story ={
    1:story_one,
    2:story_two,
    3:story_three,
    4:story_four
}
