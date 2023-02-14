class DirFile:
    parent: "DirFile"
    name: str
    size: int

    def __init__(self, name: str, parent: "Directory" = None, size=0):
        self.name = name
        self.parent = parent
        self.size = size
        if size and parent:
            parent.updateSize(size)

    def setSize(self, size: int):
        """recursively set size of self and parent(s)"""
        self.size = size
        if self.parent:
            self.parent.updateSize(size)

    def updateSize(self, size: int):
        """recursively update size of self and parent(s)"""
        self.size += size
        if self.parent:
            self.parent.updateSize(size)

    def setParent(self, parent: "Directory"):
        """set parent Directory"""
        self.parent = parent

def smallestToDelete(data: list):
    TOTAL_SPACE = 70000000
    UPDATE_SPACE = 30000000

    dirs = []
    lastCommandWasLs = False
    previousDir = None
    currentDir = None
    directory_size_for_deletion = None

    for line in data:
        if lastCommandWasLs and not line.startswith("$") and not line.startswith("dir"):
            filesize = line.split(" ")[0]

            currentDir.updateSize(int(filesize))

        elif line.startswith("$ cd"):
            previousDir = currentDir
            dest = line.split(" ")[2].strip()
            if dest not in ["..", "\n"]:
                currentDir = DirFile(name=dest, parent=previousDir)
            elif dest == "..":
                currentDir = currentDir.parent

            if currentDir not in dirs:
                dirs.append(currentDir)

            lastCommandWasLs = False
        elif line.startswith("$ ls"):
            lastCommandWasLs = True

    sizesUnder10k = sum(item.size for item in dirs if item.size < 100000)

    directory_size_for_deletion = UPDATE_SPACE - (TOTAL_SPACE - dirs[0].size)
    smallest_size = min(d.size for d in dirs if d.size > directory_size_for_deletion)

    return sizesUnder10k, smallest_size


def readInput(inputFile):
    with open(inputFile) as file:
        lines = file.readlines()
        smallestToDelete(lines)


if __name__ == '__main__':
    with open('day7Input.txt') as file:
        lines = file.readlines()
        sizeSumUnder10K, smallestSize = smallestToDelete(lines)
        print(f'Under10K: {sizeSumUnder10K}, smallestSize: {smallestSize}')
