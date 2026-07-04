class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #sort the positions and for every swap made we make the same swap to speed (nlogn)

        sorted = False
        while not sorted:
            sorted = True
            for i in range(len(position) - 1):
                if position[i] < position[i+1]:
                    placehold = position[i+1]
                    position[i+1] = position[i]
                    position[i] = placehold

                    placehold = speed[i+1]
                    speed[i+1] = speed[i]
                    speed[i] = placehold
                    sorted = False
     
        arrivals = []
        for i in range(len(position)):
            time =  (target - position[i]) / speed[i]
            if not arrivals:
                arrivals.append(time)
                print(time)
            elif time <= arrivals[-1]:
                print(f"discarded {time}")
                #dont add to stack
            else:
                arrivals.append(time)
                print(time)

                

        fleetNum = 1
        for i in range(len(arrivals)-1):
            if arrivals[i] < arrivals[i+1]:
                fleetNum += 1
            else:
                arrivals[i+1] = arrivals[i]
     
        
        return len(arrivals)
 

            
            
            

        