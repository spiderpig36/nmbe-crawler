## Istructions
Step 1. Install required python packages
```
pip install -r requirements.txt
```
Step 2. Run the website crawler for the intended url, for instance https://insekten-evb.ch/
```
python crawl_urls.py https://insekten-evb.ch/
```
Step 3. This process takes a few minutes and saves all urls that are contained in the website to a file called crawl_insekten-evb.ch.txt. Duplicate this file and name the copy progress_insekten-evb.ch.txt. Next run the archiver.
```
python archive.py progress_insekten-evb.ch.txt
```
Step 4. This process takes a long time since the archive takes a long time to make the snapshot of the website. Therefore the programm saves the progress in the file. If needed the program can be stoped and continued at a later stage.

Step 5. Go back to step 2 and repeat with another url.