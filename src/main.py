from island import Island
from islandstory import IslandStory

class Story:
    
    def __init__(self):
        self.story_size = 0
        self.story_words = 0

    def update_word_count(self, story_piece):
        words = 0
        inside_word = False
        for s in story_piece:
            if inside_word and (s == ' ' or s == '\n' or s == '\t'):
                inside_word = False
            elif not inside_word and not (s == ' ' or s == '\n' or s == '\t'):
                inside_word = True
                words = words + 1
        self.story_words = self.story_words + words


    def print_story(self, story_piece):
        self.story_size = self.story_size + len(story_piece)
        self.update_word_count(story_piece)
        print(story_piece)

    def generate_story(self):

        max_island_story_days = 10

        while self.story_words < 50000:
            i = Island()
            island_story = IslandStory(i)
            for i in xrange(0, max_island_story_days):
                self.print_story(island_story.update_day())
                # self.print_story('God created the region named as ' + i.island_name)

s = Story()
s.generate_story()
print('\n\nStory has ' + str(s.story_words) + ' words')