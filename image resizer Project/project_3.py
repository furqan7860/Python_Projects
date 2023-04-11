import cv2

# Load image
image = cv2.imread("Home-banner-Jim-Fahad-Digital.jpg", cv2.IMREAD_UNCHANGED)


# Check if image is successfully loaded
if image is not None:
    # Display image
    cv2.imshow("title", image)
    print("So here is your image")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


input_1=input("Do you want to rezise this image Press Y or N : ")
if(input_1=='y' or input_1=="Y"):

    
    scale_percent=int(input("Enter your percentage Number to resize this image: "))

    new_width = int(image.shape[1]*scale_percent/100)
    new_height = int(image.shape[0]*scale_percent/100)

    output=cv2.resize(image,(new_width,new_height))

    cv2.imwrite('newImage.png',output)
    cv2.imshow("title",output)
    # Wait for a key event
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
else:
    print("Okay Thanks!")

