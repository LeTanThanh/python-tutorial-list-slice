if __name__ == "__main__":
  # Introduction to Python List slice notation

  """
  sub_list = list[begin: end: step]
  """

  # Basic Python list slice example

  colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
  print(colors)
  sub_colors = colors[1:4]
  print(sub_colors)

  # Using Python List slice to get the n-first elements from a list

  """
  lists[:n]
  """

  colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
  print(colors)
  sub_colors = colors[:3]
  print(sub_colors)

  # Using Python List slice to get the n-last elements from a list

  """
  lists[-n]
  """

  colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
  print(colors)
  sub_colors = colors[-3:]
  print(sub_colors)

  # Using Python List slice to get every nth element from a list

  colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
  print(colors)
  sub_colors = colors[::2]
  print(sub_colors)

  # Using Python List slice to reverse a list

  colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
  print(colors)
  sub_colors = colors[::-1]
  print(sub_colors)

  # Using Python List slice to substitute part of a list

  colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
  print(colors)
  colors[0:2] = ["black", "white"]
  print(colors)

  # Using Python List slice to partially replace and resize a list
  colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
  print(colors)
  print(f"The list has {len(colors)} elements")
  colors[0:2] = ["black", "white", "gray"]
  print(colors)
  print(f"The list has {len(colors)} elements")

  # Using Python list slice to delete elements
  colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
  print(colors)
  del colors[2:5]
  print(colors)
