from matriks import Matriks

def cetakMatriks(matriks):
    for brs in range(matriks.bykBaris()):
        for klm in range(matriks.bykKolom()):
            print(f'{matriks[brs, klm]: 4d}', end=' ')
        print()

def main():

    # Definisikan matrixA = | 0 1 |
    #                       | 2 3 |
    #                       | 4 5 |
    matrixA = Matriks(3, 2)
    matrixA[0, 0] = 0
    matrixA[0, 1] = 1
    matrixA[1, 0] = 2
    matrixA[1, 1] = 3
    matrixA[2, 0] = 4
    matrixA[2, 1] = 5


    # Definisikan matrixB = |  6   7   8  |
    #                       |  9   1   0  |
    matrixB = Matriks(2, 3)
    matrixB[0, 0] = 6
    matrixB[0, 1] = 7
    matrixB[0, 2] = 8
    matrixB[1, 0] = 9
    matrixB[1, 1] = 1
    matrixB[1, 2] = 0


    # Definisikan matrixC = | 4 -3 |
    #                       | 2  1 |
    #                       | 4  3 |
    matrixC = Matriks(3, 2)
    matrixC[0, 0] = 4
    matrixC[0, 1] = -3
    matrixC[1, 0] = 2
    matrixC[1, 1] = 1
    matrixC[2, 0] = 4
    matrixC[2, 1] = 3
    
    # Lakukan perkalian matrixA * matrixB
    # menggunakan operasi multiply dengan operator *.
    matrixS = matrixA * matrixB

    # Cetak hasil perkalian matriks
    print('MatrixA * MatrixB =')
    print()
    cetakMatriks(matrixS)
    print()
    
    # Uji perkalian dua matriks tidak sesuai
    print('Uji perkalian dua matriks tidak sesuai:')
    try:
        matrixT = matrixA * matrixC
        cetakMatriks(matrixT)
    except ValueError:
        print('Matriks yang diberikan tidak sesuai!')
        
main()