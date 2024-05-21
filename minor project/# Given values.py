# Given values
physical_width_cm = 20  # Physical width in centimeters
pixel_width = 640       # Pixel width
pixel_distance = 260    # Distance in pixels

# Calculate conversion factor
conversion_factor = physical_width_cm / pixel_width

# Convert pixel distance to centimeters
distance_cm = pixel_distance * conversion_factor

print("Conversion Factor:", conversion_factor)
print("Distance in Centimeters:", distance_cm)
