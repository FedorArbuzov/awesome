# Hangman

Предлагается следующий протокол общения компьютера с пользователем:

```
> Guess a letter:
< a
> Missed, mistake 1 out of 5.
>
> The word: *****
> 
> Guess a letter:
< b
> Missed, mistake 2 out of 5.
> 
> The word: *****
> 
> Guess a letter:
< e
> Hit!
> 
> The word: *e***
> 
> Guess a letter:
< o
> Hit!
>
> The word: *e**o
> 
> Guess a letter:
< l
> Hit!
>
> The word: *ello
> 
> Guess a letter:
< h
> Hit!
>
> The word: hello
>
> You won!

```

Пример проигрыша:

```
> Guess a letter:
< x
> Missed, mistake 1 out of 5.
>
> The word: ******
>
> Guess a letter:
< y
> Missed, mistake 2 out of 5.
>
> The word: ******
>
> Guess a letter:
< z
> Missed, mistake 3 out of 5.
>
> The word: ******
> 
> Guess a letter:
< n
> Hit!
>
> The word: **n*n*
>
> Guess a letter:
< m
> Missed, mistake 4 out of 5.
>
> The word: **n*n*
>
> Guess a letter:
< o
> Missed, mistake 5 out of 5.
>
> The word: **n*n*
>
> You lost!
```

