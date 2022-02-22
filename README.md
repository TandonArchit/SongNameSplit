## SongNameSplit
The SongNameSplit library can take a song title and identify the song name and artist name. The input taken is a string, and a dictionary gives the output. This library needs to access some web pages while running, which means that the final output time is directly dependent on your internet speed.

### PyPi

Link: https://pypi.org/project/SongNameSplit/

### Sample Input and Output

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

### Sample Code


```
import SongNameSplit

result = SongNameSplit.namesplit("Coldplay - Hymn For The Weekend (Official Video)")

print("The name of the song is: ", result['songname'])
print("The name of the artist is: ", result['artist'])
```
****
### Made by
Archit Tandon.
****
