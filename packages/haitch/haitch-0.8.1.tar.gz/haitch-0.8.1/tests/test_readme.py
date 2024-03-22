import haitch as H


def test_simple_h1_example():
    # Render known `h1` tag.
    h1 = H.h1("Hello, world")

    got = str(h1)
    want = "<h1>Hello, world</h1>"

    assert got == want


def test_custom_component():
    # Render custom `foo` tag (useful for web components).
    foo = H.foo("Hello, world")

    got = str(foo)
    want = "<foo>Hello, world</foo>"

    assert got == want


def test_customers_example():
    # Fetch customers from a data store.
    customers = [
        ("jane@aol.com", False, True),
        ("bob@example.com", True, False),
        ("mark@mail.org", True, False),
        ("karen@hr.org", False, False),
    ]

    # Build the DOM tree with attributes and children.
    dom = H.div(class_="container")(
        H.h1("Customers to contact:"),
        H.ul(id_="email-customer-list")(
            H.li(H.a(href=f"mailto:{email}")(email))
            for email, is_premium, is_new in customers
            if is_premium or is_new
        ),
    )

    got = str(dom)
    want = '<div class="container"><h1>Customers to contact:</h1><ul id="email-customer-list"><li><a href="mailto:jane@aol.com">jane@aol.com</a></li><li><a href="mailto:bob@example.com">bob@example.com</a></li><li><a href="mailto:mark@mail.org">mark@mail.org</a></li></ul></div>'
    # Pipe this into prettier for improved readability: $ echo '...' | prettier --parser html

    assert got == want
