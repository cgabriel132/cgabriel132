
import cv2
import argparse

def main():

    parser = argparse.ArgumentParser(description='Atlas Car')
    parser.add_argument('-i1','--imagem1', type = str, required = False, default = '/home/gabriel/Documents/Aula5/images/atlascar.png')
    parser.add_argument('-i2','--imagem2', type = str, required = False, default = '/home/gabriel/Documents/Aula5/images/atlascar2.png')
    args = vars(parser.parse_args())

    print(args)

    image1 = cv2.imread(args["imagem1"], cv2.IMREAD_COLOR) # Load an image
    image2 = cv2.imread(args['imagem2'], cv2.IMREAD_COLOR)

    flip_flop = True
    while True:

        flip_flop = not flip_flop

        if flip_flop:
            cv2.imshow('RGB Image', image1)
        else:
            cv2.imshow('RGB Image', image2)

        cv2.waitKey(3000)


if __name__ == '__main__':
    main()