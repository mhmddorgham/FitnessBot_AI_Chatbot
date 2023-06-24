from speech_recognition import Microphone, Recognizer
import djitellopy as tello
import cv2
import time


recog = Recognizer()  # recog ur voice or audio
mic = Microphone()  # connect to your mic


drone = tello.Tello()
drone.connect()
print(drone.get_battery())
drone.streamoff()


i = 0


def voice_control():
    with mic:  # work with mic
        print("Speak Anything :")
        audio = recog.listen(mic)  # Records
        text = recog.recognize_google(audio)  # converts to text
        global i
        if (text == "go forward"):
            print("going forward")
            text = ""
            drone.move_forward(20)

        elif (text == "go back"):
            print("going back")
            text = ""
            drone.move_back(20)
        if (text == "go right "):
            print("going right")
            text = ""
            drone.move_right(20)
        elif (text == "go left"):
            print("going left")
            text = ""
            drone.move_left(20)
        if (text == "move up"):
            print("moving up")
            text = ""
            drone.move_up(20)
        elif (text == "move down"):
            print("moving down")
            text = ""
            drone.move_down(20)
        if (text == "rotate right"):
            print("rotating right")
            text = ""
            drone.rotate_clockwise(45)
        elif (text == "rotate left"):
            print("rotating left")
            text = ""
            drone.rotate_counter_clockwise(45)
        if (text == "land"):
            print("landing")
            text = ""
            drone.land()
            exit()
        elif (text == "take off"):
            print("taking off")
            text = ""
            drone.takeoff()
        if (text == "do a flip"):
            print("flip incoming")
            text = ""
            drone.flip_forward()
        elif (text == "take a picture"):
            print("smile !!")
            text = ""
            image = drone.get_frame_read().frame
            image = cv2.resize(image, (360, 240))
            a = cv2.imwrite('drone photo' + str(i) + '.jpg', image)
            i = i + 1
            time.sleep(0.2)
        if (text == "record a video"):
            print("smile !!")
            text = ""  # not done

        elif (text != "bla"):
            print("I DIDNT UNDERSTAND WHAT YOU SAID")
            text = ""


while True:
    voice_control()
    image = drone.get_frame_read().frame
    image = cv2.resize(image, (360, 240))
    cv2.imshow("DRONE VIEW", image)
    cv2.waitKey(1)
