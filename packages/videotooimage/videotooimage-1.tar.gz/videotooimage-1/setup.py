from setuptools import setup, find_packages

setup(
    name="videotooimage",
    version="1",
    description="Video to Image converter",
    long_description="""videotooimage is a Python package that provides functionality to convert video files into sequences of images. It utilizes the OpenCV library (cv2) to process video files and extract frames. This package is useful for tasks such as video analysis, object detection, and machine learning model training using video data.

    Features:
    - Convert video files (e.g., .mp4, .avi, .mov) into sequences of images.
    - Works with various video codecs and formats supported by OpenCV.
    - No need to create sub folders for directories, Created automatically
    - Very useful for machine learning training purposes,
        the original folder structure is kept as is it.

    Processing
        1 sec = 1 frame = 1 image file (.jpg format)

    Installation:
    You can install videotooimage via pip:
    ```
    pip install videotooimage
    ```

    Usage:
    ```
    python import videotooimage

    # Convert video to images
    videotooimage.videoTooImage("path/to/video/directory/"))
    ```

    How it replicates / Works
    Folder structure of videos directory (Input)
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

        -> After conversion
        /project
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
                    person2.mp4
                    person3.mp4
                    ...

            /videos
                /happy
                    person1.mp4
                    person2.mp4
                    person3.mp4
                /sad
                    person1.mp4
                    person2.mp4
                    person3.mp4

    Author:
    - Name: Raghav
    - GitHub: @raghavtwenty
    - Email: raghavtwenty@gmail.com

    License:
    This package is licensed under the MIT License.

    Contributions:
    Contributions and feedback are welcome!
    Please submit issues or pull requests on GitHub.

    For more detailed usage instructions and examples,
    please refer to the documentation at
    https://github.com/raghavtwenty/videotooimage.
    """,
    long_description_content_type="text/markdown",
    url="https://github.com/raghavtwenty/videotooimage",
    author="Raghav",
    author_email="raghavtwenty@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=["opencv-python"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
