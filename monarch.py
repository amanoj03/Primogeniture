class Monarch:
    def __init__(self, name, parent, birth, death):
        self.name = name
        self.parent = parent
        self.birth = int(birth)
        self.death = int(death) if death != "0" else None
        self.children = []

    def addChild(self, child):
        if child.parent == self.name:
            self.children += [child]
        else:
            for royal in self.children:
                royal.addChild(child)

    def traverse(self):
        succession = []

        if not self.death:
            succession += [self]

        sortedChildren = sorted(self.children, key=lambda child: (child.birth))

        for child in sortedChildren:
            succession += child.traverse()

        return succession


def main():
    count = 0
    with open("monarch.txt", "r") as fp:
        for line in fp.readlines():
            if count == 0:
                n = int(line)
                count += 1
            elif count == 1:
                person = line.split(" ")
                head = Monarch(person[0], person[1], person[2], person[3])
                count += 1

            else:
                person = line.split(" ")
                royalFamily = Monarch(
                    person[0], person[1], person[2], person[3])
                head.addChild(royalFamily)
                count += 1
    for royalFamily in head.traverse():
        print(royalFamily.name, end=" -> ")


main()
# print("Enter the First Person to be the Grand-Parent of Every others")
# print("Name -> Parent -> Birth -> Death(Year or 0)")
