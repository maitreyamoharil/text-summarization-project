### BOX MODULE AND SETUP.PY IS NOT YET UNDERSTOOD ###
# End to end text-summarization-project
# WorkFlows

Update config.yaml
Update params.yaml 
Update entity
Update configuration manager in src config
Update components
Update pipeline
Update main.py
Update app.py



# 3 Import techniques
 Example :

import level_1_file
import level_1_file as lf1
from level_1_file import function
from level_1_file import *(All functions)

FOR MULTIPLE LEVEL FILES 
from level_1_file.level_2_file import function
from level_1_file.level_2_file import *
import level_1_file.level_2_file 
import level_1_file.level_2_file as lf1_2



# Try Except block:
// Types of errors: runtime(a/b), logical(wrong formula), syntax

raise exceptionName OR Exception("Exception message") Write it in try block -->
try: (Try to execute below LOC)
  pass
  pass 
  pass
  raise Exception -> Helps to manually rasie any exception
except Exception as e: (Display the exception message if any exception occur)
    print(e)
except Exception as e:
    print("Your custom message)
else : (Else runs if try block works completely and successfully)
    pass
finally: (No matter what happens...It will run it's LOC)
    pass



# Yaml files offers human readable data serialization language format often used for configuration
Example 1
key : value

Example 2
my_list:
  - value1
  - value2
  - value3

Example 3
my_dict:
  key1: value1
  key2: value2

Example 4
multi-list-str: |
  Hello world
  How are you ?
  I am fine here



# Read and write in yaml file
// Reading a yaml file

with open(file.yaml, 'r') as f:
  contains = yaml.safe_load_all(f)
print(contains)

// Writing in yaml file
with open(file.yaml, 'w') as f:
  yaml.dump(contains, f)



# Git Commands
git init [Initialise new repository]
git add . OR git add main.py [Add files to repository]
git status [Show status about file being modifies and commited and tracked]
git branch [Shoes list of all braches present]
git branch -M main [Create new and ONLY one master branch named main] MUST STEP
git branch branch_name [Create new branch named branch_name]
git checkout branch_name [Switches the current branch with the mentioned branch]
git merge branch_name [Merges the current branch with the main branch]
git branch -d branch_name [Deletes the local development branch]
git commit -m "message" [Provides commit message to the user in stagging phase of commit]
git remote add origin "URL_FOR_THE_ORIGIN_REPOSITORY" [Initialise origin/Destination repository]
git push origin main [Push our local branch to the origin/Destination repository]
git clone "URL_FOR_THE_ORIGIN_REPOSITORY" [Clones the entire repository]
pit pull origin main [Pull every new file from the origin/Destination repository]



# Efective way to write functions
def func(*numbers : List[int]) -> Float: (*args allows to add N number of arguments in the function,: Is used to specify variable type AND also makes coding efficient by previewing content, -> Used to specify return type of the function) 



# OS Module IMPORTANT syntax
os.getcwd() : Returns the current working directory
os.chdir(' ') : Changes the current directory to the provided directory path
os.makedirs(' ') : Makes a new directory/s given in the same 
os.mkdir(' ') : Makes the rightmost directory of the path
os.removedir(' ') : Removes all the directories provided in the path
os.rmdir(' ') : Removes the rightmost directory
os.listdir() : Returns the list of directories of the current working directory
os.rename('Old_Name.txt', 'New_Name.txt') : Renames the directory name 
os.path.split(' ') : Returns the splited directories and files from the provided path 
os.path.exist(' ') : Returns the boolean value



# Zip file creation and reading

import zipfile
with zipfile.ZipFile('new_file.zip', 'w') as variable:
  variable.write('existing_file.txt')
variable.close()

import zipfile
with zipfile.ZipFile('new_file.zip', 'r') as variable:
  variable.extractall('extracted_files_folder')
variable.close()