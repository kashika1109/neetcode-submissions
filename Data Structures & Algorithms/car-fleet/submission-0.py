class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #if you make graph of time and position , then point of intersection of slope(speed) is the point where they come to same position and go with same speed. One car can also be car fleet if reached first and other never came. try calculating the time it takes for car to reach target . if the one behind reaches there first then they must collide at some point n go on with same speed
        #you would take referenc eof behind cars with the one that is most ahead , since its speed will never change and others behind will change speed as per that car if collide
        # pair = [[p,s] for p,s in zip(position,speed)] #pair of position n speed for each car one liner else use loop
        pair = []
        for i in range(len(position)):
            pair.append([position[i],speed[i]])
        
        stack = []
        for p,s in sorted(pair)[::-1]: #reverse sorted order me chlo
            stack.append((target-p) / s)  #time compare 
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


