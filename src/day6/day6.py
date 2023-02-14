# need to make a 4-space moving window

def day6():
    with open('day6Input.txt') as f:
        lines = f.readlines()
        data = lines[0].strip('\n')
        for i in range(len(data)-1):
            window=[]
            for x in range(1,15):
                if data[i+x-1] in window:
                    continue
                else:
                    window.append(data[i+x-1])
                if len(window) == 14:
                    return i+x
                    

if __name__ == '__main__':
    num = day6()
    print(num)
            
            