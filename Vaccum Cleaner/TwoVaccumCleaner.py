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
        return "right" if room.name == "A" else "left"

class TwoRoomEnvironment:
    def __init__(self, agent):
        self.r1 = Room("A")
        self.r2 = Room("B")
        self.current = self.r1
        self.agent = agent
        self.step = 1

    def executeStep(self, n=1):
        for _ in range(n):
            print(f"Step {self.step}: [{self.current.name}, {self.current.status}]")
            self.agent.sense(self)
            action = self.agent.act()
            if action == "clean":
                self.current.status = "clean"
            elif action == "right":
                self.current = self.r2
            elif action == "left":
                self.current = self.r1
            print(f"Action: {action}\n")
            self.step += 1

if __name__ == "__main__":
    agent = VacuumAgent()
    env = TwoRoomEnvironment(agent)
    env.executeStep(10)



# ---------------------    Detail 

# from abc import abstractmethod  

# class Environment(object):
#     @abstractmethod
#     def __init__(self, n):     # Constructor (must be implemented by subclasses)
#         self.n = n             # Number of steps/rooms

#     def executeStep(self, n=1):  # Execute one or more steps
#         raise NotImplementedError('action must be defined!')  # Force subclasses to implement

#     def executeAll(self):        # Execute all steps
#         raise NotImplementedError('action must be defined!')

#     def delay(self, n=100):      # Set delay for visualization
#         self.delay = n

# class Room:
#     def __init__(self, location, status="dirty"):  # Constructor
#         self.location = location  # Room ID (e.g., 'A', 'B')
#         self.status = status      # 'dirty' or 'clean'

# class Agent(object):
#     @abstractmethod
#     def __init__(self):  # Constructor
#         pass

#     @abstractmethod
#     def sense(self, environment):  # Perceive environment
#         pass

#     @abstractmethod
#     def act(self):  # Take action based on percept
#         pass

# class VaccumAgent(Agent):
#     def __init__(self):  # Constructor (no initial state)
#         pass

#     def sense(self, env):  # Store current environment
#         self.environment = env

#     def act(self):  # Condition-action rules:
#         if self.environment.currentRoom.status == 'dirty':
#             return 'clean'       # Rule 1: Clean if dirty
#         if self.environment.currentRoom.location == 'A':
#             return 'right'       # Rule 2: Move right if in Room A
#         return 'left'             # Rule 3: Move left if in Room B
    

# class TwoRoomVaccumCleanerEnvironment(Environment):
#     def __init__(self, agent):
#         self.r1 = Room('A', 'dirty')  # Room A (dirty)
#         self.r2 = Room('B', 'dirty')  # Room B (dirty)
#         self.agent = agent                 # The vacuum agent
#         self.currentRoom = self.r1         # Start in Room A
#         self.step = 1                      # Step counter
#         self.action = ""                   # Track current action

#     def executeStep(self, n=1):
#         for _ in range(0, n):
#             self.displayPerception()        # Show current state
#             self.agent.sense(self)          # Agent senses environment
#             res = self.agent.act()          # Agent decides action
#             self.action = res
#             # Update environment based on action:
#             if res == 'clean':
#                 self.currentRoom.status = 'clean'  # Clean current room
#             elif res == 'right':
#                 self.currentRoom = self.r2   # Move to Room B
#             else:
#                 self.currentRoom = self.r1   # Move to Room A
#             self.displayAction()  # Display action taken
#             self.step += 1

#     def displayPerception(self):
#         print(f"Perception at step {self.step} is [{self.currentRoom.status},{self.currentRoom.location}]")
#         # print("Perception at step %d is [%s,%s]" % 
#         #       (self.step, self.currentRoom.status, self.currentRoom.location))

#     def displayAction(self):
#         print(f"------- Action taken at step {self.step} is {self.action}")
        
# if __name__ == '__main__':
#     vcagent = VaccumAgent()  # Create agent
#     env = TwoRoomVaccumCleanerEnvironment(vcagent)  # Create environment
#     env.executeStep(10)  # Run for 50 steps
