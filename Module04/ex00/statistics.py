
def ft_statistics(*args: any, **kwargs: any) -> None:
    # for i in args
    if not args:
        print("No args")
        return
    print(type(args))
    print(args)
    print(kwargs.items())
    # if kwargs is "mean"
    #     somme = sum(args)
    #     moyenne = somme / len(args)
    #     print("mean :", moyenne)


    

if __name__ == '__main__':

    ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
    # print("-----")
    # ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    # print("-----")
    # ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
    # print("-----")
    # ft_statistics(toto="mean", tutu="median", tata="quartile")