def writing_into_file(command_output):

  """Simple method to open and close the pre_validation file to avoid locking to file issue"""

  # Opening the file in appending mode
  file1 = open("pre_validation.txt","a")

  # Writing to the File
  file1.write(command_output)

  # Closing the file
  file1.close()
  
  
def list_command(linux_command_list):
  
  """This function will accept list of linux command and iterate over it to execute those command one by one"""

  # Iterating over the list of commands
  for commands in linux_command_list:
    print(commands)

    # calling run_command method 
    command_output = run_command(commands)

    # Writing the actual command to file
    writing_into_file("Linux command: {}".format(commands)) 
    writing_into_file("\n")

    # writing the executed command output line by line to a file
    for i in range(1, len(command_output) - 1): 
        print(command_output[i])
        writing_into_file(command_output[i])
        writing_into_file("\n")
		

def run_command(linux_command):


  """This function will execute the single linux command and return the corresponding output"""

  # The linux command | Ex: ls -l --> ["ls","-l"]
  linux_cmd = linux_command.split(" ")
  
    
  # Creating the subprocess with linux command
  temp = subprocess.Popen(linux_cmd, stdout = subprocess.PIPE) 
      
  # we use the communicate function 
  # to fetch the output 
  output = str(temp.communicate()) 
      
  # splitting the output so that 
  # we can parse them line by line 
  output = output.split("\n") 
      
  output = output[0].split('\\') 
  
  # a variable to store the output
  res = [] 
  
  # iterate through the output 
  # line by line 
  for line in output:
    res.append(line) 
  
  # print the output 
  #for i in range(1, len(res) - 1): 
  #   print(res[i])

  # Returning the executed command output as a list
  return res
  
  
USAGE:
list_command(["ls -l", "ls", "df -h"])