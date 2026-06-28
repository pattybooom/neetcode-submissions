class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = []
        result = [0]*len(temperatures)
        print(temperatures)

        for i in range(len(temperatures)):
            print(f"result array: {result}")
            print(f"stack array: {temps}")
            print()

            if i == 0:
                temps.append(temperatures[i]) # add first val to stack

            else:

                if temperatures[i] > temperatures[i-1]: # if current index is greater than the one before
                    index = len(temps) -1
                    


                    # go backwards in the stack, remove elements until we find one larger than current
                    while index > -1 and temperatures[i] > temps[index]:
                        temps.pop() # remove element
                        rIndex = i-1

                        dist = 1 #distance from element we are comparing to the current temp
                        while result[rIndex] != 0:
                            rIndex -= 1
                            dist += 1

                        result[rIndex] = dist



                        index -=1
                        


                    temps.append(temperatures[i])


                else:
                    temps.append(temperatures[i]) #otherwise we add it to the stack
                    


        print(result)
        return result



            
        