# Both
Peter Swire

swirepe.com

## What is it?
You can run some commands in parallel.

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
    
        both python -m SimpleHTTPServer ++ cmd

## But what about that '&' thing?

    C:\Users\swirepe>python -m SimpleHTTPServer &
    Serving HTTP on 0.0.0.0 port 8000 ...
    Traceback (most recent call last):
      File "C:\Python27\lib\runpy.py", line 162, in _run_module_as_main
        "__main__", fname, loader, pkg_name)
      File "C:\Python27\lib\runpy.py", line 72, in _run_code
        exec code in run_globals
      File "C:\Python27\lib\SimpleHTTPServer.py", line 220, in <module>
        test()
      File "C:\Python27\lib\SimpleHTTPServer.py", line 216, in test
        BaseHTTPServer.test(HandlerClass, ServerClass)
      File "C:\Python27\lib\BaseHTTPServer.py", line 602, in test
        httpd.serve_forever()
      File "C:\Python27\lib\SocketServer.py", line 225, in serve_forever
        r, w, e = select.select([self], [], [], poll_interval)
    KeyboardInterrupt

    C:\Users\swirepe>sdfsafd
    'sdfsafd' is not recognized as an internal or external command,
    operable program or batch file.

That's a linux thing.  Big whoop, you have a real operating system.  Wanna fight?