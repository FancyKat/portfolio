# Financial Caluclators

Features

- Single Payment Compound Amount
- Single Payment Present Worth
- Uniform Series Sinking Fund
- Capital Recovery
- Uniform serices Compound Amount
- Uniform Gradient Present Worth
- Uniform Gradient Future Worth
- Uniform Gradient Uniform Series

```python
F = Future(input())
P = Present(input())
i = interest(int(input()))
n = time(input()) # datetime import
```

> NOTES: <br>
> Techincal Phrasing: <br>
> To find the future worth of money **F = P\*(1+i)<sup>n</sup> = P(F/P,i,n)**
>

Formulas are as followed cited from the
[Engineering Economics Formula Sheet](https://formulae2020jakarta.blogspot.com/2020/11/engineering-economics-formula-sheet.html)

## Django Templating

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            '/home/html/example.com',
            '/home/html/default',
        ],
    },
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [
            '/home/html/jinja2',
        ],
    },
]

```

If you call get_template('story_detail.html'), here are the files Django will look for, in order:

- `/home/html/example.com/story_detail.html ('django' engine)`
- `/home/html/default/story_detail.html ('django' engine)`
- `/home/html/jinja2/story_detail.html ('jinja2' engine)`

If you call select_template(['story_253_detail.html', 'story_detail.html']), here’s what Django will look for:

- `/home/html/example.com/story_253_detail.html ('django' engine)`
- `/home/html/default/story_253_detail.html ('django' engine)`
- `/home/html/jinja2/story_253_detail.html ('jinja2' engine)`
- `/home/html/example.com/story_detail.html ('django' engine)`
- `/home/html/default/story_detail.html ('django' engine)`
- `/home/html/jinja2/story_detail.html ('jinja2' engine)`

When Django finds a template that exists, it stops looking.

[Templates | Django documentation | Django](https://docs.djangoproject.com/en/4.0/topics/templates/#engine)
