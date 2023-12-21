# Write code using find() and string slicing to extract the number
# at the end of the line below.
# Convert the extracted value to a floating point number and print it out.

data = "From X-DSPAM-Confidence:    0.8475"

# Find the position of the last space character in the string
last_space_pos = data.rfind(' ')

# Extract the number at the end of the line using string slicing
number_at_end = data[last_space_pos+1:]

# Convert the extracted value to a floating-point number
float_number = float(number_at_end)

# Print the extracted floating-point number
print(float_number)
