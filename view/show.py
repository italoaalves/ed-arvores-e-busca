def show_view(tree):
    print("Show\n")
    try:
        tree.show()
    except Exception as e:
        print(e)
    input("ENTER to continue")
