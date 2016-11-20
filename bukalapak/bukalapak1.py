# fungsi maze pertama
def maze_hiji(input):
    i = 0
    while i < (input + 1)/4:
        print '@ ' + '@' * (input - 2)
        print '@' + ' ' * (input - 2) + '@'
        print '@' * (input - 2) + ' @'
        i += 1
        if i == (input + 1)/4:
            break
        print '@' + ' ' * (input - 2) + '@'


# fungsi maze bagian atas untuk maze kedua dan ketiga
def atas(input):
    print '@ ' + '@' * (input - 2)
    i = 0
    while i < (input - 3)/4:
        print '@ ' * (i + 2) + ' ' * ((input - 6) - 4 * i) + ' @' * (i + 1)
        print '@ ' * (i + 2) + '@' * ((input - 6) - 4 * i) + ' @' * (i + 1)
        i += 1    
    print '@ ' * ((input + 1)/2)


# fungsi maze kedua
def maze_dua(input):
    atas(input)
    j = 0
    while j < (input - 3)/4:
        print '@ ' * ((input - 3)/4 - j) + '@' * (3 + 4 * j) + ' @' * ((input - 3)/4 - j)
        print '@ ' * ((input - 3)/4 - j) + ' ' * (3 + 4 * j) + ' @' * ((input - 3)/4 - j)
        j += 1
    print '@' * input


# fungsi maze ketiga
def maze_tilu(input):
    atas(input)
    j = 0
    while j < (input - 3)/4:
        print '@ ' * ((input - 3)/4 - j) + '@' * (1 + 4 * j) + ' @' * ((input + 1)/4 - j)
        print '@ ' * ((input - 3)/4 - j) + ' ' * (1 + 4 * j) + ' @' * ((input + 1)/4 - j)
        j += 1
    print '@' * (input - 2) + ' @'


# fungsi maze keempat
def maze_opat(input):
    print '@ ' + '@' * (input - 2)
    print '@ ' * 2 + '  @ ' * ((input - 3)/4)
    i = 0
    while i < (input - 3)/4:
        print '@ ' * ((input - 3)/2 - (2 * i)) + '@' * (3 + 4 * i)
        print '@ ' * ((input - 3)/2 - (2 * i)) + ' ' * (2 + 4 * i) + '@'
        print '@ ' * ((input - 5)/2 - (2 * i)) + '@' * (3 + 4 * i) + ' @'
        print '@ ' * ((input - 5)/2 - (2 * i)) + ' ' * (3 + 4 * i) + ' @'
        i += 1
    print '@' * input
    

# fungsi untuk mencetak semua maze
def print_kabeh(input):
    try:
        if (input + 1) % 4 == 0:
            print '\nieu teh maze_hiji'
            maze_hiji(input)
            print '\nieu teh maze_dua'
            maze_dua(input)
            print '\nieu teh maze_tilu'
            maze_tilu(input)
            print '\nieu teh maze_opat'
            maze_opat(input)
        else:
            print 'bilangan harus berupa integer dengan kelipatan 4n - 1!'
    except:
        print 'input harus berupa numerik'

# e.g. print S = 23, warning! kudu kelipatan 4n - 1
print_kabeh(23)
