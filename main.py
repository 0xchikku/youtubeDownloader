from pytube import YouTube

print("YouTube Downloader!\n")
link = input('Link: ')

try:
    # YouTube() is a class and it takes the link as argument
    file = YouTube(link)
    print(
        f"Title: {file.title}\nRating: {file.rating}\nDescription: {file.description}")
    # File is being filtered
    # available is a list which contains downloadable files
    available = file.streams.filter(progressive=True, mime_type="video/mp4")
    # prints the element in the available
    for i in available:
        print(i)

    print(f"Downloading....")
    # Downloads the last best format of the file
    available[-1].download()
    print(f"Downloaded!")

except:
    print(f"Invalid!")
