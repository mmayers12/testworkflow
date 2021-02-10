print("======================== Create the text file ========================")
# Create directory if not exists
import os
new_dir = "my-test"
if os.path.isdir(new_dir) == False:
  try:
      os.makedirs(new_dir)
  except OSError:
      print ("Creation of the directory %s failed" % new_dir)
  else:
      print ("Successfully created the directory %s" % new_dir)

# Combine the strings to generate the text
x_value = 123
file_text = "var=" + str(x_value)
print("The following new text will be written into the file: %s" % file_text)

# Write the text to the file
# If the file does not exist, create it
f_w = open("my-test/test.txt", "w")

