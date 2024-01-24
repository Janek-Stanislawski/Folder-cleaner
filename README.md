This is folder sorter project.
It creates folders for some file types like PDF, music, video, pictures or fonts.
Also it creates folder for recent files, it checks modification time of the file and if file have modification time shorter than 100, it is sorted to this folder. 
If the modification time of the file in this folder exceeds 100h, then it is moved to main directory and sorted to proper folder.
It works in the background and checks if there are any changes in the directory, if it detects changes, it sorts the files and prints logs to console.
