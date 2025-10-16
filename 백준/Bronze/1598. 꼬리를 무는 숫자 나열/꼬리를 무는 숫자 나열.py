X,Y = map(int,input().split())
# -1 몫 -> 열 (뒤)
# -1 나머지 -> 행 (앞)
X_row,X_col = (X-1) // 4, (X-1) % 4
Y_row,Y_col = (Y-1) // 4, (Y-1) % 4

# print(X_row,X_col)
# print(Y_row,Y_col)

print(abs(X_row-Y_row)+ abs(X_col-Y_col))