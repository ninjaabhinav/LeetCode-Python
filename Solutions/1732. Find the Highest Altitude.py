class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        net_gain = [0] * (len(gain)+1)
        highest_altitude = 0
        for i in range(len(gain)):
            net_gain[i+1] = net_gain[i]+gain[i]
        for i in (net_gain):
            if i >= highest_altitude:
                highest_altitude = i
        return highest_altitude