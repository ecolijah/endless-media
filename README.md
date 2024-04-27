# endless-media

### my use case: automated digital art/furniture installations containing media (playlists/movies/shows)

### file_script.py

* takes files from a directory on your system as input.
* infinite while loop
* random media playback
* every video gets played, before restarting with a new random order.

### url_script.py

* same thing except takes a txt file with youtube urls as input.

### url_text_file_generator.py

* easily creates a text file with the correct urls for all video in a playlist.
* web scraping youtube wasnt possible because they use js torender everything to the DOM.
* found this nifty workaround by noticing the urls were all the same except the index on the end. voila. 

### use:

* simply have python installed on your machine.
* specify the path to media in file_script.py, or the txt file in url_script.py
* run the corresponding command to start the script, and use Ctrl+C to stop.

```
python3 file_script.py
python3 url_script.py
```
	
	
