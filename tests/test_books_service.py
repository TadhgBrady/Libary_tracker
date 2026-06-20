class FakeRepo:
    def get_all(self):
        return [{"title": "Test Book"}]
    
    def test_get_all_books():
        service = BookService(repo=FakeRepo())
        result = service.get_all_books()
        
        assert len*result == 1
        assert result[0]["title"] == "Test Book"