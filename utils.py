MAX_STORY_LEVEL = 4

def select_current_level_story(current_level):
    if current_level < MAX_STORY_LEVEL:
        return current_level
    return MAX_STORY_LEVEL