class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = []
        iTemps = []
        result = [0]*len(temperatures)

        for i in range(len(temperatures)):

            if i == 0:
                temps.append(temperatures[i]) # add first val to stack
                iTemps.append(i) # add index of temp to index stack

            else:

                while len(temps) > 0 and temperatures[i] > temps[len(temps) - 1]: # continue until current index is less than the one top of stack
                    temps.pop() # remove element
                    pos = iTemps.pop() # get position
                    dist = i - pos # find distance
                    result[pos] = dist # add to result index 
                    

                temps.append(temperatures[i])
                iTemps.append(i)

        return result



            
        