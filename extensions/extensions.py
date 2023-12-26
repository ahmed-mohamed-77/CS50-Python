def main():
    file_name = input("File name: ")
    extension = file_name.lower()

    if ".gif" in extension:
        print("image/gif")
    elif ".jpg" in extension:
        print("image/jpeg")
    elif ".jpeg" in extension:
        print("image/jpeg")
    elif ".png" in extension:
        print("image/png")
    elif ".pdf" in extension:
        print("application/pdf")
    elif ".txt" in extension:
        print("text/plain")
    elif ".zip" in extension:
        print("application/zip")
    else:
        print("application/octet-stream")

if __name__ == "__main__":
    main()
