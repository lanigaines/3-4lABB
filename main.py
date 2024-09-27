def main():
    x = int(input('Enter your input: '))
    y = int(input('Enter your input: '))
    
    if x > 0 and y > 0:
        quadrant = 1
    elif x < 0 and y > 0:
        quadrant = 2
    elif x < 0 and y < 0: 
        quadrant = 3
    elif x > 0 and y < 0:
        quadrant = 4
    else:
        quadrant = 0 

    print(f'Quadrant: {quadrant}')
    ########################################
    # Do not delete the return statement
    ########################################
    return quadrant


if __name__ == '__main__':
    main()
