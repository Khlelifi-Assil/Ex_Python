import os 
output = os.popen('wmic process get description, processid, parentprocessid').read()
 
print(output)