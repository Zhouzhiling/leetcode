# Facebook | Phone Screen | CSV Dinosaurs

**Question 1:**
You will be supplied with two data files in CSV format .
The first file contains statistics about various dinosaurs. The second file contains additional data.
Given the following formula, `speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)`
Where g = 9.8 m/s^2 (gravitational constant)



Write a program to read in the data files from disk, it must then print the names of only the bipedal dinosaurs from fastest to slowest.
Do not print any other information.



```
$ cat dataset1.csv
NAME,LEG_LENGTH,DIET
Hadrosaurus,1.4,herbivore
Struthiomimus,0.72,omnivore
Velociraptor,1.8,carnivore
Triceratops,0.47,herbivore
Euoplocephalus,2.6,herbivore
Stegosaurus,1.50,herbivore
Tyrannosaurus Rex,6.5,carnivore

$ cat dataset2.csv 
NAME,STRIDE_LENGTH,STANCE
Euoplocephalus,1.97,quadrupedal
Stegosaurus,1.70,quadrupedal
Tyrannosaurus Rex,4.76,bipedal
Hadrosaurus,1.3,bipedal
Deinonychus,1.11,bipedal
Struthiomimus,1.24,bipedal
Velociraptorr,2.62,bipedal
```



I parsed both csv rows to dicts, looped over each dict, calculated speed, and inserted using insort_left into a sorted array



## Code

```python
# Facebook | Phone Screen | CSV Dinosaurs & Split Array Equal Sum
# Facebook | Phone Screen | CSV Dinosaurs & Split Array Equal Sum
import math
import heapq
def CSVDinosaurs(path1, path2):
    g = 9.8
    stride_map = {}
    with open(path2, 'r') as f:
        line = f.readline()
        line = f.readline()
        while line:
            tmp = line.split(",")
            name, stride, stance = tmp
            if stance.strip() == "bipedal":
                stride_map[name] = float(stride)
            line = f.readline()

    outmap = {}
    with open(path1, 'r') as f:
        line = f.readline()
        line = f.readline()
        while line:
            tmp = line.split(",")
            name, leg, diet = tmp
            leg = float(leg)
            if name in stride_map:
                stride = stride_map[name]
                outmap[name] = (stride/leg-1)*math.sqrt(leg*g)
                print(outmap[name])
            line = f.readline()

    res = []
    for name in outmap:
        res.append((-outmap[name], name))
    heapq.heapify(res)
    while res:
        speed, name = heapq.heappop(res)
        print(name + ", " + str(-speed))

path1 = "dataset1.csv"
path2 = "dataset2.csv"
CSVDinosaurs(path1, path2)
```

