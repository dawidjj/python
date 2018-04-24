from contextlib import ContextDecorator

class makeparagraph(ContextDecorator):
    def __enter__(self):
        print('<p>')
        return self

    def __exit__(self, *exc):
        print('</p>')
        return False

@makeparagraph()
def emit_html():
    print('Here is some non-HTML')

emit_html()


from contextlib import contextmanager

@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
   print("foo")


def typowanie(zmienna1: str, zmienna2: bool) -> int:
    print(zmienna2)
    return 'sss'

typowanie('sss','ss')