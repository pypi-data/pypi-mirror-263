# Project Name : videotooimage
Filename : README <br>
Title : Videos to images <br>
Author : Raghav | Github : @raghavtwenty <br>
Date Created : March 18, 2024 | Last Updated : March 19, 2024 <br>
Language : Python | Version : 3.10.13 <br>

# AVAILABLE ON PIP
https://pypi.org/project/videotooimage/ <br>
pip install videotooimage


# Purpose
videotooimage is a Python package that provides functionality to convert video files into sequences of images. <br>
It utilizes the OpenCV library (cv2) to process video files and extract frames.  <br>
This package is useful for tasks such as video analysis, object detection, and machine learning model training using video data. <br>


# Features
Convert video files (e.g., .mp4, .avi, .mov) into sequences of images.<br>
Works with various video codecs and formats supported by OpenCV.<br>
No need to create sub folders for directories, Created automatically. <br>
Very useful for machine learning training purposes, the original folder structure is kept as is it.<br>

# Processing
1 sec = 1 frame = 1 image file (.jpg format)

# Installation
You can install videotooimage via pip:
```
pip install videotooimage
```

# Usage
Python3
```
from videotooimage.videotooimage import videoTooImage
result = videoTooImage("/path/to/videos/folder", "/path/to/output/folder")
print(result)
```

# Output upon successful processing
Processing done, Check the folders : /output/folder <br>


# How it replicates / Works
Folder structure of videos directory (Input) <br>
<pre>
/project
    /videos
        /happy
            person1.mp4
            person2.mp4
            person3.mp4
        /sad
            person1.mp4
            person2.mp4
            person3.mp4
</pre>


After conversion <br>
Folder structure of output directory <br>
<pre>
/output/folder/
    /v2i_images
        /happy
            person1(frame_number_1).jpg
            person1(frame_number_2).jpg
            person2.mp4
            person3.mp4
            ...
        /sad
            person1(frame_number_1).jpg
            person1(frame_number_2).jpg
            person2.jpg
            person3.jpg
            ... <br>
</pre>


# Author:
- Name: Raghav <br>
- GitHub: @raghavtwenty <br>
- Email: raghavtwenty@gmail.com <br>

# License: <br>
This package is licensed under the MIT License. <br>

# Contributions:
Contributions and feedback are welcome! <br>
Please submit issues or pull requests on GitHub. <br>
