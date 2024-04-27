# Input a youtube playlist prefix to quickly generate all the individual urls
def main():
    #change these accordingly
    filename='urls/mtv100.txt'
    playlist_length=101
    playlisturl='https://www.youtube.com/watch?v=sOnqjkJTMaA&list=PLDkAFNanIXVgDKa05y_eFqAy6ToBsL4up&index='
    
    with open(filename, 'a') as file:
        # Iterate through each item in the list
        
        for i in range(playlist_length):
            # Write the item to the file followed by a newline character
            file.write(playlisturl + str(i+1) + '\n')


if __name__ == "__main__":
    main()