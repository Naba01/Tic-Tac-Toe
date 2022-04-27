cells = [' '] * 9
def check_game_status():
    flag1 = 0
    flag2 = 0
    x_cnt = 0
    o_cnt = 0
    val=''
    empty_cells=0
    x = range(0,7,3)
    y = range(0,3,1)
    z = range(0,9,1)
    global cells
    for i in x:
        if cells[i]==cells[i+1] and cells[i+1]==cells[i+2] and cells[i]=='X':
            flag1=1
            val=cells[i]
    for i in x:
        if cells[i]==cells[i+1] and cells[i+1]==cells[i+2] and cells[i]=='O':
            flag2=1
            val=cells[i]
    for i in y:
        if cells[i]==cells[i+3] and cells[i+3]==cells[i+6] and cells[i]=='X':
            flag1=1
            val=cells[i]
    for i in y:
        if cells[i]==cells[i+3] and cells[i+3]==cells[i+6] and cells[i]=='O':
            flag2=1
            val=cells[i]
    if cells[0]==cells[4] and cells[4]==cells[8] and cells[0]=='X':
        flag1=1
        val=cells[0]
    
    if cells[0]==cells[4] and cells[4]==cells[8] and cells[0]=='O':
        flag2=1
        val=cells[0]
    
    if cells[2]==cells[4] and cells[4]==cells[6] and cells[2]=='X':
        flag1=1
        val=cells[2]

    if cells[2]==cells[4] and cells[4]==cells[6] and cells[2]=='O':
        flag1=1
        val=cells[2]
    
    if (flag1 == 1 or flag2 == 1) and (flag1 != flag2):
        print(val,'wins')
        return 4

    for i in z:
        if (cells[i]==' ') :
            empty_cells = empty_cells + 1
    if (cells[i]=='X') :
        x_cnt = x_cnt + 1
    if (cells[i]=='O') :
        o_cnt = o_cnt + 1
    if empty_cells > 0 and flag1 == 0 and flag2 == 0 and abs(x_cnt-o_cnt) <= 1:
        # print("Game not finished")
        return 5
    if empty_cells == 0 and flag1 == 0 and flag2 == 0 :
        print("Draw")
        return 6
    if empty_cells > 0 and abs(x_cnt-o_cnt) > 1:
        # print("Impossible")
        return 7
    if empty_cells > 0 and flag1 == 1 and flag2 == 1 and abs(x_cnt-o_cnt) <= 1:
        # print("Impossible")
        return 7

def draw_empty_grid():
    global cells
    print('---------')
    print('|',' ',' ',' ','|')
    print('|',' ',' ',' ','|')
    print('|',' ',' ',' ','|')
    print('---------')
    
def draw_grid(cells):

    print('---------')
    print('|',cells[0],cells[1],cells[2],'|')
    print('|',cells[3],cells[4],cells[5],'|')
    print('|',cells[6],cells[7],cells[8],'|')
    print('---------')



def new_cell_entry(sign):
    global cells
    flag = 1
    isempty= 1
    j = 0
    cnt = 0
    while j < len(cells):
        if cells[j] == ' ':
            cnt = cnt +1
        j = j + 1
   
    
    while flag==1 and isempty == 1 and cnt > 0:
        k = input('Enter the coordinates: ')
        if (not k.replace(" ", "").isnumeric()):
            print('You should enter numbers!')
        else:
            x,y = k.split()
            if not( int(x)>=1 and int(x) <=3 and int(y)>=1 and int(y)<=3):
                print('Coordinates should be from 1 to 3!')
            else:
                if not ( cells[(int(x) - 1) * 3 + (int(y) - 1)] == ' ' ):
                    print("This cell is occupied! Choose another one!")
                else:
                    cells[(int(x) - 1) * 3 + (int(y) - 1)] = sign
                    isempty = 2
                    flag = 2
            
def main():
    global cells
    draw_empty_grid()
    empty_cells_count = 9
    sign = 'X'
    while (empty_cells_count >= 0):
        new_cell_entry(sign)
        draw_grid(cells)
        chk_status = check_game_status()
        if chk_status == 5 :
            if sign == 'X':
                sign = 'O'
            else:
                sign = 'X'
            empty_cells_count -= 1
            continue
        elif (chk_status == 4 or chk_status == 6 or chk_status == 7):
            break
        
if __name__ == "__main__":
    main()
    
