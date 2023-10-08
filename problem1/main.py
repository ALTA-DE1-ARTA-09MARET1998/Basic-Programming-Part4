def play_with_asterisk(n):
    pattern = ""

    for i in range(1, n + 1):
        spaces = " " * (n - i)
        asterisks = "* " * i
        pattern += spaces + asterisks + "\n"
    return pattern

if __name__ == '__main__':
    print(play_with_asterisk(5))
    """
        *
       * *
      * * *
     * * * *
    * * * * *
    """
