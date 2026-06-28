class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    
        iTemps = []
        result = [0]*len(temperatures)

        for i in range(len(temperatures)):
            if i == 0:
                
                iTemps.append(i) # add index of temp to index stack

            else:

                while len(iTemps) > 0 and temperatures[i] > temperatures[iTemps[-1]]: # continue until current index is less than the one top of stack
                    pos = iTemps.pop() # get position
                    result[pos] = i-pos # add to result index 
                    

           
                iTemps.append(i)

        return result



            
        