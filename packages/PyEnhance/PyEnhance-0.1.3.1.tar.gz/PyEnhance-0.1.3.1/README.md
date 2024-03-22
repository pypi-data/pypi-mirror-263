# PyEnhance

## Overview

Version: Beta 0.1.3

PyEnhance is a python library with essential tools for any python project.

The modules included in this library are the following

* Stamps
* Banners
* Loading Indicators
* Timer
* WebTools
* TextSets
* Counter


<i>
    <br />
</i>

## Installation

To install PyEnhance just run the following command in your terminal of choice.

    pip install PyEnhance

<i>
    <br \>
</i>

## Modules

The following section provides all the information needed for the use of the modules included in this library.

<i>
    <br \>
</i>

## Stamps        

The Stamps module consist of pre-made status decorators meant for use in a CLI interface.

<i>
    <br \>
</i>

**Stamps Available**

* Info
* Warring
* Input
* Output
* Error

<i>
<br \>
</i>

**Usage**

**Importing the Library**

    from PyEnhance import Stamps

<i>
<br />
</i>

**Using the stamps**

Set alies for easy usage and readability

    Stamp = Stamps.Stamp

<i>
<br \>
</i>

Display Stamp

	print(Stamp.<StampName>)

<i>
<br />
</i>

**Example**

    from PyEnhance import Stamps

    Stamp = Stamps.Stamp 

    print(Stamp.Info)
    print(Stamp.Warring)
    print(Stamp.Input)
    print(Stamp.Output)
    print(Stamp.Error)

<i>
    <br />
</i>

**Visual Output**

| Loading Indicator Type | Example (Windows CMD)                   |
|------------------------|-----------------------------------------|
| Windows 10 | ![Windows.png](Images/Windows.png)|
| Linux (Ubuntu) | ![Linux.png](Images/Linux.png)|



<i>
    <br />
    <br />
    <br />
</i>

## Banners

**Banners Available**

* Info
* Warring
* Input
* Output
* Error
  
<i>
<br \>
</i>

**Usage**

**Importing the Library**

    from PyEnhance import Banners

<i>
<br \>
</i>

**Using the Banners**

Set alies for easy usage and readability


    Banner = Banners.Banner 

<i>
<br \>
</i>

Display Banner

    print(Banner.<BannerName>)

<i>
    <br />
</i>

**Example**

    from PyEnhance import Banners

    Banner = Banners.Banner

    print(Banner.Info)
    print(Banner.Warring)
    print(Banner.Input)
    print(Banner.Output)
    print(Banner.Error)

<i>
    <br />
</i>

**Visual Output**

| Operating System | Output on OS                  |
|------------------|-------------------------------|
| Windows 10       | ![Windows.png](Images/Windows_1.png) |
| Linux (Ubuntu)   | ![Linux.png](Images/Linux_1.png)     |


<i>
    <br />
    <br />
    <br />
</i>

## Loading

The Loading module consist of different visual loading indicators.

**Types of Loading Indicators**

| Loading Indicator Type | Example (Windows CMD)                   |
|------------------------|-----------------------------------------|
| Spin                   | ![Loading-Spin.gif](Images/Loading-Spin.gif)   |
| Bar                    | ![Loading-bar.gif](Images/Loading-bar.gif)     |
| Stats                  | ![Loading-stats.gif](Images/Loading-stats.gif) |


<i>
<br />
</i>

**Importing the Library**

    from PyEnhance import Loading
    
<i>
<br />
</i>

### Spin

**Parameters**

Text: The text that appears in front of the spinner

<i>
<br \>
</i>

**Usage**

Set alies for easy usage and readability:
    
    Loading = Loading.Loading()

To start the loading animation:

    Loading.Spin(Text="Any String")

To stop the loading animation:
    
    Loading.Stop()
    
<i>
<br />
</i>

**Example**

    from PyEnhance import Loading

    Loading = Loading.Loading()

    Loading.Spin(Text="Loading")
    
    # Your code here

    Loading.Stop() 


<i>
    <br />
    <br />
</i>


### Bar


**Parameters**

PrintSpeed: The time in seconds in between new bar segments being printed.

<i>
<br \>
</i>

**Usage**

Set alies for easy usage and readability:

    Loading = Loading.Loading()

To start the loading animation:

    Loading.Bar(PrintSpeed=0.3)

To stop the loading animation:

    Loading.Stop()
    
<i>
<br />
</i>

**Example**

    from PyEnhance import Loading

    Loading = Loading.Loading()

    Loading.Bar(PrintSpeed=0.3)
    
    # Your code here

    Loading.Stop()


<i>
    <br />
    <br />
</i>


### Stats

**Parameters**

Range: Specifies the total range or the maximum count of the progress bar.

<i>
<br \>
</i>

**Usage**

Set alies for easy usage and readability:

    Loading = Loading.Loading()

To using the loading animation the function placed in a loop.

    for i in range(20):
    
        # Your Code Here

        Loading.Stats(Range=20)
	
<i>
<br />
</i>

**Example**

    from PyEnhance import Loading

    Loading = Loading.Loading()

    ExampleList = [1, 2, 3, 4, 5]
    
    for i in range(len(ExampleList)):
    
        time.sleep(0.5)
    
        Loading.Stats(Range=len(ExampleList))


<i>
    <br />
    <br />
    <br />
</i>


## Timer

This module as the name indicates is a timer it outputs the elapsed time in one of two formats determined by the user.

<i>
<br />
</i>

**Types Of Output**

| Output Forms    | Example (Windows CMD)                     |
|-----------------|-------------------------------------------|
| Short (default) | ![AllShortImages.png](Images/AllShortImages.png) |
| Long            | ![AllLongImages.png](Images/AllLongImages.png)   |


<i>
<br />
</i>

**Usage**

**Importing the Library**

    from PyEnhance import Timer

**Parameters**

Form: Sets the type of output received by user. If no user input is provided Short is used by default.


Set alies for easy usage and readability

    Timer = Timer.Timer()

Short form output
    
    Timer.Start()
    
    # Your Code Here
    
    Timer.Stop()
    
    
Long form output
    
    Timer.Start(Form="Long")
    
    # Your Code Here
    
    Timer.Stop()
    
<i>
<br />
</i>

**Examples**

Short Form Output

    from PyEnhance import Timer

    Timer = Timer.Timer()
    
    Timer.Start()
    
    count = 0
    while count < 30000000:
    count += 1
    
    Timer.Stop()


Long Form Output

    from PyEnhance import Timer

    Timer = Timer.Timer()
    
    Timer.Start(From="Long")
    
    count = 0
    while count < 30000000:
    count += 1
    
    Timer.Stop()

<i>
    <br />
    <br />
    <br />
</i>

## WebTools

This module consist of tools relating to web requests and validation of URLs

**Tools included in the module**

- ValidTLD (Checks if a URL has a valid TLD)
- RefactorHTTP (Makes a http version of a user inputted URL)
- RefactorHTTPS (Makes a https version of a user inputted URL)
- HTTPcheck (Refactors a given URL to a http version and checks if it's valid)
- HTTPScheck (Refactors a given URL to a https version and checks if it's valid)
- RequestHeaders (Basic headers for making web requests)
- StatusCode (http/https status codes sorted by category for handling web request responses)

<i>
<br \>
<br \>
</i>


**Importing the library**

    from PyEnhance import WebTools

<i>
    <br />
    <br />
</i>

### ValidTLD

Checks if a URL has a valid TLD

**Parameters**

URL: Any URL

**Usage**

Set alies for easy usage and readability

    WebTools = WebTools.WebTools()

Checking TLD
   
    if WebTools.ValidTLD(URL='www.google.com') == True:
    
<i>
<br />
</i>

**Example**
    
    from PyEnhance import WebTools

    WebTools = WebTools.WebTools()

    if WebTools.ValidTLD(URL='www.google.com') == True:
        print('TLDS is valid')
    else:
        print('TLDS is invalid')
        
<i>
    <br />
    <br />
</i>

### RefactorHTTP

Makes a http version of a user inputted URL

**Parameters**

URL: Any URL

**Usage**

Set alies for easy usage and readability

    WebTools = WebTools.WebTools()

Refactor URL

    URLHTTP = WebTools.RefactorHTTP(URL='www.google.com')
    
<i>
<br />
</i>

**Example**


    from PyEnhance import WebTools

    WebTools = WebTools.WebTools()

    URLHTTP = WebTools.RefactorHTTP(URL='www.google.com')

    print(f"URL Refactored to HTTP: {URLHTTP}")  # Will print: URL Refactored to HTTP: http://www.google.comv

<i>
    <br />
    <br />
</i>

### RefactorHTTPS

Makes a https version of a user inputted URL

**Parameters**

URL: Any URL

**Usage**

Set alies for easy usage and readability

    WebTools = WebTools.WebTools()

Refactor URL

    URLHTTPS = WebTools.RefactorHTTPS(URL='www.google.com')
    
<i>
<br />
</i>

**Example**


    from PyEnhance import WebTools

    WebTools = WebTools.WebTools()

    URLHTTPS = WebTools.RefactorHTTPS(URL='www.google.com')

    print(f"URL Refactored to HTTPS: {URLHTTPS}") # Will print: URL Refactored to HTTPS: https://www.google.com

<i>
    <br />
    <br />
</i>

### HTTPcheck

Refactors a given URL to a http version and checks if it's valid

**Parameters**

URL: Any URL

**Usage**

Set alies for easy usage and readability

    WebTools = WebTools.WebTools()

Check if http is valid

    if WebTools.HTTPcheck(URL='www.google.com') == True:
    
<i>
<br />
</i>

**Example**

    from PyEnhance import WebTools

    WebTools = WebTools.WebTools()

    if WebTools.HTTPcheck(URL='www.google.com') == True:
        print('HTTP is Valid')

<i>
    <br />
    <br />
</i>

### HTTPScheck

Refactors a given URL to a https version and checks if it's valid

**Parameters**

URL: Any URL

**Usage**

Set alies for easy usage and readability

    WebTools = WebTools.WebTools()

Check if http is valid

    if WebTools.HTTPScheck(URL='www.google.com') == True:
    
<i>
<br />
</i>

**Example**

    from PyEnhance import WebTools

    WebTools = WebTools.WebTools()

    if WebTools.HTTPScheck(URL='www.google.com') == True:
        print('HTTP is Valid')

<i>
    <br />
    <br />
</i>

### RequestHeaders

Basic headers for making web requests


**Usage**

Set alies for easy usage and readability

    WebTools = WebTools.WebTools()

Make web request

    import requests # Any web request lib will work as long as it supports headers
 
    r = requests.get("www.google.com", headers=WebTools.RequestHeaders)
    
<i>
<br />
</i>

**Example**

    from PyEnhance import WebTools

    import requests
    
    WebTools = WebTools.WebTools()
    
    r = requests.get("https://www.google.com", headers=WebTools.RequestHeaders)
    
    print(r)

<i>
    <br />
    <br />
</i>

### StatusCodes

This module consist of http/https status codes sorted by category for handling web request responses

**Status code category's included in the module**

- 1xx (Informational)
- 2xx (Successful)
- 3xx (Redirection)
- 4xx (Client Error)
- 5xx (Server Error)

**Usage**

Set alies for easy usage and readability

    WebTools = WebTools.WebTools()

Calling Category's

    WebTools.StatusCodes.Informational
    WebTools.StatusCodes.Success
    WebTools.StatusCodes.Redirection
    WebTools.StatusCodes.ClientError
    WebTools.StatusCodes.ServerError
    
<i> 
<br />
</i>

**Example**

    from PyEnhance import WebTools

    import requests

    WebTools = WebTools.WebTools()

    r = requests.get(URLHTTPS, headers=WebTools.RequestHeaders)

    if r.status_code in WebTools.PositiveStatusCodes:
        print(f"{r.status_code} is in PositiveStatusCodes list")
    

<i>
<br \>
<br \>
<br \>
</i>

## TextSets

This module contains list of words/charters that can be used for filtering.

The text sets currently included

- Special Characters 
- Cuss Words

I plan on adding many more in the future.

<i>
<br \>
</i>

**Usage**

**Importing the library**

    from PyEnhance import TextSets

Set alies for easy usage and readability

    TextSet = TextSets.TextSet

Calling text sets

    TextSet.SpecialCharacters
    TextSet.CussWords
    
<i>
<br />
</i>

**Examples**

    from PyPiFiles import TextSets

    TextSet = TextSets.TextSet
    

    TestList = [0,1,2,'!']
    
    for i in (TextSet.SpecialCharacters):
    if i in TestList:
    print(f'Word Found: {i} at index {TestList.index(i)}')
    

    TestList2 = ['John', "Bob", "ass", "Chris", "BigAss"]
    
    for badword in (TextSet.CussWords):
    for word in TestList2:
    if badword in word.lower():
    print(f"Word Found: {badword} In {word}")


<i>
<br \>
<br \>
</i>


## Counter

This module like the name implies is a counter.

**Usage**

**Importing the library**

    from PyPiFiles import Counter

<i>
<br \>
</i>

Set alies for easy usage and readability

    Counter1 = Counter.Counter()  # Alies name can not be Counter

Adding to the counter
    
    Counter1.Add()

Getting the current total

    Total = Counter1.Total

or

    print(Counter1.Total

<i>
<br />
</i>

**Example**

    from PyPiFiles import Counter
    
    Counter1 = Counter.Counter()
    Counter2 = Counter.Counter()
    
    for i in range(10):
    Counter1.Add()
    print(Counter1.Total)
    
    
    for i in range(10):
    Counter2.Add()
    print(Counter2.Total)
    
