```python
#coding=utf-8
class visit_history(object):
    def __init__(self):
        # key: ip
        # value: list[time]
        self.record = {}
        self.threshold = 1000
        self.time_diff = 30
        
    def find_valid_time(times, time_threshold):
        # binary search to find the first time 
        length = len(times)
        if length == 0 or times[0] >= time_threshold:
            return 0
        st = 0
        ed = length-1
        while st < ed:
            mid = (st + ed) / 2
            if nums[mid] >= time_threshold:
                ed = mid
            else:
                st = mid + 1
        return st       
        
        
    def server(ip):
        cur_time = get_time()
        if ip not in self.record:
            self.record[ip] = [cur_time]
            return False
        else:
            time_threshold = cur_time - self.time_diff
            start_index = find_valid_time(record[ip], time_threshold)
            record[ip] = record[ip][start_index:]
            record[ip].append(cur_time)
            length = len(record[ip])
            if length > self.threshold:
                return True
            else:
                return False
```

