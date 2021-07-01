from mycroft import MycroftSkill, intent_file_handler


class Socworld(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('socworld.intent')
    def handle_socworld(self, message):
        self.speak_dialog('socworld')


def create_skill():
    return Socworld()

