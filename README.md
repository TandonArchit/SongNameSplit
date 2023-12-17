
## SongNameSplit

The SongNameSplit library can take a song title and identify the song name and artist name. The input taken is a string, and a dictionary gives the output. 



Approximate accuracy: 97% - 99%



This library needs to access some web pages while running, which means that the final output time is directly dependent on your internet speed. However, the BLAZE update, that is on all versions after 2.0.0, will greatly improve speeds.



### Example Inputs and Outputs



Input 1:

```

"Coldplay - Hymn For The Weekend (Official Video)"

```

Output 1:

```

{'artist': 'Coldplay', 'songname': 'Hymn For The Weekend'}

```



Input 2:

```

"Dua Lipa - Levitating Featuring DaBaby (Official Music Video)"

```

Output 2:

```

{'artist': 'Dua Lipa', 'songname': 'Levitating'}

```



### Installation

SongNameSplit can be installed using the following pip code. Please note that the SongNameSplit library is internet-dependent, so a stable internet connection is essential.



```

pip install SongNameSplit

```

### Import

SongNameSplit can be imported using the following code:



```

import SongNameSplit

```

### Usage

SongNameSplit can be used as:

```

SongNameSplit.namesplit("<< SONG TITLE >>")

```

Replace the "<< SONG TITLE >>" with your song title.

To run the library quietly, that is, without printing anything, use the optional "runQuietly" flag:

```
SongNameSplit.namesplit("<< SONG TITLE >>", runQuietly=True)

```

The default value of the "runQuietly" flag is False.



### Sample Code

Feel free to copy the following code to test SongNameSplit out!

```

import SongNameSplit



result = SongNameSplit.namesplit("Coldplay - Hymn For The Weekend (Official Video)")



print("The name of the song is: ", result['songname'])

print("The name of the artist is: ", result['artist'])

```

### NonStandardSongTitle Error

If you recieve the following error, it means that the title that you provided to SongNameSplit does not look like or is not formatted like how titles usually are formatted. 

```

NonStandardSongTitle: This title does not look like a standard title

```

### InternetConnectionError Error

If you recieve the following error, it means that your internet connection is either unstable or dropped while the function was running. Since SongNameSplit has componenets that need to access the internet, it is recommended to use a stable internet connection.

```

InternetConnectionError: Please make sure you have a stable internet connection

```

****

### Additional Details



**GitHub Link**

https://github.com/TandonArchit/SongNameSplit



**Made by**

Archit Tandon.

****

