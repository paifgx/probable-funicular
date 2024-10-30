import robot

def test_robot_movement():
    r = robot.Robot()
    assert r.perform_movement() == "Moving"

def test_robot_speech():
    r = robot.Robot()
    assert r.perform_speech() == "Hello, I can speak!"