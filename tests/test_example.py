def test_example(page):
    # Mở Google
    page.goto("https://www.google.com")

    # Kiểm tra tiêu đề trang có chứa "Google"
    assert "Google" in page.title()
