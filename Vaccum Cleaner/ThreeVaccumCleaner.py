class Room:
    def __init__(self, name, status="dirty"):
        self.name = name
        self.status = status

class VacuumAgent:
    def sense(self, env):
        self.env = env

    def act(self):
        room = self.env.current
        if room.status == "dirty":
            return "clean"
        if room.name == "A":
            return "right"
        if room.name == "B":
            return "right" if self.env.r3.status == "dirty" else "left"
        return "left"

class Environment:
    def __init__(self, agent):
        self.r1 = Room("A")
        self.r2 = Room("B")
        self.r3 = Room("C")
        self.current = self.r1
        self.agent = agent
        self.step = 1

    def run(self, steps):
        for _ in range(steps):
            print(f"Step {self.step}: [{self.current.name}, {self.current.status}]")
            self.agent.sense(self)
            action = self.agent.act()
            print(f"Action: {action}\n")
            if action == "clean":
                self.current.status = "clean"
            elif action == "right":
                self.current = self.r2 if self.current == self.r1 else self.r3
            elif action == "left":
                self.current = self.r2 if self.current == self.r3 else self.r1
            self.step += 1

if __name__ == "__main__":
    agent = VacuumAgent()
    env = Environment(agent)
    env.run(10)




# ---------------------Detailed


# from abc import abstractmethod

# class Environment(object):
#     @abstractmethod
#     def __init__(self, n):  # Constructor (must be implemented by subclasses)
#         self.n = n          # Number of steps/rooms

#     def executeStep(self, n=1):  # Execute one or more steps
#         raise NotImplementedError('action must be defined!')

#     def executeAll(self):
#         raise NotImplementedError('action must be defined!')

#     def delay(self, n=100):
#         self.delay = n

# class Room:
#     def __init__(self, location, status="dirty"):
#         self.location = location
#         self.status = status

# class Agent(object):
#     @abstractmethod
#     def __init__(self):
#         pass

#     @abstractmethod
#     def sense(self, environment):
#         pass

#     @abstractmethod
#     def act(self):
#         pass

# class VaccumAgent(Agent):
#     def __init__(self):
#         pass

#     def sense(self, env):
#         self.environment = env

#     def act(self):
#         room = self.environment.currentRoom

#         if room.status == 'dirty':
#             return 'clean'

#         # Move logic for three rooms
#         if room.location == 'A':
#             return 'right'
#         elif room.location == 'B':
#             # Prefer right (to explore new room C) first
#             if self.environment.r3.status == 'dirty':
#                 return 'right'
#             return 'left'
#         elif room.location == 'C':
#             return 'left'

# class ThreeRoomVaccumCleanerEnvironment(Environment):
#     def __init__(self, agent):
#         self.r1 = Room('A', 'dirty')
#         self.r2 = Room('B', 'dirty')
#         self.r3 = Room('C', 'dirty')
#         self.agent = agent
#         self.currentRoom = self.r1
#         self.step = 1
#         self.action = ""

#     def executeStep(self, n=1):
#         for _ in range(0, n):
#             self.displayPerception()
#             self.agent.sense(self)
#             res = self.agent.act()
#             self.action = res

#             if res == 'clean':
#                 self.currentRoom.status = 'clean'
#             elif res == 'right':
#                 if self.currentRoom.location == 'A':
#                     self.currentRoom = self.r2
#                 elif self.currentRoom.location == 'B':
#                     self.currentRoom = self.r3
#             elif res == 'left':
#                 if self.currentRoom.location == 'C':
#                     self.currentRoom = self.r2
#                 elif self.currentRoom.location == 'B':
#                     self.currentRoom = self.r1

#             self.displayAction()
#             self.step += 1

#     def displayPerception(self):
#         print(f"Perception at step {self.step} is [{self.currentRoom.status}, {self.currentRoom.location}]")

#     def displayAction(self):
#         print(f"------- Action taken at step {self.step} is {self.action}")

# if __name__ == '__main__':
#     vcagent = VaccumAgent()
#     env = ThreeRoomVaccumCleanerEnvironment(vcagent)
#     env.executeStep(10)



