## Adding a comment to test sync
def main():
    # Read in submission file
    with open('submit.txt') as fin:
        data = fin.read().strip('\n')

    # split across newlines
    out_data = data.split('\n')
    try:
        # ensure each line of the submit file is an integer
        out_data = [int(d) for d in out_data]
        # append the new integers onto the end of the base file
        with open('base.txt', 'a') as fout:
            for d in out_data:
                print('Adding {} to base file'.format(d))
                fout.write(str(d) + '\n')
        # reset the submit file to blank
        with open('submit.txt', 'w'):
            pass
    except:
        print('Error with submission')


if __name__ == '__main__':
    main()
