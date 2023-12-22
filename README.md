# T1A3 - Cooper Scott
My application is a wildlife conservation "entries" system that keeps track of what animals are inside the facility and information about them.

## R1-R3 (Don't require individual answers)

## R4: 
My GitHub Repo is: https://github.com/CoopersProjects/T1A3

## R5: 
I will be using the PEP-8 style guide to maintain consistency throughout my project. 

Reference:
van Rossum, G., Warsaw, B. and Coghlan, N. (2001). PEP 8 – Style Guide for Python Code | peps.python.org. [online] peps.python.org. Available at: https://peps.python.org/pep-0008/.

## R6:
List of features in my application:
- Ability to add new animals
--> This will use variables as "name", "age", "species", "zone" and "date_rescued".
--> I will be able to add new animals and information about the animals into the registery.

- Ability to delete entries once released
--> Once the conservation is no longer required, you will be able to delete the entry as it is no longer required.

- Ability to display a complete list of entries
--> This requires a loop to check over the list of entries.
--> This allows the user to see all existing entries in a list.

- Ability to search for individual zones (e.g. "Zone 2").
--> This also requires a loop to check the information and return.
--> Allows user to search for key zone to see what animals occupy a zone.

- Ability to edit existing information
--> Allows user to edit information if required, e.g. age increase.

Error handling will also be covered by making sure that appropriate messages or information is displayed when an "unexpected entry" is provided.

## R7: 
For R7 I will link my monday.com project management photos. Here I used a checklist to tick off required parts of my features.

My plan was to complete the major coding requirements by the 21st of December so that I could focus on compiling everything I need together and making sure I am happy with my work and have it organised. In order for that to happen, I created the project management page on monday.com and used it to tick off general goals that I wanted to have completed. I generally started each feature of my project with the goal of completing the method before moving on to using the method to write the code I wanted to run. Once that was complete, I tested that it worked which took a long time, especially with features such as the editing feature as I was having a recurring problem that I will mention in the slide-deck and video. I prioritised getting the features complete so that way I can move onto the other aspects of the work closer to the deadline. Below I have attached some photos of my management photos over time, however they are quite generalised as I was figuring out what I needed to do as I went along and then after learning what to do it was a lot of "rinse and repeating".

![Progress_photo_1](/Resources/T1A3%20-%20P1.png)
![Progress_photo_2](/Resources/T1A3%20-%20P2.png)
![Progress_photo_3](/Resources/T1A3%20-%20P3.png)
![Progress_photo_4](/Resources/T1A3%20-P4.png)
![Progress_photo_5](/Resources/T1A3%20-P5.png)
![Progress_photo_6](/Resources/T1A3%20-P6.png)
![Progress_photo_7](/Resources/T1A3%20-P7.png)
![Progress_photo_8](/Resources/T1A3-P8.png)

## R8: (Mac OS)
To install my application, you will need to go to github.com using this link: https://github.com/CoopersProjects/T1A3. 

Once you are there you will be presented with a public page containing the application, from there you will need to:

1. Go to the green "Code" button.
2. Click on it and select the "download as zip" option. (or you can select the open with github desktop option if you'd prefer.)
3. Download the zip file.
4. Once downloaded, you will have to open the zip file, to reveal the coding folder. 
5. You can now open the folder in vscode (or other coding software) by right clicking and opening at terminal --> code .
6. You will then be able to view my program on the "main.py" section. 
7. To run this you will need to open the terminal and type "python3 src_code/main.py"
8. This will run the program, in which case you will be able to access it and use it.

Note: To use my program, you will require the installation of python. You can check whether you have python by running my run.sh file in the folder (once opened, you will need to type "./run.sh" and that will notify you if you need to install it.) It will also check if you have the relevant imported python packages that I have utilised. 

If you do have python, you may be required to update it to the latest version to successfully view and run the program.

My program has the following dependencies: 
- Python3
- Colorama 
- Pytest

These will need to be installed. If required you can use: 

```
pip install colorama pytest
```

To use the program, you will require an operating system (Mac, Windows, Linux), python3 and enough disc space to store animal data.

EDIT: I have now created an executable file that skips all this. You can find it by following up to step 5. You need to download the zip, open it and the file is called "main". You will then be able to instantly run it. Please note that this should be completed after the run.sh commands have checked you have everything installed correctly.