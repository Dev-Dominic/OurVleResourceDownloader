# Web Page File Downloader

Takes a given course page url OURVLE and donwloads all the resource files

## Setup

```bash

```

## How to use

```bash

```

## Dependencies

### Python Dependencies
- selenium
- regex 
- sys

### Other Dependencies 
- chromedriver(Google Chrome Webrowser)

## How it works 

1. Create a holding area for files 
2. Collect login information of user from command line 
3. Log into ourvle and open each course page
4. If prompted to change password press "cancel" otherwise skip the command to press cancel (Use whether cancel is found on the page or not) 
5. Navigate to each page 
6. Search for all links containing anchor tags with pattern 'https://ourvle.mona.uwi.edu/mod/resource/view.php?id=[/d]*' (Using regex to determine the patterns)
7. On Each page after downloading mv all the files in the holding area to a newly created directory with the coures page name

### Abstraction of problem 

1. Creation of holding folder in donwload folder called 'Courses' 
2. Navigate pages - webNavigate(Login info)
	a. Downloading each page resource (Helper function) - downloadRes
	b. Creation of new folder to house new files and move them to that folder

## Issues


