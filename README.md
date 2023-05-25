Here you can follow the steps in order to correctly code and execute the program:

1) Open Command Prompt by typing "cmd" at the search bar.

2) If you don't have the "pip" command installed type "python -m pip install -U pip" to download it.

3) Download the OpenCV library by typing "pip install opencv-python" to download the latest OpenCV version. Also install "opencv-contrib-python" by typing "pip install opencv-contrib-python"
   because it fixes multiple errors caused by the versions of the opencv.

4) From this website: https://opencv.org/releases/page/6/ download the opencv(3.2.0) and extract all the content from the file. Find the following file "lbpcascade_frontalface.xml"and copy-paste them
	to the file called "opencv-files" which is located at the Desktop.

5) Install the "numpy" library by typing in the command prompt "pip install numpy".

6) We used VSCode to write and run our code. To successully run the code you need to download the following extensions:
   a)Python Image Preview.
   b)Live Share (That's optional. You just need it to make your life easier by writing code together with a colleague).

***It's necessary to have both the latest and the 3.2.0 versions of the OpenCV.

7) We converted our code into an executable file with the following steps:
   a) open command prompt typing "cmd" at the search bar.
   b) type: "pyinstaller --onefile "nameofthefile".py
   
   
The "training-data" directory should consist of individual files named s1, s2, s3, and so on, each containing meticulously captured photographs of the individuals whose faces the program aims to recognize. These images serve as the foundation for training the program's facial recognition capabilities, utilizing the powerful OpenCV library.

When contributing to the GitHub repository, it is essential to ensure that the training-data directory encompasses the aforementioned structure. Each file within this directory should exclusively feature high-quality, clear, and properly aligned photographs of the individuals' faces. These images serve as invaluable training material for the program, enabling it to acquire the necessary knowledge and proficiency to accurately identify the specified individuals in subsequent encounters.
   
  
We would like to express our heartfelt thanks to Professor KOURETAS IOANNIS, our esteemed professor of Electronics and Computers.

Sincerely,

- MICHALIS IOANNIS-EFRAIM
- GEORGIOU XRISTINA
- SIOROS STRATIS
- SOKOS BASILEIOS


Department of Electrical and Computer Engineering          

University of Patras
