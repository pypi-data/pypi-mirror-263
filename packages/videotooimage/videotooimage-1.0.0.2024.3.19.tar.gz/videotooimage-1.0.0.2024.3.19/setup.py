from setuptools import setup, find_packages

# Read the content of the README file
with open("README.md", "r", encoding="utf-8") as f:
    readme_content = f.read()

setup(
    name="videotooimage",
    version="1.0.0.2024.03.19",
    description="Video to Image converter",
    long_description="""videotooimage is a Python package that provides functionality to convert video files into sequences of images. It utilizes the OpenCV library (cv2) to process video files and extract frames. This package is useful for tasks such as video analysis, object detection, and machine learning model training using video data.
    """,
    long_description_content_type=readme_content,
    url="https://github.com/raghavtwenty/videotooimage",
    author="Raghav",
    author_email="raghavtwenty@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=["opencv-python", "cv2"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
