# hybrid_image_processing_ocr

Hybrid Image Processing For Optical Character recognition

Chaitanya Sagar
New Jersey Institute of Technology
Image Processing
Dr. Frank Shih
Date: 05 March 2022




Abstract:
This paper is structured to show the use of mixed image processing methods in identifying ASCII characters from an image while also utilizing facial detection algorithms. First, we take a look at the methods that have been used and proposed to accomplish this task in previous studies. After that, we show how the hybrid method compares with these with the actual research results being discussed.



	INTRODUCTION
In-depth research in computer vision has been done to get machines to see as human beings. However, one can infer that the mindset for accomplishing this task should change since computer vision depends on cameras that have their disadvantages (Lovell and Estivill-Castro, 2007). We take a pragmatic stance amidst all this and tackle this issue head-on by using hybridization of previous methods to maximize use cases. 
This paper will show a hybrid implementation using computer vision to identify human faces then extract English language and mathematical characters from a given input. The algorithms in this paper are implemented in python. 
	Existing Methods
The realm of digital image processing is a 'multiverse' of its own. Every researcher follows their path at implementing specific algorithms, with some having remarkably similar methodologies, only to some extent. Here we outline some of the key terms used in this paper.
	Definition of key terms
Pixels describe pixels as a collection of tiny distinct cells that divide an image into segments that enable computers to store, understand, and manipulate images. Digital Images can be said to include binary images, color images, and grayscale images in the context of image processing (Pixels Fisher et al. (1996). Binary images contain pixels with only two possible values for intensity. They typically use 1 for white and 0 for black but could change this depending on which color represents the foreground or background. Color images utilize the possibilities of blue, red, and green color combinations to represent pixels. They, therefore, have an option of 224 different intensity levels depending on color quantization (Fisher et al.1996). Grayscale images follow the paradigm of having shades of gray as the primary colors. In essence, gray seems to have equal intensities for Red, Green, and Blue if written in RGB color code format. Most of the algorithms we'll discuss in this paper require conversion in between these types of images for optimum functionality. As linguistics could depict, mathematical morphology uses mathematical concepts to bring change. In digital image processing, this is somewhat true in that this particular change is brought about by the use of concepts such as set theory to analyze binary images perform noise removal, as well as other concepts such as image enhancement, edge detection, and segmentation (Fisher et al., 1996). Structuring elements, also termed kernels, in this paper are Features with specific patterns in the form of coordinates for mathematical morphology.   
	Methods
	Haar-Like Cascade
Soo describes Haar Cascade classifiers to detect objects from an image. This research is based on the work of (Viola & Jones 2001) whose research has been reviewed and cited by numerous researchers over time (Soo 2014) notes, object detection methods can benefit members of the computer science cause and professionals with other intentions.
The Haar Cascade algorithm is one of the methods used to detect objects from an image. There are others Viola and Jones outline that the advantage of Cascading is to reduce the time complexity of the whole operation while concurrently improving the detection of objects. Detecting objects is a fundamental step in helping computers see. Having only a camera that acts as an eye is not helpful without processing images like a living organism's brain. Eyes need a brain.
The Haar classifier overcomes the inadequacies of other algorithms. An example here would be color classification which is affected by a change in lighting. Lovell and Estivill-Castro (2007, cited in Soo, 2014) tested this hypothesis in a live implementation where robots had to play a soccer match, proving that color classification required live updates.
The algorithm utilizes features to improve the speed of operation and make it easier to train the model. Viola and Jones develop features like Papageorgiou whose functions are based on the shape and size of rectangular sectors consisting of pixels within the digital image Soo (2014) describes this as using rectangular pixels next to each other at a specified point on the window.
 
Image 1: Rectangular features in Haar Algorithm
A & B represent 2-rectangle features useful by calculating the difference of the addition of pixels within the said rectangular regions. C represents 3-rectangle features. The calculation here is done through summation for the exterior rectangles subtracted from the sum of the middle rectangle. D is the 4-rectangle feature where the analysis is simply subtraction of sums for diagonally opposite rectangles (Viola &Jones 2001; Soo, 2014).
	Binarization
In this algorithm, one should take note of binary, grayscale, and color images and their differences. One standard method of binarization is thresholding. This image processing operation takes either a color image or a grayscale one as input, dividing it into segments before giving an output of a bitwise image (Fisher et al 1996).
The process can help ensure that we separate the valuable parts of an image from those that are not relevant for a given output. As we note from these images below from Sajjad black pixels can correspond to the background or foreground depending on the type of image (Sajjad 2010).The intensity threshold parameter governs the division of the image into segments.

  
Image 2: Foreground and background color
The intensity threshold parameter determines whether an input pixel will be set to black or white. All this depends on whether it is above or below the set threshold as Pratt seems to portray, it is possible to utilize several points to keep a range of intensity values set to a particular color (Pratt 2013).
As the name suggests, Bilevel Luminance Thresholding comprises varying brightness levels, and we might need to do thresholding on it as such. A probable example would be a scanned copy of the typed text that looks as follows:

  
Img 3: Poor Photocopy/ Scan
Pratt suggests that the central issue of contention is how to choose a level of thresholding. The problem is that a low threshold may cause the required content to be eroded. A medium entry might still have some noise, and a high threshold might bring about misreading since some of the foreground regions can become over dilated (Pratt (2013). The Otsu thresholding technique solves some of these issues, but most solutions still lie within the implementation (Otsu 1979, pp. 62-66).
	Noise Removal
Fisher and Pratt outline that there could be three main paradigms of processing digital images morphologically. These are Dilation, Erosion, and Skeletonization. Each of these has various renditions. Dilation is where the object increases in size consistently and spatially (Fisher et al. 1996). Skeletonization is where the foreground object is reduced into a skeleton or stick figure of the original. Erosion is where the object reduces in size consistently and with spatial regard. We can classify pixels as follows to understand this methodology (Pratt 2013)
0 0 0				0 0 0				0 0 0
0 1 1				0 1 0 				0 1 1
0 1 0				0 0 0				0 0 1
4-connected			isolated			8-connected
Mathematical morphology algorithms tend to take two main types of input; an image and the structuring kernel. Combining these with a set of operations gives a processed image as output. 8-neighbor dilate algorithm creates a foreground color pixel if a pattern matches the 8-connected shape. 
	J(i,k)=X ∪ X0  ∪   …  ∪  X7
When applied recursively, the object grows significantly. Fatten algorithm works like 8-neighbor dilate while only avoiding the creation of a bridge. Essentially, for a matrix of pixels like the one below, the center pixel would change for 8-neighbor dilate but not for the fatten algorithm (Pratt, 2013). 
			■(0&0&1@1&0&0@1&1&0)
8-neighbor erode algorithm will change one foreground pixel to the background if at least one 8-connected neighbor pixel has the background color. Too many repetitions of this algorithm can erase too much of the foreground pixels
			J(i,k) = X ∩ X0 ∩ …  ∩ X7
As the mathematics for the above algorithms show, Dilation and erosion can be implemented using hit or miss transformation. Dilation & erosion have other renditions, including Binary image thinning, binary image shrinking, and Binary image thickening.
	Digital Inversion
Rao outline the importance of preprocessing in Optical character recognition. One of the steps in digital inversion is to invert colors in an image to make it suitable for certain image processing operations that can enable feature extraction, segmentation, et cetera to be easier (Rao et al. 2016).
Bitwise-NOT is an operator used to convert the dark areas of an image to lighter versions and the whiter regions of an image to the opposite side of the spectrum (Fisher et al. 1996). They advise producing binary images first before performing these operations. It is possible to do this using a thresholding algorithm. If Bitwise-NOT is used for a gray-level image stored in byte pixel format, it is done bitwise. The result can be:
		G(j,k)	= 255 - P(j,k)	
Bitwise-NOT utilizes the truth table used in digital electronics as follows (Jain, 2003):
A	B
0	1
1	0
This infers that this operation changes the polarity of the image (Fisher et al 1996).
	HYBRID IMAGE PREPROCESSING FOR BIOMETRIC ID AND OCR
To implement an image processor capable of biometric verification and optical character recognition (OCR), I had to consider a specific use-case. The original use case in mind was using these tools to identify an employee by face then scan their ID to prevent the need for physical contact in an organization’s security check. After brainstorming, I discovered an even better use case for these tools.
This use case was facial detection and optical character recognition to help in contact-less parcel delivery or collection. I chose to implement using Python IDE in two stages. The first would be facial detection to save the face of the person collecting the parcel. This step would be followed by inputting random numbers generated to avoid tricksters, which Evtimov show can infiltrate facial recognition (Evtimov et al. 2019).
The algorithm works like a hybrid of techniques from tesseract, OpenCV, pillow, and NumPy, emphasizing preprocessing by cascade as described earlier in the paper and grayscale conversion techniques to make the preprocessing easier. Pytessaract does the heavy lifting to ensure that our text is extracted at a confidence threshold of 70%.
Once we have the image of the person picking the parcel, the system can input an image of the delivery receipt. The main assumption is that we have the actual template of our receipt in development as an image like the one below in development.
 
The main task is to process the image now and take the Parcel number and number of items delivered for use by other parts of the organization such as logistics, finance, et cetera. Currently, the system is operated from the command line, but the algorithm works. The main purpose of all this was to test the algorithm to ensure that we could extract specific data from our receipts despite them being all crumpled up. 
The main code block that does all the hard work is shown in the screenshot below. It checks the preprocessed image and extracts the required data from it by indexing the tesseract image_to_data dictionary output.
 
Eventually, once we have the result, we can know that we have it right from the saved images:
 
	COMPARISON WITH EXISTING METHODS
The algorithm is more dependent on processor power than other methods. It might be improved if acted upon by faster methods such as Otsu’s and improved upon by some preprocessing technique Sajjad outlines a better use case for text recognition which also implements the bitwise NOT operation. For text which has a preset format like numberplates, it works better but could deteriorate the quality of output for our algorithm (Sajjad 2010). 
Other scholars reiterate the importance of using color classification, although lighting affects it (Lovell et al 2007). This algorithm outclasses these in that it uses cascade classifiers instead, which can be tweaked to optimize contours and subsections of images to make it much more accurate.
	CONCLUSIONS
This paper has shown how to implement a proper algorithm that can take video input from users and utilize it to identify faces, then use OCR algorithm capture text. Working as a hybrid collective algorithm has proven to make it easier to acquire the given information, especially in systems when we know the daily operations and conditions for the input are loopholes in training data, various input, and capabilities of the machine. However, the good outweighs the bad with proper planning and implementation of the said procedures.
In essence, at such a point in time, hybrid algorithms prove to be the proper way to go, especially with so much research done that on its own has not been given a proper use case. 






References
	Bradski, G. and Kaehler, A., 2008. Learning OpenCV: Computer vision with the OpenCV library. "O'Reilly Media, Inc.".
	C. Papageorgiou, M. Oren, and T. Poggio. A general framework for object detection. In International Conference on Computer Vision, 1998.
	Evtimov, I., O'Hair, D., Fernandes, E., Calo, R., and Kobno, T., 2019. Is tricking a robot hacking?. Berkeley Tech. LJ, 34, p.891.
	Fisher, R., Perkins, S., Walker, A. and Wolfart, E., 1996. Hypermedia image processing reference. England: John Wiley & Sons Ltd, pp.118-130.
	Jain, R.P., 2003. Modern digital electronics. Tata McGraw-Hill Education.
	Lovell, N. and Estivill-Castro, V., 2007. Color classification and object recognition for robot soccer under variable illumination. IntechOpen.
	Otsu, N., 1979. A threshold selection method from gray-level histograms. IEEE transactions on systems, man, and cybernetics, 9(1), pp.62-66.
	Rao, N.V., Sastry, A.S.C.S., Chakravarthy, A.S.N. and Kalyanchakravarthi, P., 2016. OPTICAL CHARACTER RECOGNITION TECHNIQUE ALGORITHMS. Journal of Theoretical & Applied Information Technology, 83(2).
	Sajjad, K.M., 2010. Automatic license plate recognition using python and OpenCV. Department of Computer Science and Engineering MES College of Engineering.
	Soo, S., 2014. Object detection using Haar-cascade Classifier. Institute of Computer Science, University of Tartu, 2(3), pp.1-12
	Viola, P. and Jones, M., 2001, December. Rapid object detection using a boosted cascade of simple features. In Proceedings of the 2001 IEEE computer society conference on computer vision and pattern recognition. CVPR 2001 (Vol 1, pp. I-I). Ieee.

