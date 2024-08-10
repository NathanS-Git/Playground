A playground for a deep reinforcement learning algorithm backup algorithm. The objective being to minimize the amount of space caused by the backups while allowing for abitrary date retreival. The backups in this playground don't actually require any space on the drive - the space is simply simulated within the environment itself. 

environment:
    Creates a new backup once a week
    Attempts to retrieve a backup randomly

agent:
    Goal is to minimize backup count while satisfying the environments backup requests as best it can
    Can only delete backups
