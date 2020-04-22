def template(x, y, z):
    x = int(x)
    y = str(y)
    print("{}時の{}は{}".format(x, y, z))


if __name__ == "__main__":
    template(12, "気温", 22.4)
