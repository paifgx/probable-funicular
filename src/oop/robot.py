class Movement:
    def move(self) -> str:
        return "Moving"

class Speech:
    def speak(self) -> str:
        return "Hello, I can speak!"

class Robot():
    def __init__(self):
        self.movement = Movement()
        self.speech = Speech()

    def perform_movement(self) -> str:
        return self.movement.move()

    def perform_speech(self) -> str:
        return self.speech.speak()