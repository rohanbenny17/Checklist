# Checklist

Hello and welcome to your own, easy to use checklist.

This is a program to assist you to create and manipulate your own checklist.
It takes  **various command-line argument** which include options to **add items**, **remove items**, **list items**, **delete profile** and an additional **help option**. There is **no other user input** involved other than the **command-line arguments**.


# Checklist for dummies

### LINUX
If you downloaded the file for a LINUX system, follow these steps
>**How to use**
- Step 1: cd into the directory to which you downloaded the file.
- Step 2: run the program with the command discussed below.

### WINDOWS
If you downloaded the file for a WINDOWS system, follow these steps.
> **How to use**
- Step 1: open the folder to which you downloaded the file.
- Step 2: click the [address bar](https://www.google.com/imgres?imgurl=https%3A%2F%2Fwinaero.com%2Fblog%2Fwp-content%2Fuploads%2F2019%2F09%2FWindows-10-File-Explorer-Address-Bar-Full-Path.png&imgrefurl=https%3A%2F%2Fwinaero.com%2Fshow-full-path-address-bar-windows-10-file-explorer%2F&tbnid=TcqOB1NcDGyd_M&vet=12ahUKEwivzOm2xqX7AhU-3TgGHQZ4CxoQMygIegUIARDTAQ..i&docid=EOIBikiDeV8htM&w=490&h=182&q=address%20bar%20in%20windows&client=opera-gx&ved=2ahUKEwivzOm2xqX7AhU-3TgGHQZ4CxoQMygIegUIARDTAQ) and clear everything. (Do not press enter)
- Step 3: type "cmd" in the cleared address bar and hit enter.
- Step 4: A command prompt terminal now opens where you have to type the command.

## FEATURES
First of all - you need to know that, if it not a bug then its a feature. You also need to know that if it is a bug then its still a feature.
1. **Help:**:
 Displays a help screen showing how to use the program and the things you should keep in mind while using it.
-     Usage: python checklist.py --help
-     Usage: python checklist.py [PROFILE_NAME] --help
2. **Add:**:
 It adds item(s) to the checklist.

   Note: To add items with multiple words, the item must be quoted.
-     Usage: python checklist.py [PROFILE_NAME] --add hello
-     Usage: python checklist.py [PROFILE_NAME] --add hi hey bye goodbye
-     Usage: python checklist.py [PROFILE_NAME] --add "good night"
3. **Remove:**
 It is used to remove item(s) from the checklist.

   Note: To remove items with multiple words, the item must be quoted.
-     Usage: python checklist.py [PROFILE_NAME] --rm hello
-     Usage: python checklist.py [PROFILE_NAME] --rm hi hey bye goodbye
-     Usage: python checklist.py [PROFILE_NAME] --rm "good night"
4. **List Items:**
 It is used to list all the items in the check list.
 -     Usage: python checklist.py [PROFILE_NAME] --ls
5. **Delete:**
 It is used to delete a profile mentioned in the command-line argument
-     Usage: python checklist.py [PROFILE_NAME] --delete

Finally, if something happens which was not supposed to happen then CTRL + Z is you friend.

## ADDITIONALS
1. Profile name cannot be a option value.
- Eg: You can't have --add as a profile name
2. Except --add and --rm all other options don't take any extra arguments
3. If you mess with the files in the data folder you may not be able to recover the data

### CREDITS
As of now, I'm the only one who worked on the project so feel free to thank me.
> Discord : @gamin9eek#6729
> Reddit : [https://www.reddit.com/user/gamin9eek](https://www.reddit.com/user/gamin9eek)
> buymeacoffee : [https://www.buymeacoffee.com/rohanbenny17](https://www.buymeacoffee.com/rohanbenny17)

I'm ready to collab if you wish to enhance the project.
```
