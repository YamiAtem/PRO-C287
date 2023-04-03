from controller import Robot
from controller import Keyboard
from controller import DistanceSensor
import random
from controller import Camera

robot = Robot()
keyboard = Keyboard()

timestep = 64

wheel_1 = robot.getDevice("wheel1")
wheel_1.setPosition(float('inf'))
wheel_1.setVelocity(0.0)

wheel_2 = robot.getDevice("wheel2")
wheel_2.setPosition(float('inf'))
wheel_2.setVelocity(0.0)

wheel_3 = robot.getDevice("wheel3")
wheel_3.setPosition(float('inf'))
wheel_3.setVelocity(0.0)

wheel_4 = robot.getDevice("wheel4")
wheel_4.setPosition(float('inf'))
wheel_4.setVelocity(0.0)

ds_left = robot.getDevice("ds_left")
ds_right= robot.getDevice("ds_right")

camera = robot.getDevice('camera')
camera.enable(timestep)

image_num = 0

ds_left.enable(timestep)
ds_right.enable(timestep)

speed = 4
number_of_turns = 0

keyboard.enable(timestep)
random_direction = 0

prev_key = 0
key_pressed = -1

auto_mode = True

while (robot.step(timestep) != -1):
    prev_key = key_pressed
    key_pressed = keyboard.getKey()
    print(key_pressed)

    #  65 is "a" key
    if prev_key == -1  and  key_pressed == 65:
        auto_mode = not auto_mode
    
    if prev_key == -1  and  key_pressed == 83:
        camera.getImage()
        image_name = f'picture{image_num}.png'
        camera.saveImage(image_name, 50)
        image_num += 1
        
    if auto_mode:
        ds_left_value = ds_left.getValue()
        ds_right_value = ds_right.getValue()
        
        if(ds_left_value<1000 or ds_right_value<1000):
            number_of_turns = 8
        
        # when turns have not started, we choose a random direction    
        if(number_of_turns == 0):
            random_direction = random.choice([0,1])
         
        if(number_of_turns > 0):
            # In auto mode, turns when an obstacle is detected.
            number_of_turns = number_of_turns - 1
            if(random_direction == 0):
                wheel_1.setVelocity(-speed)
                wheel_2.setVelocity(speed)
                wheel_3.setVelocity(-speed)
                wheel_4.setVelocity(speed)
            elif(random_direction == 1):
                wheel_1.setVelocity(speed)
                wheel_2.setVelocity(-speed)
                wheel_3.setVelocity(speed)
                wheel_4.setVelocity(-speed)
        else:
            # In auto mode, keeps going forward when no obstacles are detected.
            wheel_1.setVelocity(speed)
            wheel_2.setVelocity(speed)
            wheel_3.setVelocity(speed)
            wheel_4.setVelocity(speed)
         
    
    if(not auto_mode):
        # front movement - press up arrow key
        if(key_pressed == 315):
            wheel_1.setVelocity(speed)
            wheel_2.setVelocity(speed)
            wheel_3.setVelocity(speed)
            wheel_4.setVelocity(speed)
            
        # back movement - press down arrow key   
        if(key_pressed == 317):
            wheel_1.setVelocity(-speed)
            wheel_2.setVelocity(-speed)
            wheel_3.setVelocity(-speed)
            wheel_4.setVelocity(-speed)
        
        # left movement - press left arrow key      
        if(key_pressed == 314):
            wheel_1.setVelocity(-speed)
            wheel_2.setVelocity(speed)
            wheel_3.setVelocity(-speed)
            wheel_4.setVelocity(speed)
        
        # right movement - press right arrow key     
        if(key_pressed == 316):
            wheel_1.setVelocity(speed)
            wheel_2.setVelocity(-speed)
            wheel_3.setVelocity(speed)
            wheel_4.setVelocity(-speed)
        
        # if no key is pressed   
        if(key_pressed == -1):
            wheel_1.setVelocity(0)
            wheel_2.setVelocity(0)
            wheel_3.setVelocity(0)
            wheel_4.setVelocity(0)
        
            
        
