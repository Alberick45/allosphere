import cv2 as cv
import time


# create a class of objects with people #
class People:
    def __init__(self):
        self.name = ""
        self.picture = ""
        self.pob = ""
        self.home = ""
        self.age = ""
        self.nationality = ""
        self.postal = ""
        self.contact = ""
        self.people = {}

    def personal(self):
        while True:
            self.name = input("Enter your name: ")
            if not self.name.isalpha():
                print("Please enter a valid name.")
                continue
            else:
                break

        while True:
            self.pob = input("Enter your place of birth: ")
            if not self.pob.isalpha():
                print("Please enter a valid place.")
                continue
            else:
                break
        while True:
            self.postal = input("Enter your postal address: ")
            if not self.postal.isalnum():
                print("Please enter a valid address.")
                continue
            else:
                break
        while True:
            self.age = input("Enter your age: ").strip()
            if not self.age.isdecimal():
                print("Please enter a valid age.")
                continue
            else:
                break
        while True:
            self.home = input("Enter your house address: ")
            if not self.home.isalnum():
                print("Please enter a valid location.")
                continue
            else:
                break
        while True:
            self.nationality = input("Enter your nationality: ")
            if not self.nationality.isalpha():
                print("Please enter a valid nationality.")
                continue
            else:
                break
        while True:
            self.contact = input("Enter your phone number: ").strip()
            if not self.contact.isdecimal():
                print("Please enter a valid phone number.")
                continue
            elif len(self.contact) != 10:
                continue
            else:
                break
        # taking picture of person #
        print("position yourself for the picture")
        time.sleep(1.5)
        cam = cv.VideoCapture(0)

        if not cam.isOpened():
            print("error opening camera")
            pass
        else:
            ret, frame = cam.read()
            cv.imshow("passport", frame)
            cv.waitKey(5)
            cv.imwrite("" + self.name + ".jpg", frame)
            cam.release()
            cv.destroyAllWindows()
        # storing picture with persons name#
        self.picture = self.name + ".jpg"
        pic = cv.imread(self.picture)
        cv.imshow("pic", pic)
        cv.waitKey(50)
        cv.destroyAllWindows()

        # initialising dictionary#

        # storing stuff in dictionary#
        self.people[self.name] = \
            {"picture": self.picture,
             "pob": self.pob,
             "age": self.age,
             "home": self.home,
             "nationality": self.nationality,
             "postal": self.postal,
             "contact": self.contact}


def entry():
    names = People()
    names.personal()
    print(names.name + " has been registered")
    pict = cv.imread(names.name + ".jpg")
    # make a copy of the original image
    imagetext = pict.copy()
    # let's write the text you want to put on the image
    text = names.name
    # org: Where you want to put the text
    org = (0, 350)
    # write the text on the input image
    cv.putText(imagetext, text, org, cv.FONT_HERSHEY_SCRIPT_COMPLEX, 1.0, (0, 0, 0))
    # display the output image with text over it
    cv.imshow("Image Text", imagetext)
    cv.waitKey(500)
    cv.imwrite(names.name + ".jpg", imagetext)
    cv.destroyAllWindows()
    # Read existing IDs from the file
    existing_ids = []
    with open("people.txt", "a+") as file:  # Use "a+" mode to create the file if it doesn't exist
        file.seek(0)  # Move the file pointer to the beginning
        for line in file:
            if line.startswith("id :"):
                existing_ids.append(int(line.split(":")[1].strip()))

    # Determine the next available ID
    next_id = 1 if not existing_ids else max(existing_ids) + 1

    # Write the next ID and the new entry to the file
    with open("people.txt", "a") as store:
        # Write the next ID
        store.write(" id : {:04d}\n".format(next_id))

        # Write the new entry
        people = (" name : %s \n home : %s \n age : %s \n pob : %s \n postal : %s \n contact : %s \n "
                  "nationality : %s \n  \n \n \n " %
                  (names.name, names.home, names.age, names.pob, names.postal,
                   names.contact, names.nationality))
        store.write(people)
