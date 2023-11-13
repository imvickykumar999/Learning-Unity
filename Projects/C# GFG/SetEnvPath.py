
import os

# Get the current PATH environment variable
path = os.environ['PATH']

# Add the new path to the PATH environment variable
path += "C:\\Users\\Vicky\\Desktop\\Repository\\Learning-Unity\\Projects\\C# GFG\\"

# Set the PATH environment variable
os.environ['PATH'] = path
