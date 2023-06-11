import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Read the image
image_path = 'sun.jpeg'
image = mpimg.imread(image_path)

# Calculate the brightness level for each pixel
brightness = np.dot(image[:, :, :], [0.21, 0.72, 0.07])
brightness/=3
# Define the brightness threshold
threshold = 30 # Adjust this value to set your desired brightness level

# Create a mask for pixels above and below the threshold
above_threshold = brightness > threshold
below_threshold = brightness <= threshold

def calculate_pixel_types(image_path, threshold):
    # Open the image
    image = plt.imread(image_path)

    # Get the image dimensions
    height, width, _ = image.shape

    # Initialize counters for typeA and typeB pixels
    typeA_count = 0
    typeB_count = 0

    # Iterate through each pixel
    for y in range(height):
        for x in range(width):
            # Get the RGB values of the pixel
            r, g, b = image[y, x]

            # Compare RGB values with the threshold
            if r > threshold[0] and g > threshold[1] and b > threshold[2]:
                typeA_count += 1
            else:
                typeB_count += 1

    # Calculate the percentages
    total_pixels = width * height
    typeA_percentage = (typeA_count / total_pixels) * 100
    typeB_percentage = (typeB_count / total_pixels) * 100

    return typeA_percentage, typeB_percentage

# Set the image path and the threshold (e.g., (160, 160, 160))
image_path = 'sun.jpeg'
threshold = (160, 160, 160)

# Calculate the pixel types
typeA_percentage, typeB_percentage = calculate_pixel_types(image_path, threshold)

# Print the results
print(f"Type A pixels: {typeA_percentage}%")
print(f"Type B pixels: {typeB_percentage}%")

# Set pixels above the threshold to black (0) and below to white (1)
bw_image = np.where(above_threshold, 1, 0)

# Create a figure with two subplots
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# Display the first image in the first subplot
axes[0].imshow(image)
axes[0].set_title('Image 1')

# Display the second image in the second subplot
axes[1].imshow(bw_image,cmap="gray")
axes[1].set_title('Image 2')

# Remove the axis labels
for ax in axes:
    ax.axis('off')

plt.tight_layout()
plt.show()



"""
# Display the image
image = plt.imread(image_path)
plt.imshow(image)
plt.axis('off')
plt.show()

"""


