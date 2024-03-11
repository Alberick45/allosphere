class Retrieval:
    def __init__(self):
        self.people = {}

    def retrieve_from_text(self):
        with open("people.txt", "r") as text_file:
            lines = text_file.readlines()
            name = None
            info_dict = {}
            for line in lines:
                line = line.strip()
                if line:  # If line is not empty
                    if line.startswith("name : "):
                        if name:
                            self.people[name] = info_dict
                        name = line[len("name : "):]
                        info_dict = {}
                    else:
                        # Check if line contains the delimiter
                        if " : " in line:
                            key, value = line.split(" : ", 1)
                            info_dict[key.strip()] = value.strip()
            if name:  # Store the last person's info
                self.people[name] = info_dict

    def feedback(self):
        response = input("Enter person's name and what you want to find (separated by space): ")
        name, item = response.split(' ', 1) if ' ' in response else (response, None)
        if name in self.people:
            if item:
                if item.strip() in self.people[name]:
                    print(self.people[name][item.strip()])
                else:
                    print("No information found for '{}'".format(response))
            else:
                print("Information for", name)
                for key, value in self.people[name].items():
                    print(f"{key}: {value}")
        else:
            print("No information found for", name)


def retrieval():
    r = Retrieval()
    r.retrieve_from_text()
    r.feedback()

    retrieve = input("Would you like to retrieve information again? (yes/no): ")
    while retrieve.lower() == "yes":
        r.feedback()
        retrieve = input("Would you like to retrieve information again? (yes/no): ")
