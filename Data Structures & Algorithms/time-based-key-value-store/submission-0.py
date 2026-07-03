class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = ([], {})
            self.timemap[key][0].append(timestamp)
            self.timemap[key][1][timestamp] = value
        else:
            if timestamp not in self.timemap[key][1]:
                self.timemap[key][0].append(timestamp)
            self.timemap[key][1][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        
        times = self.timemap[key][0]

        i = 0
        j = len(times) - 1
        largest_time = -1

        while i <= j:
            m = (i + j) // 2
            if times[m] > timestamp:
                j = m - 1
            else:
                if times[m] > largest_time:
                    largest_time = times[m]
                i = m + 1
        
        if largest_time == -1:
            return ""
        else:
            return self.timemap[key][1][largest_time]
