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
