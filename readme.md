# Both
Peter Swire
swirepe.com

## What is it?
You can run some commands in parallel

## Why?
Windows is silly, and I wanted a way to run processes in the background.

## How do I use it?

    both - run some commands at once (because windows is silly.)
    2012 Peter Swire - swirepe.com
    Input commands (and their arguments) separated by ++
    If you want this to be verbose, it has to be the first argument.
    Example usage:
        both a.exe ++ b.exe
    
        both --verbose a.exe ++ b.exe ++ c.exe
    
        both a.exe ++ b.exe barg1 barg2 ++ c.exe
    
        both ping google.com ++ echo Hello world!
    
        both pandoc --to=html from=markdown --data-dir=md ++ mv *.html *.php

