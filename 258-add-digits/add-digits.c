int addDigits(int num) {
    if (num == 0){
        return 0;
    }
    if (num%9 == 0){
        return 9;
    }
    while (num > 9){
        num = num - 9;
    } 
    return num;
}